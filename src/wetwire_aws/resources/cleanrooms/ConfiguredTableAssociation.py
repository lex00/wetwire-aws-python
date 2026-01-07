"""PropertyTypes for AWS::CleanRooms::ConfiguredTableAssociation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ConfiguredTableAssociationAnalysisRule(PropertyType):
    policy: DslValue[ConfiguredTableAssociationAnalysisRulePolicy] | None = None
    type_: DslValue[str] | None = None


@dataclass
class ConfiguredTableAssociationAnalysisRuleAggregation(PropertyType):
    allowed_additional_analyses: list[DslValue[str]] = field(default_factory=list)
    allowed_result_receivers: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ConfiguredTableAssociationAnalysisRuleCustom(PropertyType):
    allowed_additional_analyses: list[DslValue[str]] = field(default_factory=list)
    allowed_result_receivers: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ConfiguredTableAssociationAnalysisRuleList(PropertyType):
    allowed_additional_analyses: list[DslValue[str]] = field(default_factory=list)
    allowed_result_receivers: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ConfiguredTableAssociationAnalysisRulePolicy(PropertyType):
    v1: DslValue[ConfiguredTableAssociationAnalysisRulePolicyV1] | None = None


@dataclass
class ConfiguredTableAssociationAnalysisRulePolicyV1(PropertyType):
    aggregation: DslValue[ConfiguredTableAssociationAnalysisRuleAggregation] | None = (
        None
    )
    custom: DslValue[ConfiguredTableAssociationAnalysisRuleCustom] | None = None
    list: DslValue[ConfiguredTableAssociationAnalysisRuleList] | None = None
