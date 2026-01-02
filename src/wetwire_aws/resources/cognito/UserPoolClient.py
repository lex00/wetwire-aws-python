"""PropertyTypes for AWS::Cognito::UserPoolClient."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AnalyticsConfiguration(PropertyType):
    application_arn: str | None = None
    application_id: str | None = None
    external_id: str | None = None
    role_arn: str | None = None
    user_data_shared: bool | None = None


@dataclass
class RefreshTokenRotation(PropertyType):
    feature: str | None = None
    retry_grace_period_seconds: int | None = None


@dataclass
class TokenValidityUnits(PropertyType):
    access_token: str | None = None
    id_token: str | None = None
    refresh_token: str | None = None
