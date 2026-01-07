"""PropertyTypes for AWS::CustomerProfiles::Domain."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AttributeTypesSelector(PropertyType):
    attribute_matching_model: DslValue[str] | None = None
    address: list[DslValue[str]] = field(default_factory=list)
    email_address: list[DslValue[str]] = field(default_factory=list)
    phone_number: list[DslValue[str]] = field(default_factory=list)


@dataclass
class AutoMerging(PropertyType):
    enabled: DslValue[bool] | None = None
    conflict_resolution: DslValue[ConflictResolution] | None = None
    consolidation: DslValue[Consolidation] | None = None
    min_allowed_confidence_score_for_merging: DslValue[float] | None = None


@dataclass
class ConflictResolution(PropertyType):
    conflict_resolving_model: DslValue[str] | None = None
    source_name: DslValue[str] | None = None


@dataclass
class Consolidation(PropertyType):
    matching_attributes_list: DslValue[dict[str, Any]] | None = None


@dataclass
class DataStore(PropertyType):
    enabled: DslValue[bool] | None = None
    readiness: DslValue[Readiness] | None = None


@dataclass
class DomainStats(PropertyType):
    metering_profile_count: DslValue[float] | None = None
    object_count: DslValue[float] | None = None
    profile_count: DslValue[float] | None = None
    total_size: DslValue[float] | None = None


@dataclass
class ExportingConfig(PropertyType):
    s3_exporting: DslValue[S3ExportingConfig] | None = None


@dataclass
class JobSchedule(PropertyType):
    day_of_the_week: DslValue[str] | None = None
    time: DslValue[str] | None = None


@dataclass
class Matching(PropertyType):
    enabled: DslValue[bool] | None = None
    auto_merging: DslValue[AutoMerging] | None = None
    exporting_config: DslValue[ExportingConfig] | None = None
    job_schedule: DslValue[JobSchedule] | None = None


@dataclass
class MatchingRule(PropertyType):
    rule: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Readiness(PropertyType):
    message: DslValue[str] | None = None
    progress_percentage: DslValue[int] | None = None


@dataclass
class RuleBasedMatching(PropertyType):
    enabled: DslValue[bool] | None = None
    attribute_types_selector: DslValue[AttributeTypesSelector] | None = None
    conflict_resolution: DslValue[ConflictResolution] | None = None
    exporting_config: DslValue[ExportingConfig] | None = None
    matching_rules: list[DslValue[MatchingRule]] = field(default_factory=list)
    max_allowed_rule_level_for_matching: DslValue[int] | None = None
    max_allowed_rule_level_for_merging: DslValue[int] | None = None
    status: DslValue[str] | None = None


@dataclass
class S3ExportingConfig(PropertyType):
    s3_bucket_name: DslValue[str] | None = None
    s3_key_name: DslValue[str] | None = None
