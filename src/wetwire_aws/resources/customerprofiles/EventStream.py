"""PropertyTypes for AWS::CustomerProfiles::EventStream."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DestinationDetails(PropertyType):
    status: DslValue[str] | None = None
    uri: DslValue[str] | None = None
