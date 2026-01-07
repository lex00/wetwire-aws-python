"""PropertyTypes for AWS::Connect::InstanceStorageConfig."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EncryptionConfig(PropertyType):
    encryption_type: DslValue[str] | None = None
    key_id: DslValue[str] | None = None


@dataclass
class KinesisFirehoseConfig(PropertyType):
    firehose_arn: DslValue[str] | None = None


@dataclass
class KinesisStreamConfig(PropertyType):
    stream_arn: DslValue[str] | None = None


@dataclass
class KinesisVideoStreamConfig(PropertyType):
    encryption_config: DslValue[EncryptionConfig] | None = None
    prefix: DslValue[str] | None = None
    retention_period_hours: DslValue[float] | None = None


@dataclass
class S3Config(PropertyType):
    bucket_name: DslValue[str] | None = None
    bucket_prefix: DslValue[str] | None = None
    encryption_config: DslValue[EncryptionConfig] | None = None
