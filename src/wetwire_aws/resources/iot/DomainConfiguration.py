"""PropertyTypes for AWS::IoT::DomainConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AuthorizerConfig(PropertyType):
    allow_authorizer_override: bool | None = None
    default_authorizer_name: str | None = None


@dataclass
class ClientCertificateConfig(PropertyType):
    client_certificate_callback_arn: str | None = None


@dataclass
class ServerCertificateConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_ocsp_check": "EnableOCSPCheck",
    }

    enable_ocsp_check: bool | None = None
    ocsp_authorized_responder_arn: str | None = None
    ocsp_lambda_arn: str | None = None


@dataclass
class ServerCertificateSummary(PropertyType):
    server_certificate_arn: str | None = None
    server_certificate_status: str | None = None
    server_certificate_status_detail: str | None = None


@dataclass
class TlsConfig(PropertyType):
    security_policy: str | None = None
