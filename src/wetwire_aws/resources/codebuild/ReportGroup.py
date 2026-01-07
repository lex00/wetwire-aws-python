"""PropertyTypes for AWS::CodeBuild::ReportGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ReportExportConfig(PropertyType):
    export_config_type: DslValue[str] | None = None
    s3_destination: DslValue[S3ReportExportConfig] | None = None


@dataclass
class S3ReportExportConfig(PropertyType):
    bucket: DslValue[str] | None = None
    bucket_owner: DslValue[str] | None = None
    encryption_disabled: DslValue[bool] | None = None
    encryption_key: DslValue[str] | None = None
    packaging: DslValue[str] | None = None
    path: DslValue[str] | None = None
