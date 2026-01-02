"""PropertyTypes for AWS::Backup::ReportPlan."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ReportDeliveryChannel(PropertyType):
    s3_bucket_name: str | None = None
    formats: list[String] = field(default_factory=list)
    s3_key_prefix: str | None = None


@dataclass
class ReportSetting(PropertyType):
    report_template: str | None = None
    accounts: list[String] = field(default_factory=list)
    framework_arns: list[String] = field(default_factory=list)
    organization_units: list[String] = field(default_factory=list)
    regions: list[String] = field(default_factory=list)
