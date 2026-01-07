"""PropertyTypes for AWS::Bedrock::DataAutomationProject."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AudioExtractionCategory(PropertyType):
    state: DslValue[str] | None = None
    type_configuration: DslValue[AudioExtractionCategoryTypeConfiguration] | None = None
    types: list[DslValue[str]] = field(default_factory=list)


@dataclass
class AudioExtractionCategoryTypeConfiguration(PropertyType):
    transcript: DslValue[TranscriptConfiguration] | None = None


@dataclass
class AudioLanguageConfiguration(PropertyType):
    generative_output_language: DslValue[str] | None = None
    identify_multiple_languages: DslValue[bool] | None = None
    input_languages: list[DslValue[str]] = field(default_factory=list)


@dataclass
class AudioOverrideConfiguration(PropertyType):
    language_configuration: DslValue[AudioLanguageConfiguration] | None = None
    modality_processing: DslValue[ModalityProcessingConfiguration] | None = None
    sensitive_data_configuration: DslValue[SensitiveDataConfiguration] | None = None


@dataclass
class AudioStandardExtraction(PropertyType):
    category: DslValue[AudioExtractionCategory] | None = None


@dataclass
class AudioStandardGenerativeField(PropertyType):
    state: DslValue[str] | None = None
    types: list[DslValue[str]] = field(default_factory=list)


@dataclass
class AudioStandardOutputConfiguration(PropertyType):
    extraction: DslValue[AudioStandardExtraction] | None = None
    generative_field: DslValue[AudioStandardGenerativeField] | None = None


@dataclass
class BlueprintItem(PropertyType):
    blueprint_arn: DslValue[str] | None = None
    blueprint_stage: DslValue[str] | None = None
    blueprint_version: DslValue[str] | None = None


@dataclass
class ChannelLabelingConfiguration(PropertyType):
    state: DslValue[str] | None = None


@dataclass
class CustomOutputConfiguration(PropertyType):
    blueprints: list[DslValue[BlueprintItem]] = field(default_factory=list)


@dataclass
class DocumentBoundingBox(PropertyType):
    state: DslValue[str] | None = None


@dataclass
class DocumentExtractionGranularity(PropertyType):
    types: list[DslValue[str]] = field(default_factory=list)


@dataclass
class DocumentOutputAdditionalFileFormat(PropertyType):
    state: DslValue[str] | None = None


@dataclass
class DocumentOutputFormat(PropertyType):
    additional_file_format: DslValue[DocumentOutputAdditionalFileFormat] | None = None
    text_format: DslValue[DocumentOutputTextFormat] | None = None


@dataclass
class DocumentOutputTextFormat(PropertyType):
    types: list[DslValue[str]] = field(default_factory=list)


@dataclass
class DocumentOverrideConfiguration(PropertyType):
    modality_processing: DslValue[ModalityProcessingConfiguration] | None = None
    sensitive_data_configuration: DslValue[SensitiveDataConfiguration] | None = None
    splitter: DslValue[SplitterConfiguration] | None = None


@dataclass
class DocumentStandardExtraction(PropertyType):
    bounding_box: DslValue[DocumentBoundingBox] | None = None
    granularity: DslValue[DocumentExtractionGranularity] | None = None


@dataclass
class DocumentStandardGenerativeField(PropertyType):
    state: DslValue[str] | None = None


@dataclass
class DocumentStandardOutputConfiguration(PropertyType):
    extraction: DslValue[DocumentStandardExtraction] | None = None
    generative_field: DslValue[DocumentStandardGenerativeField] | None = None
    output_format: DslValue[DocumentOutputFormat] | None = None


@dataclass
class ImageBoundingBox(PropertyType):
    state: DslValue[str] | None = None


@dataclass
class ImageExtractionCategory(PropertyType):
    state: DslValue[str] | None = None
    types: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ImageOverrideConfiguration(PropertyType):
    modality_processing: DslValue[ModalityProcessingConfiguration] | None = None
    sensitive_data_configuration: DslValue[SensitiveDataConfiguration] | None = None


@dataclass
class ImageStandardExtraction(PropertyType):
    bounding_box: DslValue[ImageBoundingBox] | None = None
    category: DslValue[ImageExtractionCategory] | None = None


@dataclass
class ImageStandardGenerativeField(PropertyType):
    state: DslValue[str] | None = None
    types: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ImageStandardOutputConfiguration(PropertyType):
    extraction: DslValue[ImageStandardExtraction] | None = None
    generative_field: DslValue[ImageStandardGenerativeField] | None = None


@dataclass
class ModalityProcessingConfiguration(PropertyType):
    state: DslValue[str] | None = None


@dataclass
class ModalityRoutingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "jpeg": "jpeg",
        "mov": "mov",
        "mp4": "mp4",
        "png": "png",
    }

    jpeg: DslValue[str] | None = None
    mov: DslValue[str] | None = None
    mp4: DslValue[str] | None = None
    png: DslValue[str] | None = None


@dataclass
class OverrideConfiguration(PropertyType):
    audio: DslValue[AudioOverrideConfiguration] | None = None
    document: DslValue[DocumentOverrideConfiguration] | None = None
    image: DslValue[ImageOverrideConfiguration] | None = None
    modality_routing: DslValue[ModalityRoutingConfiguration] | None = None
    video: DslValue[VideoOverrideConfiguration] | None = None


@dataclass
class PIIEntitiesConfiguration(PropertyType):
    pii_entity_types: list[DslValue[str]] = field(default_factory=list)
    redaction_mask_mode: DslValue[str] | None = None


@dataclass
class SensitiveDataConfiguration(PropertyType):
    detection_mode: DslValue[str] | None = None
    detection_scope: list[DslValue[str]] = field(default_factory=list)
    pii_entities_configuration: DslValue[PIIEntitiesConfiguration] | None = None


@dataclass
class SpeakerLabelingConfiguration(PropertyType):
    state: DslValue[str] | None = None


@dataclass
class SplitterConfiguration(PropertyType):
    state: DslValue[str] | None = None


@dataclass
class StandardOutputConfiguration(PropertyType):
    audio: DslValue[AudioStandardOutputConfiguration] | None = None
    document: DslValue[DocumentStandardOutputConfiguration] | None = None
    image: DslValue[ImageStandardOutputConfiguration] | None = None
    video: DslValue[VideoStandardOutputConfiguration] | None = None


@dataclass
class TranscriptConfiguration(PropertyType):
    channel_labeling: DslValue[ChannelLabelingConfiguration] | None = None
    speaker_labeling: DslValue[SpeakerLabelingConfiguration] | None = None


@dataclass
class VideoBoundingBox(PropertyType):
    state: DslValue[str] | None = None


@dataclass
class VideoExtractionCategory(PropertyType):
    state: DslValue[str] | None = None
    types: list[DslValue[str]] = field(default_factory=list)


@dataclass
class VideoOverrideConfiguration(PropertyType):
    modality_processing: DslValue[ModalityProcessingConfiguration] | None = None
    sensitive_data_configuration: DslValue[SensitiveDataConfiguration] | None = None


@dataclass
class VideoStandardExtraction(PropertyType):
    bounding_box: DslValue[VideoBoundingBox] | None = None
    category: DslValue[VideoExtractionCategory] | None = None


@dataclass
class VideoStandardGenerativeField(PropertyType):
    state: DslValue[str] | None = None
    types: list[DslValue[str]] = field(default_factory=list)


@dataclass
class VideoStandardOutputConfiguration(PropertyType):
    extraction: DslValue[VideoStandardExtraction] | None = None
    generative_field: DslValue[VideoStandardGenerativeField] | None = None
