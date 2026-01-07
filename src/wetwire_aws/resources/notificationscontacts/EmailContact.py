"""PropertyTypes for AWS::NotificationsContacts::EmailContact."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EmailContact(PropertyType):
    address: DslValue[str] | None = None
    arn: DslValue[str] | None = None
    creation_time: DslValue[str] | None = None
    name: DslValue[str] | None = None
    status: DslValue[str] | None = None
    update_time: DslValue[str] | None = None
