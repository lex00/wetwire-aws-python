"""PropertyTypes for AWS::AIOps::InvestigationGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ChatbotNotificationChannel(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sns_topic_arn": "SNSTopicArn",
    }

    chat_configuration_arns: list[DslValue[str]] = field(default_factory=list)
    sns_topic_arn: DslValue[str] | None = None


@dataclass
class CrossAccountConfiguration(PropertyType):
    source_role_arn: DslValue[str] | None = None


@dataclass
class EncryptionConfigMap(PropertyType):
    encryption_configuration_type: DslValue[str] | None = None
    kms_key_id: DslValue[str] | None = None
