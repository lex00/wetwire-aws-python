"""PropertyTypes for AWS::AccessAnalyzer::Analyzer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AnalysisRule(PropertyType):
    exclusions: list[DslValue[AnalysisRuleCriteria]] = field(default_factory=list)


@dataclass
class AnalysisRuleCriteria(PropertyType):
    account_ids: list[DslValue[str]] = field(default_factory=list)
    resource_tags: DslValue[dict[str, Any]] | None = None


@dataclass
class AnalyzerConfiguration(PropertyType):
    internal_access_configuration: DslValue[InternalAccessConfiguration] | None = None
    unused_access_configuration: DslValue[UnusedAccessConfiguration] | None = None


@dataclass
class ArchiveRule(PropertyType):
    filter: list[DslValue[Filter]] = field(default_factory=list)
    rule_name: DslValue[str] | None = None


@dataclass
class Filter(PropertyType):
    property: DslValue[str] | None = None
    contains: list[DslValue[str]] = field(default_factory=list)
    eq: list[DslValue[str]] = field(default_factory=list)
    exists: DslValue[bool] | None = None
    neq: list[DslValue[str]] = field(default_factory=list)


@dataclass
class InternalAccessAnalysisRule(PropertyType):
    inclusions: list[DslValue[InternalAccessAnalysisRuleCriteria]] = field(
        default_factory=list
    )


@dataclass
class InternalAccessAnalysisRuleCriteria(PropertyType):
    account_ids: list[DslValue[str]] = field(default_factory=list)
    resource_arns: list[DslValue[str]] = field(default_factory=list)
    resource_types: list[DslValue[str]] = field(default_factory=list)


@dataclass
class InternalAccessConfiguration(PropertyType):
    internal_access_analysis_rule: DslValue[InternalAccessAnalysisRule] | None = None


@dataclass
class UnusedAccessConfiguration(PropertyType):
    analysis_rule: DslValue[AnalysisRule] | None = None
    unused_access_age: DslValue[int] | None = None
