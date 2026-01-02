"""PropertyTypes for AWS::Bedrock::DataAutomationProject."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AudioExtractionCategory(PropertyType):
    state: str | None = None
    type_configuration: AudioExtractionCategoryTypeConfiguration | None = None
    types: list[String] = field(default_factory=list)


@dataclass
class AudioExtractionCategoryTypeConfiguration(PropertyType):
    transcript: TranscriptConfiguration | None = None


@dataclass
class AudioLanguageConfiguration(PropertyType):
    generative_output_language: str | None = None
    identify_multiple_languages: bool | None = None
    input_languages: list[String] = field(default_factory=list)


@dataclass
class AudioOverrideConfiguration(PropertyType):
    language_configuration: AudioLanguageConfiguration | None = None
    modality_processing: ModalityProcessingConfiguration | None = None
    sensitive_data_configuration: SensitiveDataConfiguration | None = None


@dataclass
class AudioStandardExtraction(PropertyType):
    category: AudioExtractionCategory | None = None


@dataclass
class AudioStandardGenerativeField(PropertyType):
    state: str | None = None
    types: list[String] = field(default_factory=list)


@dataclass
class AudioStandardOutputConfiguration(PropertyType):
    extraction: AudioStandardExtraction | None = None
    generative_field: AudioStandardGenerativeField | None = None


@dataclass
class BlueprintItem(PropertyType):
    blueprint_arn: str | None = None
    blueprint_stage: str | None = None
    blueprint_version: str | None = None


@dataclass
class ChannelLabelingConfiguration(PropertyType):
    state: str | None = None


@dataclass
class CustomOutputConfiguration(PropertyType):
    blueprints: list[BlueprintItem] = field(default_factory=list)


@dataclass
class DocumentBoundingBox(PropertyType):
    state: str | None = None


@dataclass
class DocumentExtractionGranularity(PropertyType):
    types: list[String] = field(default_factory=list)


@dataclass
class DocumentOutputAdditionalFileFormat(PropertyType):
    state: str | None = None


@dataclass
class DocumentOutputFormat(PropertyType):
    additional_file_format: DocumentOutputAdditionalFileFormat | None = None
    text_format: DocumentOutputTextFormat | None = None


@dataclass
class DocumentOutputTextFormat(PropertyType):
    types: list[String] = field(default_factory=list)


@dataclass
class DocumentOverrideConfiguration(PropertyType):
    modality_processing: ModalityProcessingConfiguration | None = None
    sensitive_data_configuration: SensitiveDataConfiguration | None = None
    splitter: SplitterConfiguration | None = None


@dataclass
class DocumentStandardExtraction(PropertyType):
    bounding_box: DocumentBoundingBox | None = None
    granularity: DocumentExtractionGranularity | None = None


@dataclass
class DocumentStandardGenerativeField(PropertyType):
    state: str | None = None


@dataclass
class DocumentStandardOutputConfiguration(PropertyType):
    extraction: DocumentStandardExtraction | None = None
    generative_field: DocumentStandardGenerativeField | None = None
    output_format: DocumentOutputFormat | None = None


@dataclass
class ImageBoundingBox(PropertyType):
    state: str | None = None


@dataclass
class ImageExtractionCategory(PropertyType):
    state: str | None = None
    types: list[String] = field(default_factory=list)


@dataclass
class ImageOverrideConfiguration(PropertyType):
    modality_processing: ModalityProcessingConfiguration | None = None
    sensitive_data_configuration: SensitiveDataConfiguration | None = None


@dataclass
class ImageStandardExtraction(PropertyType):
    bounding_box: ImageBoundingBox | None = None
    category: ImageExtractionCategory | None = None


@dataclass
class ImageStandardGenerativeField(PropertyType):
    state: str | None = None
    types: list[String] = field(default_factory=list)


@dataclass
class ImageStandardOutputConfiguration(PropertyType):
    extraction: ImageStandardExtraction | None = None
    generative_field: ImageStandardGenerativeField | None = None


@dataclass
class ModalityProcessingConfiguration(PropertyType):
    state: str | None = None


@dataclass
class ModalityRoutingConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "jpeg": "jpeg",
        "mov": "mov",
        "mp4": "mp4",
        "png": "png",
    }

    jpeg: str | None = None
    mov: str | None = None
    mp4: str | None = None
    png: str | None = None


@dataclass
class OverrideConfiguration(PropertyType):
    audio: AudioOverrideConfiguration | None = None
    document: DocumentOverrideConfiguration | None = None
    image: ImageOverrideConfiguration | None = None
    modality_routing: ModalityRoutingConfiguration | None = None
    video: VideoOverrideConfiguration | None = None


@dataclass
class PIIEntitiesConfiguration(PropertyType):
    pii_entity_types: list[String] = field(default_factory=list)
    redaction_mask_mode: str | None = None


@dataclass
class SensitiveDataConfiguration(PropertyType):
    detection_mode: str | None = None
    detection_scope: list[String] = field(default_factory=list)
    pii_entities_configuration: PIIEntitiesConfiguration | None = None


@dataclass
class SpeakerLabelingConfiguration(PropertyType):
    state: str | None = None


@dataclass
class SplitterConfiguration(PropertyType):
    state: str | None = None


@dataclass
class StandardOutputConfiguration(PropertyType):
    audio: AudioStandardOutputConfiguration | None = None
    document: DocumentStandardOutputConfiguration | None = None
    image: ImageStandardOutputConfiguration | None = None
    video: VideoStandardOutputConfiguration | None = None


@dataclass
class TranscriptConfiguration(PropertyType):
    channel_labeling: ChannelLabelingConfiguration | None = None
    speaker_labeling: SpeakerLabelingConfiguration | None = None


@dataclass
class VideoBoundingBox(PropertyType):
    state: str | None = None


@dataclass
class VideoExtractionCategory(PropertyType):
    state: str | None = None
    types: list[String] = field(default_factory=list)


@dataclass
class VideoOverrideConfiguration(PropertyType):
    modality_processing: ModalityProcessingConfiguration | None = None
    sensitive_data_configuration: SensitiveDataConfiguration | None = None


@dataclass
class VideoStandardExtraction(PropertyType):
    bounding_box: VideoBoundingBox | None = None
    category: VideoExtractionCategory | None = None


@dataclass
class VideoStandardGenerativeField(PropertyType):
    state: str | None = None
    types: list[String] = field(default_factory=list)


@dataclass
class VideoStandardOutputConfiguration(PropertyType):
    extraction: VideoStandardExtraction | None = None
    generative_field: VideoStandardGenerativeField | None = None
