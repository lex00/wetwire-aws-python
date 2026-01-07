"""PropertyTypes for AWS::Backup::ReportPlan."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ReportDeliveryChannel(PropertyType):
    s3_bucket_name: DslValue[str] | None = None
    formats: list[DslValue[str]] = field(default_factory=list)
    s3_key_prefix: DslValue[str] | None = None


@dataclass
class ReportSetting(PropertyType):
    report_template: DslValue[str] | None = None
    accounts: list[DslValue[str]] = field(default_factory=list)
    framework_arns: list[DslValue[str]] = field(default_factory=list)
    organization_units: list[DslValue[str]] = field(default_factory=list)
    regions: list[DslValue[str]] = field(default_factory=list)
