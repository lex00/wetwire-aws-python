# wetwire-aws-python FAQ

This FAQ covers questions specific to the Python implementation of wetwire for AWS CloudFormation. For general wetwire questions, see the [central FAQ](https://github.com/lex00/wetwire/blob/main/docs/FAQ.md).

---

## Getting Started

### How do I install wetwire-aws?

```bash
pip install wetwire-aws
```

### How do I create a new project?

```bash
wetwire-aws init my-infrastructure
cd my-infrastructure
```

### How do I build a CloudFormation template?

```bash
wetwire-aws build --module my_infrastructure
```

---

## Syntax

### How do I declare a resource?

```python
from . import *

class MyBucket(s3.Bucket):
    bucket_name = "my-data-bucket"
```

### How do I reference another resource?

Use direct class references:

```python
class MyFunction(lambda_.Function):
    role = MyRole.Arn  # GetAtt reference
```

### How do I reference a resource without an attribute?

Use the class name directly:

```python
class MySecurityGroup(ec2.SecurityGroup):
    vpc_id = MyVPC  # Ref reference
```

### Why is Lambda spelled `lambda_`?

`lambda` is a reserved keyword in Python. The underscore suffix avoids the conflict.

### Why does the linter flag my `ref()` usage?

The linter enforces direct references for analyzability. Instead of:

```python
# Flagged by linter
role = ref(MyRole)
```

Use:

```python
# Preferred
role = MyRole
```

---

## Lint Rules

### What lint rules are available?

See the [CLI documentation](CLI.md) for the full list of lint rules. Key rules include:

- Use typed enum constants instead of strings
- Use direct references instead of `ref()`/`get_att()`
- Extract nested structures to named classes
- Avoid oversized files

### How do I auto-fix lint issues?

```bash
wetwire-aws lint --fix path/to/file.py
```

---

## Import

### How do I convert an existing CloudFormation template?

```bash
wetwire-aws import template.yaml --output my_infrastructure/
```

### Import produced code with errors?

Import is best-effort. Complex templates may need manual cleanup:

1. Run `wetwire-aws lint --fix` to apply automatic fixes
2. Review and manually fix remaining issues
3. Check import logs for unsupported features

---

## Design Mode

### How do I use AI-assisted design?

```bash
export ANTHROPIC_API_KEY=your-key
wetwire-aws design
```

### What happens in design mode?

1. You describe what infrastructure you need
2. AI generates wetwire code
3. Linter enforces patterns
4. You review and refine

---

## Troubleshooting

### ModuleNotFoundError

Ensure wetwire-aws is installed:

```bash
pip install wetwire-aws
```

### Build produces empty template

Check that:
1. Resources are declared as classes inheriting from a resource type (e.g., `class MyBucket(s3.Bucket)`)
2. The module path is correct in the build command
3. Classes are in a module that gets imported

### TypeError with resource references

Ensure you're using direct class references, not string names:

```python
# Wrong
vpc_id = "MyVPC"

# Correct
vpc_id = MyVPC
```

---

## Resources

- [Wetwire Specification](https://github.com/lex00/wetwire/blob/main/docs/WETWIRE_SPEC.md)
- [CLI Documentation](CLI.md)
- [Quick Start](QUICK_START.md)
