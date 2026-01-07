"""PropertyTypes for AWS::Bedrock::DataSource."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BedrockDataAutomationConfiguration(PropertyType):
    parsing_modality: DslValue[str] | None = None


@dataclass
class BedrockFoundationModelConfiguration(PropertyType):
    model_arn: DslValue[str] | None = None
    parsing_modality: DslValue[str] | None = None
    parsing_prompt: DslValue[ParsingPrompt] | None = None


@dataclass
class BedrockFoundationModelContextEnrichmentConfiguration(PropertyType):
    enrichment_strategy_configuration: (
        DslValue[EnrichmentStrategyConfiguration] | None
    ) = None
    model_arn: DslValue[str] | None = None


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
class ConfluenceCrawlerConfiguration(PropertyType):
    filter_configuration: DslValue[CrawlFilterConfiguration] | None = None


@dataclass
class ConfluenceDataSourceConfiguration(PropertyType):
    source_configuration: DslValue[ConfluenceSourceConfiguration] | None = None
    crawler_configuration: DslValue[ConfluenceCrawlerConfiguration] | None = None


@dataclass
class ConfluenceSourceConfiguration(PropertyType):
    auth_type: DslValue[str] | None = None
    credentials_secret_arn: DslValue[str] | None = None
    host_type: DslValue[str] | None = None
    host_url: DslValue[str] | None = None


@dataclass
class ContextEnrichmentConfiguration(PropertyType):
    type_: DslValue[str] | None = None
    bedrock_foundation_model_configuration: (
        DslValue[BedrockFoundationModelContextEnrichmentConfiguration] | None
    ) = None


@dataclass
class CrawlFilterConfiguration(PropertyType):
    type_: DslValue[str] | None = None
    pattern_object_filter: DslValue[PatternObjectFilterConfiguration] | None = None


@dataclass
class CustomTransformationConfiguration(PropertyType):
    intermediate_storage: DslValue[IntermediateStorage] | None = None
    transformations: list[DslValue[Transformation]] = field(default_factory=list)


@dataclass
class DataSourceConfiguration(PropertyType):
    type_: DslValue[str] | None = None
    confluence_configuration: DslValue[ConfluenceDataSourceConfiguration] | None = None
    s3_configuration: DslValue[S3DataSourceConfiguration] | None = None
    salesforce_configuration: DslValue[SalesforceDataSourceConfiguration] | None = None
    share_point_configuration: DslValue[SharePointDataSourceConfiguration] | None = None
    web_configuration: DslValue[WebDataSourceConfiguration] | None = None


@dataclass
class EnrichmentStrategyConfiguration(PropertyType):
    method: DslValue[str] | None = None


@dataclass
class FixedSizeChunkingConfiguration(PropertyType):
    max_tokens: DslValue[int] | None = None
    overlap_percentage: DslValue[int] | None = None


@dataclass
class HierarchicalChunkingConfiguration(PropertyType):
    level_configurations: list[DslValue[HierarchicalChunkingLevelConfiguration]] = (
        field(default_factory=list)
    )
    overlap_tokens: DslValue[int] | None = None


@dataclass
class HierarchicalChunkingLevelConfiguration(PropertyType):
    max_tokens: DslValue[int] | None = None


@dataclass
class IntermediateStorage(PropertyType):
    s3_location: DslValue[S3Location] | None = None


@dataclass
class ParsingConfiguration(PropertyType):
    parsing_strategy: DslValue[str] | None = None
    bedrock_data_automation_configuration: (
        DslValue[BedrockDataAutomationConfiguration] | None
    ) = None
    bedrock_foundation_model_configuration: (
        DslValue[BedrockFoundationModelConfiguration] | None
    ) = None


@dataclass
class ParsingPrompt(PropertyType):
    parsing_prompt_text: DslValue[str] | None = None


@dataclass
class PatternObjectFilter(PropertyType):
    object_type: DslValue[str] | None = None
    exclusion_filters: list[DslValue[str]] = field(default_factory=list)
    inclusion_filters: list[DslValue[str]] = field(default_factory=list)


@dataclass
class PatternObjectFilterConfiguration(PropertyType):
    filters: list[DslValue[PatternObjectFilter]] = field(default_factory=list)


@dataclass
class S3DataSourceConfiguration(PropertyType):
    bucket_arn: DslValue[str] | None = None
    bucket_owner_account_id: DslValue[str] | None = None
    inclusion_prefixes: list[DslValue[str]] = field(default_factory=list)


@dataclass
class S3Location(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "uri": "URI",
    }

    uri: DslValue[str] | None = None


@dataclass
class SalesforceCrawlerConfiguration(PropertyType):
    filter_configuration: DslValue[CrawlFilterConfiguration] | None = None


@dataclass
class SalesforceDataSourceConfiguration(PropertyType):
    source_configuration: DslValue[SalesforceSourceConfiguration] | None = None
    crawler_configuration: DslValue[SalesforceCrawlerConfiguration] | None = None


@dataclass
class SalesforceSourceConfiguration(PropertyType):
    auth_type: DslValue[str] | None = None
    credentials_secret_arn: DslValue[str] | None = None
    host_url: DslValue[str] | None = None


@dataclass
class SeedUrl(PropertyType):
    url: DslValue[str] | None = None


@dataclass
class SemanticChunkingConfiguration(PropertyType):
    breakpoint_percentile_threshold: DslValue[int] | None = None
    buffer_size: DslValue[int] | None = None
    max_tokens: DslValue[int] | None = None


@dataclass
class ServerSideEncryptionConfiguration(PropertyType):
    kms_key_arn: DslValue[str] | None = None


@dataclass
class SharePointCrawlerConfiguration(PropertyType):
    filter_configuration: DslValue[CrawlFilterConfiguration] | None = None


@dataclass
class SharePointDataSourceConfiguration(PropertyType):
    source_configuration: DslValue[SharePointSourceConfiguration] | None = None
    crawler_configuration: DslValue[SharePointCrawlerConfiguration] | None = None


@dataclass
class SharePointSourceConfiguration(PropertyType):
    auth_type: DslValue[str] | None = None
    credentials_secret_arn: DslValue[str] | None = None
    domain: DslValue[str] | None = None
    host_type: DslValue[str] | None = None
    site_urls: list[DslValue[str]] = field(default_factory=list)
    tenant_id: DslValue[str] | None = None


@dataclass
class Transformation(PropertyType):
    step_to_apply: DslValue[str] | None = None
    transformation_function: DslValue[TransformationFunction] | None = None


@dataclass
class TransformationFunction(PropertyType):
    transformation_lambda_configuration: (
        DslValue[TransformationLambdaConfiguration] | None
    ) = None


@dataclass
class TransformationLambdaConfiguration(PropertyType):
    lambda_arn: DslValue[str] | None = None


@dataclass
class UrlConfiguration(PropertyType):
    seed_urls: list[DslValue[SeedUrl]] = field(default_factory=list)


@dataclass
class VectorIngestionConfiguration(PropertyType):
    chunking_configuration: DslValue[ChunkingConfiguration] | None = None
    context_enrichment_configuration: (
        DslValue[ContextEnrichmentConfiguration] | None
    ) = None
    custom_transformation_configuration: (
        DslValue[CustomTransformationConfiguration] | None
    ) = None
    parsing_configuration: DslValue[ParsingConfiguration] | None = None


@dataclass
class WebCrawlerConfiguration(PropertyType):
    crawler_limits: DslValue[WebCrawlerLimits] | None = None
    exclusion_filters: list[DslValue[str]] = field(default_factory=list)
    inclusion_filters: list[DslValue[str]] = field(default_factory=list)
    scope: DslValue[str] | None = None
    user_agent: DslValue[str] | None = None
    user_agent_header: DslValue[str] | None = None


@dataclass
class WebCrawlerLimits(PropertyType):
    max_pages: DslValue[int] | None = None
    rate_limit: DslValue[int] | None = None


@dataclass
class WebDataSourceConfiguration(PropertyType):
    source_configuration: DslValue[WebSourceConfiguration] | None = None
    crawler_configuration: DslValue[WebCrawlerConfiguration] | None = None


@dataclass
class WebSourceConfiguration(PropertyType):
    url_configuration: DslValue[UrlConfiguration] | None = None
