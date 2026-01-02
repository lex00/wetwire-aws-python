"""PropertyTypes for AWS::IoTSiteWise::ComputationModel."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AnomalyDetectionComputationModelConfiguration(PropertyType):
    input_properties: str | None = None
    result_property: str | None = None


@dataclass
class AssetModelPropertyBindingValue(PropertyType):
    asset_model_id: str | None = None
    property_id: str | None = None


@dataclass
class AssetPropertyBindingValue(PropertyType):
    asset_id: str | None = None
    property_id: str | None = None


@dataclass
class ComputationModelConfiguration(PropertyType):
    anomaly_detection: AnomalyDetectionComputationModelConfiguration | None = None


@dataclass
class ComputationModelDataBindingValue(PropertyType):
    asset_model_property: AssetModelPropertyBindingValue | None = None
    asset_property: AssetPropertyBindingValue | None = None
    list: list[ComputationModelDataBindingValue] = field(default_factory=list)
