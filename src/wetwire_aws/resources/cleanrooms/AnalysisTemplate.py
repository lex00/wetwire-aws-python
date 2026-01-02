"""PropertyTypes for AWS::CleanRooms::AnalysisTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AnalysisParameter(PropertyType):
    name: str | None = None
    type_: str | None = None
    default_value: str | None = None


@dataclass
class AnalysisSchema(PropertyType):
    referenced_tables: list[String] = field(default_factory=list)


@dataclass
class AnalysisSource(PropertyType):
    artifacts: AnalysisTemplateArtifacts | None = None
    text: str | None = None


@dataclass
class AnalysisSourceMetadata(PropertyType):
    artifacts: AnalysisTemplateArtifactMetadata | None = None


@dataclass
class AnalysisTemplateArtifact(PropertyType):
    location: S3Location | None = None


@dataclass
class AnalysisTemplateArtifactMetadata(PropertyType):
    entry_point_hash: Hash | None = None
    additional_artifact_hashes: list[Hash] = field(default_factory=list)


@dataclass
class AnalysisTemplateArtifacts(PropertyType):
    entry_point: AnalysisTemplateArtifact | None = None
    role_arn: str | None = None
    additional_artifacts: list[AnalysisTemplateArtifact] = field(default_factory=list)


@dataclass
class ColumnClassificationDetails(PropertyType):
    column_mapping: list[SyntheticDataColumnProperties] = field(default_factory=list)


@dataclass
class ErrorMessageConfiguration(PropertyType):
    type_: str | None = None


@dataclass
class Hash(PropertyType):
    sha256: str | None = None


@dataclass
class MLSyntheticDataParameters(PropertyType):
    column_classification: ColumnClassificationDetails | None = None
    epsilon: float | None = None
    max_membership_inference_attack_score: float | None = None


@dataclass
class S3Location(PropertyType):
    bucket: str | None = None
    key: str | None = None


@dataclass
class SyntheticDataColumnProperties(PropertyType):
    column_name: str | None = None
    column_type: str | None = None
    is_predictive_value: bool | None = None


@dataclass
class SyntheticDataParameters(PropertyType):
    ml_synthetic_data_parameters: MLSyntheticDataParameters | None = None
