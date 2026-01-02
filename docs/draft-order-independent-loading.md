# Order-Independent Resource Loading

## Problem

Currently, resources within the same file must be ordered so that dependencies come before dependents:

```python
# This works - B defined before A references it
@wetwire_aws
class B:
    resource: s3.Bucket

@wetwire_aws
class A:
    resource: s3.BucketPolicy
    bucket = B  # B exists, OK
```

```python
# This fails - A references B before B is defined
@wetwire_aws
class A:
    resource: s3.BucketPolicy
    bucket = B  # NameError: name 'B' is not defined

@wetwire_aws
class B:
    resource: s3.Bucket
```

The importer handles this via topological sort, but users writing code by hand may find this ordering constraint surprising.

## Solution: Two-Pass Loading with Placeholders

### Overview

1. **First pass**: Parse file to discover all class names
2. **Inject placeholders**: Before executing module, inject placeholder objects for all class names
3. **Execute module**: Class bodies can now reference any class name (resolves to placeholder)
4. **Resolve placeholders**: After execution, replace placeholder references with real classes

### Implementation

#### 1. Placeholder Class

```python
# In dataclass_dsl/_loader.py

class _ClassPlaceholder:
    """Placeholder for a class that will be defined later in the file."""

    __slots__ = ('_name', '_module')

    def __init__(self, name: str, module: str):
        self._name = name
        self._module = module

    def __repr__(self) -> str:
        return f"<Placeholder for {self._module}.{self._name}>"
```

#### 2. Modified Module Loading

```python
def _load_module_with_namespace(
    mod_name: str,
    full_mod_name: str,
    pkg_path: Path,
    namespace: dict[str, Any],
    local_class_names: list[str],  # NEW: classes defined in this file
) -> ModuleType:
    """Load a module with namespace injection and placeholder support."""
    file_path = pkg_path / f"{mod_name}.py"

    spec = importlib.util.spec_from_file_location(full_mod_name, file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module {full_mod_name}")

    module = importlib.util.module_from_spec(spec)

    # Inject cross-file classes from namespace
    for name, obj in namespace.items():
        setattr(module, name, obj)

    # NEW: Inject placeholders for same-file classes not yet defined
    for class_name in local_class_names:
        if not hasattr(module, class_name):
            setattr(module, class_name, _ClassPlaceholder(class_name, full_mod_name))

    sys.modules[full_mod_name] = module
    spec.loader.exec_module(module)

    # NEW: Resolve placeholders after execution
    _resolve_placeholders(module, local_class_names)

    return module
```

#### 3. Placeholder Resolution

```python
def _resolve_placeholders(module: ModuleType, class_names: list[str]) -> None:
    """Replace placeholder references with real classes after module execution."""
    # Build map of real classes
    real_classes: dict[str, type] = {}
    for name in class_names:
        obj = getattr(module, name, None)
        if obj is not None and isinstance(obj, type):
            real_classes[name] = obj

    # Walk each class and resolve placeholder references
    for name, cls in real_classes.items():
        _resolve_class_placeholders(cls, real_classes)


def _resolve_class_placeholders(cls: type, class_map: dict[str, type]) -> None:
    """Resolve placeholder references in a class's attributes."""
    for attr_name in list(vars(cls)):
        if attr_name.startswith('_'):
            continue

        value = getattr(cls, attr_name)
        resolved = _resolve_value(value, class_map)

        if resolved is not value:
            setattr(cls, attr_name, resolved)


def _resolve_value(value: Any, class_map: dict[str, type]) -> Any:
    """Recursively resolve placeholders in a value."""
    if isinstance(value, _ClassPlaceholder):
        real_class = class_map.get(value._name)
        if real_class is None:
            raise NameError(f"Placeholder '{value._name}' could not be resolved")
        return real_class

    if isinstance(value, list):
        return [_resolve_value(v, class_map) for v in value]

    if isinstance(value, tuple):
        return tuple(_resolve_value(v, class_map) for v in value)

    if isinstance(value, dict):
        return {k: _resolve_value(v, class_map) for k, v in value.items()}

    # Handle intrinsic functions that wrap class references
    # e.g., get_att(Placeholder, "Arn") -> get_att(RealClass, "Arn")
    if hasattr(value, '_resolve_placeholders'):
        return value._resolve_placeholders(class_map)

    return value
```

#### 4. Intrinsic Function Support

Intrinsic functions like `get_att()` need to support placeholder resolution:

```python
# In wetwire_aws/intrinsics/refs.py

class GetAtt:
    def __init__(self, resource: type | str | _ClassPlaceholder, attribute: str):
        self._resource = resource
        self._attribute = attribute

    def _resolve_placeholders(self, class_map: dict[str, type]) -> 'GetAtt':
        """Return a new GetAtt with placeholders resolved."""
        if isinstance(self._resource, _ClassPlaceholder):
            real_class = class_map.get(self._resource._name)
            if real_class is None:
                raise NameError(f"Placeholder '{self._resource._name}' not resolved")
            return GetAtt(real_class, self._attribute)
        return self
```

### Changes Required

| File | Change |
|------|--------|
| `dataclass_dsl/_loader.py` | Add `_ClassPlaceholder`, modify `_load_module_with_namespace`, add `_resolve_placeholders` |
| `wetwire_aws/intrinsics/refs.py` | Add `_resolve_placeholders` method to `GetAtt`, `Ref` classes |
| `wetwire_aws/intrinsics/functions.py` | Add `_resolve_placeholders` to intrinsic functions that can contain class refs |

### Edge Cases

1. **Circular references within decorators**: The `@wetwire_aws` decorator runs after the class is defined, so it sees the placeholder. Need to ensure resolution happens before decorator processing.

2. **Type annotations**: `resource: Ref[B]` - type annotations are evaluated lazily in Python 3.10+ with `from __future__ import annotations`. This should work without changes.

3. **Default values that call functions**: `x = some_func(B)` - if `some_func` is called during class body evaluation with a placeholder, it may fail. Solution: `some_func` should accept placeholders and defer resolution.

4. **Nested classes**: Placeholders in nested class definitions need to be resolved too.

### Testing

```python
def test_forward_reference_in_same_file():
    """Resources can reference classes defined later in the same file."""
    code = '''
from . import *

@wetwire_aws
class BucketPolicy:
    resource: s3.BucketPolicy
    bucket = DataBucket  # Forward reference!

@wetwire_aws
class DataBucket:
    resource: s3.Bucket
    bucket_name = "my-bucket"
'''
    # Should work without NameError
    module = load_module_from_string(code)
    assert module.BucketPolicy.bucket is module.DataBucket
```

### Migration

This is a backwards-compatible enhancement. Existing code that already orders dependencies correctly will continue to work. New code gains the flexibility to order resources in any way.

### Performance

Minimal impact:
- First pass (parsing for class names) already happens
- Placeholder injection is O(n) for n classes
- Resolution is O(n * m) where m is average attributes per class
- Only affects module load time, not runtime

### Alternatives Considered

1. **String-based references everywhere**: `bucket = "DataBucket"` - loses IDE support
2. **Lazy lambdas**: `bucket = lambda: DataBucket` - awkward syntax
3. **Module `__getattr__`**: Only works for module-level access, not class bodies
4. **AST transformation**: Complex, hard to debug

The placeholder approach is the cleanest solution that preserves the natural `bucket = DataBucket` syntax while enabling order independence.
