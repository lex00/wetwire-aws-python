"""PropertyTypes for AWS::Cloud9::EnvironmentEC2."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Repository(PropertyType):
    path_component: DslValue[str] | None = None
    repository_url: DslValue[str] | None = None
