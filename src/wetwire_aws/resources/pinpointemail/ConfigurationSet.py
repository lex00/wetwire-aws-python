"""PropertyTypes for AWS::PinpointEmail::ConfigurationSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DeliveryOptions(PropertyType):
    sending_pool_name: DslValue[str] | None = None


@dataclass
class ReputationOptions(PropertyType):
    reputation_metrics_enabled: DslValue[bool] | None = None


@dataclass
class SendingOptions(PropertyType):
    sending_enabled: DslValue[bool] | None = None


@dataclass
class Tags(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class TrackingOptions(PropertyType):
    custom_redirect_domain: DslValue[str] | None = None
