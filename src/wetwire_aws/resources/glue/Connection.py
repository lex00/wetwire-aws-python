"""PropertyTypes for AWS::Glue::Connection."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AuthenticationConfigurationInput(PropertyType):
    authentication_type: str | None = None
    basic_authentication_credentials: BasicAuthenticationCredentials | None = None
    custom_authentication_credentials: dict[str, Any] | None = None
    kms_key_arn: str | None = None
    o_auth2_properties: OAuth2PropertiesInput | None = None
    secret_arn: str | None = None


@dataclass
class AuthorizationCodeProperties(PropertyType):
    authorization_code: str | None = None
    redirect_uri: str | None = None


@dataclass
class BasicAuthenticationCredentials(PropertyType):
    password: str | None = None
    username: str | None = None


@dataclass
class ConnectionInput(PropertyType):
    connection_type: str | None = None
    athena_properties: dict[str, Any] | None = None
    authentication_configuration: AuthenticationConfigurationInput | None = None
    connection_properties: dict[str, Any] | None = None
    description: str | None = None
    match_criteria: list[String] = field(default_factory=list)
    name: str | None = None
    physical_connection_requirements: PhysicalConnectionRequirements | None = None
    python_properties: dict[str, Any] | None = None
    spark_properties: dict[str, Any] | None = None
    validate_credentials: bool | None = None
    validate_for_compute_environments: list[String] = field(default_factory=list)


@dataclass
class OAuth2ClientApplication(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_managed_client_application_reference": "AWSManagedClientApplicationReference",
    }

    aws_managed_client_application_reference: str | None = None
    user_managed_client_application_client_id: str | None = None


@dataclass
class OAuth2Credentials(PropertyType):
    access_token: str | None = None
    jwt_token: str | None = None
    refresh_token: str | None = None
    user_managed_client_application_client_secret: str | None = None


@dataclass
class OAuth2PropertiesInput(PropertyType):
    authorization_code_properties: AuthorizationCodeProperties | None = None
    o_auth2_client_application: OAuth2ClientApplication | None = None
    o_auth2_credentials: OAuth2Credentials | None = None
    o_auth2_grant_type: str | None = None
    token_url: str | None = None
    token_url_parameters_map: dict[str, Any] | None = None


@dataclass
class PhysicalConnectionRequirements(PropertyType):
    availability_zone: str | None = None
    security_group_id_list: list[String] = field(default_factory=list)
    subnet_id: str | None = None
