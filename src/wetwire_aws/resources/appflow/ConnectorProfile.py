"""PropertyTypes for AWS::AppFlow::ConnectorProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AmplitudeConnectorProfileCredentials(PropertyType):
    api_key: str | None = None
    secret_key: str | None = None


@dataclass
class ApiKeyCredentials(PropertyType):
    api_key: str | None = None
    api_secret_key: str | None = None


@dataclass
class BasicAuthCredentials(PropertyType):
    password: str | None = None
    username: str | None = None


@dataclass
class ConnectorOAuthRequest(PropertyType):
    auth_code: str | None = None
    redirect_uri: str | None = None


@dataclass
class ConnectorProfileConfig(PropertyType):
    connector_profile_credentials: ConnectorProfileCredentials | None = None
    connector_profile_properties: ConnectorProfileProperties | None = None


@dataclass
class ConnectorProfileCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sapo_data": "SAPOData",
    }

    amplitude: AmplitudeConnectorProfileCredentials | None = None
    custom_connector: CustomConnectorProfileCredentials | None = None
    datadog: DatadogConnectorProfileCredentials | None = None
    dynatrace: DynatraceConnectorProfileCredentials | None = None
    google_analytics: GoogleAnalyticsConnectorProfileCredentials | None = None
    infor_nexus: InforNexusConnectorProfileCredentials | None = None
    marketo: MarketoConnectorProfileCredentials | None = None
    pardot: PardotConnectorProfileCredentials | None = None
    redshift: RedshiftConnectorProfileCredentials | None = None
    salesforce: SalesforceConnectorProfileCredentials | None = None
    sapo_data: SAPODataConnectorProfileCredentials | None = None
    service_now: ServiceNowConnectorProfileCredentials | None = None
    singular: SingularConnectorProfileCredentials | None = None
    slack: SlackConnectorProfileCredentials | None = None
    snowflake: SnowflakeConnectorProfileCredentials | None = None
    trendmicro: TrendmicroConnectorProfileCredentials | None = None
    veeva: VeevaConnectorProfileCredentials | None = None
    zendesk: ZendeskConnectorProfileCredentials | None = None


@dataclass
class ConnectorProfileProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sapo_data": "SAPOData",
    }

    custom_connector: CustomConnectorProfileProperties | None = None
    datadog: DatadogConnectorProfileProperties | None = None
    dynatrace: DynatraceConnectorProfileProperties | None = None
    infor_nexus: InforNexusConnectorProfileProperties | None = None
    marketo: MarketoConnectorProfileProperties | None = None
    pardot: PardotConnectorProfileProperties | None = None
    redshift: RedshiftConnectorProfileProperties | None = None
    salesforce: SalesforceConnectorProfileProperties | None = None
    sapo_data: SAPODataConnectorProfileProperties | None = None
    service_now: ServiceNowConnectorProfileProperties | None = None
    slack: SlackConnectorProfileProperties | None = None
    snowflake: SnowflakeConnectorProfileProperties | None = None
    veeva: VeevaConnectorProfileProperties | None = None
    zendesk: ZendeskConnectorProfileProperties | None = None


@dataclass
class CustomAuthCredentials(PropertyType):
    custom_authentication_type: str | None = None
    credentials_map: dict[str, String] = field(default_factory=dict)


@dataclass
class CustomConnectorProfileCredentials(PropertyType):
    authentication_type: str | None = None
    api_key: ApiKeyCredentials | None = None
    basic: BasicAuthCredentials | None = None
    custom: CustomAuthCredentials | None = None
    oauth2: OAuth2Credentials | None = None


@dataclass
class CustomConnectorProfileProperties(PropertyType):
    o_auth2_properties: OAuth2Properties | None = None
    profile_properties: dict[str, String] = field(default_factory=dict)


@dataclass
class DatadogConnectorProfileCredentials(PropertyType):
    api_key: str | None = None
    application_key: str | None = None


@dataclass
class DatadogConnectorProfileProperties(PropertyType):
    instance_url: str | None = None


@dataclass
class DynatraceConnectorProfileCredentials(PropertyType):
    api_token: str | None = None


@dataclass
class DynatraceConnectorProfileProperties(PropertyType):
    instance_url: str | None = None


@dataclass
class GoogleAnalyticsConnectorProfileCredentials(PropertyType):
    client_id: str | None = None
    client_secret: str | None = None
    access_token: str | None = None
    connector_o_auth_request: ConnectorOAuthRequest | None = None
    refresh_token: str | None = None


@dataclass
class InforNexusConnectorProfileCredentials(PropertyType):
    access_key_id: str | None = None
    datakey: str | None = None
    secret_access_key: str | None = None
    user_id: str | None = None


@dataclass
class InforNexusConnectorProfileProperties(PropertyType):
    instance_url: str | None = None


@dataclass
class MarketoConnectorProfileCredentials(PropertyType):
    client_id: str | None = None
    client_secret: str | None = None
    access_token: str | None = None
    connector_o_auth_request: ConnectorOAuthRequest | None = None


@dataclass
class MarketoConnectorProfileProperties(PropertyType):
    instance_url: str | None = None


@dataclass
class OAuth2Credentials(PropertyType):
    access_token: str | None = None
    client_id: str | None = None
    client_secret: str | None = None
    o_auth_request: ConnectorOAuthRequest | None = None
    refresh_token: str | None = None


@dataclass
class OAuth2Properties(PropertyType):
    o_auth2_grant_type: str | None = None
    token_url: str | None = None
    token_url_custom_properties: dict[str, String] = field(default_factory=dict)


@dataclass
class OAuthCredentials(PropertyType):
    access_token: str | None = None
    client_id: str | None = None
    client_secret: str | None = None
    connector_o_auth_request: ConnectorOAuthRequest | None = None
    refresh_token: str | None = None


@dataclass
class OAuthProperties(PropertyType):
    auth_code_url: str | None = None
    o_auth_scopes: list[String] = field(default_factory=list)
    token_url: str | None = None


@dataclass
class PardotConnectorProfileCredentials(PropertyType):
    access_token: str | None = None
    client_credentials_arn: str | None = None
    connector_o_auth_request: ConnectorOAuthRequest | None = None
    refresh_token: str | None = None


@dataclass
class PardotConnectorProfileProperties(PropertyType):
    business_unit_id: str | None = None
    instance_url: str | None = None
    is_sandbox_environment: bool | None = None


@dataclass
class RedshiftConnectorProfileCredentials(PropertyType):
    password: str | None = None
    username: str | None = None


@dataclass
class RedshiftConnectorProfileProperties(PropertyType):
    bucket_name: str | None = None
    role_arn: str | None = None
    bucket_prefix: str | None = None
    cluster_identifier: str | None = None
    data_api_role_arn: str | None = None
    database_name: str | None = None
    database_url: str | None = None
    is_redshift_serverless: bool | None = None
    workgroup_name: str | None = None


@dataclass
class SAPODataConnectorProfileCredentials(PropertyType):
    basic_auth_credentials: BasicAuthCredentials | None = None
    o_auth_credentials: OAuthCredentials | None = None


@dataclass
class SAPODataConnectorProfileProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "disable_sso": "DisableSSO",
    }

    application_host_url: str | None = None
    application_service_path: str | None = None
    client_number: str | None = None
    disable_sso: bool | None = None
    logon_language: str | None = None
    o_auth_properties: OAuthProperties | None = None
    port_number: int | None = None
    private_link_service_name: str | None = None


@dataclass
class SalesforceConnectorProfileCredentials(PropertyType):
    access_token: str | None = None
    client_credentials_arn: str | None = None
    connector_o_auth_request: ConnectorOAuthRequest | None = None
    jwt_token: str | None = None
    o_auth2_grant_type: str | None = None
    refresh_token: str | None = None


@dataclass
class SalesforceConnectorProfileProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "is_sandbox_environment": "isSandboxEnvironment",
        "use_private_link_for_metadata_and_authorization": "usePrivateLinkForMetadataAndAuthorization",
    }

    instance_url: str | None = None
    is_sandbox_environment: bool | None = None
    use_private_link_for_metadata_and_authorization: bool | None = None


@dataclass
class ServiceNowConnectorProfileCredentials(PropertyType):
    o_auth2_credentials: OAuth2Credentials | None = None
    password: str | None = None
    username: str | None = None


@dataclass
class ServiceNowConnectorProfileProperties(PropertyType):
    instance_url: str | None = None


@dataclass
class SingularConnectorProfileCredentials(PropertyType):
    api_key: str | None = None


@dataclass
class SlackConnectorProfileCredentials(PropertyType):
    client_id: str | None = None
    client_secret: str | None = None
    access_token: str | None = None
    connector_o_auth_request: ConnectorOAuthRequest | None = None


@dataclass
class SlackConnectorProfileProperties(PropertyType):
    instance_url: str | None = None


@dataclass
class SnowflakeConnectorProfileCredentials(PropertyType):
    password: str | None = None
    username: str | None = None


@dataclass
class SnowflakeConnectorProfileProperties(PropertyType):
    bucket_name: str | None = None
    stage: str | None = None
    warehouse: str | None = None
    account_name: str | None = None
    bucket_prefix: str | None = None
    private_link_service_name: str | None = None
    region: str | None = None


@dataclass
class TrendmicroConnectorProfileCredentials(PropertyType):
    api_secret_key: str | None = None


@dataclass
class VeevaConnectorProfileCredentials(PropertyType):
    password: str | None = None
    username: str | None = None


@dataclass
class VeevaConnectorProfileProperties(PropertyType):
    instance_url: str | None = None


@dataclass
class ZendeskConnectorProfileCredentials(PropertyType):
    client_id: str | None = None
    client_secret: str | None = None
    access_token: str | None = None
    connector_o_auth_request: ConnectorOAuthRequest | None = None


@dataclass
class ZendeskConnectorProfileProperties(PropertyType):
    instance_url: str | None = None
