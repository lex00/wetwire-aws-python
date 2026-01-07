"""PropertyTypes for AWS::Pinpoint::ApplicationSettings."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CampaignHook(PropertyType):
    lambda_function_name: DslValue[str] | None = None
    mode: DslValue[str] | None = None
    web_url: DslValue[str] | None = None


@dataclass
class Limits(PropertyType):
    daily: DslValue[int] | None = None
    maximum_duration: DslValue[int] | None = None
    messages_per_second: DslValue[int] | None = None
    total: DslValue[int] | None = None


@dataclass
class QuietTime(PropertyType):
    end: DslValue[str] | None = None
    start: DslValue[str] | None = None
