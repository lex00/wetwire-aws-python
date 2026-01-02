"""PropertyTypes for AWS::DataZone::Connection."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AmazonQPropertiesInput(PropertyType):
    auth_mode: str | None = None
    is_enabled: bool | None = None
    profile_arn: str | None = None


@dataclass
class AthenaPropertiesInput(PropertyType):
    workgroup_name: str | None = None


@dataclass
class AuthenticationConfigurationInput(PropertyType):
    authentication_type: str | None = None
    basic_authentication_credentials: BasicAuthenticationCredentials | None = None
    custom_authentication_credentials: dict[str, String] = field(default_factory=dict)
    kms_key_arn: str | None = None
    o_auth2_properties: OAuth2Properties | None = None
    secret_arn: str | None = None


@dataclass
class AuthorizationCodeProperties(PropertyType):
    authorization_code: str | None = None
    redirect_uri: str | None = None


@dataclass
class AwsLocation(PropertyType):
    access_role: str | None = None
    aws_account_id: str | None = None
    aws_region: str | None = None
    iam_connection_id: str | None = None


@dataclass
class BasicAuthenticationCredentials(PropertyType):
    password: str | None = None
    user_name: str | None = None


@dataclass
class ConnectionPropertiesInput(PropertyType):
    amazon_q_properties: AmazonQPropertiesInput | None = None
    athena_properties: AthenaPropertiesInput | None = None
    glue_properties: GluePropertiesInput | None = None
    hyper_pod_properties: HyperPodPropertiesInput | None = None
    iam_properties: IamPropertiesInput | None = None
    mlflow_properties: MlflowPropertiesInput | None = None
    redshift_properties: RedshiftPropertiesInput | None = None
    s3_properties: S3PropertiesInput | None = None
    spark_emr_properties: SparkEmrPropertiesInput | None = None
    spark_glue_properties: SparkGluePropertiesInput | None = None


@dataclass
class GlueConnectionInput(PropertyType):
    athena_properties: dict[str, String] = field(default_factory=dict)
    authentication_configuration: AuthenticationConfigurationInput | None = None
    connection_properties: dict[str, String] = field(default_factory=dict)
    connection_type: str | None = None
    description: str | None = None
    match_criteria: str | None = None
    name: str | None = None
    physical_connection_requirements: PhysicalConnectionRequirements | None = None
    python_properties: dict[str, String] = field(default_factory=dict)
    spark_properties: dict[str, String] = field(default_factory=dict)
    validate_credentials: bool | None = None
    validate_for_compute_environments: list[String] = field(default_factory=list)


@dataclass
class GlueOAuth2Credentials(PropertyType):
    access_token: str | None = None
    jwt_token: str | None = None
    refresh_token: str | None = None
    user_managed_client_application_client_secret: str | None = None


@dataclass
class GluePropertiesInput(PropertyType):
    glue_connection_input: GlueConnectionInput | None = None


@dataclass
class HyperPodPropertiesInput(PropertyType):
    cluster_name: str | None = None


@dataclass
class IamPropertiesInput(PropertyType):
    glue_lineage_sync_enabled: bool | None = None


@dataclass
class LineageSyncSchedule(PropertyType):
    schedule: str | None = None


@dataclass
class MlflowPropertiesInput(PropertyType):
    tracking_server_arn: str | None = None


@dataclass
class OAuth2ClientApplication(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_managed_client_application_reference": "AWSManagedClientApplicationReference",
    }

    aws_managed_client_application_reference: str | None = None
    user_managed_client_application_client_id: str | None = None


@dataclass
class OAuth2Properties(PropertyType):
    authorization_code_properties: AuthorizationCodeProperties | None = None
    o_auth2_client_application: OAuth2ClientApplication | None = None
    o_auth2_credentials: GlueOAuth2Credentials | None = None
    o_auth2_grant_type: str | None = None
    token_url: str | None = None
    token_url_parameters_map: dict[str, String] = field(default_factory=dict)


@dataclass
class PhysicalConnectionRequirements(PropertyType):
    availability_zone: str | None = None
    security_group_id_list: list[String] = field(default_factory=list)
    subnet_id: str | None = None
    subnet_id_list: list[String] = field(default_factory=list)


@dataclass
class RedshiftCredentials(PropertyType):
    secret_arn: str | None = None
    username_password: UsernamePassword | None = None


@dataclass
class RedshiftLineageSyncConfigurationInput(PropertyType):
    enabled: bool | None = None
    schedule: LineageSyncSchedule | None = None


@dataclass
class RedshiftPropertiesInput(PropertyType):
    credentials: RedshiftCredentials | None = None
    database_name: str | None = None
    host: str | None = None
    lineage_sync: RedshiftLineageSyncConfigurationInput | None = None
    port: float | None = None
    storage: RedshiftStorageProperties | None = None


@dataclass
class RedshiftStorageProperties(PropertyType):
    cluster_name: str | None = None
    workgroup_name: str | None = None


@dataclass
class S3PropertiesInput(PropertyType):
    s3_uri: str | None = None
    s3_access_grant_location_id: str | None = None


@dataclass
class SparkEmrPropertiesInput(PropertyType):
    compute_arn: str | None = None
    instance_profile_arn: str | None = None
    java_virtual_env: str | None = None
    log_uri: str | None = None
    managed_endpoint_arn: str | None = None
    python_virtual_env: str | None = None
    runtime_role: str | None = None
    trusted_certificates_s3_uri: str | None = None


@dataclass
class SparkGlueArgs(PropertyType):
    connection: str | None = None


@dataclass
class SparkGluePropertiesInput(PropertyType):
    additional_args: SparkGlueArgs | None = None
    glue_connection_name: str | None = None
    glue_version: str | None = None
    idle_timeout: float | None = None
    java_virtual_env: str | None = None
    number_of_workers: float | None = None
    python_virtual_env: str | None = None
    worker_type: str | None = None


@dataclass
class UsernamePassword(PropertyType):
    password: str | None = None
    username: str | None = None
