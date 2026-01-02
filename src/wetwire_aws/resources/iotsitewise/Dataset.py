"""PropertyTypes for AWS::IoTSiteWise::Dataset."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DatasetSource(PropertyType):
    source_format: str | None = None
    source_type: str | None = None
    source_detail: SourceDetail | None = None


@dataclass
class KendraSourceDetail(PropertyType):
    knowledge_base_arn: str | None = None
    role_arn: str | None = None


@dataclass
class SourceDetail(PropertyType):
    kendra: KendraSourceDetail | None = None
