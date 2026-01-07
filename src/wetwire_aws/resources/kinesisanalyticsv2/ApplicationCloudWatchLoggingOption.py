"""PropertyTypes for AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CloudWatchLoggingOption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "log_stream_arn": "LogStreamARN",
    }

    log_stream_arn: DslValue[str] | None = None
