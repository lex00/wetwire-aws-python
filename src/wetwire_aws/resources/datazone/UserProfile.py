"""PropertyTypes for AWS::DataZone::UserProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class IamUserProfileDetails(PropertyType):
    arn: DslValue[str] | None = None


@dataclass
class SsoUserProfileDetails(PropertyType):
    first_name: DslValue[str] | None = None
    last_name: DslValue[str] | None = None
    username: DslValue[str] | None = None


@dataclass
class UserProfileDetails(PropertyType):
    iam: DslValue[IamUserProfileDetails] | None = None
    sso: DslValue[SsoUserProfileDetails] | None = None
