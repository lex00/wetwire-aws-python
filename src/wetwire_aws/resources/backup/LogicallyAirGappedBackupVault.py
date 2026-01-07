"""PropertyTypes for AWS::Backup::LogicallyAirGappedBackupVault."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class NotificationObjectType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sns_topic_arn": "SNSTopicArn",
    }

    backup_vault_events: list[DslValue[str]] = field(default_factory=list)
    sns_topic_arn: DslValue[str] | None = None
