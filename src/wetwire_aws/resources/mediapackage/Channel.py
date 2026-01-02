"""PropertyTypes for AWS::MediaPackage::Channel."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class HlsIngest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ingest_endpoints": "ingestEndpoints",
    }

    ingest_endpoints: list[IngestEndpoint] = field(default_factory=list)


@dataclass
class IngestEndpoint(PropertyType):
    id: str | None = None
    password: str | None = None
    url: str | None = None
    username: str | None = None


@dataclass
class LogConfiguration(PropertyType):
    log_group_name: str | None = None
