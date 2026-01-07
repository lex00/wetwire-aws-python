"""PropertyTypes for AWS::SMSVOICE::PhoneNumber."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class MandatoryKeyword(PropertyType):
    message: DslValue[str] | None = None


@dataclass
class MandatoryKeywords(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "help": "HELP",
        "stop": "STOP",
    }

    help: DslValue[MandatoryKeyword] | None = None
    stop: DslValue[MandatoryKeyword] | None = None


@dataclass
class OptionalKeyword(PropertyType):
    action: DslValue[str] | None = None
    keyword: DslValue[str] | None = None
    message: DslValue[str] | None = None


@dataclass
class TwoWay(PropertyType):
    enabled: DslValue[bool] | None = None
    channel_arn: DslValue[str] | None = None
    channel_role: DslValue[str] | None = None
