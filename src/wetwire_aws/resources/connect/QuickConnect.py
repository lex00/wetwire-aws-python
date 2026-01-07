"""PropertyTypes for AWS::Connect::QuickConnect."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class PhoneNumberQuickConnectConfig(PropertyType):
    phone_number: DslValue[str] | None = None


@dataclass
class QueueQuickConnectConfig(PropertyType):
    contact_flow_arn: DslValue[str] | None = None
    queue_arn: DslValue[str] | None = None


@dataclass
class QuickConnectConfig(PropertyType):
    quick_connect_type: DslValue[str] | None = None
    phone_config: DslValue[PhoneNumberQuickConnectConfig] | None = None
    queue_config: DslValue[QueueQuickConnectConfig] | None = None
    user_config: DslValue[UserQuickConnectConfig] | None = None


@dataclass
class UserQuickConnectConfig(PropertyType):
    contact_flow_arn: DslValue[str] | None = None
    user_arn: DslValue[str] | None = None
