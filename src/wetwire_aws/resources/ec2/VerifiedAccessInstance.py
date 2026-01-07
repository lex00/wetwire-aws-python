"""PropertyTypes for AWS::EC2::VerifiedAccessInstance."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CloudWatchLogs(PropertyType):
    enabled: DslValue[bool] | None = None
    log_group: DslValue[str] | None = None


@dataclass
class KinesisDataFirehose(PropertyType):
    delivery_stream: DslValue[str] | None = None
    enabled: DslValue[bool] | None = None


@dataclass
class S3(PropertyType):
    bucket_name: DslValue[str] | None = None
    bucket_owner: DslValue[str] | None = None
    enabled: DslValue[bool] | None = None
    prefix: DslValue[str] | None = None


@dataclass
class VerifiedAccessLogs(PropertyType):
    cloud_watch_logs: DslValue[CloudWatchLogs] | None = None
    include_trust_context: DslValue[bool] | None = None
    kinesis_data_firehose: DslValue[KinesisDataFirehose] | None = None
    log_version: DslValue[str] | None = None
    s3: DslValue[S3] | None = None


@dataclass
class VerifiedAccessTrustProvider(PropertyType):
    description: DslValue[str] | None = None
    device_trust_provider_type: DslValue[str] | None = None
    trust_provider_type: DslValue[str] | None = None
    user_trust_provider_type: DslValue[str] | None = None
    verified_access_trust_provider_id: DslValue[str] | None = None
