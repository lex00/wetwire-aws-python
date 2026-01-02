"""PropertyTypes for AWS::Bedrock::KnowledgeBase."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AudioConfiguration(PropertyType):
    segmentation_configuration: AudioSegmentationConfiguration | None = None


@dataclass
class AudioSegmentationConfiguration(PropertyType):
    fixed_length_duration: int | None = None


@dataclass
class BedrockEmbeddingModelConfiguration(PropertyType):
    audio: list[AudioConfiguration] = field(default_factory=list)
    dimensions: int | None = None
    embedding_data_type: str | None = None
    video: list[VideoConfiguration] = field(default_factory=list)


@dataclass
class CuratedQuery(PropertyType):
    natural_language: str | None = None
    sql: str | None = None


@dataclass
class EmbeddingModelConfiguration(PropertyType):
    bedrock_embedding_model_configuration: BedrockEmbeddingModelConfiguration | None = (
        None
    )


@dataclass
class KendraKnowledgeBaseConfiguration(PropertyType):
    kendra_index_arn: str | None = None


@dataclass
class KnowledgeBaseConfiguration(PropertyType):
    type_: str | None = None
    kendra_knowledge_base_configuration: KendraKnowledgeBaseConfiguration | None = None
    sql_knowledge_base_configuration: SqlKnowledgeBaseConfiguration | None = None
    vector_knowledge_base_configuration: VectorKnowledgeBaseConfiguration | None = None


@dataclass
class MongoDbAtlasConfiguration(PropertyType):
    collection_name: str | None = None
    credentials_secret_arn: str | None = None
    database_name: str | None = None
    endpoint: str | None = None
    field_mapping: MongoDbAtlasFieldMapping | None = None
    vector_index_name: str | None = None
    endpoint_service_name: str | None = None
    text_index_name: str | None = None


@dataclass
class MongoDbAtlasFieldMapping(PropertyType):
    metadata_field: str | None = None
    text_field: str | None = None
    vector_field: str | None = None


@dataclass
class NeptuneAnalyticsConfiguration(PropertyType):
    field_mapping: NeptuneAnalyticsFieldMapping | None = None
    graph_arn: str | None = None


@dataclass
class NeptuneAnalyticsFieldMapping(PropertyType):
    metadata_field: str | None = None
    text_field: str | None = None


@dataclass
class OpenSearchManagedClusterConfiguration(PropertyType):
    domain_arn: str | None = None
    domain_endpoint: str | None = None
    field_mapping: OpenSearchManagedClusterFieldMapping | None = None
    vector_index_name: str | None = None


@dataclass
class OpenSearchManagedClusterFieldMapping(PropertyType):
    metadata_field: str | None = None
    text_field: str | None = None
    vector_field: str | None = None


@dataclass
class OpenSearchServerlessConfiguration(PropertyType):
    collection_arn: str | None = None
    field_mapping: OpenSearchServerlessFieldMapping | None = None
    vector_index_name: str | None = None


@dataclass
class OpenSearchServerlessFieldMapping(PropertyType):
    metadata_field: str | None = None
    text_field: str | None = None
    vector_field: str | None = None


@dataclass
class PineconeConfiguration(PropertyType):
    connection_string: str | None = None
    credentials_secret_arn: str | None = None
    field_mapping: PineconeFieldMapping | None = None
    namespace: str | None = None


@dataclass
class PineconeFieldMapping(PropertyType):
    metadata_field: str | None = None
    text_field: str | None = None


@dataclass
class QueryGenerationColumn(PropertyType):
    description: str | None = None
    inclusion: str | None = None
    name: str | None = None


@dataclass
class QueryGenerationConfiguration(PropertyType):
    execution_timeout_seconds: int | None = None
    generation_context: QueryGenerationContext | None = None


@dataclass
class QueryGenerationContext(PropertyType):
    curated_queries: list[CuratedQuery] = field(default_factory=list)
    tables: list[QueryGenerationTable] = field(default_factory=list)


@dataclass
class QueryGenerationTable(PropertyType):
    name: str | None = None
    columns: list[QueryGenerationColumn] = field(default_factory=list)
    description: str | None = None
    inclusion: str | None = None


@dataclass
class RdsConfiguration(PropertyType):
    credentials_secret_arn: str | None = None
    database_name: str | None = None
    field_mapping: RdsFieldMapping | None = None
    resource_arn: str | None = None
    table_name: str | None = None


@dataclass
class RdsFieldMapping(PropertyType):
    metadata_field: str | None = None
    primary_key_field: str | None = None
    text_field: str | None = None
    vector_field: str | None = None
    custom_metadata_field: str | None = None


@dataclass
class RedshiftConfiguration(PropertyType):
    query_engine_configuration: RedshiftQueryEngineConfiguration | None = None
    storage_configurations: list[RedshiftQueryEngineStorageConfiguration] = field(
        default_factory=list
    )
    query_generation_configuration: QueryGenerationConfiguration | None = None


@dataclass
class RedshiftProvisionedAuthConfiguration(PropertyType):
    type_: str | None = None
    database_user: str | None = None
    username_password_secret_arn: str | None = None


@dataclass
class RedshiftProvisionedConfiguration(PropertyType):
    auth_configuration: RedshiftProvisionedAuthConfiguration | None = None
    cluster_identifier: str | None = None


@dataclass
class RedshiftQueryEngineAwsDataCatalogStorageConfiguration(PropertyType):
    table_names: list[String] = field(default_factory=list)


@dataclass
class RedshiftQueryEngineConfiguration(PropertyType):
    type_: str | None = None
    provisioned_configuration: RedshiftProvisionedConfiguration | None = None
    serverless_configuration: RedshiftServerlessConfiguration | None = None


@dataclass
class RedshiftQueryEngineRedshiftStorageConfiguration(PropertyType):
    database_name: str | None = None


@dataclass
class RedshiftQueryEngineStorageConfiguration(PropertyType):
    type_: str | None = None
    aws_data_catalog_configuration: (
        RedshiftQueryEngineAwsDataCatalogStorageConfiguration | None
    ) = None
    redshift_configuration: RedshiftQueryEngineRedshiftStorageConfiguration | None = (
        None
    )


@dataclass
class RedshiftServerlessAuthConfiguration(PropertyType):
    type_: str | None = None
    username_password_secret_arn: str | None = None


@dataclass
class RedshiftServerlessConfiguration(PropertyType):
    auth_configuration: RedshiftServerlessAuthConfiguration | None = None
    workgroup_arn: str | None = None


@dataclass
class S3Location(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "uri": "URI",
    }

    uri: str | None = None


@dataclass
class S3VectorsConfiguration(PropertyType):
    index_arn: str | None = None
    index_name: str | None = None
    vector_bucket_arn: str | None = None


@dataclass
class SqlKnowledgeBaseConfiguration(PropertyType):
    type_: str | None = None
    redshift_configuration: RedshiftConfiguration | None = None


@dataclass
class StorageConfiguration(PropertyType):
    type_: str | None = None
    mongo_db_atlas_configuration: MongoDbAtlasConfiguration | None = None
    neptune_analytics_configuration: NeptuneAnalyticsConfiguration | None = None
    opensearch_managed_cluster_configuration: (
        OpenSearchManagedClusterConfiguration | None
    ) = None
    opensearch_serverless_configuration: OpenSearchServerlessConfiguration | None = None
    pinecone_configuration: PineconeConfiguration | None = None
    rds_configuration: RdsConfiguration | None = None
    s3_vectors_configuration: S3VectorsConfiguration | None = None


@dataclass
class SupplementalDataStorageConfiguration(PropertyType):
    supplemental_data_storage_locations: list[SupplementalDataStorageLocation] = field(
        default_factory=list
    )


@dataclass
class SupplementalDataStorageLocation(PropertyType):
    supplemental_data_storage_location_type: str | None = None
    s3_location: S3Location | None = None


@dataclass
class VectorKnowledgeBaseConfiguration(PropertyType):
    embedding_model_arn: str | None = None
    embedding_model_configuration: EmbeddingModelConfiguration | None = None
    supplemental_data_storage_configuration: (
        SupplementalDataStorageConfiguration | None
    ) = None


@dataclass
class VideoConfiguration(PropertyType):
    segmentation_configuration: VideoSegmentationConfiguration | None = None


@dataclass
class VideoSegmentationConfiguration(PropertyType):
    fixed_length_duration: int | None = None
