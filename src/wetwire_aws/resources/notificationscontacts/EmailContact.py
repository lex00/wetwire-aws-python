"""PropertyTypes for AWS::NotificationsContacts::EmailContact."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EmailContact(PropertyType):
    address: str | None = None
    arn: str | None = None
    creation_time: str | None = None
    name: str | None = None
    status: str | None = None
    update_time: str | None = None
