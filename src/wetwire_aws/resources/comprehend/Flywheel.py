"""PropertyTypes for AWS::Comprehend::Flywheel."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DataSecurityConfig(PropertyType):
    data_lake_kms_key_id: str | None = None
    model_kms_key_id: str | None = None
    volume_kms_key_id: str | None = None
    vpc_config: VpcConfig | None = None


@dataclass
class DocumentClassificationConfig(PropertyType):
    mode: str | None = None
    labels: list[String] = field(default_factory=list)


@dataclass
class EntityRecognitionConfig(PropertyType):
    entity_types: list[EntityTypesListItem] = field(default_factory=list)


@dataclass
class EntityTypesListItem(PropertyType):
    type_: str | None = None


@dataclass
class TaskConfig(PropertyType):
    language_code: str | None = None
    document_classification_config: DocumentClassificationConfig | None = None
    entity_recognition_config: EntityRecognitionConfig | None = None


@dataclass
class VpcConfig(PropertyType):
    security_group_ids: list[String] = field(default_factory=list)
    subnets: list[String] = field(default_factory=list)
