"""PropertyTypes for AWS::Cognito::IdentityPool."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CognitoIdentityProvider(PropertyType):
    client_id: str | None = None
    provider_name: str | None = None
    server_side_token_check: bool | None = None


@dataclass
class CognitoStreams(PropertyType):
    role_arn: str | None = None
    stream_name: str | None = None
    streaming_status: str | None = None


@dataclass
class PushSync(PropertyType):
    application_arns: list[String] = field(default_factory=list)
    role_arn: str | None = None
