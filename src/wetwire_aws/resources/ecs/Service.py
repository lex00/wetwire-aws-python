"""PropertyTypes for AWS::ECS::Service."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AdvancedConfiguration(PropertyType):
    alternate_target_group_arn: DslValue[str] | None = None
    production_listener_rule: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    test_listener_rule: DslValue[str] | None = None


@dataclass
class AwsVpcConfiguration(PropertyType):
    assign_public_ip: DslValue[str] | None = None
    security_groups: list[DslValue[str]] = field(default_factory=list)
    subnets: list[DslValue[str]] = field(default_factory=list)


@dataclass
class CanaryConfiguration(PropertyType):
    canary_bake_time_in_minutes: DslValue[int] | None = None
    canary_percent: DslValue[float] | None = None


@dataclass
class CapacityProviderStrategyItem(PropertyType):
    base: DslValue[int] | None = None
    capacity_provider: DslValue[str] | None = None
    weight: DslValue[int] | None = None


@dataclass
class DeploymentAlarms(PropertyType):
    alarm_names: list[DslValue[str]] = field(default_factory=list)
    enable: DslValue[bool] | None = None
    rollback: DslValue[bool] | None = None


@dataclass
class DeploymentCircuitBreaker(PropertyType):
    enable: DslValue[bool] | None = None
    rollback: DslValue[bool] | None = None


@dataclass
class DeploymentConfiguration(PropertyType):
    alarms: DslValue[DeploymentAlarms] | None = None
    bake_time_in_minutes: DslValue[int] | None = None
    canary_configuration: DslValue[CanaryConfiguration] | None = None
    deployment_circuit_breaker: DslValue[DeploymentCircuitBreaker] | None = None
    lifecycle_hooks: list[DslValue[DeploymentLifecycleHook]] = field(
        default_factory=list
    )
    linear_configuration: DslValue[LinearConfiguration] | None = None
    maximum_percent: DslValue[int] | None = None
    minimum_healthy_percent: DslValue[int] | None = None
    strategy: DslValue[str] | None = None


@dataclass
class DeploymentController(PropertyType):
    type_: DslValue[str] | None = None


@dataclass
class DeploymentLifecycleHook(PropertyType):
    hook_target_arn: DslValue[str] | None = None
    lifecycle_stages: list[DslValue[str]] = field(default_factory=list)
    role_arn: DslValue[str] | None = None
    hook_details: DslValue[dict[str, Any]] | None = None


@dataclass
class EBSTagSpecification(PropertyType):
    resource_type: DslValue[str] | None = None
    propagate_tags: DslValue[str] | None = None
    tags: list[DslValue[Tag]] = field(default_factory=list)


@dataclass
class ForceNewDeployment(PropertyType):
    enable_force_new_deployment: DslValue[bool] | None = None
    force_new_deployment_nonce: DslValue[str] | None = None


@dataclass
class LinearConfiguration(PropertyType):
    step_bake_time_in_minutes: DslValue[int] | None = None
    step_percent: DslValue[float] | None = None


@dataclass
class LoadBalancer(PropertyType):
    advanced_configuration: DslValue[AdvancedConfiguration] | None = None
    container_name: DslValue[str] | None = None
    container_port: DslValue[int] | None = None
    load_balancer_name: DslValue[str] | None = None
    target_group_arn: DslValue[str] | None = None


@dataclass
class LogConfiguration(PropertyType):
    log_driver: DslValue[str] | None = None
    options: dict[str, DslValue[str]] = field(default_factory=dict)
    secret_options: list[DslValue[Secret]] = field(default_factory=list)


@dataclass
class NetworkConfiguration(PropertyType):
    awsvpc_configuration: DslValue[AwsVpcConfiguration] | None = None


@dataclass
class PlacementConstraint(PropertyType):
    type_: DslValue[str] | None = None
    expression: DslValue[str] | None = None


@dataclass
class PlacementStrategy(PropertyType):
    type_: DslValue[str] | None = None
    field_: DslValue[str] | None = None


@dataclass
class Secret(PropertyType):
    name: DslValue[str] | None = None
    value_from: DslValue[str] | None = None


@dataclass
class ServiceConnectAccessLogConfiguration(PropertyType):
    format: DslValue[str] | None = None
    include_query_parameters: DslValue[str] | None = None


@dataclass
class ServiceConnectClientAlias(PropertyType):
    port: DslValue[int] | None = None
    dns_name: DslValue[str] | None = None
    test_traffic_rules: DslValue[ServiceConnectTestTrafficRules] | None = None


@dataclass
class ServiceConnectConfiguration(PropertyType):
    enabled: DslValue[bool] | None = None
    access_log_configuration: DslValue[ServiceConnectAccessLogConfiguration] | None = (
        None
    )
    log_configuration: DslValue[LogConfiguration] | None = None
    namespace: DslValue[str] | None = None
    services: list[DslValue[ServiceConnectService]] = field(default_factory=list)


@dataclass
class ServiceConnectService(PropertyType):
    port_name: DslValue[str] | None = None
    client_aliases: list[DslValue[ServiceConnectClientAlias]] = field(
        default_factory=list
    )
    discovery_name: DslValue[str] | None = None
    ingress_port_override: DslValue[int] | None = None
    timeout: DslValue[TimeoutConfiguration] | None = None
    tls: DslValue[ServiceConnectTlsConfiguration] | None = None


@dataclass
class ServiceConnectTestTrafficRules(PropertyType):
    header: DslValue[ServiceConnectTestTrafficRulesHeader] | None = None


@dataclass
class ServiceConnectTestTrafficRulesHeader(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[ServiceConnectTestTrafficRulesHeaderValue] | None = None


@dataclass
class ServiceConnectTestTrafficRulesHeaderValue(PropertyType):
    exact: DslValue[str] | None = None


@dataclass
class ServiceConnectTlsCertificateAuthority(PropertyType):
    aws_pca_authority_arn: DslValue[str] | None = None


@dataclass
class ServiceConnectTlsConfiguration(PropertyType):
    issuer_certificate_authority: (
        DslValue[ServiceConnectTlsCertificateAuthority] | None
    ) = None
    kms_key: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None


@dataclass
class ServiceManagedEBSVolumeConfiguration(PropertyType):
    role_arn: DslValue[str] | None = None
    encrypted: DslValue[bool] | None = None
    filesystem_type: DslValue[str] | None = None
    iops: DslValue[int] | None = None
    kms_key_id: DslValue[str] | None = None
    size_in_gi_b: DslValue[int] | None = None
    snapshot_id: DslValue[str] | None = None
    tag_specifications: list[DslValue[EBSTagSpecification]] = field(
        default_factory=list
    )
    throughput: DslValue[int] | None = None
    volume_initialization_rate: DslValue[int] | None = None
    volume_type: DslValue[str] | None = None


@dataclass
class ServiceRegistry(PropertyType):
    container_name: DslValue[str] | None = None
    container_port: DslValue[int] | None = None
    port: DslValue[int] | None = None
    registry_arn: DslValue[str] | None = None


@dataclass
class ServiceVolumeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "managed_ebs_volume": "ManagedEBSVolume",
    }

    name: DslValue[str] | None = None
    managed_ebs_volume: DslValue[ServiceManagedEBSVolumeConfiguration] | None = None


@dataclass
class TimeoutConfiguration(PropertyType):
    idle_timeout_seconds: DslValue[int] | None = None
    per_request_timeout_seconds: DslValue[int] | None = None


@dataclass
class VpcLatticeConfiguration(PropertyType):
    port_name: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    target_group_arn: DslValue[str] | None = None
