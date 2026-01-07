"""PropertyTypes for AWS::Cognito::IdentityPool."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CognitoIdentityProvider(PropertyType):
    client_id: DslValue[str] | None = None
    provider_name: DslValue[str] | None = None
    server_side_token_check: DslValue[bool] | None = None


@dataclass
class CognitoStreams(PropertyType):
    role_arn: DslValue[str] | None = None
    stream_name: DslValue[str] | None = None
    streaming_status: DslValue[str] | None = None


@dataclass
class PushSync(PropertyType):
    application_arns: list[DslValue[str]] = field(default_factory=list)
    role_arn: DslValue[str] | None = None
