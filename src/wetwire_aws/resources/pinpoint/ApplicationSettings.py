"""PropertyTypes for AWS::Pinpoint::ApplicationSettings."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CampaignHook(PropertyType):
    lambda_function_name: str | None = None
    mode: str | None = None
    web_url: str | None = None


@dataclass
class Limits(PropertyType):
    daily: int | None = None
    maximum_duration: int | None = None
    messages_per_second: int | None = None
    total: int | None = None


@dataclass
class QuietTime(PropertyType):
    end: str | None = None
    start: str | None = None
