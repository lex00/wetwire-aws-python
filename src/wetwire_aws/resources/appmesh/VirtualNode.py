"""PropertyTypes for AWS::AppMesh::VirtualNode."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AccessLog(PropertyType):
    file: DslValue[FileAccessLog] | None = None


@dataclass
class AwsCloudMapInstanceAttribute(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class AwsCloudMapServiceDiscovery(PropertyType):
    namespace_name: DslValue[str] | None = None
    service_name: DslValue[str] | None = None
    attributes: list[DslValue[AwsCloudMapInstanceAttribute]] = field(
        default_factory=list
    )
    ip_preference: DslValue[str] | None = None


@dataclass
class Backend(PropertyType):
    virtual_service: DslValue[VirtualServiceBackend] | None = None


@dataclass
class BackendDefaults(PropertyType):
    client_policy: DslValue[ClientPolicy] | None = None


@dataclass
class ClientPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "tls": "TLS",
    }

    tls: DslValue[ClientPolicyTls] | None = None


@dataclass
class ClientPolicyTls(PropertyType):
    validation: DslValue[TlsValidationContext] | None = None
    certificate: DslValue[ClientTlsCertificate] | None = None
    enforce: DslValue[bool] | None = None
    ports: list[DslValue[int]] = field(default_factory=list)


@dataclass
class ClientTlsCertificate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sds": "SDS",
    }

    file: DslValue[ListenerTlsFileCertificate] | None = None
    sds: DslValue[ListenerTlsSdsCertificate] | None = None


@dataclass
class DnsServiceDiscovery(PropertyType):
    hostname: DslValue[str] | None = None
    ip_preference: DslValue[str] | None = None
    response_type: DslValue[str] | None = None


@dataclass
class Duration(PropertyType):
    unit: DslValue[str] | None = None
    value: DslValue[int] | None = None


@dataclass
class FileAccessLog(PropertyType):
    path: DslValue[str] | None = None
    format: DslValue[LoggingFormat] | None = None


@dataclass
class GrpcTimeout(PropertyType):
    idle: DslValue[Duration] | None = None
    per_request: DslValue[Duration] | None = None


@dataclass
class HealthCheck(PropertyType):
    healthy_threshold: DslValue[int] | None = None
    interval_millis: DslValue[int] | None = None
    protocol: DslValue[str] | None = None
    timeout_millis: DslValue[int] | None = None
    unhealthy_threshold: DslValue[int] | None = None
    path: DslValue[str] | None = None
    port: DslValue[int] | None = None


@dataclass
class HttpTimeout(PropertyType):
    idle: DslValue[Duration] | None = None
    per_request: DslValue[Duration] | None = None


@dataclass
class JsonFormatRef(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class Listener(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "tls": "TLS",
    }

    port_mapping: DslValue[PortMapping] | None = None
    connection_pool: DslValue[VirtualNodeConnectionPool] | None = None
    health_check: DslValue[HealthCheck] | None = None
    outlier_detection: DslValue[OutlierDetection] | None = None
    timeout: DslValue[ListenerTimeout] | None = None
    tls: DslValue[ListenerTls] | None = None


@dataclass
class ListenerTimeout(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "grpc": "GRPC",
        "http": "HTTP",
        "http2": "HTTP2",
        "tcp": "TCP",
    }

    grpc: DslValue[GrpcTimeout] | None = None
    http: DslValue[HttpTimeout] | None = None
    http2: DslValue[HttpTimeout] | None = None
    tcp: DslValue[TcpTimeout] | None = None


@dataclass
class ListenerTls(PropertyType):
    certificate: DslValue[ListenerTlsCertificate] | None = None
    mode: DslValue[str] | None = None
    validation: DslValue[ListenerTlsValidationContext] | None = None


@dataclass
class ListenerTlsAcmCertificate(PropertyType):
    certificate_arn: DslValue[str] | None = None


@dataclass
class ListenerTlsCertificate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "acm": "ACM",
        "sds": "SDS",
    }

    acm: DslValue[ListenerTlsAcmCertificate] | None = None
    file: DslValue[ListenerTlsFileCertificate] | None = None
    sds: DslValue[ListenerTlsSdsCertificate] | None = None


@dataclass
class ListenerTlsFileCertificate(PropertyType):
    certificate_chain: DslValue[str] | None = None
    private_key: DslValue[str] | None = None


@dataclass
class ListenerTlsSdsCertificate(PropertyType):
    secret_name: DslValue[str] | None = None


@dataclass
class ListenerTlsValidationContext(PropertyType):
    trust: DslValue[ListenerTlsValidationContextTrust] | None = None
    subject_alternative_names: DslValue[SubjectAlternativeNames] | None = None


@dataclass
class ListenerTlsValidationContextTrust(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sds": "SDS",
    }

    file: DslValue[TlsValidationContextFileTrust] | None = None
    sds: DslValue[TlsValidationContextSdsTrust] | None = None


@dataclass
class Logging(PropertyType):
    access_log: DslValue[AccessLog] | None = None


@dataclass
class LoggingFormat(PropertyType):
    json: list[DslValue[JsonFormatRef]] = field(default_factory=list)
    text: DslValue[str] | None = None


@dataclass
class OutlierDetection(PropertyType):
    base_ejection_duration: DslValue[Duration] | None = None
    interval: DslValue[Duration] | None = None
    max_ejection_percent: DslValue[int] | None = None
    max_server_errors: DslValue[int] | None = None


@dataclass
class PortMapping(PropertyType):
    port: DslValue[int] | None = None
    protocol: DslValue[str] | None = None


@dataclass
class ServiceDiscovery(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_cloud_map": "AWSCloudMap",
        "dns": "DNS",
    }

    aws_cloud_map: DslValue[AwsCloudMapServiceDiscovery] | None = None
    dns: DslValue[DnsServiceDiscovery] | None = None


@dataclass
class SubjectAlternativeNameMatchers(PropertyType):
    exact: list[DslValue[str]] = field(default_factory=list)


@dataclass
class SubjectAlternativeNames(PropertyType):
    match: DslValue[SubjectAlternativeNameMatchers] | None = None


@dataclass
class TcpTimeout(PropertyType):
    idle: DslValue[Duration] | None = None


@dataclass
class TlsValidationContext(PropertyType):
    trust: DslValue[TlsValidationContextTrust] | None = None
    subject_alternative_names: DslValue[SubjectAlternativeNames] | None = None


@dataclass
class TlsValidationContextAcmTrust(PropertyType):
    certificate_authority_arns: list[DslValue[str]] = field(default_factory=list)


@dataclass
class TlsValidationContextFileTrust(PropertyType):
    certificate_chain: DslValue[str] | None = None


@dataclass
class TlsValidationContextSdsTrust(PropertyType):
    secret_name: DslValue[str] | None = None


@dataclass
class TlsValidationContextTrust(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "acm": "ACM",
        "sds": "SDS",
    }

    acm: DslValue[TlsValidationContextAcmTrust] | None = None
    file: DslValue[TlsValidationContextFileTrust] | None = None
    sds: DslValue[TlsValidationContextSdsTrust] | None = None


@dataclass
class VirtualNodeConnectionPool(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "grpc": "GRPC",
        "http": "HTTP",
        "http2": "HTTP2",
        "tcp": "TCP",
    }

    grpc: DslValue[VirtualNodeGrpcConnectionPool] | None = None
    http: DslValue[VirtualNodeHttpConnectionPool] | None = None
    http2: DslValue[VirtualNodeHttp2ConnectionPool] | None = None
    tcp: DslValue[VirtualNodeTcpConnectionPool] | None = None


@dataclass
class VirtualNodeGrpcConnectionPool(PropertyType):
    max_requests: DslValue[int] | None = None


@dataclass
class VirtualNodeHttp2ConnectionPool(PropertyType):
    max_requests: DslValue[int] | None = None


@dataclass
class VirtualNodeHttpConnectionPool(PropertyType):
    max_connections: DslValue[int] | None = None
    max_pending_requests: DslValue[int] | None = None


@dataclass
class VirtualNodeSpec(PropertyType):
    backend_defaults: DslValue[BackendDefaults] | None = None
    backends: list[DslValue[Backend]] = field(default_factory=list)
    listeners: list[DslValue[Listener]] = field(default_factory=list)
    logging: DslValue[Logging] | None = None
    service_discovery: DslValue[ServiceDiscovery] | None = None


@dataclass
class VirtualNodeTcpConnectionPool(PropertyType):
    max_connections: DslValue[int] | None = None


@dataclass
class VirtualServiceBackend(PropertyType):
    virtual_service_name: DslValue[str] | None = None
    client_policy: DslValue[ClientPolicy] | None = None
