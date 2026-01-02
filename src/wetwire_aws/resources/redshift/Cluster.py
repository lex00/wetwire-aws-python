"""PropertyTypes for AWS::Redshift::Cluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Endpoint(PropertyType):
    address: str | None = None
    port: str | None = None


@dataclass
class LoggingProperties(PropertyType):
    bucket_name: str | None = None
    log_destination_type: str | None = None
    log_exports: list[String] = field(default_factory=list)
    s3_key_prefix: str | None = None
