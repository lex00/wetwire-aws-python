"""PropertyTypes for AWS::PinpointEmail::Identity."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class MailFromAttributes(PropertyType):
    behavior_on_mx_failure: DslValue[str] | None = None
    mail_from_domain: DslValue[str] | None = None


@dataclass
class Tags(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None
