"""PropertyTypes for AWS::QBusiness::Application."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AttachmentsConfiguration(PropertyType):
    attachments_control_mode: DslValue[str] | None = None


@dataclass
class AutoSubscriptionConfiguration(PropertyType):
    auto_subscribe: DslValue[str] | None = None
    default_subscription_type: DslValue[str] | None = None


@dataclass
class EncryptionConfiguration(PropertyType):
    kms_key_id: DslValue[str] | None = None


@dataclass
class PersonalizationConfiguration(PropertyType):
    personalization_control_mode: DslValue[str] | None = None


@dataclass
class QAppsConfiguration(PropertyType):
    q_apps_control_mode: DslValue[str] | None = None


@dataclass
class QuickSightConfiguration(PropertyType):
    client_namespace: DslValue[str] | None = None
