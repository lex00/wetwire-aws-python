"""PropertyTypes for AWS::Events::Connection."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ApiKeyAuthParameters(PropertyType):
    api_key_name: DslValue[str] | None = None
    api_key_value: DslValue[str] | None = None


@dataclass
class AuthParameters(PropertyType):
    api_key_auth_parameters: DslValue[ApiKeyAuthParameters] | None = None
    basic_auth_parameters: DslValue[BasicAuthParameters] | None = None
    connectivity_parameters: DslValue[ConnectivityParameters] | None = None
    invocation_http_parameters: DslValue[ConnectionHttpParameters] | None = None
    o_auth_parameters: DslValue[OAuthParameters] | None = None


@dataclass
class BasicAuthParameters(PropertyType):
    password: DslValue[str] | None = None
    username: DslValue[str] | None = None


@dataclass
class ClientParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "client_id": "ClientID",
    }

    client_id: DslValue[str] | None = None
    client_secret: DslValue[str] | None = None


@dataclass
class ConnectionHttpParameters(PropertyType):
    body_parameters: list[DslValue[Parameter]] = field(default_factory=list)
    header_parameters: list[DslValue[Parameter]] = field(default_factory=list)
    query_string_parameters: list[DslValue[Parameter]] = field(default_factory=list)


@dataclass
class ConnectivityParameters(PropertyType):
    resource_parameters: DslValue[ResourceParameters] | None = None


@dataclass
class InvocationConnectivityParameters(PropertyType):
    resource_parameters: DslValue[ResourceParameters] | None = None


@dataclass
class OAuthParameters(PropertyType):
    authorization_endpoint: DslValue[str] | None = None
    client_parameters: DslValue[ClientParameters] | None = None
    http_method: DslValue[str] | None = None
    o_auth_http_parameters: DslValue[ConnectionHttpParameters] | None = None


@dataclass
class Parameter(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None
    is_value_secret: DslValue[bool] | None = None


@dataclass
class ResourceParameters(PropertyType):
    resource_configuration_arn: DslValue[str] | None = None
    resource_association_arn: DslValue[str] | None = None
