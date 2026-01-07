"""PropertyTypes for AWS::Cognito::UserPoolClient."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AnalyticsConfiguration(PropertyType):
    application_arn: DslValue[str] | None = None
    application_id: DslValue[str] | None = None
    external_id: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    user_data_shared: DslValue[bool] | None = None


@dataclass
class RefreshTokenRotation(PropertyType):
    feature: DslValue[str] | None = None
    retry_grace_period_seconds: DslValue[int] | None = None


@dataclass
class TokenValidityUnits(PropertyType):
    access_token: DslValue[str] | None = None
    id_token: DslValue[str] | None = None
    refresh_token: DslValue[str] | None = None
