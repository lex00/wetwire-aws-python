"""PropertyTypes for AWS::EC2::ClientVpnEndpoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CertificateAuthenticationRequest(PropertyType):
    client_root_certificate_chain_arn: DslValue[str] | None = None


@dataclass
class ClientAuthenticationRequest(PropertyType):
    type_: DslValue[str] | None = None
    active_directory: DslValue[DirectoryServiceAuthenticationRequest] | None = None
    federated_authentication: DslValue[FederatedAuthenticationRequest] | None = None
    mutual_authentication: DslValue[CertificateAuthenticationRequest] | None = None


@dataclass
class ClientConnectOptions(PropertyType):
    enabled: DslValue[bool] | None = None
    lambda_function_arn: DslValue[str] | None = None


@dataclass
class ClientLoginBannerOptions(PropertyType):
    enabled: DslValue[bool] | None = None
    banner_text: DslValue[str] | None = None


@dataclass
class ClientRouteEnforcementOptions(PropertyType):
    enforced: DslValue[bool] | None = None


@dataclass
class ConnectionLogOptions(PropertyType):
    enabled: DslValue[bool] | None = None
    cloudwatch_log_group: DslValue[str] | None = None
    cloudwatch_log_stream: DslValue[str] | None = None


@dataclass
class DirectoryServiceAuthenticationRequest(PropertyType):
    directory_id: DslValue[str] | None = None


@dataclass
class FederatedAuthenticationRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "saml_provider_arn": "SAMLProviderArn",
        "self_service_saml_provider_arn": "SelfServiceSAMLProviderArn",
    }

    saml_provider_arn: DslValue[str] | None = None
    self_service_saml_provider_arn: DslValue[str] | None = None


@dataclass
class TagSpecification(PropertyType):
    resource_type: DslValue[str] | None = None
    tags: list[DslValue[Tag]] = field(default_factory=list)
