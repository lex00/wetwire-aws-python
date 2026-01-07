"""PropertyTypes for AWS::QBusiness::DataSource."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AudioExtractionConfiguration(PropertyType):
    audio_extraction_status: DslValue[str] | None = None


@dataclass
class DataSourceVpcConfiguration(PropertyType):
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnet_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class DocumentAttributeCondition(PropertyType):
    key: DslValue[str] | None = None
    operator: DslValue[str] | None = None
    value: DslValue[DocumentAttributeValue] | None = None


@dataclass
class DocumentAttributeTarget(PropertyType):
    key: DslValue[str] | None = None
    attribute_value_operator: DslValue[str] | None = None
    value: DslValue[DocumentAttributeValue] | None = None


@dataclass
class DocumentAttributeValue(PropertyType):
    date_value: DslValue[str] | None = None
    long_value: DslValue[float] | None = None
    string_list_value: list[DslValue[str]] = field(default_factory=list)
    string_value: DslValue[str] | None = None


@dataclass
class DocumentEnrichmentConfiguration(PropertyType):
    inline_configurations: list[DslValue[InlineDocumentEnrichmentConfiguration]] = (
        field(default_factory=list)
    )
    post_extraction_hook_configuration: DslValue[HookConfiguration] | None = None
    pre_extraction_hook_configuration: DslValue[HookConfiguration] | None = None


@dataclass
class HookConfiguration(PropertyType):
    invocation_condition: DslValue[DocumentAttributeCondition] | None = None
    lambda_arn: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    s3_bucket_name: DslValue[str] | None = None


@dataclass
class ImageExtractionConfiguration(PropertyType):
    image_extraction_status: DslValue[str] | None = None


@dataclass
class InlineDocumentEnrichmentConfiguration(PropertyType):
    condition: DslValue[DocumentAttributeCondition] | None = None
    document_content_operator: DslValue[str] | None = None
    target: DslValue[DocumentAttributeTarget] | None = None


@dataclass
class MediaExtractionConfiguration(PropertyType):
    audio_extraction_configuration: DslValue[AudioExtractionConfiguration] | None = None
    image_extraction_configuration: DslValue[ImageExtractionConfiguration] | None = None
    video_extraction_configuration: DslValue[VideoExtractionConfiguration] | None = None


@dataclass
class VideoExtractionConfiguration(PropertyType):
    video_extraction_status: DslValue[str] | None = None
