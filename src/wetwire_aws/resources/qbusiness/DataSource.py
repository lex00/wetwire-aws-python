"""PropertyTypes for AWS::QBusiness::DataSource."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AudioExtractionConfiguration(PropertyType):
    audio_extraction_status: str | None = None


@dataclass
class DataSourceVpcConfiguration(PropertyType):
    security_group_ids: list[String] = field(default_factory=list)
    subnet_ids: list[String] = field(default_factory=list)


@dataclass
class DocumentAttributeCondition(PropertyType):
    key: str | None = None
    operator: str | None = None
    value: DocumentAttributeValue | None = None


@dataclass
class DocumentAttributeTarget(PropertyType):
    key: str | None = None
    attribute_value_operator: str | None = None
    value: DocumentAttributeValue | None = None


@dataclass
class DocumentAttributeValue(PropertyType):
    date_value: str | None = None
    long_value: float | None = None
    string_list_value: list[String] = field(default_factory=list)
    string_value: str | None = None


@dataclass
class DocumentEnrichmentConfiguration(PropertyType):
    inline_configurations: list[InlineDocumentEnrichmentConfiguration] = field(
        default_factory=list
    )
    post_extraction_hook_configuration: HookConfiguration | None = None
    pre_extraction_hook_configuration: HookConfiguration | None = None


@dataclass
class HookConfiguration(PropertyType):
    invocation_condition: DocumentAttributeCondition | None = None
    lambda_arn: str | None = None
    role_arn: str | None = None
    s3_bucket_name: str | None = None


@dataclass
class ImageExtractionConfiguration(PropertyType):
    image_extraction_status: str | None = None


@dataclass
class InlineDocumentEnrichmentConfiguration(PropertyType):
    condition: DocumentAttributeCondition | None = None
    document_content_operator: str | None = None
    target: DocumentAttributeTarget | None = None


@dataclass
class MediaExtractionConfiguration(PropertyType):
    audio_extraction_configuration: AudioExtractionConfiguration | None = None
    image_extraction_configuration: ImageExtractionConfiguration | None = None
    video_extraction_configuration: VideoExtractionConfiguration | None = None


@dataclass
class VideoExtractionConfiguration(PropertyType):
    video_extraction_status: str | None = None
