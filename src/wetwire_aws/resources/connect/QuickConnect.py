"""PropertyTypes for AWS::Connect::QuickConnect."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class PhoneNumberQuickConnectConfig(PropertyType):
    phone_number: str | None = None


@dataclass
class QueueQuickConnectConfig(PropertyType):
    contact_flow_arn: str | None = None
    queue_arn: str | None = None


@dataclass
class QuickConnectConfig(PropertyType):
    quick_connect_type: str | None = None
    phone_config: PhoneNumberQuickConnectConfig | None = None
    queue_config: QueueQuickConnectConfig | None = None
    user_config: UserQuickConnectConfig | None = None


@dataclass
class UserQuickConnectConfig(PropertyType):
    contact_flow_arn: str | None = None
    user_arn: str | None = None
