"""PropertyTypes for AWS::S3Express::DirectoryBucket."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AbortIncompleteMultipartUpload(PropertyType):
    days_after_initiation: DslValue[int] | None = None


@dataclass
class BucketEncryption(PropertyType):
    server_side_encryption_configuration: list[DslValue[ServerSideEncryptionRule]] = (
        field(default_factory=list)
    )


@dataclass
class LifecycleConfiguration(PropertyType):
    rules: list[DslValue[Rule]] = field(default_factory=list)


@dataclass
class Rule(PropertyType):
    status: DslValue[str] | None = None
    abort_incomplete_multipart_upload: (
        DslValue[AbortIncompleteMultipartUpload] | None
    ) = None
    expiration_in_days: DslValue[int] | None = None
    id: DslValue[str] | None = None
    object_size_greater_than: DslValue[str] | None = None
    object_size_less_than: DslValue[str] | None = None
    prefix: DslValue[str] | None = None


@dataclass
class ServerSideEncryptionByDefault(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_master_key_id": "KMSMasterKeyID",
        "sse_algorithm": "SSEAlgorithm",
    }

    sse_algorithm: DslValue[str] | None = None
    kms_master_key_id: DslValue[str] | None = None


@dataclass
class ServerSideEncryptionRule(PropertyType):
    bucket_key_enabled: DslValue[bool] | None = None
    server_side_encryption_by_default: (
        DslValue[ServerSideEncryptionByDefault] | None
    ) = None
