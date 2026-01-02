"""PropertyTypes for AWS::SMSVOICE::ProtectConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CountryRule(PropertyType):
    country_code: str | None = None
    protect_status: str | None = None


@dataclass
class CountryRuleSet(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mms": "MMS",
        "sms": "SMS",
        "voice": "VOICE",
    }

    mms: list[CountryRule] = field(default_factory=list)
    sms: list[CountryRule] = field(default_factory=list)
    voice: list[CountryRule] = field(default_factory=list)
