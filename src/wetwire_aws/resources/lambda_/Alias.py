"""PropertyTypes for AWS::Lambda::Alias."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AliasRoutingConfiguration(PropertyType):
    additional_version_weights: list[DslValue[VersionWeight]] = field(
        default_factory=list
    )


@dataclass
class ProvisionedConcurrencyConfiguration(PropertyType):
    provisioned_concurrent_executions: DslValue[int] | None = None


@dataclass
class VersionWeight(PropertyType):
    function_version: DslValue[str] | None = None
    function_weight: DslValue[float] | None = None
