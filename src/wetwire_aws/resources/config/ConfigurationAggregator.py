"""PropertyTypes for AWS::Config::ConfigurationAggregator."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AccountAggregationSource(PropertyType):
    account_ids: list[DslValue[str]] = field(default_factory=list)
    all_aws_regions: DslValue[bool] | None = None
    aws_regions: list[DslValue[str]] = field(default_factory=list)


@dataclass
class OrganizationAggregationSource(PropertyType):
    role_arn: DslValue[str] | None = None
    all_aws_regions: DslValue[bool] | None = None
    aws_regions: list[DslValue[str]] = field(default_factory=list)
