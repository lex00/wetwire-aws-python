"""PropertyTypes for AWS::IoTAnalytics::Channel."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ChannelStorage(PropertyType):
    customer_managed_s3: CustomerManagedS3 | None = None
    service_managed_s3: dict[str, Any] | None = None


@dataclass
class CustomerManagedS3(PropertyType):
    bucket: str | None = None
    role_arn: str | None = None
    key_prefix: str | None = None


@dataclass
class RetentionPeriod(PropertyType):
    number_of_days: int | None = None
    unlimited: bool | None = None
