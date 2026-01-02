"""PropertyTypes for AWS::AppMesh::VirtualGateway."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class JsonFormatRef(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class LoggingFormat(PropertyType):
    json: list[JsonFormatRef] = field(default_factory=list)
    text: str | None = None


@dataclass
class SubjectAlternativeNameMatchers(PropertyType):
    exact: list[String] = field(default_factory=list)


@dataclass
class SubjectAlternativeNames(PropertyType):
    match: SubjectAlternativeNameMatchers | None = None


@dataclass
class VirtualGatewayAccessLog(PropertyType):
    file: VirtualGatewayFileAccessLog | None = None


@dataclass
class VirtualGatewayBackendDefaults(PropertyType):
    client_policy: VirtualGatewayClientPolicy | None = None


@dataclass
class VirtualGatewayClientPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "tls": "TLS",
    }

    tls: VirtualGatewayClientPolicyTls | None = None


@dataclass
class VirtualGatewayClientPolicyTls(PropertyType):
    validation: VirtualGatewayTlsValidationContext | None = None
    certificate: VirtualGatewayClientTlsCertificate | None = None
    enforce: bool | None = None
    ports: list[Integer] = field(default_factory=list)


@dataclass
class VirtualGatewayClientTlsCertificate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sds": "SDS",
    }

    file: VirtualGatewayListenerTlsFileCertificate | None = None
    sds: VirtualGatewayListenerTlsSdsCertificate | None = None


@dataclass
class VirtualGatewayConnectionPool(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "grpc": "GRPC",
        "http": "HTTP",
        "http2": "HTTP2",
    }

    grpc: VirtualGatewayGrpcConnectionPool | None = None
    http: VirtualGatewayHttpConnectionPool | None = None
    http2: VirtualGatewayHttp2ConnectionPool | None = None


@dataclass
class VirtualGatewayFileAccessLog(PropertyType):
    path: str | None = None
    format: LoggingFormat | None = None


@dataclass
class VirtualGatewayGrpcConnectionPool(PropertyType):
    max_requests: int | None = None


@dataclass
class VirtualGatewayHealthCheckPolicy(PropertyType):
    healthy_threshold: int | None = None
    interval_millis: int | None = None
    protocol: str | None = None
    timeout_millis: int | None = None
    unhealthy_threshold: int | None = None
    path: str | None = None
    port: int | None = None


@dataclass
class VirtualGatewayHttp2ConnectionPool(PropertyType):
    max_requests: int | None = None


@dataclass
class VirtualGatewayHttpConnectionPool(PropertyType):
    max_connections: int | None = None
    max_pending_requests: int | None = None


@dataclass
class VirtualGatewayListener(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "tls": "TLS",
    }

    port_mapping: VirtualGatewayPortMapping | None = None
    connection_pool: VirtualGatewayConnectionPool | None = None
    health_check: VirtualGatewayHealthCheckPolicy | None = None
    tls: VirtualGatewayListenerTls | None = None


@dataclass
class VirtualGatewayListenerTls(PropertyType):
    certificate: VirtualGatewayListenerTlsCertificate | None = None
    mode: str | None = None
    validation: VirtualGatewayListenerTlsValidationContext | None = None


@dataclass
class VirtualGatewayListenerTlsAcmCertificate(PropertyType):
    certificate_arn: str | None = None


@dataclass
class VirtualGatewayListenerTlsCertificate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "acm": "ACM",
        "sds": "SDS",
    }

    acm: VirtualGatewayListenerTlsAcmCertificate | None = None
    file: VirtualGatewayListenerTlsFileCertificate | None = None
    sds: VirtualGatewayListenerTlsSdsCertificate | None = None


@dataclass
class VirtualGatewayListenerTlsFileCertificate(PropertyType):
    certificate_chain: str | None = None
    private_key: str | None = None


@dataclass
class VirtualGatewayListenerTlsSdsCertificate(PropertyType):
    secret_name: str | None = None


@dataclass
class VirtualGatewayListenerTlsValidationContext(PropertyType):
    trust: VirtualGatewayListenerTlsValidationContextTrust | None = None
    subject_alternative_names: SubjectAlternativeNames | None = None


@dataclass
class VirtualGatewayListenerTlsValidationContextTrust(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sds": "SDS",
    }

    file: VirtualGatewayTlsValidationContextFileTrust | None = None
    sds: VirtualGatewayTlsValidationContextSdsTrust | None = None


@dataclass
class VirtualGatewayLogging(PropertyType):
    access_log: VirtualGatewayAccessLog | None = None


@dataclass
class VirtualGatewayPortMapping(PropertyType):
    port: int | None = None
    protocol: str | None = None


@dataclass
class VirtualGatewaySpec(PropertyType):
    listeners: list[VirtualGatewayListener] = field(default_factory=list)
    backend_defaults: VirtualGatewayBackendDefaults | None = None
    logging: VirtualGatewayLogging | None = None


@dataclass
class VirtualGatewayTlsValidationContext(PropertyType):
    trust: VirtualGatewayTlsValidationContextTrust | None = None
    subject_alternative_names: SubjectAlternativeNames | None = None


@dataclass
class VirtualGatewayTlsValidationContextAcmTrust(PropertyType):
    certificate_authority_arns: list[String] = field(default_factory=list)


@dataclass
class VirtualGatewayTlsValidationContextFileTrust(PropertyType):
    certificate_chain: str | None = None


@dataclass
class VirtualGatewayTlsValidationContextSdsTrust(PropertyType):
    secret_name: str | None = None


@dataclass
class VirtualGatewayTlsValidationContextTrust(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "acm": "ACM",
        "sds": "SDS",
    }

    acm: VirtualGatewayTlsValidationContextAcmTrust | None = None
    file: VirtualGatewayTlsValidationContextFileTrust | None = None
    sds: VirtualGatewayTlsValidationContextSdsTrust | None = None
