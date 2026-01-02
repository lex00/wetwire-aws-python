"""PropertyTypes for AWS::EKS::Cluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AccessConfig(PropertyType):
    authentication_mode: str | None = None
    bootstrap_cluster_creator_admin_permissions: bool | None = None


@dataclass
class BlockStorage(PropertyType):
    enabled: bool | None = None


@dataclass
class ClusterLogging(PropertyType):
    enabled_types: list[LoggingTypeConfig] = field(default_factory=list)


@dataclass
class ComputeConfig(PropertyType):
    enabled: bool | None = None
    node_pools: list[String] = field(default_factory=list)
    node_role_arn: str | None = None


@dataclass
class ControlPlanePlacement(PropertyType):
    group_name: str | None = None


@dataclass
class ControlPlaneScalingConfig(PropertyType):
    tier: str | None = None


@dataclass
class ElasticLoadBalancing(PropertyType):
    enabled: bool | None = None


@dataclass
class EncryptionConfig(PropertyType):
    provider: Provider | None = None
    resources: list[String] = field(default_factory=list)


@dataclass
class KubernetesNetworkConfig(PropertyType):
    elastic_load_balancing: ElasticLoadBalancing | None = None
    ip_family: str | None = None
    service_ipv4_cidr: str | None = None
    service_ipv6_cidr: str | None = None


@dataclass
class Logging(PropertyType):
    cluster_logging: ClusterLogging | None = None


@dataclass
class LoggingTypeConfig(PropertyType):
    type_: str | None = None


@dataclass
class OutpostConfig(PropertyType):
    control_plane_instance_type: str | None = None
    outpost_arns: list[String] = field(default_factory=list)
    control_plane_placement: ControlPlanePlacement | None = None


@dataclass
class Provider(PropertyType):
    key_arn: str | None = None


@dataclass
class RemoteNetworkConfig(PropertyType):
    remote_node_networks: list[RemoteNodeNetwork] = field(default_factory=list)
    remote_pod_networks: list[RemotePodNetwork] = field(default_factory=list)


@dataclass
class RemoteNodeNetwork(PropertyType):
    cidrs: list[String] = field(default_factory=list)


@dataclass
class RemotePodNetwork(PropertyType):
    cidrs: list[String] = field(default_factory=list)


@dataclass
class ResourcesVpcConfig(PropertyType):
    subnet_ids: list[String] = field(default_factory=list)
    endpoint_private_access: bool | None = None
    endpoint_public_access: bool | None = None
    public_access_cidrs: list[String] = field(default_factory=list)
    security_group_ids: list[String] = field(default_factory=list)


@dataclass
class StorageConfig(PropertyType):
    block_storage: BlockStorage | None = None


@dataclass
class UpgradePolicy(PropertyType):
    support_type: str | None = None


@dataclass
class ZonalShiftConfig(PropertyType):
    enabled: bool | None = None
