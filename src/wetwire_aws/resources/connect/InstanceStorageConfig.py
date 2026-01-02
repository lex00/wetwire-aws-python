"""PropertyTypes for AWS::Connect::InstanceStorageConfig."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EncryptionConfig(PropertyType):
    encryption_type: str | None = None
    key_id: str | None = None


@dataclass
class KinesisFirehoseConfig(PropertyType):
    firehose_arn: str | None = None


@dataclass
class KinesisStreamConfig(PropertyType):
    stream_arn: str | None = None


@dataclass
class KinesisVideoStreamConfig(PropertyType):
    encryption_config: EncryptionConfig | None = None
    prefix: str | None = None
    retention_period_hours: float | None = None


@dataclass
class S3Config(PropertyType):
    bucket_name: str | None = None
    bucket_prefix: str | None = None
    encryption_config: EncryptionConfig | None = None
