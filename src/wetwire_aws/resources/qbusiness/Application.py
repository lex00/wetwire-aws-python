"""PropertyTypes for AWS::QBusiness::Application."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AttachmentsConfiguration(PropertyType):
    attachments_control_mode: str | None = None


@dataclass
class AutoSubscriptionConfiguration(PropertyType):
    auto_subscribe: str | None = None
    default_subscription_type: str | None = None


@dataclass
class EncryptionConfiguration(PropertyType):
    kms_key_id: str | None = None


@dataclass
class PersonalizationConfiguration(PropertyType):
    personalization_control_mode: str | None = None


@dataclass
class QAppsConfiguration(PropertyType):
    q_apps_control_mode: str | None = None


@dataclass
class QuickSightConfiguration(PropertyType):
    client_namespace: str | None = None
