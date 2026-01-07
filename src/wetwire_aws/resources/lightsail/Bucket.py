"""PropertyTypes for AWS::Lightsail::Bucket."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AccessRules(PropertyType):
    allow_public_overrides: DslValue[bool] | None = None
    get_object: DslValue[str] | None = None
