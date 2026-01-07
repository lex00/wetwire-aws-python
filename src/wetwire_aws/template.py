"""
CloudFormation template generation.

CloudFormationTemplate collects registered resources and generates
valid CloudFormation JSON or YAML.
"""

import builtins
import json
from dataclasses import dataclass, field
from typing import Any, ClassVar, cast

from wetwire_aws.decorator import cf_registry
from wetwire_aws.intrinsics.functions import IntrinsicFunction

# Alias for type() builtin since 'type' is used as parameter name
builtins_type = builtins.type


class ParameterMeta(type):
    """Metaclass for Parameter that enables Ref-style access.

    When a Parameter subclass is referenced (e.g., `MyParam`), it can be
    detected as a reference marker for CloudFormation Ref intrinsics.
    """

    _refs_marker: ClassVar[bool] = True


class Parameter(metaclass=ParameterMeta):
    """CloudFormation template parameter base class.

    Use inheritance to define parameters:
        class Environment(Parameter):
            type = STRING
            default = "dev"
    """

    # Class-level defaults that can be overridden by subclasses
    type: str = "String"
    description: str = ""
    default: Any = None
    allowed_values: list[str] | None = None
    allowed_pattern: str | None = None
    min_length: int | None = None
    max_length: int | None = None
    min_value: int | None = None
    max_value: int | None = None
    no_echo: bool = False
    constraint_description: str | None = None

    # Marker for reference detection
    _refs_marker: ClassVar[bool] = True

    @classmethod
    def to_dict(cls) -> dict[str, Any]:
        """Convert parameter to CloudFormation dict format."""
        result: dict[str, Any] = {"Type": cls.type}
        if cls.description:
            result["Description"] = cls.description
        if cls.default is not None:
            result["Default"] = cls.default
        if cls.allowed_values:
            result["AllowedValues"] = cls.allowed_values
        if cls.allowed_pattern:
            result["AllowedPattern"] = cls.allowed_pattern
        if cls.min_length is not None:
            result["MinLength"] = cls.min_length
        if cls.max_length is not None:
            result["MaxLength"] = cls.max_length
        if cls.min_value is not None:
            result["MinValue"] = cls.min_value
        if cls.max_value is not None:
            result["MaxValue"] = cls.max_value
        if cls.no_echo:
            result["NoEcho"] = True
        if cls.constraint_description:
            result["ConstraintDescription"] = cls.constraint_description
        return result


class Output:
    """CloudFormation template output base class.

    Use inheritance to define outputs:
        class BucketArnOutput(Output):
            value = MyBucket.Arn
            description = "Bucket ARN"
    """

    value: Any = None
    description: str = ""
    export_name: str | None = None
    condition: str | None = None

    @classmethod
    def to_dict(cls) -> dict[str, Any]:
        """Convert output to CloudFormation dict format."""
        value = cls.value
        if isinstance(value, IntrinsicFunction):
            value = value.to_dict()
        result: dict[str, Any] = {"Value": value}
        if cls.description:
            result["Description"] = cls.description
        if cls.export_name:
            result["Export"] = {"Name": cls.export_name}
        if cls.condition:
            result["Condition"] = cls.condition
        return result


class Mapping:
    """CloudFormation template mapping base class.

    Use inheritance to define mappings:
        class RegionMapMapping(Mapping):
            map_data = {"us-east-1": {"AMI": "ami-12345"}}
    """

    map_data: dict[str, dict[str, Any]] = {}

    @classmethod
    def to_dict(cls) -> dict[str, dict[str, Any]]:
        """Return the mapping data."""
        return cls.map_data


class TemplateCondition:
    """CloudFormation template condition base class.

    Use inheritance to define conditions:
        class IsProdCondition(TemplateCondition):
            expression = Equals(Environment, "prod")

    Note: Named TemplateCondition to avoid conflict with the Condition
    intrinsic function.
    """

    expression: Any = None
    logical_id: str | None = None  # Optional override for the condition name

    @classmethod
    def get_expression(cls) -> Any:
        """Get the condition expression."""
        return cls.expression


# Alias for backward compatibility
Condition = TemplateCondition


@dataclass
class CloudFormationTemplate:
    """
    CloudFormation template container.

    Collects resources, parameters, outputs, and generates
    valid CloudFormation JSON or YAML.
    """

    description: str = ""
    parameters: dict[str, type[Parameter]] = field(default_factory=dict)
    mappings: dict[str, dict[str, dict[str, Any]]] = field(default_factory=dict)
    conditions: dict[str, Any] = field(default_factory=dict)
    resources: dict[str, Any] = field(default_factory=dict)
    outputs: dict[str, type[Output]] = field(default_factory=dict)
    transform: str | list[str] | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_registry(
        cls,
        scope_package: str | None = None,
        description: str = "",
        parameters: dict[str, type["Parameter"]] | None = None,
        outputs: dict[str, type["Output"]] | None = None,
    ) -> "CloudFormationTemplate":
        """
        Create a template from registered resources and template elements.

        Resources, Parameters, Outputs, Mappings, and Conditions are
        automatically collected from their respective registries.

        Resources are topologically sorted by dependencies using dataclass-dsl
        get_dependencies(), so resources appear in creation order.

        Args:
            scope_package: Optional package name to filter resources
            description: Template description
            parameters: Additional parameters (merged with auto-collected)
            outputs: Additional outputs (merged with auto-collected)

        Returns:
            CloudFormationTemplate with all registered elements
        """
        from wetwire_aws.decorator import (
            condition_registry,
            mapping_registry,
            output_registry,
            param_registry,
        )

        registry = cf_registry
        resources: dict[str, Any] = {}

        # Auto-collect parameters from registry
        auto_parameters: dict[str, type[Parameter]] = {}
        for param_cls in param_registry.get_all(scope_package):
            auto_parameters[param_cls.__name__] = param_cls

        # Auto-collect outputs from registry
        auto_outputs: dict[str, type[Output]] = {}
        for output_cls in output_registry.get_all(scope_package):
            # Remove "Output" suffix if present for cleaner names
            name = output_cls.__name__
            if name.endswith("Output"):
                name = name[:-6]
            auto_outputs[name] = output_cls

        # Auto-collect mappings from registry
        auto_mappings: dict[str, dict[str, dict[str, Any]]] = {}
        for mapping_cls in mapping_registry.get_all(scope_package):
            # Remove "Mapping" suffix if present
            name = mapping_cls.__name__
            if name.endswith("Mapping"):
                name = name[:-7]
            auto_mappings[name] = mapping_cls.to_dict()

        # Auto-collect conditions from registry
        auto_conditions: dict[str, Any] = {}
        for cond_cls in condition_registry.get_all(scope_package):
            # Use logical_id if set, otherwise derive from class name
            name = getattr(cond_cls, "logical_id", None) or cond_cls.__name__
            if name.endswith("Condition"):
                name = name[:-9]
            auto_conditions[name] = cond_cls.get_expression()


        from dataclass_dsl import is_attr_ref, is_class_ref

        from wetwire_aws.base import CloudFormationResource
        from wetwire_aws.intrinsics.functions import GetAtt
        from wetwire_aws.intrinsics.functions import Ref as RefIntrinsic
        from wetwire_aws.intrinsics.refs import resolve_refs_from_annotations

        # Get all wrapper classes
        all_wrappers = list(registry.get_all(scope_package))

        # Custom dependency detection for inheritance pattern
        # dataclass_dsl doesn't detect dependencies from class attributes
        def get_wrapper_dependencies(cls: type) -> set[type]:
            """Get dependencies from class attributes (AttrRef and class refs)."""
            deps: set[type] = set()
            for name, value in cls.__dict__.items():
                if name.startswith("_"):
                    continue
                if is_attr_ref(value):
                    deps.add(value.target)
                elif is_class_ref(value):
                    deps.add(value)
                elif isinstance(value, type) and issubclass(value, CloudFormationResource):
                    deps.add(value)
            return deps

        # Custom topological sort using our dependency detection
        def custom_topological_sort(classes: list[type]) -> list[type]:
            """Sort classes by dependencies (dependencies first)."""
            class_set = set(classes)
            sorted_result: list[type] = []
            remaining = set(classes)

            while remaining:
                # Find classes whose dependencies are all satisfied
                ready = [
                    cls
                    for cls in remaining
                    if get_wrapper_dependencies(cls).intersection(class_set).issubset(
                        set(sorted_result)
                    )
                ]

                if not ready:
                    # No progress - take any remaining class to break cycle
                    ready = [next(iter(remaining))]

                for cls in ready:
                    sorted_result.append(cls)
                    remaining.remove(cls)

            return sorted_result

        # Use custom sort instead of dataclass_dsl's topological_sort
        sorted_wrappers = custom_topological_sort(all_wrappers)

        for wrapper_cls in sorted_wrappers:
            logical_name = wrapper_cls.__name__

            # Get resource type from base class inheritance
            resource_type_cls = None
            for base in wrapper_cls.__mro__[1:]:  # Skip the class itself
                if (
                    base is not CloudFormationResource
                    and isinstance(base, type)
                    and issubclass(base, CloudFormationResource)
                    and hasattr(base, "_resource_type")
                    and base._resource_type
                ):
                    resource_type_cls = base
                    break

            if resource_type_cls is None:
                continue

            # Create wrapper instance to get property values
            wrapper_instance = wrapper_cls()

            # Resolve Ref[T] and Attr[T, "name"] annotations to intrinsics
            resolved_refs = resolve_refs_from_annotations(wrapper_instance)

            # Collect properties from class attributes (inheritance pattern stores
            # overridden values as class attributes, not instance attributes)
            props: dict[str, Any] = {}

            # Get field names from the resource type's dataclass fields
            if hasattr(resource_type_cls, "__dataclass_fields__"):
                field_names = set(resource_type_cls.__dataclass_fields__.keys())
            else:
                field_names = set()

            # Check class attributes that override dataclass field defaults
            for k in field_names:
                if k.startswith("_"):
                    continue
                # Get from class dict to find overridden values
                # Check wrapper class's own __dict__ first, then instance
                if k in wrapper_cls.__dict__:
                    v = wrapper_cls.__dict__[k]
                elif k in wrapper_instance.__dict__:
                    v = wrapper_instance.__dict__[k]
                else:
                    continue

                if v is None:
                    continue

                # Handle no-parens pattern: AttrRef markers (e.g., MyRole.Arn)
                if is_attr_ref(v):
                    props[k] = GetAtt(v.target.__name__, v.attr)
                # Handle no-parens pattern: class references (e.g., MyVPC)
                elif is_class_ref(v):
                    props[k] = RefIntrinsic(v.__name__)
                elif isinstance(v, type) and hasattr(v, "_refs_marker"):
                    props[k] = RefIntrinsic(v.__name__)
                else:
                    props[k] = v

            # Merge resolved refs - these are the dataclass-dsl annotations resolved
            # to CloudFormation intrinsics. Only include refs that resolve to
            # fields the resource actually accepts.
            for field_name, ref_value in resolved_refs.items():
                # Don't overwrite already-resolved no-parens refs
                if field_name not in props:
                    props[field_name] = ref_value

            # Create resource instance with collected properties
            resource_instance = resource_type_cls(**props)
            resources[logical_name] = resource_instance.to_dict()

        # Merge auto-collected with manually passed elements
        # Manual parameters/outputs override auto-collected ones
        final_parameters = {**auto_parameters, **(parameters or {})}
        final_outputs = {**auto_outputs, **(outputs or {})}

        return cls(
            description=description,
            parameters=final_parameters,
            mappings=auto_mappings,
            conditions=auto_conditions,
            resources=resources,
            outputs=final_outputs,
        )

    def to_dict(self) -> dict[str, Any]:
        """Convert template to CloudFormation-compatible dict."""
        result: dict[str, Any] = {
            "AWSTemplateFormatVersion": "2010-09-09",
        }

        if self.description:
            result["Description"] = self.description

        if self.transform:
            result["Transform"] = self.transform

        if self.metadata:
            result["Metadata"] = self.metadata

        if self.parameters:
            result["Parameters"] = {
                name: param.to_dict() for name, param in self.parameters.items()
            }

        if self.mappings:
            result["Mappings"] = self.mappings

        if self.conditions:
            result["Conditions"] = self._resolve_conditions(self.conditions)

        # Resources is always included (empty dict if none)
        result["Resources"] = (
            self._resolve_resources(self.resources) if self.resources else {}
        )

        if self.outputs:
            result["Outputs"] = {
                name: output.to_dict() for name, output in self.outputs.items()
            }

        return result

    def _resolve_resources(self, resources: dict[str, Any]) -> dict[str, Any]:
        """Resolve any intrinsic functions in resources."""
        resolved: dict[str, Any] = self._resolve_value(resources)
        return resolved

    def _resolve_conditions(self, conditions: dict[str, Any]) -> dict[str, Any]:
        """Resolve any intrinsic functions in conditions."""
        return {
            name: (cond.to_dict() if isinstance(cond, IntrinsicFunction) else cond)
            for name, cond in conditions.items()
        }

    def _resolve_value(self, value: Any) -> Any:
        """Recursively resolve intrinsic functions in a value."""
        if isinstance(value, IntrinsicFunction):
            return value.to_dict()
        elif isinstance(value, dict):
            return {k: self._resolve_value(v) for k, v in value.items()}
        elif isinstance(value, list):
            return [self._resolve_value(v) for v in value]
        else:
            return value

    def to_json(self, indent: int = 2) -> str:
        """Generate CloudFormation JSON."""
        return json.dumps(self.to_dict(), indent=indent)

    def to_yaml(self) -> str:
        """Generate CloudFormation YAML."""
        try:
            import yaml

            return yaml.dump(
                self.to_dict(),
                default_flow_style=False,
                sort_keys=False,
                allow_unicode=True,
            )
        except ImportError:
            raise ImportError("PyYAML is required for YAML output: pip install pyyaml")

    def add_parameter(
        self,
        name: str,
        *,
        type: str,
        description: str = "",
        default: Any = None,
        allowed_values: list[str] | None = None,
        allowed_pattern: str | None = None,
        min_length: int | None = None,
        max_length: int | None = None,
        min_value: int | None = None,
        max_value: int | None = None,
        no_echo: bool = False,
        constraint_description: str | None = None,
    ) -> None:
        """Add a parameter to the template.

        Dynamically creates a Parameter subclass with the given attributes.
        """
        attrs: dict[str, Any] = {"type": type}
        if description:
            attrs["description"] = description
        if default is not None:
            attrs["default"] = default
        if allowed_values:
            attrs["allowed_values"] = allowed_values
        if allowed_pattern:
            attrs["allowed_pattern"] = allowed_pattern
        if min_length is not None:
            attrs["min_length"] = min_length
        if max_length is not None:
            attrs["max_length"] = max_length
        if min_value is not None:
            attrs["min_value"] = min_value
        if max_value is not None:
            attrs["max_value"] = max_value
        if no_echo:
            attrs["no_echo"] = no_echo
        if constraint_description:
            attrs["constraint_description"] = constraint_description

        # Dynamically create a Parameter subclass
        param_cls = cast("builtins.type[Parameter]", builtins_type(name, (Parameter,), attrs))
        self.parameters[name] = param_cls

    def add_output(
        self,
        name: str,
        *,
        value: Any,
        description: str = "",
        export_name: str | None = None,
        condition: str | None = None,
    ) -> None:
        """Add an output to the template.

        Dynamically creates an Output subclass with the given attributes.
        """
        attrs: dict[str, Any] = {"value": value}
        if description:
            attrs["description"] = description
        if export_name:
            attrs["export_name"] = export_name
        if condition:
            attrs["condition"] = condition

        # Dynamically create an Output subclass
        output_cls = cast(type[Output], builtins_type(name, (Output,), attrs))
        self.outputs[name] = output_cls

    def add_resource(self, logical_name: str, resource: Any) -> None:
        """Add a resource to the template."""
        if hasattr(resource, "to_dict"):
            self.resources[logical_name] = resource.to_dict()
        else:
            self.resources[logical_name] = resource

    def add_condition(self, name: str, condition: Any) -> None:
        """Add a condition to the template."""
        self.conditions[name] = condition

    def add_mapping(self, name: str, mapping: dict[str, dict[str, Any]]) -> None:
        """Add a mapping to the template."""
        self.mappings[name] = mapping
