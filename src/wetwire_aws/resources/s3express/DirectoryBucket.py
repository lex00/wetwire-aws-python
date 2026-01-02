"""PropertyTypes for AWS::S3Express::DirectoryBucket."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AbortIncompleteMultipartUpload(PropertyType):
    days_after_initiation: int | None = None


@dataclass
class BucketEncryption(PropertyType):
    server_side_encryption_configuration: list[ServerSideEncryptionRule] = field(
        default_factory=list
    )


@dataclass
class LifecycleConfiguration(PropertyType):
    rules: list[Rule] = field(default_factory=list)


@dataclass
class Rule(PropertyType):
    status: str | None = None
    abort_incomplete_multipart_upload: AbortIncompleteMultipartUpload | None = None
    expiration_in_days: int | None = None
    id: str | None = None
    object_size_greater_than: str | None = None
    object_size_less_than: str | None = None
    prefix: str | None = None


@dataclass
class ServerSideEncryptionByDefault(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_master_key_id": "KMSMasterKeyID",
        "sse_algorithm": "SSEAlgorithm",
    }

    sse_algorithm: str | None = None
    kms_master_key_id: str | None = None


@dataclass
class ServerSideEncryptionRule(PropertyType):
    bucket_key_enabled: bool | None = None
    server_side_encryption_by_default: ServerSideEncryptionByDefault | None = None
