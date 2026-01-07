"""PropertyTypes for AWS::Glue::Connection."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AuthenticationConfigurationInput(PropertyType):
    authentication_type: DslValue[str] | None = None
    basic_authentication_credentials: (
        DslValue[BasicAuthenticationCredentials] | None
    ) = None
    custom_authentication_credentials: DslValue[dict[str, Any]] | None = None
    kms_key_arn: DslValue[str] | None = None
    o_auth2_properties: DslValue[OAuth2PropertiesInput] | None = None
    secret_arn: DslValue[str] | None = None


@dataclass
class AuthorizationCodeProperties(PropertyType):
    authorization_code: DslValue[str] | None = None
    redirect_uri: DslValue[str] | None = None


@dataclass
class BasicAuthenticationCredentials(PropertyType):
    password: DslValue[str] | None = None
    username: DslValue[str] | None = None


@dataclass
class ConnectionInput(PropertyType):
    connection_type: DslValue[str] | None = None
    athena_properties: DslValue[dict[str, Any]] | None = None
    authentication_configuration: DslValue[AuthenticationConfigurationInput] | None = (
        None
    )
    connection_properties: DslValue[dict[str, Any]] | None = None
    description: DslValue[str] | None = None
    match_criteria: list[DslValue[str]] = field(default_factory=list)
    name: DslValue[str] | None = None
    physical_connection_requirements: (
        DslValue[PhysicalConnectionRequirements] | None
    ) = None
    python_properties: DslValue[dict[str, Any]] | None = None
    spark_properties: DslValue[dict[str, Any]] | None = None
    validate_credentials: DslValue[bool] | None = None
    validate_for_compute_environments: list[DslValue[str]] = field(default_factory=list)


@dataclass
class OAuth2ClientApplication(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_managed_client_application_reference": "AWSManagedClientApplicationReference",
    }

    aws_managed_client_application_reference: DslValue[str] | None = None
    user_managed_client_application_client_id: DslValue[str] | None = None


@dataclass
class OAuth2Credentials(PropertyType):
    access_token: DslValue[str] | None = None
    jwt_token: DslValue[str] | None = None
    refresh_token: DslValue[str] | None = None
    user_managed_client_application_client_secret: DslValue[str] | None = None


@dataclass
class OAuth2PropertiesInput(PropertyType):
    authorization_code_properties: DslValue[AuthorizationCodeProperties] | None = None
    o_auth2_client_application: DslValue[OAuth2ClientApplication] | None = None
    o_auth2_credentials: DslValue[OAuth2Credentials] | None = None
    o_auth2_grant_type: DslValue[str] | None = None
    token_url: DslValue[str] | None = None
    token_url_parameters_map: DslValue[dict[str, Any]] | None = None


@dataclass
class PhysicalConnectionRequirements(PropertyType):
    availability_zone: DslValue[str] | None = None
    security_group_id_list: list[DslValue[str]] = field(default_factory=list)
    subnet_id: DslValue[str] | None = None
