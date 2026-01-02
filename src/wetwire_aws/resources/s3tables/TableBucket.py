"""PropertyTypes for AWS::S3Tables::TableBucket."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EncryptionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KMSKeyArn",
        "sse_algorithm": "SSEAlgorithm",
    }

    kms_key_arn: str | None = None
    sse_algorithm: str | None = None


@dataclass
class MetricsConfiguration(PropertyType):
    status: str | None = None


@dataclass
class StorageClassConfiguration(PropertyType):
    storage_class: str | None = None


@dataclass
class UnreferencedFileRemoval(PropertyType):
    noncurrent_days: int | None = None
    status: str | None = None
    unreferenced_days: int | None = None
