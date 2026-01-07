"""PropertyTypes for AWS::MSK::Cluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BrokerLogs(PropertyType):
    cloud_watch_logs: DslValue[CloudWatchLogs] | None = None
    firehose: DslValue[Firehose] | None = None
    s3: DslValue[S3] | None = None


@dataclass
class BrokerNodeGroupInfo(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "broker_az_distribution": "BrokerAZDistribution",
    }

    client_subnets: list[DslValue[str]] = field(default_factory=list)
    instance_type: DslValue[str] | None = None
    broker_az_distribution: DslValue[str] | None = None
    connectivity_info: DslValue[ConnectivityInfo] | None = None
    security_groups: list[DslValue[str]] = field(default_factory=list)
    storage_info: DslValue[StorageInfo] | None = None


@dataclass
class ClientAuthentication(PropertyType):
    sasl: DslValue[Sasl] | None = None
    tls: DslValue[Tls] | None = None
    unauthenticated: DslValue[Unauthenticated] | None = None


@dataclass
class CloudWatchLogs(PropertyType):
    enabled: DslValue[bool] | None = None
    log_group: DslValue[str] | None = None


@dataclass
class ConfigurationInfo(PropertyType):
    arn: DslValue[str] | None = None
    revision: DslValue[int] | None = None


@dataclass
class ConnectivityInfo(PropertyType):
    network_type: DslValue[str] | None = None
    public_access: DslValue[PublicAccess] | None = None
    vpc_connectivity: DslValue[VpcConnectivity] | None = None


@dataclass
class EBSStorageInfo(PropertyType):
    provisioned_throughput: DslValue[ProvisionedThroughput] | None = None
    volume_size: DslValue[int] | None = None


@dataclass
class EncryptionAtRest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "data_volume_kms_key_id": "DataVolumeKMSKeyId",
    }

    data_volume_kms_key_id: DslValue[str] | None = None


@dataclass
class EncryptionInTransit(PropertyType):
    client_broker: DslValue[str] | None = None
    in_cluster: DslValue[bool] | None = None


@dataclass
class EncryptionInfo(PropertyType):
    encryption_at_rest: DslValue[EncryptionAtRest] | None = None
    encryption_in_transit: DslValue[EncryptionInTransit] | None = None


@dataclass
class Firehose(PropertyType):
    enabled: DslValue[bool] | None = None
    delivery_stream: DslValue[str] | None = None


@dataclass
class Iam(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class JmxExporter(PropertyType):
    enabled_in_broker: DslValue[bool] | None = None


@dataclass
class LoggingInfo(PropertyType):
    broker_logs: DslValue[BrokerLogs] | None = None


@dataclass
class NodeExporter(PropertyType):
    enabled_in_broker: DslValue[bool] | None = None


@dataclass
class OpenMonitoring(PropertyType):
    prometheus: DslValue[Prometheus] | None = None


@dataclass
class Prometheus(PropertyType):
    jmx_exporter: DslValue[JmxExporter] | None = None
    node_exporter: DslValue[NodeExporter] | None = None


@dataclass
class ProvisionedThroughput(PropertyType):
    enabled: DslValue[bool] | None = None
    volume_throughput: DslValue[int] | None = None


@dataclass
class PublicAccess(PropertyType):
    type_: DslValue[str] | None = None


@dataclass
class Rebalancing(PropertyType):
    status: DslValue[str] | None = None


@dataclass
class S3(PropertyType):
    enabled: DslValue[bool] | None = None
    bucket: DslValue[str] | None = None
    prefix: DslValue[str] | None = None


@dataclass
class Sasl(PropertyType):
    iam: DslValue[Iam] | None = None
    scram: DslValue[Scram] | None = None


@dataclass
class Scram(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class StorageInfo(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ebs_storage_info": "EBSStorageInfo",
    }

    ebs_storage_info: DslValue[EBSStorageInfo] | None = None


@dataclass
class Tls(PropertyType):
    certificate_authority_arn_list: list[DslValue[str]] = field(default_factory=list)
    enabled: DslValue[bool] | None = None


@dataclass
class Unauthenticated(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class VpcConnectivity(PropertyType):
    client_authentication: DslValue[VpcConnectivityClientAuthentication] | None = None


@dataclass
class VpcConnectivityClientAuthentication(PropertyType):
    sasl: DslValue[VpcConnectivitySasl] | None = None
    tls: DslValue[VpcConnectivityTls] | None = None


@dataclass
class VpcConnectivityIam(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class VpcConnectivitySasl(PropertyType):
    iam: DslValue[VpcConnectivityIam] | None = None
    scram: DslValue[VpcConnectivityScram] | None = None


@dataclass
class VpcConnectivityScram(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class VpcConnectivityTls(PropertyType):
    enabled: DslValue[bool] | None = None
