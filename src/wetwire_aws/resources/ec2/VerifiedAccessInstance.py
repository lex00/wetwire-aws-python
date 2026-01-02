"""PropertyTypes for AWS::EC2::VerifiedAccessInstance."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CloudWatchLogs(PropertyType):
    enabled: bool | None = None
    log_group: str | None = None


@dataclass
class KinesisDataFirehose(PropertyType):
    delivery_stream: str | None = None
    enabled: bool | None = None


@dataclass
class S3(PropertyType):
    bucket_name: str | None = None
    bucket_owner: str | None = None
    enabled: bool | None = None
    prefix: str | None = None


@dataclass
class VerifiedAccessLogs(PropertyType):
    cloud_watch_logs: CloudWatchLogs | None = None
    include_trust_context: bool | None = None
    kinesis_data_firehose: KinesisDataFirehose | None = None
    log_version: str | None = None
    s3: S3 | None = None


@dataclass
class VerifiedAccessTrustProvider(PropertyType):
    description: str | None = None
    device_trust_provider_type: str | None = None
    trust_provider_type: str | None = None
    user_trust_provider_type: str | None = None
    verified_access_trust_provider_id: str | None = None
