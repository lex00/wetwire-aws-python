"""PropertyTypes for AWS::Cloud9::EnvironmentEC2."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Repository(PropertyType):
    path_component: str | None = None
    repository_url: str | None = None
