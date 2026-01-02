"""PropertyTypes for AWS::RolesAnywhere::TrustAnchor."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class NotificationSetting(PropertyType):
    enabled: bool | None = None
    event: str | None = None
    channel: str | None = None
    threshold: float | None = None


@dataclass
class Source(PropertyType):
    source_data: SourceData | None = None
    source_type: str | None = None


@dataclass
class SourceData(PropertyType):
    acm_pca_arn: str | None = None
    x509_certificate_data: str | None = None
