"""PropertyTypes for AWS::Cognito::UserPoolUser."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AttributeType(PropertyType):
    name: str | None = None
    value: str | None = None
