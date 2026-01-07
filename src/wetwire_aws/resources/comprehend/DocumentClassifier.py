"""PropertyTypes for AWS::Comprehend::DocumentClassifier."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AugmentedManifestsListItem(PropertyType):
    attribute_names: list[DslValue[str]] = field(default_factory=list)
    s3_uri: DslValue[str] | None = None
    split: DslValue[str] | None = None


@dataclass
class DocumentClassifierDocuments(PropertyType):
    s3_uri: DslValue[str] | None = None
    test_s3_uri: DslValue[str] | None = None


@dataclass
class DocumentClassifierInputDataConfig(PropertyType):
    augmented_manifests: list[DslValue[AugmentedManifestsListItem]] = field(
        default_factory=list
    )
    data_format: DslValue[str] | None = None
    document_reader_config: DslValue[DocumentReaderConfig] | None = None
    document_type: DslValue[str] | None = None
    documents: DslValue[DocumentClassifierDocuments] | None = None
    label_delimiter: DslValue[str] | None = None
    s3_uri: DslValue[str] | None = None
    test_s3_uri: DslValue[str] | None = None


@dataclass
class DocumentClassifierOutputDataConfig(PropertyType):
    kms_key_id: DslValue[str] | None = None
    s3_uri: DslValue[str] | None = None


@dataclass
class DocumentReaderConfig(PropertyType):
    document_read_action: DslValue[str] | None = None
    document_read_mode: DslValue[str] | None = None
    feature_types: list[DslValue[str]] = field(default_factory=list)


@dataclass
class VpcConfig(PropertyType):
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnets: list[DslValue[str]] = field(default_factory=list)
