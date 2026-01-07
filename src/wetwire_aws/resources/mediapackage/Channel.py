"""PropertyTypes for AWS::MediaPackage::Channel."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class HlsIngest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ingest_endpoints": "ingestEndpoints",
    }

    ingest_endpoints: list[DslValue[IngestEndpoint]] = field(default_factory=list)


@dataclass
class IngestEndpoint(PropertyType):
    id: DslValue[str] | None = None
    password: DslValue[str] | None = None
    url: DslValue[str] | None = None
    username: DslValue[str] | None = None


@dataclass
class LogConfiguration(PropertyType):
    log_group_name: DslValue[str] | None = None
