"""PropertyTypes for AWS::Lex::BotVersion."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BotVersionLocaleDetails(PropertyType):
    source_bot_version: str | None = None


@dataclass
class BotVersionLocaleSpecification(PropertyType):
    bot_version_locale_details: BotVersionLocaleDetails | None = None
    locale_id: str | None = None
