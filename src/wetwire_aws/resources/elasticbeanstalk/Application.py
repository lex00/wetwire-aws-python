"""PropertyTypes for AWS::ElasticBeanstalk::Application."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ApplicationResourceLifecycleConfig(PropertyType):
    service_role: DslValue[str] | None = None
    version_lifecycle_config: DslValue[ApplicationVersionLifecycleConfig] | None = None


@dataclass
class ApplicationVersionLifecycleConfig(PropertyType):
    max_age_rule: DslValue[MaxAgeRule] | None = None
    max_count_rule: DslValue[MaxCountRule] | None = None


@dataclass
class MaxAgeRule(PropertyType):
    delete_source_from_s3: DslValue[bool] | None = None
    enabled: DslValue[bool] | None = None
    max_age_in_days: DslValue[int] | None = None


@dataclass
class MaxCountRule(PropertyType):
    delete_source_from_s3: DslValue[bool] | None = None
    enabled: DslValue[bool] | None = None
    max_count: DslValue[int] | None = None
