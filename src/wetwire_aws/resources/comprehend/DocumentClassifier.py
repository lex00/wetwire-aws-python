"""PropertyTypes for AWS::Comprehend::DocumentClassifier."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AugmentedManifestsListItem(PropertyType):
    attribute_names: list[String] = field(default_factory=list)
    s3_uri: str | None = None
    split: str | None = None


@dataclass
class DocumentClassifierDocuments(PropertyType):
    s3_uri: str | None = None
    test_s3_uri: str | None = None


@dataclass
class DocumentClassifierInputDataConfig(PropertyType):
    augmented_manifests: list[AugmentedManifestsListItem] = field(default_factory=list)
    data_format: str | None = None
    document_reader_config: DocumentReaderConfig | None = None
    document_type: str | None = None
    documents: DocumentClassifierDocuments | None = None
    label_delimiter: str | None = None
    s3_uri: str | None = None
    test_s3_uri: str | None = None


@dataclass
class DocumentClassifierOutputDataConfig(PropertyType):
    kms_key_id: str | None = None
    s3_uri: str | None = None


@dataclass
class DocumentReaderConfig(PropertyType):
    document_read_action: str | None = None
    document_read_mode: str | None = None
    feature_types: list[String] = field(default_factory=list)


@dataclass
class VpcConfig(PropertyType):
    security_group_ids: list[String] = field(default_factory=list)
    subnets: list[String] = field(default_factory=list)
