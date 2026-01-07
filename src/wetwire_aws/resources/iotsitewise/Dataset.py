"""PropertyTypes for AWS::IoTSiteWise::Dataset."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DatasetSource(PropertyType):
    source_format: DslValue[str] | None = None
    source_type: DslValue[str] | None = None
    source_detail: DslValue[SourceDetail] | None = None


@dataclass
class KendraSourceDetail(PropertyType):
    knowledge_base_arn: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None


@dataclass
class SourceDetail(PropertyType):
    kendra: DslValue[KendraSourceDetail] | None = None
