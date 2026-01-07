"""PropertyTypes for AWS::Comprehend::Flywheel."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DataSecurityConfig(PropertyType):
    data_lake_kms_key_id: DslValue[str] | None = None
    model_kms_key_id: DslValue[str] | None = None
    volume_kms_key_id: DslValue[str] | None = None
    vpc_config: DslValue[VpcConfig] | None = None


@dataclass
class DocumentClassificationConfig(PropertyType):
    mode: DslValue[str] | None = None
    labels: list[DslValue[str]] = field(default_factory=list)


@dataclass
class EntityRecognitionConfig(PropertyType):
    entity_types: list[DslValue[EntityTypesListItem]] = field(default_factory=list)


@dataclass
class EntityTypesListItem(PropertyType):
    type_: DslValue[str] | None = None


@dataclass
class TaskConfig(PropertyType):
    language_code: DslValue[str] | None = None
    document_classification_config: DslValue[DocumentClassificationConfig] | None = None
    entity_recognition_config: DslValue[EntityRecognitionConfig] | None = None


@dataclass
class VpcConfig(PropertyType):
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnets: list[DslValue[str]] = field(default_factory=list)
