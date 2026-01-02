"""PropertyTypes for AWS::SecurityLake::SubscriberNotification."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class HttpsNotificationConfiguration(PropertyType):
    endpoint: str | None = None
    target_role_arn: str | None = None
    authorization_api_key_name: str | None = None
    authorization_api_key_value: str | None = None
    http_method: str | None = None


@dataclass
class NotificationConfiguration(PropertyType):
    https_notification_configuration: HttpsNotificationConfiguration | None = None
    sqs_notification_configuration: dict[str, Any] | None = None
