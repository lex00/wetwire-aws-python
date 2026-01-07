"""PropertyTypes for AWS::EKS::Cluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AccessConfig(PropertyType):
    authentication_mode: DslValue[str] | None = None
    bootstrap_cluster_creator_admin_permissions: DslValue[bool] | None = None


@dataclass
class BlockStorage(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class ClusterLogging(PropertyType):
    enabled_types: list[DslValue[LoggingTypeConfig]] = field(default_factory=list)


@dataclass
class ComputeConfig(PropertyType):
    enabled: DslValue[bool] | None = None
    node_pools: list[DslValue[str]] = field(default_factory=list)
    node_role_arn: DslValue[str] | None = None


@dataclass
class ControlPlanePlacement(PropertyType):
    group_name: DslValue[str] | None = None


@dataclass
class ControlPlaneScalingConfig(PropertyType):
    tier: DslValue[str] | None = None


@dataclass
class ElasticLoadBalancing(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class EncryptionConfig(PropertyType):
    provider: DslValue[Provider] | None = None
    resources: list[DslValue[str]] = field(default_factory=list)


@dataclass
class KubernetesNetworkConfig(PropertyType):
    elastic_load_balancing: DslValue[ElasticLoadBalancing] | None = None
    ip_family: DslValue[str] | None = None
    service_ipv4_cidr: DslValue[str] | None = None
    service_ipv6_cidr: DslValue[str] | None = None


@dataclass
class Logging(PropertyType):
    cluster_logging: DslValue[ClusterLogging] | None = None


@dataclass
class LoggingTypeConfig(PropertyType):
    type_: DslValue[str] | None = None


@dataclass
class OutpostConfig(PropertyType):
    control_plane_instance_type: DslValue[str] | None = None
    outpost_arns: list[DslValue[str]] = field(default_factory=list)
    control_plane_placement: DslValue[ControlPlanePlacement] | None = None


@dataclass
class Provider(PropertyType):
    key_arn: DslValue[str] | None = None


@dataclass
class RemoteNetworkConfig(PropertyType):
    remote_node_networks: list[DslValue[RemoteNodeNetwork]] = field(
        default_factory=list
    )
    remote_pod_networks: list[DslValue[RemotePodNetwork]] = field(default_factory=list)


@dataclass
class RemoteNodeNetwork(PropertyType):
    cidrs: list[DslValue[str]] = field(default_factory=list)


@dataclass
class RemotePodNetwork(PropertyType):
    cidrs: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ResourcesVpcConfig(PropertyType):
    subnet_ids: list[DslValue[str]] = field(default_factory=list)
    endpoint_private_access: DslValue[bool] | None = None
    endpoint_public_access: DslValue[bool] | None = None
    public_access_cidrs: list[DslValue[str]] = field(default_factory=list)
    security_group_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class StorageConfig(PropertyType):
    block_storage: DslValue[BlockStorage] | None = None


@dataclass
class UpgradePolicy(PropertyType):
    support_type: DslValue[str] | None = None


@dataclass
class ZonalShiftConfig(PropertyType):
    enabled: DslValue[bool] | None = None
