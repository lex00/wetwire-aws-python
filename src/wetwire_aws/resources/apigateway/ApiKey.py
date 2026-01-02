"""PropertyTypes for AWS::ApiGateway::ApiKey."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class StageKey(PropertyType):
    rest_api_id: str | None = None
    stage_name: str | None = None
