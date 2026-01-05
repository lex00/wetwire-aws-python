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
    """Extract CF resource type from base class inheritance."""
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
