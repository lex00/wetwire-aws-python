"""PropertyTypes for AWS::Connect::User."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class UserIdentityInfo(PropertyType):
    email: DslValue[str] | None = None
    first_name: DslValue[str] | None = None
    last_name: DslValue[str] | None = None
    mobile: DslValue[str] | None = None
    secondary_email: DslValue[str] | None = None


@dataclass
class UserPhoneConfig(PropertyType):
    phone_type: DslValue[str] | None = None
    after_contact_work_time_limit: DslValue[int] | None = None
    auto_accept: DslValue[bool] | None = None
    desk_phone_number: DslValue[str] | None = None
    persistent_connection: DslValue[bool] | None = None


@dataclass
class UserProficiency(PropertyType):
    attribute_name: DslValue[str] | None = None
    attribute_value: DslValue[str] | None = None
    level: DslValue[float] | None = None
