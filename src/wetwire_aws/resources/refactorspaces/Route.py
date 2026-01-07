"""PropertyTypes for AWS::RefactorSpaces::Route."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DefaultRouteInput(PropertyType):
    activation_state: DslValue[str] | None = None


@dataclass
class UriPathRouteInput(PropertyType):
    activation_state: DslValue[str] | None = None
    append_source_path: DslValue[bool] | None = None
    include_child_paths: DslValue[bool] | None = None
    methods: list[DslValue[str]] = field(default_factory=list)
    source_path: DslValue[str] | None = None
