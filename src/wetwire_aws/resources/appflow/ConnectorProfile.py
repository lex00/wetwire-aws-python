"""PropertyTypes for AWS::AppFlow::ConnectorProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AmplitudeConnectorProfileCredentials(PropertyType):
    api_key: DslValue[str] | None = None
    secret_key: DslValue[str] | None = None


@dataclass
class ApiKeyCredentials(PropertyType):
    api_key: DslValue[str] | None = None
    api_secret_key: DslValue[str] | None = None


@dataclass
class BasicAuthCredentials(PropertyType):
    password: DslValue[str] | None = None
    username: DslValue[str] | None = None


@dataclass
class ConnectorOAuthRequest(PropertyType):
    auth_code: DslValue[str] | None = None
    redirect_uri: DslValue[str] | None = None


@dataclass
class ConnectorProfileConfig(PropertyType):
    connector_profile_credentials: DslValue[ConnectorProfileCredentials] | None = None
    connector_profile_properties: DslValue[ConnectorProfileProperties] | None = None


@dataclass
class ConnectorProfileCredentials(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sapo_data": "SAPOData",
    }

    amplitude: DslValue[AmplitudeConnectorProfileCredentials] | None = None
    custom_connector: DslValue[CustomConnectorProfileCredentials] | None = None
    datadog: DslValue[DatadogConnectorProfileCredentials] | None = None
    dynatrace: DslValue[DynatraceConnectorProfileCredentials] | None = None
    google_analytics: DslValue[GoogleAnalyticsConnectorProfileCredentials] | None = None
    infor_nexus: DslValue[InforNexusConnectorProfileCredentials] | None = None
    marketo: DslValue[MarketoConnectorProfileCredentials] | None = None
    pardot: DslValue[PardotConnectorProfileCredentials] | None = None
    redshift: DslValue[RedshiftConnectorProfileCredentials] | None = None
    salesforce: DslValue[SalesforceConnectorProfileCredentials] | None = None
    sapo_data: DslValue[SAPODataConnectorProfileCredentials] | None = None
    service_now: DslValue[ServiceNowConnectorProfileCredentials] | None = None
    singular: DslValue[SingularConnectorProfileCredentials] | None = None
    slack: DslValue[SlackConnectorProfileCredentials] | None = None
    snowflake: DslValue[SnowflakeConnectorProfileCredentials] | None = None
    trendmicro: DslValue[TrendmicroConnectorProfileCredentials] | None = None
    veeva: DslValue[VeevaConnectorProfileCredentials] | None = None
    zendesk: DslValue[ZendeskConnectorProfileCredentials] | None = None


@dataclass
class ConnectorProfileProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sapo_data": "SAPOData",
    }

    custom_connector: DslValue[CustomConnectorProfileProperties] | None = None
    datadog: DslValue[DatadogConnectorProfileProperties] | None = None
    dynatrace: DslValue[DynatraceConnectorProfileProperties] | None = None
    infor_nexus: DslValue[InforNexusConnectorProfileProperties] | None = None
    marketo: DslValue[MarketoConnectorProfileProperties] | None = None
    pardot: DslValue[PardotConnectorProfileProperties] | None = None
    redshift: DslValue[RedshiftConnectorProfileProperties] | None = None
    salesforce: DslValue[SalesforceConnectorProfileProperties] | None = None
    sapo_data: DslValue[SAPODataConnectorProfileProperties] | None = None
    service_now: DslValue[ServiceNowConnectorProfileProperties] | None = None
    slack: DslValue[SlackConnectorProfileProperties] | None = None
    snowflake: DslValue[SnowflakeConnectorProfileProperties] | None = None
    veeva: DslValue[VeevaConnectorProfileProperties] | None = None
    zendesk: DslValue[ZendeskConnectorProfileProperties] | None = None


@dataclass
class CustomAuthCredentials(PropertyType):
    custom_authentication_type: DslValue[str] | None = None
    credentials_map: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class CustomConnectorProfileCredentials(PropertyType):
    authentication_type: DslValue[str] | None = None
    api_key: DslValue[ApiKeyCredentials] | None = None
    basic: DslValue[BasicAuthCredentials] | None = None
    custom: DslValue[CustomAuthCredentials] | None = None
    oauth2: DslValue[OAuth2Credentials] | None = None


@dataclass
class CustomConnectorProfileProperties(PropertyType):
    o_auth2_properties: DslValue[OAuth2Properties] | None = None
    profile_properties: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class DatadogConnectorProfileCredentials(PropertyType):
    api_key: DslValue[str] | None = None
    application_key: DslValue[str] | None = None


@dataclass
class DatadogConnectorProfileProperties(PropertyType):
    instance_url: DslValue[str] | None = None


@dataclass
class DynatraceConnectorProfileCredentials(PropertyType):
    api_token: DslValue[str] | None = None


@dataclass
class DynatraceConnectorProfileProperties(PropertyType):
    instance_url: DslValue[str] | None = None


@dataclass
class GoogleAnalyticsConnectorProfileCredentials(PropertyType):
    client_id: DslValue[str] | None = None
    client_secret: DslValue[str] | None = None
    access_token: DslValue[str] | None = None
    connector_o_auth_request: DslValue[ConnectorOAuthRequest] | None = None
    refresh_token: DslValue[str] | None = None


@dataclass
class InforNexusConnectorProfileCredentials(PropertyType):
    access_key_id: DslValue[str] | None = None
    datakey: DslValue[str] | None = None
    secret_access_key: DslValue[str] | None = None
    user_id: DslValue[str] | None = None


@dataclass
class InforNexusConnectorProfileProperties(PropertyType):
    instance_url: DslValue[str] | None = None


@dataclass
class MarketoConnectorProfileCredentials(PropertyType):
    client_id: DslValue[str] | None = None
    client_secret: DslValue[str] | None = None
    access_token: DslValue[str] | None = None
    connector_o_auth_request: DslValue[ConnectorOAuthRequest] | None = None


@dataclass
class MarketoConnectorProfileProperties(PropertyType):
    instance_url: DslValue[str] | None = None


@dataclass
class OAuth2Credentials(PropertyType):
    access_token: DslValue[str] | None = None
    client_id: DslValue[str] | None = None
    client_secret: DslValue[str] | None = None
    o_auth_request: DslValue[ConnectorOAuthRequest] | None = None
    refresh_token: DslValue[str] | None = None


@dataclass
class OAuth2Properties(PropertyType):
    o_auth2_grant_type: DslValue[str] | None = None
    token_url: DslValue[str] | None = None
    token_url_custom_properties: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class OAuthCredentials(PropertyType):
    access_token: DslValue[str] | None = None
    client_id: DslValue[str] | None = None
    client_secret: DslValue[str] | None = None
    connector_o_auth_request: DslValue[ConnectorOAuthRequest] | None = None
    refresh_token: DslValue[str] | None = None


@dataclass
class OAuthProperties(PropertyType):
    auth_code_url: DslValue[str] | None = None
    o_auth_scopes: list[DslValue[str]] = field(default_factory=list)
    token_url: DslValue[str] | None = None


@dataclass
class PardotConnectorProfileCredentials(PropertyType):
    access_token: DslValue[str] | None = None
    client_credentials_arn: DslValue[str] | None = None
    connector_o_auth_request: DslValue[ConnectorOAuthRequest] | None = None
    refresh_token: DslValue[str] | None = None


@dataclass
class PardotConnectorProfileProperties(PropertyType):
    business_unit_id: DslValue[str] | None = None
    instance_url: DslValue[str] | None = None
    is_sandbox_environment: DslValue[bool] | None = None


@dataclass
class RedshiftConnectorProfileCredentials(PropertyType):
    password: DslValue[str] | None = None
    username: DslValue[str] | None = None


@dataclass
class RedshiftConnectorProfileProperties(PropertyType):
    bucket_name: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    bucket_prefix: DslValue[str] | None = None
    cluster_identifier: DslValue[str] | None = None
    data_api_role_arn: DslValue[str] | None = None
    database_name: DslValue[str] | None = None
    database_url: DslValue[str] | None = None
    is_redshift_serverless: DslValue[bool] | None = None
    workgroup_name: DslValue[str] | None = None


@dataclass
class SAPODataConnectorProfileCredentials(PropertyType):
    basic_auth_credentials: DslValue[BasicAuthCredentials] | None = None
    o_auth_credentials: DslValue[OAuthCredentials] | None = None


@dataclass
class SAPODataConnectorProfileProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "disable_sso": "DisableSSO",
    }

    application_host_url: DslValue[str] | None = None
    application_service_path: DslValue[str] | None = None
    client_number: DslValue[str] | None = None
    disable_sso: DslValue[bool] | None = None
    logon_language: DslValue[str] | None = None
    o_auth_properties: DslValue[OAuthProperties] | None = None
    port_number: DslValue[int] | None = None
    private_link_service_name: DslValue[str] | None = None


@dataclass
class SalesforceConnectorProfileCredentials(PropertyType):
    access_token: DslValue[str] | None = None
    client_credentials_arn: DslValue[str] | None = None
    connector_o_auth_request: DslValue[ConnectorOAuthRequest] | None = None
    jwt_token: DslValue[str] | None = None
    o_auth2_grant_type: DslValue[str] | None = None
    refresh_token: DslValue[str] | None = None


@dataclass
class SalesforceConnectorProfileProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "is_sandbox_environment": "isSandboxEnvironment",
        "use_private_link_for_metadata_and_authorization": "usePrivateLinkForMetadataAndAuthorization",
    }

    instance_url: DslValue[str] | None = None
    is_sandbox_environment: DslValue[bool] | None = None
    use_private_link_for_metadata_and_authorization: DslValue[bool] | None = None


@dataclass
class ServiceNowConnectorProfileCredentials(PropertyType):
    o_auth2_credentials: DslValue[OAuth2Credentials] | None = None
    password: DslValue[str] | None = None
    username: DslValue[str] | None = None


@dataclass
class ServiceNowConnectorProfileProperties(PropertyType):
    instance_url: DslValue[str] | None = None


@dataclass
class SingularConnectorProfileCredentials(PropertyType):
    api_key: DslValue[str] | None = None


@dataclass
class SlackConnectorProfileCredentials(PropertyType):
    client_id: DslValue[str] | None = None
    client_secret: DslValue[str] | None = None
    access_token: DslValue[str] | None = None
    connector_o_auth_request: DslValue[ConnectorOAuthRequest] | None = None


@dataclass
class SlackConnectorProfileProperties(PropertyType):
    instance_url: DslValue[str] | None = None


@dataclass
class SnowflakeConnectorProfileCredentials(PropertyType):
    password: DslValue[str] | None = None
    username: DslValue[str] | None = None


@dataclass
class SnowflakeConnectorProfileProperties(PropertyType):
    bucket_name: DslValue[str] | None = None
    stage: DslValue[str] | None = None
    warehouse: DslValue[str] | None = None
    account_name: DslValue[str] | None = None
    bucket_prefix: DslValue[str] | None = None
    private_link_service_name: DslValue[str] | None = None
    region: DslValue[str] | None = None


@dataclass
class TrendmicroConnectorProfileCredentials(PropertyType):
    api_secret_key: DslValue[str] | None = None


@dataclass
class VeevaConnectorProfileCredentials(PropertyType):
    password: DslValue[str] | None = None
    username: DslValue[str] | None = None


@dataclass
class VeevaConnectorProfileProperties(PropertyType):
    instance_url: DslValue[str] | None = None


@dataclass
class ZendeskConnectorProfileCredentials(PropertyType):
    client_id: DslValue[str] | None = None
    client_secret: DslValue[str] | None = None
    access_token: DslValue[str] | None = None
    connector_o_auth_request: DslValue[ConnectorOAuthRequest] | None = None


@dataclass
class ZendeskConnectorProfileProperties(PropertyType):
    instance_url: DslValue[str] | None = None
