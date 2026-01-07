"""PropertyTypes for AWS::ElasticBeanstalk::Environment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class OptionSetting(PropertyType):
    namespace: DslValue[str] | None = None
    option_name: DslValue[str] | None = None
    resource_name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class Tier(PropertyType):
    name: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    version: DslValue[str] | None = None
