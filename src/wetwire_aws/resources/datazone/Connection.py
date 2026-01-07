"""PropertyTypes for AWS::DataZone::Connection."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AmazonQPropertiesInput(PropertyType):
    auth_mode: DslValue[str] | None = None
    is_enabled: DslValue[bool] | None = None
    profile_arn: DslValue[str] | None = None


@dataclass
class AthenaPropertiesInput(PropertyType):
    workgroup_name: DslValue[str] | None = None


@dataclass
class AuthenticationConfigurationInput(PropertyType):
    authentication_type: DslValue[str] | None = None
    basic_authentication_credentials: (
        DslValue[BasicAuthenticationCredentials] | None
    ) = None
    custom_authentication_credentials: dict[str, DslValue[str]] = field(
        default_factory=dict
    )
    kms_key_arn: DslValue[str] | None = None
    o_auth2_properties: DslValue[OAuth2Properties] | None = None
    secret_arn: DslValue[str] | None = None


@dataclass
class AuthorizationCodeProperties(PropertyType):
    authorization_code: DslValue[str] | None = None
    redirect_uri: DslValue[str] | None = None


@dataclass
class AwsLocation(PropertyType):
    access_role: DslValue[str] | None = None
    aws_account_id: DslValue[str] | None = None
    aws_region: DslValue[str] | None = None
    iam_connection_id: DslValue[str] | None = None


@dataclass
class BasicAuthenticationCredentials(PropertyType):
    password: DslValue[str] | None = None
    user_name: DslValue[str] | None = None


@dataclass
class ConnectionPropertiesInput(PropertyType):
    amazon_q_properties: DslValue[AmazonQPropertiesInput] | None = None
    athena_properties: DslValue[AthenaPropertiesInput] | None = None
    glue_properties: DslValue[GluePropertiesInput] | None = None
    hyper_pod_properties: DslValue[HyperPodPropertiesInput] | None = None
    iam_properties: DslValue[IamPropertiesInput] | None = None
    mlflow_properties: DslValue[MlflowPropertiesInput] | None = None
    redshift_properties: DslValue[RedshiftPropertiesInput] | None = None
    s3_properties: DslValue[S3PropertiesInput] | None = None
    spark_emr_properties: DslValue[SparkEmrPropertiesInput] | None = None
    spark_glue_properties: DslValue[SparkGluePropertiesInput] | None = None


@dataclass
class GlueConnectionInput(PropertyType):
    athena_properties: dict[str, DslValue[str]] = field(default_factory=dict)
    authentication_configuration: DslValue[AuthenticationConfigurationInput] | None = (
        None
    )
    connection_properties: dict[str, DslValue[str]] = field(default_factory=dict)
    connection_type: DslValue[str] | None = None
    description: DslValue[str] | None = None
    match_criteria: DslValue[str] | None = None
    name: DslValue[str] | None = None
    physical_connection_requirements: (
        DslValue[PhysicalConnectionRequirements] | None
    ) = None
    python_properties: dict[str, DslValue[str]] = field(default_factory=dict)
    spark_properties: dict[str, DslValue[str]] = field(default_factory=dict)
    validate_credentials: DslValue[bool] | None = None
    validate_for_compute_environments: list[DslValue[str]] = field(default_factory=list)


@dataclass
class GlueOAuth2Credentials(PropertyType):
    access_token: DslValue[str] | None = None
    jwt_token: DslValue[str] | None = None
    refresh_token: DslValue[str] | None = None
    user_managed_client_application_client_secret: DslValue[str] | None = None


@dataclass
class GluePropertiesInput(PropertyType):
    glue_connection_input: DslValue[GlueConnectionInput] | None = None


@dataclass
class HyperPodPropertiesInput(PropertyType):
    cluster_name: DslValue[str] | None = None


@dataclass
class IamPropertiesInput(PropertyType):
    glue_lineage_sync_enabled: DslValue[bool] | None = None


@dataclass
class LineageSyncSchedule(PropertyType):
    schedule: DslValue[str] | None = None


@dataclass
class MlflowPropertiesInput(PropertyType):
    tracking_server_arn: DslValue[str] | None = None


@dataclass
class OAuth2ClientApplication(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_managed_client_application_reference": "AWSManagedClientApplicationReference",
    }

    aws_managed_client_application_reference: DslValue[str] | None = None
    user_managed_client_application_client_id: DslValue[str] | None = None


@dataclass
class OAuth2Properties(PropertyType):
    authorization_code_properties: DslValue[AuthorizationCodeProperties] | None = None
    o_auth2_client_application: DslValue[OAuth2ClientApplication] | None = None
    o_auth2_credentials: DslValue[GlueOAuth2Credentials] | None = None
    o_auth2_grant_type: DslValue[str] | None = None
    token_url: DslValue[str] | None = None
    token_url_parameters_map: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class PhysicalConnectionRequirements(PropertyType):
    availability_zone: DslValue[str] | None = None
    security_group_id_list: list[DslValue[str]] = field(default_factory=list)
    subnet_id: DslValue[str] | None = None
    subnet_id_list: list[DslValue[str]] = field(default_factory=list)


@dataclass
class RedshiftCredentials(PropertyType):
    secret_arn: DslValue[str] | None = None
    username_password: DslValue[UsernamePassword] | None = None


@dataclass
class RedshiftLineageSyncConfigurationInput(PropertyType):
    enabled: DslValue[bool] | None = None
    schedule: DslValue[LineageSyncSchedule] | None = None


@dataclass
class RedshiftPropertiesInput(PropertyType):
    credentials: DslValue[RedshiftCredentials] | None = None
    database_name: DslValue[str] | None = None
    host: DslValue[str] | None = None
    lineage_sync: DslValue[RedshiftLineageSyncConfigurationInput] | None = None
    port: DslValue[float] | None = None
    storage: DslValue[RedshiftStorageProperties] | None = None


@dataclass
class RedshiftStorageProperties(PropertyType):
    cluster_name: DslValue[str] | None = None
    workgroup_name: DslValue[str] | None = None


@dataclass
class S3PropertiesInput(PropertyType):
    s3_uri: DslValue[str] | None = None
    s3_access_grant_location_id: DslValue[str] | None = None


@dataclass
class SparkEmrPropertiesInput(PropertyType):
    compute_arn: DslValue[str] | None = None
    instance_profile_arn: DslValue[str] | None = None
    java_virtual_env: DslValue[str] | None = None
    log_uri: DslValue[str] | None = None
    managed_endpoint_arn: DslValue[str] | None = None
    python_virtual_env: DslValue[str] | None = None
    runtime_role: DslValue[str] | None = None
    trusted_certificates_s3_uri: DslValue[str] | None = None


@dataclass
class SparkGlueArgs(PropertyType):
    connection: DslValue[str] | None = None


@dataclass
class SparkGluePropertiesInput(PropertyType):
    additional_args: DslValue[SparkGlueArgs] | None = None
    glue_connection_name: DslValue[str] | None = None
    glue_version: DslValue[str] | None = None
    idle_timeout: DslValue[float] | None = None
    java_virtual_env: DslValue[str] | None = None
    number_of_workers: DslValue[float] | None = None
    python_virtual_env: DslValue[str] | None = None
    worker_type: DslValue[str] | None = None


@dataclass
class UsernamePassword(PropertyType):
    password: DslValue[str] | None = None
    username: DslValue[str] | None = None
