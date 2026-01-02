"""PropertyTypes for AWS::SecurityLake::DataLake."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EncryptionConfiguration(PropertyType):
    kms_key_id: str | None = None


@dataclass
class Expiration(PropertyType):
    days: int | None = None


@dataclass
class LifecycleConfiguration(PropertyType):
    expiration: Expiration | None = None
    transitions: list[Transitions] = field(default_factory=list)


@dataclass
class ReplicationConfiguration(PropertyType):
    regions: list[String] = field(default_factory=list)
    role_arn: str | None = None


@dataclass
class Transitions(PropertyType):
    days: int | None = None
    storage_class: str | None = None
