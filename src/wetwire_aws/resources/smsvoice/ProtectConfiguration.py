"""PropertyTypes for AWS::SMSVOICE::ProtectConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CountryRule(PropertyType):
    country_code: DslValue[str] | None = None
    protect_status: DslValue[str] | None = None


@dataclass
class CountryRuleSet(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mms": "MMS",
        "sms": "SMS",
        "voice": "VOICE",
    }

    mms: list[DslValue[CountryRule]] = field(default_factory=list)
    sms: list[DslValue[CountryRule]] = field(default_factory=list)
    voice: list[DslValue[CountryRule]] = field(default_factory=list)
