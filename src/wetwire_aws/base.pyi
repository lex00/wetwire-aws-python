"""Type stubs for base CloudFormation classes.

This stub file explicitly declares the metaclass __getattr__ behavior
that enables the no-parens pattern: MyBucket.Arn -> AttrRef

Without this stub, some type checkers cannot see that ResourceMeta.__getattr__
provides dynamic attribute access for CloudFormation GetAtt references.
"""

from dataclasses import dataclass
from typing import Any, ClassVar

from dataclass_dsl import AttrRef

class ResourceMeta(type):
    """Metaclass that provides GetAtt attribute access on resource classes.

    This enables: MyBucket.Arn -> AttrRef(MyBucket, "Arn")
    """

    def __getattr__(cls, name: str) -> AttrRef: ...


@dataclass
class PropertyType:
    """Base class for CloudFormation property types (nested structures)."""

    _property_mappings: ClassVar[dict[str, str]]

    def to_dict(self) -> dict[str, Any]: ...


@dataclass
class Tag(PropertyType):
    """Standard AWS resource tag."""

    key: str | None
    value: str | None


@dataclass
class PolicyStatement:
    """IAM Policy Statement."""

    sid: str | None
    effect: str
    principal: Any
    action: Any
    resource_arn: Any
    condition: dict[str, Any] | None

    def to_dict(self) -> dict[str, Any]: ...


@dataclass
class DenyStatement(PolicyStatement):
    """IAM Deny Policy Statement."""

    effect: str


@dataclass
class PolicyDocument:
    """IAM Policy Document."""

    version: str
    statement: list[Any]

    def to_dict(self) -> dict[str, Any]: ...


@dataclass
class CloudFormationResource(metaclass=ResourceMeta):
    """Base class for all CloudFormation resource types.

    The ResourceMeta metaclass provides __getattr__ for GetAtt references,
    enabling patterns like: role = MyRole.Arn
    """

    _resource_type: ClassVar[str]
    _property_mappings: ClassVar[dict[str, str]]

    depends_on: list[type] | None
    condition: str | None
    metadata: dict[str, Any] | None
    deletion_policy: str | None
    update_replace_policy: str | None

    def to_dict(self) -> dict[str, Any]: ...

    @classmethod
    def get_resource_type(cls) -> str: ...


@dataclass
class Context:
    """Base context for environment-specific values."""

    project: str
    environment: str

    def get(self, name: str, default: Any = None) -> Any: ...
    def resolve(self, context_ref: object) -> Any: ...
