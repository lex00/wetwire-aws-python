"""PropertyTypes for AWS::Redshift::Cluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Endpoint(PropertyType):
    address: DslValue[str] | None = None
    port: DslValue[str] | None = None


@dataclass
class LoggingProperties(PropertyType):
    bucket_name: DslValue[str] | None = None
    log_destination_type: DslValue[str] | None = None
    log_exports: list[DslValue[str]] = field(default_factory=list)
    s3_key_prefix: DslValue[str] | None = None
