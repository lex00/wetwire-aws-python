"""PropertyTypes for AWS::IoTAnalytics::Channel."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ChannelStorage(PropertyType):
    customer_managed_s3: DslValue[CustomerManagedS3] | None = None
    service_managed_s3: DslValue[dict[str, Any]] | None = None


@dataclass
class CustomerManagedS3(PropertyType):
    bucket: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    key_prefix: DslValue[str] | None = None


@dataclass
class RetentionPeriod(PropertyType):
    number_of_days: DslValue[int] | None = None
    unlimited: DslValue[bool] | None = None
