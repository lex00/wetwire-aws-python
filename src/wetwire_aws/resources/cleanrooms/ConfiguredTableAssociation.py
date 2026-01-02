"""PropertyTypes for AWS::CleanRooms::ConfiguredTableAssociation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ConfiguredTableAssociationAnalysisRule(PropertyType):
    policy: ConfiguredTableAssociationAnalysisRulePolicy | None = None
    type_: str | None = None


@dataclass
class ConfiguredTableAssociationAnalysisRuleAggregation(PropertyType):
    allowed_additional_analyses: list[String] = field(default_factory=list)
    allowed_result_receivers: list[String] = field(default_factory=list)


@dataclass
class ConfiguredTableAssociationAnalysisRuleCustom(PropertyType):
    allowed_additional_analyses: list[String] = field(default_factory=list)
    allowed_result_receivers: list[String] = field(default_factory=list)


@dataclass
class ConfiguredTableAssociationAnalysisRuleList(PropertyType):
    allowed_additional_analyses: list[String] = field(default_factory=list)
    allowed_result_receivers: list[String] = field(default_factory=list)


@dataclass
class ConfiguredTableAssociationAnalysisRulePolicy(PropertyType):
    v1: ConfiguredTableAssociationAnalysisRulePolicyV1 | None = None


@dataclass
class ConfiguredTableAssociationAnalysisRulePolicyV1(PropertyType):
    aggregation: ConfiguredTableAssociationAnalysisRuleAggregation | None = None
    custom: ConfiguredTableAssociationAnalysisRuleCustom | None = None
    list: ConfiguredTableAssociationAnalysisRuleList | None = None
