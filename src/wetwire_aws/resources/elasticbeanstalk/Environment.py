"""PropertyTypes for AWS::ElasticBeanstalk::Environment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class OptionSetting(PropertyType):
    namespace: str | None = None
    option_name: str | None = None
    resource_name: str | None = None
    value: str | None = None


@dataclass
class Tier(PropertyType):
    name: str | None = None
    type_: str | None = None
    version: str | None = None
