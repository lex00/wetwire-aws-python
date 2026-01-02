"""PropertyTypes for AWS::AppConfig::ConfigurationProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Tags(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class Validators(PropertyType):
    content: str | None = None
    type_: str | None = None
