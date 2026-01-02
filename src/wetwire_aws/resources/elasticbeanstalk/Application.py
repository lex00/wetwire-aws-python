"""PropertyTypes for AWS::ElasticBeanstalk::Application."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ApplicationResourceLifecycleConfig(PropertyType):
    service_role: str | None = None
    version_lifecycle_config: ApplicationVersionLifecycleConfig | None = None


@dataclass
class ApplicationVersionLifecycleConfig(PropertyType):
    max_age_rule: MaxAgeRule | None = None
    max_count_rule: MaxCountRule | None = None


@dataclass
class MaxAgeRule(PropertyType):
    delete_source_from_s3: bool | None = None
    enabled: bool | None = None
    max_age_in_days: int | None = None


@dataclass
class MaxCountRule(PropertyType):
    delete_source_from_s3: bool | None = None
    enabled: bool | None = None
    max_count: int | None = None
