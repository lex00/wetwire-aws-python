"""PropertyTypes for AWS::PinpointEmail::ConfigurationSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DeliveryOptions(PropertyType):
    sending_pool_name: str | None = None


@dataclass
class ReputationOptions(PropertyType):
    reputation_metrics_enabled: bool | None = None


@dataclass
class SendingOptions(PropertyType):
    sending_enabled: bool | None = None


@dataclass
class Tags(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class TrackingOptions(PropertyType):
    custom_redirect_domain: str | None = None
