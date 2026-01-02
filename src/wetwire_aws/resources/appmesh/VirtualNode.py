"""PropertyTypes for AWS::AppMesh::VirtualNode."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AccessLog(PropertyType):
    file: FileAccessLog | None = None


@dataclass
class AwsCloudMapInstanceAttribute(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class AwsCloudMapServiceDiscovery(PropertyType):
    namespace_name: str | None = None
    service_name: str | None = None
    attributes: list[AwsCloudMapInstanceAttribute] = field(default_factory=list)
    ip_preference: str | None = None


@dataclass
class Backend(PropertyType):
    virtual_service: VirtualServiceBackend | None = None


@dataclass
class BackendDefaults(PropertyType):
    client_policy: ClientPolicy | None = None


@dataclass
class ClientPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "tls": "TLS",
    }

    tls: ClientPolicyTls | None = None


@dataclass
class ClientPolicyTls(PropertyType):
    validation: TlsValidationContext | None = None
    certificate: ClientTlsCertificate | None = None
    enforce: bool | None = None
    ports: list[Integer] = field(default_factory=list)


@dataclass
class ClientTlsCertificate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sds": "SDS",
    }

    file: ListenerTlsFileCertificate | None = None
    sds: ListenerTlsSdsCertificate | None = None


@dataclass
class DnsServiceDiscovery(PropertyType):
    hostname: str | None = None
    ip_preference: str | None = None
    response_type: str | None = None


@dataclass
class Duration(PropertyType):
    unit: str | None = None
    value: int | None = None


@dataclass
class FileAccessLog(PropertyType):
    path: str | None = None
    format: LoggingFormat | None = None


@dataclass
class GrpcTimeout(PropertyType):
    idle: Duration | None = None
    per_request: Duration | None = None


@dataclass
class HealthCheck(PropertyType):
    healthy_threshold: int | None = None
    interval_millis: int | None = None
    protocol: str | None = None
    timeout_millis: int | None = None
    unhealthy_threshold: int | None = None
    path: str | None = None
    port: int | None = None


@dataclass
class HttpTimeout(PropertyType):
    idle: Duration | None = None
    per_request: Duration | None = None


@dataclass
class JsonFormatRef(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class Listener(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "tls": "TLS",
    }

    port_mapping: PortMapping | None = None
    connection_pool: VirtualNodeConnectionPool | None = None
    health_check: HealthCheck | None = None
    outlier_detection: OutlierDetection | None = None
    timeout: ListenerTimeout | None = None
    tls: ListenerTls | None = None


@dataclass
class ListenerTimeout(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "grpc": "GRPC",
        "http": "HTTP",
        "http2": "HTTP2",
        "tcp": "TCP",
    }

    grpc: GrpcTimeout | None = None
    http: HttpTimeout | None = None
    http2: HttpTimeout | None = None
    tcp: TcpTimeout | None = None


@dataclass
class ListenerTls(PropertyType):
    certificate: ListenerTlsCertificate | None = None
    mode: str | None = None
    validation: ListenerTlsValidationContext | None = None


@dataclass
class ListenerTlsAcmCertificate(PropertyType):
    certificate_arn: str | None = None


@dataclass
class ListenerTlsCertificate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "acm": "ACM",
        "sds": "SDS",
    }

    acm: ListenerTlsAcmCertificate | None = None
    file: ListenerTlsFileCertificate | None = None
    sds: ListenerTlsSdsCertificate | None = None


@dataclass
class ListenerTlsFileCertificate(PropertyType):
    certificate_chain: str | None = None
    private_key: str | None = None


@dataclass
class ListenerTlsSdsCertificate(PropertyType):
    secret_name: str | None = None


@dataclass
class ListenerTlsValidationContext(PropertyType):
    trust: ListenerTlsValidationContextTrust | None = None
    subject_alternative_names: SubjectAlternativeNames | None = None


@dataclass
class ListenerTlsValidationContextTrust(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sds": "SDS",
    }

    file: TlsValidationContextFileTrust | None = None
    sds: TlsValidationContextSdsTrust | None = None


@dataclass
class Logging(PropertyType):
    access_log: AccessLog | None = None


@dataclass
class LoggingFormat(PropertyType):
    json: list[JsonFormatRef] = field(default_factory=list)
    text: str | None = None


@dataclass
class OutlierDetection(PropertyType):
    base_ejection_duration: Duration | None = None
    interval: Duration | None = None
    max_ejection_percent: int | None = None
    max_server_errors: int | None = None


@dataclass
class PortMapping(PropertyType):
    port: int | None = None
    protocol: str | None = None


@dataclass
class ServiceDiscovery(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "aws_cloud_map": "AWSCloudMap",
        "dns": "DNS",
    }

    aws_cloud_map: AwsCloudMapServiceDiscovery | None = None
    dns: DnsServiceDiscovery | None = None


@dataclass
class SubjectAlternativeNameMatchers(PropertyType):
    exact: list[String] = field(default_factory=list)


@dataclass
class SubjectAlternativeNames(PropertyType):
    match: SubjectAlternativeNameMatchers | None = None


@dataclass
class TcpTimeout(PropertyType):
    idle: Duration | None = None


@dataclass
class TlsValidationContext(PropertyType):
    trust: TlsValidationContextTrust | None = None
    subject_alternative_names: SubjectAlternativeNames | None = None


@dataclass
class TlsValidationContextAcmTrust(PropertyType):
    certificate_authority_arns: list[String] = field(default_factory=list)


@dataclass
class TlsValidationContextFileTrust(PropertyType):
    certificate_chain: str | None = None


@dataclass
class TlsValidationContextSdsTrust(PropertyType):
    secret_name: str | None = None


@dataclass
class TlsValidationContextTrust(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "acm": "ACM",
        "sds": "SDS",
    }

    acm: TlsValidationContextAcmTrust | None = None
    file: TlsValidationContextFileTrust | None = None
    sds: TlsValidationContextSdsTrust | None = None


@dataclass
class VirtualNodeConnectionPool(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "grpc": "GRPC",
        "http": "HTTP",
        "http2": "HTTP2",
        "tcp": "TCP",
    }

    grpc: VirtualNodeGrpcConnectionPool | None = None
    http: VirtualNodeHttpConnectionPool | None = None
    http2: VirtualNodeHttp2ConnectionPool | None = None
    tcp: VirtualNodeTcpConnectionPool | None = None


@dataclass
class VirtualNodeGrpcConnectionPool(PropertyType):
    max_requests: int | None = None


@dataclass
class VirtualNodeHttp2ConnectionPool(PropertyType):
    max_requests: int | None = None


@dataclass
class VirtualNodeHttpConnectionPool(PropertyType):
    max_connections: int | None = None
    max_pending_requests: int | None = None


@dataclass
class VirtualNodeSpec(PropertyType):
    backend_defaults: BackendDefaults | None = None
    backends: list[Backend] = field(default_factory=list)
    listeners: list[Listener] = field(default_factory=list)
    logging: Logging | None = None
    service_discovery: ServiceDiscovery | None = None


@dataclass
class VirtualNodeTcpConnectionPool(PropertyType):
    max_connections: int | None = None


@dataclass
class VirtualServiceBackend(PropertyType):
    virtual_service_name: str | None = None
    client_policy: ClientPolicy | None = None
