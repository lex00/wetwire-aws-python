"""PropertyTypes for AWS::Evidently::Project."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AppConfigResourceObject(PropertyType):
    application_id: str | None = None
    environment_id: str | None = None


@dataclass
class DataDeliveryObject(PropertyType):
    log_group: str | None = None
    s3: S3Destination | None = None


@dataclass
class S3Destination(PropertyType):
    bucket_name: str | None = None
    prefix: str | None = None
