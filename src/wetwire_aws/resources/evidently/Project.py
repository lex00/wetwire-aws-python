"""PropertyTypes for AWS::Evidently::Project."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AppConfigResourceObject(PropertyType):
    application_id: DslValue[str] | None = None
    environment_id: DslValue[str] | None = None


@dataclass
class DataDeliveryObject(PropertyType):
    log_group: DslValue[str] | None = None
    s3: DslValue[S3Destination] | None = None


@dataclass
class S3Destination(PropertyType):
    bucket_name: DslValue[str] | None = None
    prefix: DslValue[str] | None = None
