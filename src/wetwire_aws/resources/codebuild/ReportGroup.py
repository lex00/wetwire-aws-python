"""PropertyTypes for AWS::CodeBuild::ReportGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ReportExportConfig(PropertyType):
    export_config_type: str | None = None
    s3_destination: S3ReportExportConfig | None = None


@dataclass
class S3ReportExportConfig(PropertyType):
    bucket: str | None = None
    bucket_owner: str | None = None
    encryption_disabled: bool | None = None
    encryption_key: str | None = None
    packaging: str | None = None
    path: str | None = None
