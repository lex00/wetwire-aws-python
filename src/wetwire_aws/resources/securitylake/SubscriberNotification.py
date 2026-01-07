"""PropertyTypes for AWS::SecurityLake::SubscriberNotification."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class HttpsNotificationConfiguration(PropertyType):
    endpoint: DslValue[str] | None = None
    target_role_arn: DslValue[str] | None = None
    authorization_api_key_name: DslValue[str] | None = None
    authorization_api_key_value: DslValue[str] | None = None
    http_method: DslValue[str] | None = None


@dataclass
class NotificationConfiguration(PropertyType):
    https_notification_configuration: (
        DslValue[HttpsNotificationConfiguration] | None
    ) = None
    sqs_notification_configuration: DslValue[dict[str, Any]] | None = None
