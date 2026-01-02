"""PropertyTypes for AWS::ElastiCache::ServerlessCache."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CacheUsageLimits(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ecpu_per_second": "ECPUPerSecond",
    }

    data_storage: DataStorage | None = None
    ecpu_per_second: ECPUPerSecond | None = None


@dataclass
class DataStorage(PropertyType):
    unit: str | None = None
    maximum: int | None = None
    minimum: int | None = None


@dataclass
class ECPUPerSecond(PropertyType):
    maximum: int | None = None
    minimum: int | None = None


@dataclass
class Endpoint(PropertyType):
    address: str | None = None
    port: str | None = None
