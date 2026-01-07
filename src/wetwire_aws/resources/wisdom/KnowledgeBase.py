"""PropertyTypes for AWS::Wisdom::KnowledgeBase."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AppIntegrationsConfiguration(PropertyType):
    app_integration_arn: DslValue[str] | None = None
    object_fields: list[DslValue[str]] = field(default_factory=list)


@dataclass
class BedrockFoundationModelConfiguration(PropertyType):
    model_arn: DslValue[str] | None = None
    parsing_prompt: DslValue[ParsingPrompt] | None = None


@dataclass
class ChunkingConfiguration(PropertyType):
    chunking_strategy: DslValue[str] | None = None
    fixed_size_chunking_configuration: (
        DslValue[FixedSizeChunkingConfiguration] | None
    ) = None
    hierarchical_chunking_configuration: (
        DslValue[HierarchicalChunkingConfiguration] | None
    ) = None
    semantic_chunking_configuration: DslValue[SemanticChunkingConfiguration] | None = (
        None
    )


@dataclass
class CrawlerLimits(PropertyType):
    rate_limit: DslValue[float] | None = None


@dataclass
class FixedSizeChunkingConfiguration(PropertyType):
    max_tokens: DslValue[float] | None = None
    overlap_percentage: DslValue[float] | None = None


@dataclass
class HierarchicalChunkingConfiguration(PropertyType):
    level_configurations: list[DslValue[HierarchicalChunkingLevelConfiguration]] = (
        field(default_factory=list)
    )
    overlap_tokens: DslValue[float] | None = None


@dataclass
class HierarchicalChunkingLevelConfiguration(PropertyType):
    max_tokens: DslValue[float] | None = None


@dataclass
class ManagedSourceConfiguration(PropertyType):
    web_crawler_configuration: DslValue[WebCrawlerConfiguration] | None = None


@dataclass
class ParsingConfiguration(PropertyType):
    parsing_strategy: DslValue[str] | None = None
    bedrock_foundation_model_configuration: (
        DslValue[BedrockFoundationModelConfiguration] | None
    ) = None


@dataclass
class ParsingPrompt(PropertyType):
    parsing_prompt_text: DslValue[str] | None = None


@dataclass
class RenderingConfiguration(PropertyType):
    template_uri: DslValue[str] | None = None


@dataclass
class SeedUrl(PropertyType):
    url: DslValue[str] | None = None


@dataclass
class SemanticChunkingConfiguration(PropertyType):
    breakpoint_percentile_threshold: DslValue[float] | None = None
    buffer_size: DslValue[float] | None = None
    max_tokens: DslValue[float] | None = None


@dataclass
class ServerSideEncryptionConfiguration(PropertyType):
    kms_key_id: DslValue[str] | None = None


@dataclass
class SourceConfiguration(PropertyType):
    app_integrations: DslValue[AppIntegrationsConfiguration] | None = None
    managed_source_configuration: DslValue[ManagedSourceConfiguration] | None = None


@dataclass
class UrlConfiguration(PropertyType):
    seed_urls: list[DslValue[SeedUrl]] = field(default_factory=list)


@dataclass
class VectorIngestionConfiguration(PropertyType):
    chunking_configuration: DslValue[ChunkingConfiguration] | None = None
    parsing_configuration: DslValue[ParsingConfiguration] | None = None


@dataclass
class WebCrawlerConfiguration(PropertyType):
    url_configuration: DslValue[UrlConfiguration] | None = None
    crawler_limits: DslValue[CrawlerLimits] | None = None
    exclusion_filters: list[DslValue[str]] = field(default_factory=list)
    inclusion_filters: list[DslValue[str]] = field(default_factory=list)
    scope: DslValue[str] | None = None
