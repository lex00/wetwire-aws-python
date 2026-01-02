"""PropertyTypes for AWS::Config::ConfigurationRecorder."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ExclusionByResourceTypes(PropertyType):
    resource_types: list[String] = field(default_factory=list)


@dataclass
class RecordingGroup(PropertyType):
    all_supported: bool | None = None
    exclusion_by_resource_types: ExclusionByResourceTypes | None = None
    include_global_resource_types: bool | None = None
    recording_strategy: RecordingStrategy | None = None
    resource_types: list[String] = field(default_factory=list)


@dataclass
class RecordingMode(PropertyType):
    recording_frequency: str | None = None
    recording_mode_overrides: list[RecordingModeOverride] = field(default_factory=list)


@dataclass
class RecordingModeOverride(PropertyType):
    recording_frequency: str | None = None
    resource_types: list[String] = field(default_factory=list)
    description: str | None = None


@dataclass
class RecordingStrategy(PropertyType):
    use_only: str | None = None
