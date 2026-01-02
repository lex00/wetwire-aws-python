"""PropertyTypes for AWS::MSK::ServerlessCluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ClientAuthentication(PropertyType):
    sasl: Sasl | None = None


@dataclass
class Iam(PropertyType):
    enabled: bool | None = None


@dataclass
class Sasl(PropertyType):
    iam: Iam | None = None


@dataclass
class VpcConfig(PropertyType):
    subnet_ids: list[String] = field(default_factory=list)
    security_groups: list[String] = field(default_factory=list)
