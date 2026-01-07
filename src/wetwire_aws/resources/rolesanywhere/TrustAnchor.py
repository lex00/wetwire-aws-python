"""PropertyTypes for AWS::RolesAnywhere::TrustAnchor."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class NotificationSetting(PropertyType):
    enabled: DslValue[bool] | None = None
    event: DslValue[str] | None = None
    channel: DslValue[str] | None = None
    threshold: DslValue[float] | None = None


@dataclass
class Source(PropertyType):
    source_data: DslValue[SourceData] | None = None
    source_type: DslValue[str] | None = None


@dataclass
class SourceData(PropertyType):
    acm_pca_arn: DslValue[str] | None = None
    x509_certificate_data: DslValue[str] | None = None
