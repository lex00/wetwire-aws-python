"""PropertyTypes for AWS::Wisdom::KnowledgeBase."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AppIntegrationsConfiguration(PropertyType):
    app_integration_arn: str | None = None
    object_fields: list[String] = field(default_factory=list)


@dataclass
class BedrockFoundationModelConfiguration(PropertyType):
    model_arn: str | None = None
    parsing_prompt: ParsingPrompt | None = None


@dataclass
class ChunkingConfiguration(PropertyType):
    chunking_strategy: str | None = None
    fixed_size_chunking_configuration: FixedSizeChunkingConfiguration | None = None
    hierarchical_chunking_configuration: HierarchicalChunkingConfiguration | None = None
    semantic_chunking_configuration: SemanticChunkingConfiguration | None = None


@dataclass
class CrawlerLimits(PropertyType):
    rate_limit: float | None = None


@dataclass
class FixedSizeChunkingConfiguration(PropertyType):
    max_tokens: float | None = None
    overlap_percentage: float | None = None


@dataclass
class HierarchicalChunkingConfiguration(PropertyType):
    level_configurations: list[HierarchicalChunkingLevelConfiguration] = field(
        default_factory=list
    )
    overlap_tokens: float | None = None


@dataclass
class HierarchicalChunkingLevelConfiguration(PropertyType):
    max_tokens: float | None = None


@dataclass
class ManagedSourceConfiguration(PropertyType):
    web_crawler_configuration: WebCrawlerConfiguration | None = None


@dataclass
class ParsingConfiguration(PropertyType):
    parsing_strategy: str | None = None
    bedrock_foundation_model_configuration: (
        BedrockFoundationModelConfiguration | None
    ) = None


@dataclass
class ParsingPrompt(PropertyType):
    parsing_prompt_text: str | None = None


@dataclass
class RenderingConfiguration(PropertyType):
    template_uri: str | None = None


@dataclass
class SeedUrl(PropertyType):
    url: str | None = None


@dataclass
class SemanticChunkingConfiguration(PropertyType):
    breakpoint_percentile_threshold: float | None = None
    buffer_size: float | None = None
    max_tokens: float | None = None


@dataclass
class ServerSideEncryptionConfiguration(PropertyType):
    kms_key_id: str | None = None


@dataclass
class SourceConfiguration(PropertyType):
    app_integrations: AppIntegrationsConfiguration | None = None
    managed_source_configuration: ManagedSourceConfiguration | None = None


@dataclass
class UrlConfiguration(PropertyType):
    seed_urls: list[SeedUrl] = field(default_factory=list)


@dataclass
class VectorIngestionConfiguration(PropertyType):
    chunking_configuration: ChunkingConfiguration | None = None
    parsing_configuration: ParsingConfiguration | None = None


@dataclass
class WebCrawlerConfiguration(PropertyType):
    url_configuration: UrlConfiguration | None = None
    crawler_limits: CrawlerLimits | None = None
    exclusion_filters: list[String] = field(default_factory=list)
    inclusion_filters: list[String] = field(default_factory=list)
    scope: str | None = None
