"""PropertyTypes for AWS::SageMaker::Workteam."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CognitoMemberDefinition(PropertyType):
    cognito_client_id: DslValue[str] | None = None
    cognito_user_group: DslValue[str] | None = None
    cognito_user_pool: DslValue[str] | None = None


@dataclass
class MemberDefinition(PropertyType):
    cognito_member_definition: DslValue[CognitoMemberDefinition] | None = None
    oidc_member_definition: DslValue[OidcMemberDefinition] | None = None


@dataclass
class NotificationConfiguration(PropertyType):
    notification_topic_arn: DslValue[str] | None = None


@dataclass
class OidcMemberDefinition(PropertyType):
    oidc_groups: list[DslValue[str]] = field(default_factory=list)
