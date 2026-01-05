"""
CloudFormation serialization provider.

Implements the core Provider interface for CloudFormation-specific
serialization of references, attributes, and resources.
"""

from __future__ import annotations

from typing import Any

from dataclass_dsl import Provider, is_attr_ref, is_class_ref

from wetwire_aws.intrinsics.functions import GetAtt, IntrinsicFunction, Ref


class CloudFormationProvider(Provider):
    """
    CloudFormation-specific serialization provider.

    Converts dataclass-dsl Ref and Attr annotations to
    CloudFormation intrinsic functions {"Ref": "..."} and
    {"Fn::GetAtt": ["...", "..."]}.

    Example:
        >>> provider = CloudFormationProvider()
        >>> provider.serialize_ref(MyFunction, MyBucket)
        {'Ref': 'MyBucket'}
        >>> provider.serialize_attr(MyFunction, MyRole, 'Arn')
        {'Fn::GetAtt': ['MyRole', 'Arn']}
    """

    name = "cloudformation"

    def serialize_ref(
        self,
        source: type[Any],
        target: type[Any],
    ) -> dict[str, str]:
        """
        Serialize a Ref[T] to CloudFormation {"Ref": "LogicalId"}.

        Args:
            source: The referencing wrapper class
            target: The referenced wrapper class

        Returns:
            CloudFormation Ref intrinsic: {"Ref": "TargetClassName"}
        """
        logical_id = self.get_logical_id(target)
        return Ref(logical_id).to_dict()

    def serialize_attr(
        self,
        source: type[Any],
        target: type[Any],
        attr_name: str,
    ) -> dict[str, list[str]]:
        """
        Serialize an Attr[T, name] to CloudFormation {"Fn::GetAtt": [...]}.

        Args:
            source: The referencing wrapper class
            target: The referenced wrapper class
            attr_name: The attribute to retrieve (e.g., "Arn")

        Returns:
            CloudFormation GetAtt intrinsic: {"Fn::GetAtt": ["Target", "Arn"]}
        """
        logical_id = self.get_logical_id(target)
        return GetAtt(logical_id, attr_name).to_dict()

    def serialize_resource(
        self,
        resource: Any,
    ) -> dict[str, Any]:
        """
        Serialize a wrapper resource to CloudFormation format.

        Extracts the resource type from base class inheritance and
        builds the CloudFormation resource definition.

        Args:
            resource: The wrapper resource instance

        Returns:
            CloudFormation resource dict with Type and Properties
        """
        from wetwire_aws.base import CloudFormationResource

        wrapper_cls = type(resource)

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
            raise ValueError(
                f"Wrapper class {wrapper_cls.__name__} must inherit from a "
                "CloudFormationResource subclass (e.g., s3.Bucket, iam.Role)"
            )

        # Get the AWS resource type string
        cf_type = resource_type_cls._resource_type

        # Build properties from wrapper instance
        properties = self._build_properties(resource, wrapper_cls, resource_type_cls)

        return {
            "Type": cf_type,
            "Properties": properties,
        }

    def _build_properties(
        self,
        wrapper_instance: Any,
        wrapper_cls: type[Any],
        resource_type_cls: type[Any],
    ) -> dict[str, Any]:
        """
        Build CloudFormation properties from a wrapper instance.

        Args:
            wrapper_instance: The wrapper resource instance
            wrapper_cls: The wrapper class
            resource_type_cls: The resource type class

        Returns:
            Dict of CloudFormation properties (PascalCase keys)
        """
        from wetwire_aws.base import CloudFormationResource
        from wetwire_aws.intrinsics.refs import resolve_refs_from_annotations

        # Collect properties from class attributes (inheritance pattern stores
        # overridden values as class attributes)
        props: dict[str, Any] = {}

        # Get field names from the resource type's dataclass fields
        if hasattr(resource_type_cls, "__dataclass_fields__"):
            field_names = set(resource_type_cls.__dataclass_fields__.keys())
        else:
            field_names = set()

        # Check class attributes that override dataclass field defaults
        for name in field_names:
            if name.startswith("_"):
                continue

            # Get from class dict to find overridden values
            # Check wrapper class's own __dict__ first, then instance
            if name in wrapper_cls.__dict__:
                value = wrapper_cls.__dict__[name]
            elif name in wrapper_instance.__dict__:
                value = wrapper_instance.__dict__[name]
            else:
                continue

            if value is None:
                continue

            # Handle no-parens pattern: runtime AttrRef markers
            if is_attr_ref(value):
                # MyRole.Arn -> {"Fn::GetAtt": ["MyRole", "Arn"]}
                props[name] = GetAtt(value.target.__name__, value.attr)
            # Handle no-parens pattern: class references
            elif is_class_ref(value):
                # MyBucket -> {"Ref": "MyBucket"}
                props[name] = Ref(value.__name__)
            elif isinstance(value, type) and issubclass(value, CloudFormationResource):
                # Fallback for inherited classes
                props[name] = Ref(value.__name__)
            else:
                props[name] = value

        # Resolve dataclass-dsl annotations to intrinsics (for type annotation pattern)
        resolved_refs = resolve_refs_from_annotations(wrapper_instance)
        for field_name, ref_value in resolved_refs.items():
            # Only use annotation-based resolution if not already resolved
            if field_name not in props:
                props[field_name] = ref_value

        # Create resource instance and serialize
        resource_instance = resource_type_cls(**props)

        # Use the resource's to_dict() for proper serialization
        result = resource_instance.to_dict()

        # Return just the Properties portion
        properties: dict[str, Any] = result.get("Properties", {})
        return properties

    def _serialize_value(self, value: Any) -> Any:
        """
        Recursively serialize a value for CloudFormation.

        Args:
            value: The value to serialize

        Returns:
            Serialized value suitable for CloudFormation JSON
        """
        # Handle no-parens pattern: AttrRef markers
        if is_attr_ref(value):
            return GetAtt(value.target.__name__, value.attr).to_dict()
        # Handle no-parens pattern: class references
        if is_class_ref(value):
            return Ref(value.__name__).to_dict()
        if isinstance(value, type) and hasattr(value, "_refs_marker"):
            return Ref(value.__name__).to_dict()
        if isinstance(value, IntrinsicFunction):
            return value.to_dict()
        if hasattr(value, "to_dict"):
            return value.to_dict()
        if isinstance(value, list):
            return [self._serialize_value(item) for item in value]
        if isinstance(value, dict):
            return {k: self._serialize_value(v) for k, v in value.items()}
        return value
