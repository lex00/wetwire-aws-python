"""PropertyTypes for AWS::Config::ConfigurationRecorder."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ExclusionByResourceTypes(PropertyType):
    resource_types: list[DslValue[str]] = field(default_factory=list)


@dataclass
class RecordingGroup(PropertyType):
    all_supported: DslValue[bool] | None = None
    exclusion_by_resource_types: DslValue[ExclusionByResourceTypes] | None = None
    include_global_resource_types: DslValue[bool] | None = None
    recording_strategy: DslValue[RecordingStrategy] | None = None
    resource_types: list[DslValue[str]] = field(default_factory=list)


@dataclass
class RecordingMode(PropertyType):
    recording_frequency: DslValue[str] | None = None
    recording_mode_overrides: list[DslValue[RecordingModeOverride]] = field(
        default_factory=list
    )


@dataclass
class RecordingModeOverride(PropertyType):
    recording_frequency: DslValue[str] | None = None
    resource_types: list[DslValue[str]] = field(default_factory=list)
    description: DslValue[str] | None = None


@dataclass
class RecordingStrategy(PropertyType):
    use_only: DslValue[str] | None = None
