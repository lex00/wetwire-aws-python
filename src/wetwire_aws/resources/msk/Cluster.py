"""PropertyTypes for AWS::MSK::Cluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BrokerLogs(PropertyType):
    cloud_watch_logs: CloudWatchLogs | None = None
    firehose: Firehose | None = None
    s3: S3 | None = None


@dataclass
class BrokerNodeGroupInfo(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "broker_az_distribution": "BrokerAZDistribution",
    }

    client_subnets: list[String] = field(default_factory=list)
    instance_type: str | None = None
    broker_az_distribution: str | None = None
    connectivity_info: ConnectivityInfo | None = None
    security_groups: list[String] = field(default_factory=list)
    storage_info: StorageInfo | None = None


@dataclass
class ClientAuthentication(PropertyType):
    sasl: Sasl | None = None
    tls: Tls | None = None
    unauthenticated: Unauthenticated | None = None


@dataclass
class CloudWatchLogs(PropertyType):
    enabled: bool | None = None
    log_group: str | None = None


@dataclass
class ConfigurationInfo(PropertyType):
    arn: str | None = None
    revision: int | None = None


@dataclass
class ConnectivityInfo(PropertyType):
    network_type: str | None = None
    public_access: PublicAccess | None = None
    vpc_connectivity: VpcConnectivity | None = None


@dataclass
class EBSStorageInfo(PropertyType):
    provisioned_throughput: ProvisionedThroughput | None = None
    volume_size: int | None = None


@dataclass
class EncryptionAtRest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_volume_kms_key_id": "DataVolumeKMSKeyId",
    }

    data_volume_kms_key_id: str | None = None


@dataclass
class EncryptionInTransit(PropertyType):
    client_broker: str | None = None
    in_cluster: bool | None = None


@dataclass
class EncryptionInfo(PropertyType):
    encryption_at_rest: EncryptionAtRest | None = None
    encryption_in_transit: EncryptionInTransit | None = None


@dataclass
class Firehose(PropertyType):
    enabled: bool | None = None
    delivery_stream: str | None = None


@dataclass
class Iam(PropertyType):
    enabled: bool | None = None


@dataclass
class JmxExporter(PropertyType):
    enabled_in_broker: bool | None = None


@dataclass
class LoggingInfo(PropertyType):
    broker_logs: BrokerLogs | None = None


@dataclass
class NodeExporter(PropertyType):
    enabled_in_broker: bool | None = None


@dataclass
class OpenMonitoring(PropertyType):
    prometheus: Prometheus | None = None


@dataclass
class Prometheus(PropertyType):
    jmx_exporter: JmxExporter | None = None
    node_exporter: NodeExporter | None = None


@dataclass
class ProvisionedThroughput(PropertyType):
    enabled: bool | None = None
    volume_throughput: int | None = None


@dataclass
class PublicAccess(PropertyType):
    type_: str | None = None


@dataclass
class Rebalancing(PropertyType):
    status: str | None = None


@dataclass
class S3(PropertyType):
    enabled: bool | None = None
    bucket: str | None = None
    prefix: str | None = None


@dataclass
class Sasl(PropertyType):
    iam: Iam | None = None
    scram: Scram | None = None


@dataclass
class Scram(PropertyType):
    enabled: bool | None = None


@dataclass
class StorageInfo(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ebs_storage_info": "EBSStorageInfo",
    }

    ebs_storage_info: EBSStorageInfo | None = None


@dataclass
class Tls(PropertyType):
    certificate_authority_arn_list: list[String] = field(default_factory=list)
    enabled: bool | None = None


@dataclass
class Unauthenticated(PropertyType):
    enabled: bool | None = None


@dataclass
class VpcConnectivity(PropertyType):
    client_authentication: VpcConnectivityClientAuthentication | None = None


@dataclass
class VpcConnectivityClientAuthentication(PropertyType):
    sasl: VpcConnectivitySasl | None = None
    tls: VpcConnectivityTls | None = None


@dataclass
class VpcConnectivityIam(PropertyType):
    enabled: bool | None = None


@dataclass
class VpcConnectivitySasl(PropertyType):
    iam: VpcConnectivityIam | None = None
    scram: VpcConnectivityScram | None = None


@dataclass
class VpcConnectivityScram(PropertyType):
    enabled: bool | None = None


@dataclass
class VpcConnectivityTls(PropertyType):
    enabled: bool | None = None
