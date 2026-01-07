"""PropertyTypes for AWS::SecurityLake::DataLake."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EncryptionConfiguration(PropertyType):
    kms_key_id: DslValue[str] | None = None


@dataclass
class Expiration(PropertyType):
    days: DslValue[int] | None = None


@dataclass
class LifecycleConfiguration(PropertyType):
    expiration: DslValue[Expiration] | None = None
    transitions: list[DslValue[Transitions]] = field(default_factory=list)


@dataclass
class ReplicationConfiguration(PropertyType):
    regions: list[DslValue[str]] = field(default_factory=list)
    role_arn: DslValue[str] | None = None


@dataclass
class Transitions(PropertyType):
    days: DslValue[int] | None = None
    storage_class: DslValue[str] | None = None
