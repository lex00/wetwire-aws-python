"""PropertyTypes for AWS::CleanRooms::AnalysisTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AnalysisParameter(PropertyType):
    name: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    default_value: DslValue[str] | None = None


@dataclass
class AnalysisSchema(PropertyType):
    referenced_tables: list[DslValue[str]] = field(default_factory=list)


@dataclass
class AnalysisSource(PropertyType):
    artifacts: DslValue[AnalysisTemplateArtifacts] | None = None
    text: DslValue[str] | None = None


@dataclass
class AnalysisSourceMetadata(PropertyType):
    artifacts: DslValue[AnalysisTemplateArtifactMetadata] | None = None


@dataclass
class AnalysisTemplateArtifact(PropertyType):
    location: DslValue[S3Location] | None = None


@dataclass
class AnalysisTemplateArtifactMetadata(PropertyType):
    entry_point_hash: DslValue[Hash] | None = None
    additional_artifact_hashes: list[DslValue[Hash]] = field(default_factory=list)


@dataclass
class AnalysisTemplateArtifacts(PropertyType):
    entry_point: DslValue[AnalysisTemplateArtifact] | None = None
    role_arn: DslValue[str] | None = None
    additional_artifacts: list[DslValue[AnalysisTemplateArtifact]] = field(
        default_factory=list
    )


@dataclass
class ColumnClassificationDetails(PropertyType):
    column_mapping: list[DslValue[SyntheticDataColumnProperties]] = field(
        default_factory=list
    )


@dataclass
class ErrorMessageConfiguration(PropertyType):
    type_: DslValue[str] | None = None


@dataclass
class Hash(PropertyType):
    sha256: DslValue[str] | None = None


@dataclass
class MLSyntheticDataParameters(PropertyType):
    column_classification: DslValue[ColumnClassificationDetails] | None = None
    epsilon: DslValue[float] | None = None
    max_membership_inference_attack_score: DslValue[float] | None = None


@dataclass
class S3Location(PropertyType):
    bucket: DslValue[str] | None = None
    key: DslValue[str] | None = None


@dataclass
class SyntheticDataColumnProperties(PropertyType):
    column_name: DslValue[str] | None = None
    column_type: DslValue[str] | None = None
    is_predictive_value: DslValue[bool] | None = None


@dataclass
class SyntheticDataParameters(PropertyType):
    ml_synthetic_data_parameters: DslValue[MLSyntheticDataParameters] | None = None
