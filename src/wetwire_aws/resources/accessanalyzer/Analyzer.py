"""PropertyTypes for AWS::AccessAnalyzer::Analyzer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AnalysisRule(PropertyType):
    exclusions: list[AnalysisRuleCriteria] = field(default_factory=list)


@dataclass
class AnalysisRuleCriteria(PropertyType):
    account_ids: list[String] = field(default_factory=list)
    resource_tags: dict[str, Any] | None = None


@dataclass
class AnalyzerConfiguration(PropertyType):
    internal_access_configuration: InternalAccessConfiguration | None = None
    unused_access_configuration: UnusedAccessConfiguration | None = None


@dataclass
class ArchiveRule(PropertyType):
    filter: list[Filter] = field(default_factory=list)
    rule_name: str | None = None


@dataclass
class Filter(PropertyType):
    property: str | None = None
    contains: list[String] = field(default_factory=list)
    eq: list[String] = field(default_factory=list)
    exists: bool | None = None
    neq: list[String] = field(default_factory=list)


@dataclass
class InternalAccessAnalysisRule(PropertyType):
    inclusions: list[InternalAccessAnalysisRuleCriteria] = field(default_factory=list)


@dataclass
class InternalAccessAnalysisRuleCriteria(PropertyType):
    account_ids: list[String] = field(default_factory=list)
    resource_arns: list[String] = field(default_factory=list)
    resource_types: list[String] = field(default_factory=list)


@dataclass
class InternalAccessConfiguration(PropertyType):
    internal_access_analysis_rule: InternalAccessAnalysisRule | None = None


@dataclass
class UnusedAccessConfiguration(PropertyType):
    analysis_rule: AnalysisRule | None = None
    unused_access_age: int | None = None
