"""PropertyTypes for AWS::ElastiCache::ServerlessCache."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CacheUsageLimits(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ecpu_per_second": "ECPUPerSecond",
    }

    data_storage: DslValue[DataStorage] | None = None
    ecpu_per_second: DslValue[ECPUPerSecond] | None = None


@dataclass
class DataStorage(PropertyType):
    unit: DslValue[str] | None = None
    maximum: DslValue[int] | None = None
    minimum: DslValue[int] | None = None


@dataclass
class ECPUPerSecond(PropertyType):
    maximum: DslValue[int] | None = None
    minimum: DslValue[int] | None = None


@dataclass
class Endpoint(PropertyType):
    address: DslValue[str] | None = None
    port: DslValue[str] | None = None
