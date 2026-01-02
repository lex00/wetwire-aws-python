"""PropertyTypes for AWS::SMSVOICE::PhoneNumber."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class MandatoryKeyword(PropertyType):
    message: str | None = None


@dataclass
class MandatoryKeywords(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "help": "HELP",
        "stop": "STOP",
    }

    help: MandatoryKeyword | None = None
    stop: MandatoryKeyword | None = None


@dataclass
class OptionalKeyword(PropertyType):
    action: str | None = None
    keyword: str | None = None
    message: str | None = None


@dataclass
class TwoWay(PropertyType):
    enabled: bool | None = None
    channel_arn: str | None = None
    channel_role: str | None = None
