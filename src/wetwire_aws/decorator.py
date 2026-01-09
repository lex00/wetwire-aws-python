"""
The @wetwire_aws decorator.

This decorator uses dataclass-dsl to create a CloudFormation-specific
decorator with automatic resource registration.
"""

from typing import Any

from dataclass_dsl import ResourceRegistry, create_decorator

from wetwire_aws.base import CloudFormationResource, PropertyType

# AWS-specific registry for CloudFormation resources
cf_registry = ResourceRegistry()

# Registries for template elements (Parameters, Outputs, Mappings, Conditions)
param_registry = ResourceRegistry()
output_registry = ResourceRegistry()
mapping_registry = ResourceRegistry()
condition_registry = ResourceRegistry()


def _get_resource_class(cls: type[Any]) -> type[Any] | None:
    """Extract CloudFormation resource class from base classes.

    Looks for a base class that is a subclass of CloudFormationResource
    (but not CloudFormationResource itself).

    Args:
        cls: The wrapper class to inspect.

    Returns:
        The CloudFormationResource subclass, or None if not found.
    """
    for base in cls.__bases__:
        if base is not CloudFormationResource and isinstance(base, type):
            if issubclass(base, CloudFormationResource):
                return base
    return None


def _get_property_type_class(cls: type[Any]) -> type[Any] | None:
    """Extract PropertyType class from base classes.

    Looks for a base class that is a subclass of PropertyType
    (but not PropertyType itself).

    Args:
        cls: The wrapper class to inspect.

    Returns:
        The PropertyType subclass, or None if not found.
    """
    for base in cls.__bases__:
        if base is not PropertyType and isinstance(base, type):
            if issubclass(base, PropertyType):
                return base
    return None


def _get_resource_type(cls: type[Any]) -> type[Any] | str | None:
    """Extract CloudFormation resource type from base class inheritance.

    Looks up the _resource_type attribute on the CloudFormationResource base
    class to determine the AWS resource type (e.g., "AWS::S3::Bucket").

    Args:
        cls: The wrapper class to inspect.

    Returns:
        The CloudFormation resource type string, or None if not found.
    """
    resource_class = _get_resource_class(cls)
    if resource_class is not None:
        return getattr(resource_class, "_resource_type", None)
    return None


# Create the @wetwire_aws decorator using the factory
# Note: We don't pass resource_field since we use inheritance-based detection
# via get_resource_type instead of the `resource:` annotation pattern.
wetwire_aws = create_decorator(
    registry=cf_registry,
    get_resource_type=_get_resource_type,
)


def get_aws_registry() -> ResourceRegistry:
    """Get the AWS resource registry.

    Returns:
        The global ResourceRegistry instance containing all classes
        decorated with @wetwire_aws.
    """
    return cf_registry


# =============================================================================
# Template Element Detection and Registration
# =============================================================================


def _is_parameter_subclass(cls: type[Any]) -> bool:
    """Check if cls inherits from Parameter (but is not Parameter itself).

    Args:
        cls: The class to check.

    Returns:
        True if cls is a user-defined Parameter subclass.
    """
    # Import here to avoid circular imports
    from wetwire_aws.template import Parameter

    return isinstance(cls, type) and issubclass(cls, Parameter) and cls is not Parameter


def _is_output_subclass(cls: type[Any]) -> bool:
    """Check if cls inherits from Output (but is not Output itself).

    Args:
        cls: The class to check.

    Returns:
        True if cls is a user-defined Output subclass.
    """
    from wetwire_aws.template import Output

    return isinstance(cls, type) and issubclass(cls, Output) and cls is not Output


def _is_mapping_subclass(cls: type[Any]) -> bool:
    """Check if cls inherits from Mapping (but is not Mapping itself).

    Args:
        cls: The class to check.

    Returns:
        True if cls is a user-defined Mapping subclass.
    """
    from wetwire_aws.template import Mapping

    return isinstance(cls, type) and issubclass(cls, Mapping) and cls is not Mapping


def _is_condition_subclass(cls: type[Any]) -> bool:
    """Check if cls inherits from TemplateCondition (but is not itself).

    Args:
        cls: The class to check.

    Returns:
        True if cls is a user-defined TemplateCondition subclass.
    """
    from wetwire_aws.template import TemplateCondition

    return (
        isinstance(cls, type)
        and issubclass(cls, TemplateCondition)
        and cls is not TemplateCondition
    )


def register_parameter(cls: type[Any]) -> type[Any]:
    """Register a Parameter subclass in the param_registry.

    Args:
        cls: The Parameter subclass to register.

    Returns:
        The class unchanged (allows use as a decorator).
    """
    param_registry.register(cls, "Parameter")
    return cls


def register_output(cls: type[Any]) -> type[Any]:
    """Register an Output subclass in the output_registry.

    Args:
        cls: The Output subclass to register.

    Returns:
        The class unchanged (allows use as a decorator).
    """
    output_registry.register(cls, "Output")
    return cls


def register_mapping(cls: type[Any]) -> type[Any]:
    """Register a Mapping subclass in the mapping_registry.

    Args:
        cls: The Mapping subclass to register.

    Returns:
        The class unchanged (allows use as a decorator).
    """
    mapping_registry.register(cls, "Mapping")
    return cls


def register_condition(cls: type[Any]) -> type[Any]:
    """Register a Condition subclass in the condition_registry.

    Args:
        cls: The Condition subclass to register.

    Returns:
        The class unchanged (allows use as a decorator).
    """
    condition_registry.register(cls, "Condition")
    return cls
