"""PropertyTypes for AWS::Glue::SecurityConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CloudWatchEncryption(PropertyType):
    cloud_watch_encryption_mode: DslValue[str] | None = None
    kms_key_arn: DslValue[str] | None = None


@dataclass
class EncryptionConfiguration(PropertyType):
    cloud_watch_encryption: DslValue[CloudWatchEncryption] | None = None
    job_bookmarks_encryption: DslValue[JobBookmarksEncryption] | None = None
    s3_encryptions: DslValue[S3Encryptions] | None = None


@dataclass
class JobBookmarksEncryption(PropertyType):
    job_bookmarks_encryption_mode: DslValue[str] | None = None
    kms_key_arn: DslValue[str] | None = None


@dataclass
class S3Encryption(PropertyType):
    kms_key_arn: DslValue[str] | None = None
    s3_encryption_mode: DslValue[str] | None = None


@dataclass
class S3Encryptions(PropertyType):
    pass
