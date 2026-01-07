"""PropertyTypes for AWS::AppMesh::VirtualGateway."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class JsonFormatRef(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class LoggingFormat(PropertyType):
    json: list[DslValue[JsonFormatRef]] = field(default_factory=list)
    text: DslValue[str] | None = None


@dataclass
class SubjectAlternativeNameMatchers(PropertyType):
    exact: list[DslValue[str]] = field(default_factory=list)


@dataclass
class SubjectAlternativeNames(PropertyType):
    match: DslValue[SubjectAlternativeNameMatchers] | None = None


@dataclass
class VirtualGatewayAccessLog(PropertyType):
    file: DslValue[VirtualGatewayFileAccessLog] | None = None


@dataclass
class VirtualGatewayBackendDefaults(PropertyType):
    client_policy: DslValue[VirtualGatewayClientPolicy] | None = None


@dataclass
class VirtualGatewayClientPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "tls": "TLS",
    }

    tls: DslValue[VirtualGatewayClientPolicyTls] | None = None


@dataclass
class VirtualGatewayClientPolicyTls(PropertyType):
    validation: DslValue[VirtualGatewayTlsValidationContext] | None = None
    certificate: DslValue[VirtualGatewayClientTlsCertificate] | None = None
    enforce: DslValue[bool] | None = None
    ports: list[DslValue[int]] = field(default_factory=list)


@dataclass
class VirtualGatewayClientTlsCertificate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sds": "SDS",
    }

    file: DslValue[VirtualGatewayListenerTlsFileCertificate] | None = None
    sds: DslValue[VirtualGatewayListenerTlsSdsCertificate] | None = None


@dataclass
class VirtualGatewayConnectionPool(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "grpc": "GRPC",
        "http": "HTTP",
        "http2": "HTTP2",
    }

    grpc: DslValue[VirtualGatewayGrpcConnectionPool] | None = None
    http: DslValue[VirtualGatewayHttpConnectionPool] | None = None
    http2: DslValue[VirtualGatewayHttp2ConnectionPool] | None = None


@dataclass
class VirtualGatewayFileAccessLog(PropertyType):
    path: DslValue[str] | None = None
    format: DslValue[LoggingFormat] | None = None


@dataclass
class VirtualGatewayGrpcConnectionPool(PropertyType):
    max_requests: DslValue[int] | None = None


@dataclass
class VirtualGatewayHealthCheckPolicy(PropertyType):
    healthy_threshold: DslValue[int] | None = None
    interval_millis: DslValue[int] | None = None
    protocol: DslValue[str] | None = None
    timeout_millis: DslValue[int] | None = None
    unhealthy_threshold: DslValue[int] | None = None
    path: DslValue[str] | None = None
    port: DslValue[int] | None = None


@dataclass
class VirtualGatewayHttp2ConnectionPool(PropertyType):
    max_requests: DslValue[int] | None = None


@dataclass
class VirtualGatewayHttpConnectionPool(PropertyType):
    max_connections: DslValue[int] | None = None
    max_pending_requests: DslValue[int] | None = None


@dataclass
class VirtualGatewayListener(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "tls": "TLS",
    }

    port_mapping: DslValue[VirtualGatewayPortMapping] | None = None
    connection_pool: DslValue[VirtualGatewayConnectionPool] | None = None
    health_check: DslValue[VirtualGatewayHealthCheckPolicy] | None = None
    tls: DslValue[VirtualGatewayListenerTls] | None = None


@dataclass
class VirtualGatewayListenerTls(PropertyType):
    certificate: DslValue[VirtualGatewayListenerTlsCertificate] | None = None
    mode: DslValue[str] | None = None
    validation: DslValue[VirtualGatewayListenerTlsValidationContext] | None = None


@dataclass
class VirtualGatewayListenerTlsAcmCertificate(PropertyType):
    certificate_arn: DslValue[str] | None = None


@dataclass
class VirtualGatewayListenerTlsCertificate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "acm": "ACM",
        "sds": "SDS",
    }

    acm: DslValue[VirtualGatewayListenerTlsAcmCertificate] | None = None
    file: DslValue[VirtualGatewayListenerTlsFileCertificate] | None = None
    sds: DslValue[VirtualGatewayListenerTlsSdsCertificate] | None = None


@dataclass
class VirtualGatewayListenerTlsFileCertificate(PropertyType):
    certificate_chain: DslValue[str] | None = None
    private_key: DslValue[str] | None = None


@dataclass
class VirtualGatewayListenerTlsSdsCertificate(PropertyType):
    secret_name: DslValue[str] | None = None


@dataclass
class VirtualGatewayListenerTlsValidationContext(PropertyType):
    trust: DslValue[VirtualGatewayListenerTlsValidationContextTrust] | None = None
    subject_alternative_names: DslValue[SubjectAlternativeNames] | None = None


@dataclass
class VirtualGatewayListenerTlsValidationContextTrust(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sds": "SDS",
    }

    file: DslValue[VirtualGatewayTlsValidationContextFileTrust] | None = None
    sds: DslValue[VirtualGatewayTlsValidationContextSdsTrust] | None = None


@dataclass
class VirtualGatewayLogging(PropertyType):
    access_log: DslValue[VirtualGatewayAccessLog] | None = None


@dataclass
class VirtualGatewayPortMapping(PropertyType):
    port: DslValue[int] | None = None
    protocol: DslValue[str] | None = None


@dataclass
class VirtualGatewaySpec(PropertyType):
    listeners: list[DslValue[VirtualGatewayListener]] = field(default_factory=list)
    backend_defaults: DslValue[VirtualGatewayBackendDefaults] | None = None
    logging: DslValue[VirtualGatewayLogging] | None = None


@dataclass
class VirtualGatewayTlsValidationContext(PropertyType):
    trust: DslValue[VirtualGatewayTlsValidationContextTrust] | None = None
    subject_alternative_names: DslValue[SubjectAlternativeNames] | None = None


@dataclass
class VirtualGatewayTlsValidationContextAcmTrust(PropertyType):
    certificate_authority_arns: list[DslValue[str]] = field(default_factory=list)


@dataclass
class VirtualGatewayTlsValidationContextFileTrust(PropertyType):
    certificate_chain: DslValue[str] | None = None


@dataclass
class VirtualGatewayTlsValidationContextSdsTrust(PropertyType):
    secret_name: DslValue[str] | None = None


@dataclass
class VirtualGatewayTlsValidationContextTrust(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "acm": "ACM",
        "sds": "SDS",
    }

    acm: DslValue[VirtualGatewayTlsValidationContextAcmTrust] | None = None
    file: DslValue[VirtualGatewayTlsValidationContextFileTrust] | None = None
    sds: DslValue[VirtualGatewayTlsValidationContextSdsTrust] | None = None
