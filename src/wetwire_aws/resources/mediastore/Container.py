"""PropertyTypes for AWS::MediaStore::Container."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CorsRule(PropertyType):
    allowed_headers: list[String] = field(default_factory=list)
    allowed_methods: list[String] = field(default_factory=list)
    allowed_origins: list[String] = field(default_factory=list)
    expose_headers: list[String] = field(default_factory=list)
    max_age_seconds: int | None = None


@dataclass
class MetricPolicy(PropertyType):
    container_level_metrics: str | None = None
    metric_policy_rules: list[MetricPolicyRule] = field(default_factory=list)


@dataclass
class MetricPolicyRule(PropertyType):
    object_group: str | None = None
    object_group_name: str | None = None
