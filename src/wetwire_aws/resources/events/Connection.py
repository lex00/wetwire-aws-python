"""PropertyTypes for AWS::Events::Connection."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ApiKeyAuthParameters(PropertyType):
    api_key_name: str | None = None
    api_key_value: str | None = None


@dataclass
class AuthParameters(PropertyType):
    api_key_auth_parameters: ApiKeyAuthParameters | None = None
    basic_auth_parameters: BasicAuthParameters | None = None
    connectivity_parameters: ConnectivityParameters | None = None
    invocation_http_parameters: ConnectionHttpParameters | None = None
    o_auth_parameters: OAuthParameters | None = None


@dataclass
class BasicAuthParameters(PropertyType):
    password: str | None = None
    username: str | None = None


@dataclass
class ClientParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "client_id": "ClientID",
    }

    client_id: str | None = None
    client_secret: str | None = None


@dataclass
class ConnectionHttpParameters(PropertyType):
    body_parameters: list[Parameter] = field(default_factory=list)
    header_parameters: list[Parameter] = field(default_factory=list)
    query_string_parameters: list[Parameter] = field(default_factory=list)


@dataclass
class ConnectivityParameters(PropertyType):
    resource_parameters: ResourceParameters | None = None


@dataclass
class InvocationConnectivityParameters(PropertyType):
    resource_parameters: ResourceParameters | None = None


@dataclass
class OAuthParameters(PropertyType):
    authorization_endpoint: str | None = None
    client_parameters: ClientParameters | None = None
    http_method: str | None = None
    o_auth_http_parameters: ConnectionHttpParameters | None = None


@dataclass
class Parameter(PropertyType):
    key: str | None = None
    value: str | None = None
    is_value_secret: bool | None = None


@dataclass
class ResourceParameters(PropertyType):
    resource_configuration_arn: str | None = None
    resource_association_arn: str | None = None
