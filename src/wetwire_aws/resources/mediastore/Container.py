"""PropertyTypes for AWS::MediaStore::Container."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CorsRule(PropertyType):
    allowed_headers: list[DslValue[str]] = field(default_factory=list)
    allowed_methods: list[DslValue[str]] = field(default_factory=list)
    allowed_origins: list[DslValue[str]] = field(default_factory=list)
    expose_headers: list[DslValue[str]] = field(default_factory=list)
    max_age_seconds: DslValue[int] | None = None


@dataclass
class MetricPolicy(PropertyType):
    container_level_metrics: DslValue[str] | None = None
    metric_policy_rules: list[DslValue[MetricPolicyRule]] = field(default_factory=list)


@dataclass
class MetricPolicyRule(PropertyType):
    object_group: DslValue[str] | None = None
    object_group_name: DslValue[str] | None = None
