"""PropertyTypes for AWS::Bedrock::KnowledgeBase."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AudioConfiguration(PropertyType):
    segmentation_configuration: DslValue[AudioSegmentationConfiguration] | None = None


@dataclass
class AudioSegmentationConfiguration(PropertyType):
    fixed_length_duration: DslValue[int] | None = None


@dataclass
class BedrockEmbeddingModelConfiguration(PropertyType):
    audio: list[DslValue[AudioConfiguration]] = field(default_factory=list)
    dimensions: DslValue[int] | None = None
    embedding_data_type: DslValue[str] | None = None
    video: list[DslValue[VideoConfiguration]] = field(default_factory=list)


@dataclass
class CuratedQuery(PropertyType):
    natural_language: DslValue[str] | None = None
    sql: DslValue[str] | None = None


@dataclass
class EmbeddingModelConfiguration(PropertyType):
    bedrock_embedding_model_configuration: (
        DslValue[BedrockEmbeddingModelConfiguration] | None
    ) = None


@dataclass
class KendraKnowledgeBaseConfiguration(PropertyType):
    kendra_index_arn: DslValue[str] | None = None


@dataclass
class KnowledgeBaseConfiguration(PropertyType):
    type_: DslValue[str] | None = None
    kendra_knowledge_base_configuration: (
        DslValue[KendraKnowledgeBaseConfiguration] | None
    ) = None
    sql_knowledge_base_configuration: DslValue[SqlKnowledgeBaseConfiguration] | None = (
        None
    )
    vector_knowledge_base_configuration: (
        DslValue[VectorKnowledgeBaseConfiguration] | None
    ) = None


@dataclass
class MongoDbAtlasConfiguration(PropertyType):
    collection_name: DslValue[str] | None = None
    credentials_secret_arn: DslValue[str] | None = None
    database_name: DslValue[str] | None = None
    endpoint: DslValue[str] | None = None
    field_mapping: DslValue[MongoDbAtlasFieldMapping] | None = None
    vector_index_name: DslValue[str] | None = None
    endpoint_service_name: DslValue[str] | None = None
    text_index_name: DslValue[str] | None = None


@dataclass
class MongoDbAtlasFieldMapping(PropertyType):
    metadata_field: DslValue[str] | None = None
    text_field: DslValue[str] | None = None
    vector_field: DslValue[str] | None = None


@dataclass
class NeptuneAnalyticsConfiguration(PropertyType):
    field_mapping: DslValue[NeptuneAnalyticsFieldMapping] | None = None
    graph_arn: DslValue[str] | None = None


@dataclass
class NeptuneAnalyticsFieldMapping(PropertyType):
    metadata_field: DslValue[str] | None = None
    text_field: DslValue[str] | None = None


@dataclass
class OpenSearchManagedClusterConfiguration(PropertyType):
    domain_arn: DslValue[str] | None = None
    domain_endpoint: DslValue[str] | None = None
    field_mapping: DslValue[OpenSearchManagedClusterFieldMapping] | None = None
    vector_index_name: DslValue[str] | None = None


@dataclass
class OpenSearchManagedClusterFieldMapping(PropertyType):
    metadata_field: DslValue[str] | None = None
    text_field: DslValue[str] | None = None
    vector_field: DslValue[str] | None = None


@dataclass
class OpenSearchServerlessConfiguration(PropertyType):
    collection_arn: DslValue[str] | None = None
    field_mapping: DslValue[OpenSearchServerlessFieldMapping] | None = None
    vector_index_name: DslValue[str] | None = None


@dataclass
class OpenSearchServerlessFieldMapping(PropertyType):
    metadata_field: DslValue[str] | None = None
    text_field: DslValue[str] | None = None
    vector_field: DslValue[str] | None = None


@dataclass
class PineconeConfiguration(PropertyType):
    connection_string: DslValue[str] | None = None
    credentials_secret_arn: DslValue[str] | None = None
    field_mapping: DslValue[PineconeFieldMapping] | None = None
    namespace: DslValue[str] | None = None


@dataclass
class PineconeFieldMapping(PropertyType):
    metadata_field: DslValue[str] | None = None
    text_field: DslValue[str] | None = None


@dataclass
class QueryGenerationColumn(PropertyType):
    description: DslValue[str] | None = None
    inclusion: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class QueryGenerationConfiguration(PropertyType):
    execution_timeout_seconds: DslValue[int] | None = None
    generation_context: DslValue[QueryGenerationContext] | None = None


@dataclass
class QueryGenerationContext(PropertyType):
    curated_queries: list[DslValue[CuratedQuery]] = field(default_factory=list)
    tables: list[DslValue[QueryGenerationTable]] = field(default_factory=list)


@dataclass
class QueryGenerationTable(PropertyType):
    name: DslValue[str] | None = None
    columns: list[DslValue[QueryGenerationColumn]] = field(default_factory=list)
    description: DslValue[str] | None = None
    inclusion: DslValue[str] | None = None


@dataclass
class RdsConfiguration(PropertyType):
    credentials_secret_arn: DslValue[str] | None = None
    database_name: DslValue[str] | None = None
    field_mapping: DslValue[RdsFieldMapping] | None = None
    resource_arn: DslValue[str] | None = None
    table_name: DslValue[str] | None = None


@dataclass
class RdsFieldMapping(PropertyType):
    metadata_field: DslValue[str] | None = None
    primary_key_field: DslValue[str] | None = None
    text_field: DslValue[str] | None = None
    vector_field: DslValue[str] | None = None
    custom_metadata_field: DslValue[str] | None = None


@dataclass
class RedshiftConfiguration(PropertyType):
    query_engine_configuration: DslValue[RedshiftQueryEngineConfiguration] | None = None
    storage_configurations: list[DslValue[RedshiftQueryEngineStorageConfiguration]] = (
        field(default_factory=list)
    )
    query_generation_configuration: DslValue[QueryGenerationConfiguration] | None = None


@dataclass
class RedshiftProvisionedAuthConfiguration(PropertyType):
    type_: DslValue[str] | None = None
    database_user: DslValue[str] | None = None
    username_password_secret_arn: DslValue[str] | None = None


@dataclass
class RedshiftProvisionedConfiguration(PropertyType):
    auth_configuration: DslValue[RedshiftProvisionedAuthConfiguration] | None = None
    cluster_identifier: DslValue[str] | None = None


@dataclass
class RedshiftQueryEngineAwsDataCatalogStorageConfiguration(PropertyType):
    table_names: list[DslValue[str]] = field(default_factory=list)


@dataclass
class RedshiftQueryEngineConfiguration(PropertyType):
    type_: DslValue[str] | None = None
    provisioned_configuration: DslValue[RedshiftProvisionedConfiguration] | None = None
    serverless_configuration: DslValue[RedshiftServerlessConfiguration] | None = None


@dataclass
class RedshiftQueryEngineRedshiftStorageConfiguration(PropertyType):
    database_name: DslValue[str] | None = None


@dataclass
class RedshiftQueryEngineStorageConfiguration(PropertyType):
    type_: DslValue[str] | None = None
    aws_data_catalog_configuration: (
        DslValue[RedshiftQueryEngineAwsDataCatalogStorageConfiguration] | None
    ) = None
    redshift_configuration: (
        DslValue[RedshiftQueryEngineRedshiftStorageConfiguration] | None
    ) = None


@dataclass
class RedshiftServerlessAuthConfiguration(PropertyType):
    type_: DslValue[str] | None = None
    username_password_secret_arn: DslValue[str] | None = None


@dataclass
class RedshiftServerlessConfiguration(PropertyType):
    auth_configuration: DslValue[RedshiftServerlessAuthConfiguration] | None = None
    workgroup_arn: DslValue[str] | None = None


@dataclass
class S3Location(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "uri": "URI",
    }

    uri: DslValue[str] | None = None


@dataclass
class S3VectorsConfiguration(PropertyType):
    index_arn: DslValue[str] | None = None
    index_name: DslValue[str] | None = None
    vector_bucket_arn: DslValue[str] | None = None


@dataclass
class SqlKnowledgeBaseConfiguration(PropertyType):
    type_: DslValue[str] | None = None
    redshift_configuration: DslValue[RedshiftConfiguration] | None = None


@dataclass
class StorageConfiguration(PropertyType):
    type_: DslValue[str] | None = None
    mongo_db_atlas_configuration: DslValue[MongoDbAtlasConfiguration] | None = None
    neptune_analytics_configuration: DslValue[NeptuneAnalyticsConfiguration] | None = (
        None
    )
    opensearch_managed_cluster_configuration: (
        DslValue[OpenSearchManagedClusterConfiguration] | None
    ) = None
    opensearch_serverless_configuration: (
        DslValue[OpenSearchServerlessConfiguration] | None
    ) = None
    pinecone_configuration: DslValue[PineconeConfiguration] | None = None
    rds_configuration: DslValue[RdsConfiguration] | None = None
    s3_vectors_configuration: DslValue[S3VectorsConfiguration] | None = None


@dataclass
class SupplementalDataStorageConfiguration(PropertyType):
    supplemental_data_storage_locations: list[
        DslValue[SupplementalDataStorageLocation]
    ] = field(default_factory=list)


@dataclass
class SupplementalDataStorageLocation(PropertyType):
    supplemental_data_storage_location_type: DslValue[str] | None = None
    s3_location: DslValue[S3Location] | None = None


@dataclass
class VectorKnowledgeBaseConfiguration(PropertyType):
    embedding_model_arn: DslValue[str] | None = None
    embedding_model_configuration: DslValue[EmbeddingModelConfiguration] | None = None
    supplemental_data_storage_configuration: (
        DslValue[SupplementalDataStorageConfiguration] | None
    ) = None


@dataclass
class VideoConfiguration(PropertyType):
    segmentation_configuration: DslValue[VideoSegmentationConfiguration] | None = None


@dataclass
class VideoSegmentationConfiguration(PropertyType):
    fixed_length_duration: DslValue[int] | None = None
