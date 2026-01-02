"""PropertyTypes for AWS::RefactorSpaces::Route."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DefaultRouteInput(PropertyType):
    activation_state: str | None = None


@dataclass
class UriPathRouteInput(PropertyType):
    activation_state: str | None = None
    append_source_path: bool | None = None
    include_child_paths: bool | None = None
    methods: list[String] = field(default_factory=list)
    source_path: str | None = None
