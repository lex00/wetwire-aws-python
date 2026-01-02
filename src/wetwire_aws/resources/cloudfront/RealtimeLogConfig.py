"""PropertyTypes for AWS::CloudFront::RealtimeLogConfig."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EndPoint(PropertyType):
    kinesis_stream_config: KinesisStreamConfig | None = None
    stream_type: str | None = None


@dataclass
class KinesisStreamConfig(PropertyType):
    role_arn: str | None = None
    stream_arn: str | None = None
