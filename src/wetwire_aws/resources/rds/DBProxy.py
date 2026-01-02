"""PropertyTypes for AWS::RDS::DBProxy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AuthFormat(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "iam_auth": "IAMAuth",
    }

    auth_scheme: str | None = None
    client_password_auth_type: str | None = None
    description: str | None = None
    iam_auth: str | None = None
    secret_arn: str | None = None


@dataclass
class TagFormat(PropertyType):
    key: str | None = None
    value: str | None = None
