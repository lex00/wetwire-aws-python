"""PropertyTypes for AWS::DataZone::UserProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class IamUserProfileDetails(PropertyType):
    arn: str | None = None


@dataclass
class SsoUserProfileDetails(PropertyType):
    first_name: str | None = None
    last_name: str | None = None
    username: str | None = None


@dataclass
class UserProfileDetails(PropertyType):
    iam: IamUserProfileDetails | None = None
    sso: SsoUserProfileDetails | None = None
