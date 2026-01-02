"""PropertyTypes for AWS::DataZone::EnvironmentBlueprintConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class LakeFormationConfiguration(PropertyType):
    location_registration_exclude_s3_locations: list[String] = field(
        default_factory=list
    )
    location_registration_role: str | None = None


@dataclass
class ProvisioningConfiguration(PropertyType):
    lake_formation_configuration: LakeFormationConfiguration | None = None


@dataclass
class RegionalParameter(PropertyType):
    parameters: dict[str, String] = field(default_factory=dict)
    region: str | None = None
