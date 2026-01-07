"""
Base classes for CloudFormation resources.

CloudFormationResource is the base class for all AWS resource types.
PropertyType is the base class for nested property structures.
Context is the base class for environment-specific configuration.
"""

from dataclasses import dataclass, field
from typing import Annotated, Any, ClassVar, Generic, TypeVar, cast, overload

from dataclass_dsl import AttrRef, ContextRef, Resource, is_attr_ref, is_class_ref
from dataclass_dsl import PropertyType as PropertyTypeBase
from dataclass_dsl._decorator import RefMeta
from dataclass_dsl._loader import _ClassPlaceholder

# TypeVar for generic PropertyType proxy
_PT = TypeVar("_PT", bound="PropertyType")


class ResourceMeta(RefMeta, type(Resource)):
    """Metaclass for CloudFormationResource that provides attribute ref access.

    This metaclass inherits from both RefMeta (for dataclass_dsl decorator compatibility)
    and the metaclass of Resource (ABCMeta) to avoid metaclass conflicts.

    It adds `__getattr__` for attribute refs, allowing `MyResource.Arn` syntax
    to return an AttrRef marker that gets serialized to CloudFormation
    `{"Fn::GetAtt": ["MyResource", "Arn"]}`.
    """

    def __getattr__(cls, name: str) -> AttrRef:
        """Return an AttrRef marker for CloudFormation GetAtt references.

        This enables the no-parens pattern: `role = MyRole.Arn`
        """
        # Don't intercept dunder attributes or private attributes
        if name.startswith("_"):
            raise AttributeError(
                f"type object {cls.__name__!r} has no attribute {name!r}"
            )
        # Return an AttrRef marker for CloudFormation attributes
        return AttrRef(cls, name)


class PropertyTypeProxy(Generic[_PT]):
    """Proxy for PropertyType access that enables nested AttrRef chaining.

    When accessing a PropertyType at class level (e.g., MyDB.Endpoint), this proxy
    is returned instead of the PropertyType class directly. This enables:

    - Nested attribute access: MyDB.Endpoint.Address -> AttrRef("MyDB", "Endpoint.Address")
    - Instantiation: MyDB.Endpoint(...) -> creates Endpoint instance

    Without this proxy, PropertyType classes attached to resources would shadow
    the metaclass __getattr__, preventing nested GetAtt references.

    Example:
        >>> class MyDB(rds.DBInstance): pass
        >>> MyDB.Endpoint  # Returns PropertyTypeProxy
        >>> MyDB.Endpoint.Address  # Returns AttrRef("MyDB", "Endpoint.Address")
        >>> MyDB.Endpoint(address="...", port=3306)  # Creates Endpoint instance
    """

    __slots__ = ("_resource", "_name", "_class")

    def __init__(self, resource_class: type, pt_name: str, pt_class: type[_PT]) -> None:
        """Initialize the proxy.

        Args:
            resource_class: The resource class this PropertyType belongs to
            pt_name: The name of the PropertyType (e.g., "Endpoint")
            pt_class: The actual PropertyType class
        """
        object.__setattr__(self, "_resource", resource_class)
        object.__setattr__(self, "_name", pt_name)
        object.__setattr__(self, "_class", pt_class)

    def __getattr__(self, name: str) -> AttrRef:
        """Return AttrRef for nested attribute access.

        Enables: MyDB.Endpoint.Address -> AttrRef("MyDB", "Endpoint.Address")
        """
        # Don't intercept dunder attributes
        if name.startswith("__") and name.endswith("__"):
            raise AttributeError(
                f"'{type(self).__name__}' object has no attribute '{name}'"
            )
        resource = object.__getattribute__(self, "_resource")
        pt_name = object.__getattribute__(self, "_name")
        return AttrRef(resource, f"{pt_name}.{name}")

    def __call__(self, *args: Any, **kwargs: Any) -> _PT:
        """Instantiate the PropertyType.

        Enables: MyDB.Endpoint(address="...", port=3306)
        """
        pt_class = object.__getattribute__(self, "_class")
        return pt_class(*args, **kwargs)

    def __repr__(self) -> str:
        resource = object.__getattribute__(self, "_resource")
        pt_name = object.__getattribute__(self, "_name")
        return f"<PropertyTypeProxy {resource.__name__}.{pt_name}>"

    # Support isinstance/issubclass checks against the wrapped class
    @property
    def __wrapped__(self) -> type[_PT]:
        """Return the wrapped PropertyType class."""
        return object.__getattribute__(self, "_class")

    def __mro_entries__(self, bases: tuple[type, ...]) -> tuple[type[_PT]]:
        """Allow PropertyTypeProxy to be used as a base class.

        When Python sees `class X(PropertyTypeProxy):`, it calls __mro_entries__
        and substitutes the result into the base classes. This enables:

            class MyEncryption(s3.Bucket.BucketEncryption):
                ...

        To work correctly by inheriting from the actual BucketEncryption class.
        See PEP 560 for details.
        """
        return (object.__getattribute__(self, "_class"),)


class PropertyTypeDescriptor(Generic[_PT]):
    """Descriptor that returns PropertyTypeProxy for class-level access.

    This descriptor wraps PropertyType classes attached to resources,
    returning a PropertyTypeProxy when accessed at class level to enable
    nested GetAtt references.

    Example:
        # In generated code:
        DBInstance.Endpoint = PropertyTypeDescriptor(_DBInstance.Endpoint, "Endpoint")

        # Usage:
        class MyDB(rds.DBInstance): pass
        MyDB.Endpoint  # Returns PropertyTypeProxy (enables .Address etc.)
    """

    __slots__ = ("_class", "_name")

    def __init__(self, pt_class: type[_PT], pt_name: str) -> None:
        """Initialize the descriptor.

        Args:
            pt_class: The PropertyType class to wrap
            pt_name: The name of the PropertyType
        """
        self._class = pt_class
        self._name = pt_name

    @overload
    def __get__(self, obj: None, owner: type) -> type[_PT]: ...

    @overload
    def __get__(self, obj: object, owner: type) -> type[_PT]: ...

    def __get__(
        self, obj: object | None, owner: type
    ) -> type[_PT]:
        """Return PropertyTypeProxy for class access, actual class for instance access.

        Args:
            obj: Instance (None for class-level access)
            owner: The class that owns this descriptor

        Returns:
            PropertyTypeProxy for class-level access, PropertyType class otherwise

        Note:
            We cast PropertyTypeProxy to type[_PT] because PropertyTypeProxy implements
            __mro_entries__ (PEP 560) which allows it to be used as a base class.
            The cast tells type checkers this is intentional.
        """
        if obj is None:
            # Class-level access: MyDB.Endpoint
            # Cast is safe because PropertyTypeProxy implements __mro_entries__
            return cast(type[_PT], PropertyTypeProxy(owner, self._name, self._class))
        # Instance-level access (rare, but return the actual class)
        return self._class

    def __set_name__(self, owner: type, name: str) -> None:
        """Called when descriptor is assigned to a class attribute."""
        self._name = name

    def __repr__(self) -> str:
        return f"<PropertyTypeDescriptor {self._name}={self._class.__name__}>"


def _is_property_type_wrapper(cls: type) -> bool:
    """Check if a class is a PropertyType wrapper (not a Resource wrapper).

    PropertyType wrappers inherit from a PropertyType subclass.
    Resource wrappers inherit from CloudFormationResource subclasses.

    Args:
        cls: The class to check.

    Returns:
        True if the class inherits from a PropertyType, False otherwise.
    """
    for base in cls.__bases__:
        if base is PropertyType:
            continue
        if isinstance(base, type) and issubclass(base, PropertyType):
            # It's a PropertyType subclass, but make sure it's not a CloudFormationResource
            if not issubclass(base, CloudFormationResource):
                return True
    return False


def _get_property_type_base(cls: type) -> type | None:
    """Get the PropertyType base class from a wrapper class.

    Args:
        cls: The wrapper class to inspect.

    Returns:
        The PropertyType subclass that cls inherits from, or None.
    """
    for base in cls.__bases__:
        if base is PropertyType:
            continue
        if isinstance(base, type) and issubclass(base, PropertyType):
            if not issubclass(base, CloudFormationResource):
                return base
    return None


def _instantiate_property_type_wrapper(wrapper_cls: type) -> Any:
    """Create a PropertyType instance from a wrapper class.

    Wrapper classes inherit from a PropertyType subclass. This function
    extracts the property values from the wrapper and creates an actual
    PropertyType instance.

    Args:
        wrapper_cls: A class that inherits from a PropertyType.

    Returns:
        An instance of the PropertyType with values from the wrapper.
    """
    # Get the PropertyType class from the wrapper's base classes
    property_type_cls = _get_property_type_base(wrapper_cls)
    if property_type_cls is None:
        # Shouldn't happen if _is_property_type_wrapper was True
        return None

    # Create wrapper instance to get its property values
    wrapper_instance = wrapper_cls()

    # Collect properties from wrapper (excluding private attrs)
    props: dict[str, Any] = {}
    for k, v in wrapper_instance.__dict__.items():
        if k.startswith("_") or v is None:
            continue
        # Recursively serialize nested values (handles nested wrappers, lists, etc.)
        props[k] = _serialize_value(v)

    # Create and return the PropertyType instance
    # Use to_dict() on the PropertyType instance
    property_instance = property_type_cls(**props)
    return property_instance


def _serialize_value(value: Any) -> Any:
    """Recursively serialize a value for CloudFormation JSON.

    Args:
        value: The value to serialize. Can be a primitive, list, dict,
            or object with a to_dict() method.

    Returns:
        The serialized value suitable for CloudFormation JSON output.
    """
    # Handle unresolved placeholders (should be resolved by loader, but handle gracefully)
    if isinstance(value, _ClassPlaceholder):
        from wetwire_aws.intrinsics import Ref

        return Ref(value._name).to_dict()
    # Handle no-parens pattern: AttrRef markers (e.g., MyRole.Arn)
    if is_attr_ref(value):
        from wetwire_aws.intrinsics import GetAtt

        return GetAtt(value.target.__name__, value.attr).to_dict()
    # Handle PropertyTypeProxy (e.g., MyDB.Endpoint without further attribute access)
    # This shouldn't typically happen but can occur if PropertyType is used directly
    if isinstance(value, PropertyTypeProxy):
        from wetwire_aws.intrinsics import GetAtt

        resource_name = (
            value._resource.__name__
            if isinstance(value._resource, type)
            else value._resource
        )
        return GetAtt(resource_name, value._name).to_dict()
    # Handle no-parens pattern: class references (e.g., MyBucket)
    # Also handle plain class types that inherit from CloudFormationResource or PropertyType
    if is_class_ref(value) or (
        isinstance(value, type)
        and (
            issubclass(value, CloudFormationResource) or issubclass(value, PropertyType)
        )
    ):
        # Check if this is a PropertyType wrapper - if so, instantiate and serialize
        if _is_property_type_wrapper(value):
            property_instance = _instantiate_property_type_wrapper(value)
            if property_instance is not None and hasattr(property_instance, "to_dict"):
                return property_instance.to_dict()
        # Otherwise it's a Resource wrapper - serialize as Ref
        from wetwire_aws.intrinsics import Ref

        return Ref(value.__name__).to_dict()
    # Handle PolicyDocument/PolicyStatement subclasses (used in IAM policies)
    # These are classes that define policy documents with class attributes
    if isinstance(value, type) and issubclass(
        value, (PolicyDocument, PolicyStatement, DenyStatement)
    ):
        # Instantiate and serialize the policy class
        instance = value()
        return instance.to_dict()
    # Check for to_dict method - use callable() to avoid AttrRef false positives
    # (AttrRef's __getattr__ returns AttrRef for any attribute access)
    # Only call on instances, not classes (to avoid missing 'self' errors)
    if not isinstance(value, type):
        to_dict_method = getattr(value, "to_dict", None)
        if to_dict_method is not None and callable(to_dict_method):
            return to_dict_method()
    if isinstance(value, list):
        return [_serialize_value(item) for item in value]
    if isinstance(value, dict):
        return {k: _serialize_value(v) for k, v in value.items()}
    return value


def _to_cf_name(snake_name: str) -> str:
    """Convert snake_case to PascalCase for CloudFormation.

    Args:
        snake_name: A snake_case property name (e.g., "bucket_name").
            Trailing underscores are stripped to handle Python keyword escapes.

    Returns:
        PascalCase string (e.g., "BucketName").
    """
    # Strip trailing underscore (used for Python keyword escape)
    if snake_name.endswith("_") and not snake_name.endswith("__"):
        snake_name = snake_name[:-1]
    return "".join(word.capitalize() for word in snake_name.split("_"))


@dataclass
class PropertyType(PropertyTypeBase):
    """
    Base class for CloudFormation property types (nested structures).

    Property types represent complex nested properties within resources,
    such as S3 Bucket's VersioningConfiguration or EC2 Instance's BlockDeviceMapping.
    """

    # Mapping from Python property names to CloudFormation names for special cases
    # (e.g., sse_algorithm -> SSEAlgorithm where simple PascalCase won't work)
    _property_mappings: ClassVar[dict[str, str]] = {}

    def to_dict(self) -> dict[str, Any]:
        """Convert property to CloudFormation-compatible dict.

        Transforms all instance attributes to PascalCase keys and recursively
        serializes nested values. None values and empty collections are omitted.

        Returns:
            Dict with PascalCase keys suitable for CloudFormation JSON.
        """
        result: dict[str, Any] = {}

        for prop_name, prop_value in self.__dict__.items():
            if prop_value is None:
                continue
            if prop_name.startswith("_"):
                continue
            # Skip empty lists and dicts (they're just default values)
            if isinstance(prop_value, (list, dict)) and len(prop_value) == 0:
                continue

            # Check for explicit property mapping first
            if prop_name in self._property_mappings:
                cf_name = self._property_mappings[prop_name]
            else:
                # Convert to CloudFormation property name (snake_case to PascalCase)
                cf_name = _to_cf_name(prop_name)
            result[cf_name] = _serialize_value(prop_value)

        return result


@dataclass
class Tag(PropertyType):
    """
    Standard AWS resource tag.

    Most AWS resources support tagging via a list of Tag objects.
    This is defined centrally to avoid generating 200+ identical copies.

    Example:
        >>> tags = [Tag(key="Environment", value="Production")]
    """

    key: str | None = None
    value: str | None = None


@dataclass
class PolicyStatement:
    """
    IAM Policy Statement for use with the wrapper dataclass pattern.

    This class allows you to define IAM policy statements as separate
    dataclasses that can be referenced by PolicyDocument and Role resources.

    Note: Uses 'resource_arn' instead of 'resource' to avoid conflicts
    with the wrapper pattern's 'resource:' type annotation field.

    Example:
        @wetwire_aws
        class AllowS3ReadStatement:
            resource: PolicyStatement
            action = ["s3:GetObject", "s3:ListBucket"]
            resource_arn = [MyBucket.Arn, Sub("${MyBucket.Arn}/*")]

        @wetwire_aws
        class MyPolicy:
            resource: PolicyDocument
            statement = [AllowS3ReadStatement]
    """

    sid: str | None = None
    effect: str = "Allow"
    principal: Any = None
    action: Any = None
    resource_arn: Any = None
    condition: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        """Serialize statement to IAM policy format."""
        stmt: dict[str, Any] = {"Effect": self.effect}

        if self.sid:
            stmt["Sid"] = self.sid
        if self.principal is not None:
            stmt["Principal"] = _serialize_value(self.principal)
        if self.action is not None:
            stmt["Action"] = _serialize_value(self.action)
        if self.resource_arn is not None:
            stmt["Resource"] = _serialize_value(self.resource_arn)
        if self.condition is not None:
            stmt["Condition"] = _serialize_value(self.condition)

        return stmt


@dataclass
class DenyStatement(PolicyStatement):
    """
    IAM Deny Policy Statement.

    Subclass of PolicyStatement with effect pre-set to "Deny".

    Example:
        @wetwire_aws
        class DenyDeleteStatement:
            resource: DenyStatement
            action = ["s3:DeleteObject", "s3:DeleteBucket"]
            resource_arn = "*"
    """

    effect: str = "Deny"


@dataclass
class PolicyDocument:
    """
    IAM Policy Document for use with the wrapper dataclass pattern.

    This class allows you to define IAM policy documents as separate
    dataclasses that can be referenced by Role resources.

    Example:
        @wetwire_aws
        class AssumeRolePolicy:
            resource: PolicyDocument
            statement = [AllowAssumeRoleStatement]

        @wetwire_aws
        class MyRole:
            resource: iam.Role
            assume_role_policy_document = AssumeRolePolicy
    """

    version: str = "2012-10-17"
    statement: list[Any] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Serialize policy document to IAM format."""
        return {
            "Version": self.version,
            "Statement": [
                s.to_dict() if hasattr(s, "to_dict") else s for s in self.statement
            ],
        }


@dataclass
class CloudFormationResource(Resource, metaclass=ResourceMeta):
    """
    Base class for all CloudFormation resource types.

    Subclasses must define:
    - _resource_type: The AWS resource type (e.g., "AWS::S3::Bucket")

    Optional class variables:
    - _property_mappings: Dict mapping Python names to CF property names

    The ResourceMeta metaclass provides `__getattr__` for attribute refs,
    enabling the no-parens pattern: `role = MyRole.Arn`
    """

    _resource_type: ClassVar[str] = ""
    _property_mappings: ClassVar[dict[str, str]] = {}

    # Optional resource metadata (kw_only to allow subclasses to have required fields)
    depends_on: list[type] | None = field(default=None, repr=False, kw_only=True)
    condition: str | None = field(default=None, repr=False, kw_only=True)
    metadata: dict[str, Any] | None = field(default=None, repr=False, kw_only=True)
    deletion_policy: str | None = field(default=None, repr=False, kw_only=True)
    update_replace_policy: str | None = field(default=None, repr=False, kw_only=True)

    def to_dict(self) -> dict[str, Any]:
        """Convert resource to CloudFormation-compatible dict.

        Generates a complete CloudFormation resource definition including
        Type, Properties, and optional metadata fields (DependsOn, Condition, etc.).

        Returns:
            Dict with CloudFormation resource structure:
            {"Type": "AWS::...", "Properties": {...}, ...}
        """
        properties: dict[str, Any] = {}

        # Get all fields that are actual properties (not metadata)
        metadata_fields = {
            "depends_on",
            "condition",
            "metadata",
            "deletion_policy",
            "update_replace_policy",
        }

        for prop_name, prop_value in self.__dict__.items():
            if prop_value is None:
                continue
            if prop_name.startswith("_"):
                continue
            if prop_name in metadata_fields:
                continue
            # Skip empty lists and dicts (they're just default values)
            if isinstance(prop_value, (list, dict)) and len(prop_value) == 0:
                continue

            # Check for explicit property mapping
            if prop_name in self._property_mappings:
                cf_name = self._property_mappings[prop_name]
            else:
                cf_name = _to_cf_name(prop_name)

            # Serialize the value (handles PropertyTypes, IntrinsicFunctions, etc.)
            properties[cf_name] = _serialize_value(prop_value)

        result: dict[str, Any] = {
            "Type": self._resource_type,
            "Properties": properties,
        }

        # Add optional metadata fields
        if self.depends_on:
            result["DependsOn"] = [
                dep if isinstance(dep, str) else dep.__name__ for dep in self.depends_on
            ]
        if self.condition:
            result["Condition"] = self.condition
        if self.metadata:
            result["Metadata"] = self.metadata
        if self.deletion_policy:
            result["DeletionPolicy"] = self.deletion_policy
        if self.update_replace_policy:
            result["UpdateReplacePolicy"] = self.update_replace_policy

        return result

    @classmethod
    def get_resource_type(cls) -> str:
        """Return the AWS resource type string.

        Returns:
            The CloudFormation resource type (e.g., "AWS::S3::Bucket").
        """
        return cls._resource_type


@dataclass
class Context:
    """
    Base context for environment-specific values.

    Subclass to add domain-specific values:

        @dataclass
        class AWSContext(Context):
            account_id: str = ""
            region: str = ""
            stack_name: str = ""

    Example:
        >>> ctx = Context(project="myapp", environment="production")
        >>> ctx.get("project")
        'myapp'
    """

    project: str = ""
    environment: str = ""

    def get(self, name: str, default: Any = None) -> Any:
        """
        Get a context value by name.

        Args:
            name: The context value name
            default: Default value if not found

        Returns:
            The context value or default
        """
        return getattr(self, name, default)

    def resolve(self, context_ref: object) -> Any:
        """
        Resolve a ContextRef to its value.

        Args:
            context_ref: The context reference to resolve

        Returns:
            The resolved value
        """
        # Extract the name from the ContextRef
        # ContextRef["name"] has the name as the type argument
        args = getattr(context_ref, "__args__", ())
        if args:
            name = args[0]
            if isinstance(name, str):
                return self.get(name)
        return None


# Type aliases for common context references
# These are used as type annotations: field: PROJECT
PROJECT = Annotated[str, ContextRef("project")]
ENVIRONMENT = Annotated[str, ContextRef("environment")]
