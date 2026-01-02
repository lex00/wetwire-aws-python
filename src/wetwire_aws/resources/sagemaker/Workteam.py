"""PropertyTypes for AWS::SageMaker::Workteam."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CognitoMemberDefinition(PropertyType):
    cognito_client_id: str | None = None
    cognito_user_group: str | None = None
    cognito_user_pool: str | None = None


@dataclass
class MemberDefinition(PropertyType):
    cognito_member_definition: CognitoMemberDefinition | None = None
    oidc_member_definition: OidcMemberDefinition | None = None


@dataclass
class NotificationConfiguration(PropertyType):
    notification_topic_arn: str | None = None


@dataclass
class OidcMemberDefinition(PropertyType):
    oidc_groups: list[String] = field(default_factory=list)
