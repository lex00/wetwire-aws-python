"""PropertyTypes for AWS::RDS::DBProxy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AuthFormat(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "iam_auth": "IAMAuth",
    }

    auth_scheme: DslValue[str] | None = None
    client_password_auth_type: DslValue[str] | None = None
    description: DslValue[str] | None = None
    iam_auth: DslValue[str] | None = None
    secret_arn: DslValue[str] | None = None


@dataclass
class TagFormat(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None
