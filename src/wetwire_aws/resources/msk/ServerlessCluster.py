"""PropertyTypes for AWS::MSK::ServerlessCluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ClientAuthentication(PropertyType):
    sasl: DslValue[Sasl] | None = None


@dataclass
class Iam(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class Sasl(PropertyType):
    iam: DslValue[Iam] | None = None


@dataclass
class VpcConfig(PropertyType):
    subnet_ids: list[DslValue[str]] = field(default_factory=list)
    security_groups: list[DslValue[str]] = field(default_factory=list)
