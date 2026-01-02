"""PropertyTypes for AWS::Config::ConfigurationAggregator."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AccountAggregationSource(PropertyType):
    account_ids: list[String] = field(default_factory=list)
    all_aws_regions: bool | None = None
    aws_regions: list[String] = field(default_factory=list)


@dataclass
class OrganizationAggregationSource(PropertyType):
    role_arn: str | None = None
    all_aws_regions: bool | None = None
    aws_regions: list[String] = field(default_factory=list)
