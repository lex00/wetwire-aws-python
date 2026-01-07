"""PropertyTypes for AWS::Lex::BotVersion."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BotVersionLocaleDetails(PropertyType):
    source_bot_version: DslValue[str] | None = None


@dataclass
class BotVersionLocaleSpecification(PropertyType):
    bot_version_locale_details: DslValue[BotVersionLocaleDetails] | None = None
    locale_id: DslValue[str] | None = None
