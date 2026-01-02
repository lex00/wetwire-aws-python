"""PropertyTypes for AWS::EC2::ClientVpnEndpoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CertificateAuthenticationRequest(PropertyType):
    client_root_certificate_chain_arn: str | None = None


@dataclass
class ClientAuthenticationRequest(PropertyType):
    type_: str | None = None
    active_directory: DirectoryServiceAuthenticationRequest | None = None
    federated_authentication: FederatedAuthenticationRequest | None = None
    mutual_authentication: CertificateAuthenticationRequest | None = None


@dataclass
class ClientConnectOptions(PropertyType):
    enabled: bool | None = None
    lambda_function_arn: str | None = None


@dataclass
class ClientLoginBannerOptions(PropertyType):
    enabled: bool | None = None
    banner_text: str | None = None


@dataclass
class ClientRouteEnforcementOptions(PropertyType):
    enforced: bool | None = None


@dataclass
class ConnectionLogOptions(PropertyType):
    enabled: bool | None = None
    cloudwatch_log_group: str | None = None
    cloudwatch_log_stream: str | None = None


@dataclass
class DirectoryServiceAuthenticationRequest(PropertyType):
    directory_id: str | None = None


@dataclass
class FederatedAuthenticationRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "saml_provider_arn": "SAMLProviderArn",
        "self_service_saml_provider_arn": "SelfServiceSAMLProviderArn",
    }

    saml_provider_arn: str | None = None
    self_service_saml_provider_arn: str | None = None


@dataclass
class TagSpecification(PropertyType):
    resource_type: str | None = None
    tags: list[Tag] = field(default_factory=list)
