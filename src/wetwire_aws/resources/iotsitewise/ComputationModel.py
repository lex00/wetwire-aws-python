"""PropertyTypes for AWS::IoTSiteWise::ComputationModel."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AnomalyDetectionComputationModelConfiguration(PropertyType):
    input_properties: DslValue[str] | None = None
    result_property: DslValue[str] | None = None


@dataclass
class AssetModelPropertyBindingValue(PropertyType):
    asset_model_id: DslValue[str] | None = None
    property_id: DslValue[str] | None = None


@dataclass
class AssetPropertyBindingValue(PropertyType):
    asset_id: DslValue[str] | None = None
    property_id: DslValue[str] | None = None


@dataclass
class ComputationModelConfiguration(PropertyType):
    anomaly_detection: (
        DslValue[AnomalyDetectionComputationModelConfiguration] | None
    ) = None


@dataclass
class ComputationModelDataBindingValue(PropertyType):
    asset_model_property: DslValue[AssetModelPropertyBindingValue] | None = None
    asset_property: DslValue[AssetPropertyBindingValue] | None = None
    list: list[DslValue[ComputationModelDataBindingValue]] = field(default_factory=list)
