"""PropertyTypes for AWS::DataZone::EnvironmentBlueprintConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class LakeFormationConfiguration(PropertyType):
    location_registration_exclude_s3_locations: list[DslValue[str]] = field(
        default_factory=list
    )
    location_registration_role: DslValue[str] | None = None


@dataclass
class ProvisioningConfiguration(PropertyType):
    lake_formation_configuration: DslValue[LakeFormationConfiguration] | None = None


@dataclass
class RegionalParameter(PropertyType):
    parameters: dict[str, DslValue[str]] = field(default_factory=dict)
    region: DslValue[str] | None = None
