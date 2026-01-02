"""PropertyTypes for AWS::PinpointEmail::Identity."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class MailFromAttributes(PropertyType):
    behavior_on_mx_failure: str | None = None
    mail_from_domain: str | None = None


@dataclass
class Tags(PropertyType):
    key: str | None = None
    value: str | None = None
