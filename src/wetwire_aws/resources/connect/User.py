"""PropertyTypes for AWS::Connect::User."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class UserIdentityInfo(PropertyType):
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    mobile: str | None = None
    secondary_email: str | None = None


@dataclass
class UserPhoneConfig(PropertyType):
    phone_type: str | None = None
    after_contact_work_time_limit: int | None = None
    auto_accept: bool | None = None
    desk_phone_number: str | None = None
    persistent_connection: bool | None = None


@dataclass
class UserProficiency(PropertyType):
    attribute_name: str | None = None
    attribute_value: str | None = None
    level: float | None = None
