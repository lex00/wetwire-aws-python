"""PropertyTypes for AWS::Bedrock::DataSource."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BedrockDataAutomationConfiguration(PropertyType):
    parsing_modality: str | None = None


@dataclass
class BedrockFoundationModelConfiguration(PropertyType):
    model_arn: str | None = None
    parsing_modality: str | None = None
    parsing_prompt: ParsingPrompt | None = None


@dataclass
class BedrockFoundationModelContextEnrichmentConfiguration(PropertyType):
    enrichment_strategy_configuration: EnrichmentStrategyConfiguration | None = None
    model_arn: str | None = None


@dataclass
class ChunkingConfiguration(PropertyType):
    chunking_strategy: str | None = None
    fixed_size_chunking_configuration: FixedSizeChunkingConfiguration | None = None
    hierarchical_chunking_configuration: HierarchicalChunkingConfiguration | None = None
    semantic_chunking_configuration: SemanticChunkingConfiguration | None = None


@dataclass
class ConfluenceCrawlerConfiguration(PropertyType):
    filter_configuration: CrawlFilterConfiguration | None = None


@dataclass
class ConfluenceDataSourceConfiguration(PropertyType):
    source_configuration: ConfluenceSourceConfiguration | None = None
    crawler_configuration: ConfluenceCrawlerConfiguration | None = None


@dataclass
class ConfluenceSourceConfiguration(PropertyType):
    auth_type: str | None = None
    credentials_secret_arn: str | None = None
    host_type: str | None = None
    host_url: str | None = None


@dataclass
class ContextEnrichmentConfiguration(PropertyType):
    type_: str | None = None
    bedrock_foundation_model_configuration: (
        BedrockFoundationModelContextEnrichmentConfiguration | None
    ) = None


@dataclass
class CrawlFilterConfiguration(PropertyType):
    type_: str | None = None
    pattern_object_filter: PatternObjectFilterConfiguration | None = None


@dataclass
class CustomTransformationConfiguration(PropertyType):
    intermediate_storage: IntermediateStorage | None = None
    transformations: list[Transformation] = field(default_factory=list)


@dataclass
class DataSourceConfiguration(PropertyType):
    type_: str | None = None
    confluence_configuration: ConfluenceDataSourceConfiguration | None = None
    s3_configuration: S3DataSourceConfiguration | None = None
    salesforce_configuration: SalesforceDataSourceConfiguration | None = None
    share_point_configuration: SharePointDataSourceConfiguration | None = None
    web_configuration: WebDataSourceConfiguration | None = None


@dataclass
class EnrichmentStrategyConfiguration(PropertyType):
    method: str | None = None


@dataclass
class FixedSizeChunkingConfiguration(PropertyType):
    max_tokens: int | None = None
    overlap_percentage: int | None = None


@dataclass
class HierarchicalChunkingConfiguration(PropertyType):
    level_configurations: list[HierarchicalChunkingLevelConfiguration] = field(
        default_factory=list
    )
    overlap_tokens: int | None = None


@dataclass
class HierarchicalChunkingLevelConfiguration(PropertyType):
    max_tokens: int | None = None


@dataclass
class IntermediateStorage(PropertyType):
    s3_location: S3Location | None = None


@dataclass
class ParsingConfiguration(PropertyType):
    parsing_strategy: str | None = None
    bedrock_data_automation_configuration: BedrockDataAutomationConfiguration | None = (
        None
    )
    bedrock_foundation_model_configuration: (
        BedrockFoundationModelConfiguration | None
    ) = None


@dataclass
class ParsingPrompt(PropertyType):
    parsing_prompt_text: str | None = None


@dataclass
class PatternObjectFilter(PropertyType):
    object_type: str | None = None
    exclusion_filters: list[String] = field(default_factory=list)
    inclusion_filters: list[String] = field(default_factory=list)


@dataclass
class PatternObjectFilterConfiguration(PropertyType):
    filters: list[PatternObjectFilter] = field(default_factory=list)


@dataclass
class S3DataSourceConfiguration(PropertyType):
    bucket_arn: str | None = None
    bucket_owner_account_id: str | None = None
    inclusion_prefixes: list[String] = field(default_factory=list)


@dataclass
class S3Location(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "uri": "URI",
    }

    uri: str | None = None


@dataclass
class SalesforceCrawlerConfiguration(PropertyType):
    filter_configuration: CrawlFilterConfiguration | None = None


@dataclass
class SalesforceDataSourceConfiguration(PropertyType):
    source_configuration: SalesforceSourceConfiguration | None = None
    crawler_configuration: SalesforceCrawlerConfiguration | None = None


@dataclass
class SalesforceSourceConfiguration(PropertyType):
    auth_type: str | None = None
    credentials_secret_arn: str | None = None
    host_url: str | None = None


@dataclass
class SeedUrl(PropertyType):
    url: str | None = None


@dataclass
class SemanticChunkingConfiguration(PropertyType):
    breakpoint_percentile_threshold: int | None = None
    buffer_size: int | None = None
    max_tokens: int | None = None


@dataclass
class ServerSideEncryptionConfiguration(PropertyType):
    kms_key_arn: str | None = None


@dataclass
class SharePointCrawlerConfiguration(PropertyType):
    filter_configuration: CrawlFilterConfiguration | None = None


@dataclass
class SharePointDataSourceConfiguration(PropertyType):
    source_configuration: SharePointSourceConfiguration | None = None
    crawler_configuration: SharePointCrawlerConfiguration | None = None


@dataclass
class SharePointSourceConfiguration(PropertyType):
    auth_type: str | None = None
    credentials_secret_arn: str | None = None
    domain: str | None = None
    host_type: str | None = None
    site_urls: list[String] = field(default_factory=list)
    tenant_id: str | None = None


@dataclass
class Transformation(PropertyType):
    step_to_apply: str | None = None
    transformation_function: TransformationFunction | None = None


@dataclass
class TransformationFunction(PropertyType):
    transformation_lambda_configuration: TransformationLambdaConfiguration | None = None


@dataclass
class TransformationLambdaConfiguration(PropertyType):
    lambda_arn: str | None = None


@dataclass
class UrlConfiguration(PropertyType):
    seed_urls: list[SeedUrl] = field(default_factory=list)


@dataclass
class VectorIngestionConfiguration(PropertyType):
    chunking_configuration: ChunkingConfiguration | None = None
    context_enrichment_configuration: ContextEnrichmentConfiguration | None = None
    custom_transformation_configuration: CustomTransformationConfiguration | None = None
    parsing_configuration: ParsingConfiguration | None = None


@dataclass
class WebCrawlerConfiguration(PropertyType):
    crawler_limits: WebCrawlerLimits | None = None
    exclusion_filters: list[String] = field(default_factory=list)
    inclusion_filters: list[String] = field(default_factory=list)
    scope: str | None = None
    user_agent: str | None = None
    user_agent_header: str | None = None


@dataclass
class WebCrawlerLimits(PropertyType):
    max_pages: int | None = None
    rate_limit: int | None = None


@dataclass
class WebDataSourceConfiguration(PropertyType):
    source_configuration: WebSourceConfiguration | None = None
    crawler_configuration: WebCrawlerConfiguration | None = None


@dataclass
class WebSourceConfiguration(PropertyType):
    url_configuration: UrlConfiguration | None = None
