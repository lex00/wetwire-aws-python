"""PropertyTypes for AWS::CustomerProfiles::Domain."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AttributeTypesSelector(PropertyType):
    attribute_matching_model: str | None = None
    address: list[String] = field(default_factory=list)
    email_address: list[String] = field(default_factory=list)
    phone_number: list[String] = field(default_factory=list)


@dataclass
class AutoMerging(PropertyType):
    enabled: bool | None = None
    conflict_resolution: ConflictResolution | None = None
    consolidation: Consolidation | None = None
    min_allowed_confidence_score_for_merging: float | None = None


@dataclass
class ConflictResolution(PropertyType):
    conflict_resolving_model: str | None = None
    source_name: str | None = None


@dataclass
class Consolidation(PropertyType):
    matching_attributes_list: dict[str, Any] | None = None


@dataclass
class DataStore(PropertyType):
    enabled: bool | None = None
    readiness: Readiness | None = None


@dataclass
class DomainStats(PropertyType):
    metering_profile_count: float | None = None
    object_count: float | None = None
    profile_count: float | None = None
    total_size: float | None = None


@dataclass
class ExportingConfig(PropertyType):
    s3_exporting: S3ExportingConfig | None = None


@dataclass
class JobSchedule(PropertyType):
    day_of_the_week: str | None = None
    time: str | None = None


@dataclass
class Matching(PropertyType):
    enabled: bool | None = None
    auto_merging: AutoMerging | None = None
    exporting_config: ExportingConfig | None = None
    job_schedule: JobSchedule | None = None


@dataclass
class MatchingRule(PropertyType):
    rule: list[String] = field(default_factory=list)


@dataclass
class Readiness(PropertyType):
    message: str | None = None
    progress_percentage: int | None = None


@dataclass
class RuleBasedMatching(PropertyType):
    enabled: bool | None = None
    attribute_types_selector: AttributeTypesSelector | None = None
    conflict_resolution: ConflictResolution | None = None
    exporting_config: ExportingConfig | None = None
    matching_rules: list[MatchingRule] = field(default_factory=list)
    max_allowed_rule_level_for_matching: int | None = None
    max_allowed_rule_level_for_merging: int | None = None
    status: str | None = None


@dataclass
class S3ExportingConfig(PropertyType):
    s3_bucket_name: str | None = None
    s3_key_name: str | None = None
