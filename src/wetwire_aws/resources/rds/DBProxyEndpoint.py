"""PropertyTypes for AWS::RDS::DBProxyEndpoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class TagFormat(PropertyType):
    key: str | None = None
    value: str | None = None
