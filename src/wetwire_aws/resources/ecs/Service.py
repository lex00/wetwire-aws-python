"""PropertyTypes for AWS::ECS::Service."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AdvancedConfiguration(PropertyType):
    alternate_target_group_arn: str | None = None
    production_listener_rule: str | None = None
    role_arn: str | None = None
    test_listener_rule: str | None = None


@dataclass
class AwsVpcConfiguration(PropertyType):
    assign_public_ip: str | None = None
    security_groups: list[String] = field(default_factory=list)
    subnets: list[String] = field(default_factory=list)


@dataclass
class CanaryConfiguration(PropertyType):
    canary_bake_time_in_minutes: int | None = None
    canary_percent: float | None = None


@dataclass
class CapacityProviderStrategyItem(PropertyType):
    base: int | None = None
    capacity_provider: str | None = None
    weight: int | None = None


@dataclass
class DeploymentAlarms(PropertyType):
    alarm_names: list[String] = field(default_factory=list)
    enable: bool | None = None
    rollback: bool | None = None


@dataclass
class DeploymentCircuitBreaker(PropertyType):
    enable: bool | None = None
    rollback: bool | None = None


@dataclass
class DeploymentConfiguration(PropertyType):
    alarms: DeploymentAlarms | None = None
    bake_time_in_minutes: int | None = None
    canary_configuration: CanaryConfiguration | None = None
    deployment_circuit_breaker: DeploymentCircuitBreaker | None = None
    lifecycle_hooks: list[DeploymentLifecycleHook] = field(default_factory=list)
    linear_configuration: LinearConfiguration | None = None
    maximum_percent: int | None = None
    minimum_healthy_percent: int | None = None
    strategy: str | None = None


@dataclass
class DeploymentController(PropertyType):
    type_: str | None = None


@dataclass
class DeploymentLifecycleHook(PropertyType):
    hook_target_arn: str | None = None
    lifecycle_stages: list[String] = field(default_factory=list)
    role_arn: str | None = None
    hook_details: dict[str, Any] | None = None


@dataclass
class EBSTagSpecification(PropertyType):
    resource_type: str | None = None
    propagate_tags: str | None = None
    tags: list[Tag] = field(default_factory=list)


@dataclass
class ForceNewDeployment(PropertyType):
    enable_force_new_deployment: bool | None = None
    force_new_deployment_nonce: str | None = None


@dataclass
class LinearConfiguration(PropertyType):
    step_bake_time_in_minutes: int | None = None
    step_percent: float | None = None


@dataclass
class LoadBalancer(PropertyType):
    advanced_configuration: AdvancedConfiguration | None = None
    container_name: str | None = None
    container_port: int | None = None
    load_balancer_name: str | None = None
    target_group_arn: str | None = None


@dataclass
class LogConfiguration(PropertyType):
    log_driver: str | None = None
    options: dict[str, String] = field(default_factory=dict)
    secret_options: list[Secret] = field(default_factory=list)


@dataclass
class NetworkConfiguration(PropertyType):
    awsvpc_configuration: AwsVpcConfiguration | None = None


@dataclass
class PlacementConstraint(PropertyType):
    type_: str | None = None
    expression: str | None = None


@dataclass
class PlacementStrategy(PropertyType):
    type_: str | None = None
    field_: str | None = None


@dataclass
class Secret(PropertyType):
    name: str | None = None
    value_from: str | None = None


@dataclass
class ServiceConnectAccessLogConfiguration(PropertyType):
    format: str | None = None
    include_query_parameters: str | None = None


@dataclass
class ServiceConnectClientAlias(PropertyType):
    port: int | None = None
    dns_name: str | None = None
    test_traffic_rules: ServiceConnectTestTrafficRules | None = None


@dataclass
class ServiceConnectConfiguration(PropertyType):
    enabled: bool | None = None
    access_log_configuration: ServiceConnectAccessLogConfiguration | None = None
    log_configuration: LogConfiguration | None = None
    namespace: str | None = None
    services: list[ServiceConnectService] = field(default_factory=list)


@dataclass
class ServiceConnectService(PropertyType):
    port_name: str | None = None
    client_aliases: list[ServiceConnectClientAlias] = field(default_factory=list)
    discovery_name: str | None = None
    ingress_port_override: int | None = None
    timeout: TimeoutConfiguration | None = None
    tls: ServiceConnectTlsConfiguration | None = None


@dataclass
class ServiceConnectTestTrafficRules(PropertyType):
    header: ServiceConnectTestTrafficRulesHeader | None = None


@dataclass
class ServiceConnectTestTrafficRulesHeader(PropertyType):
    name: str | None = None
    value: ServiceConnectTestTrafficRulesHeaderValue | None = None


@dataclass
class ServiceConnectTestTrafficRulesHeaderValue(PropertyType):
    exact: str | None = None


@dataclass
class ServiceConnectTlsCertificateAuthority(PropertyType):
    aws_pca_authority_arn: str | None = None


@dataclass
class ServiceConnectTlsConfiguration(PropertyType):
    issuer_certificate_authority: ServiceConnectTlsCertificateAuthority | None = None
    kms_key: str | None = None
    role_arn: str | None = None


@dataclass
class ServiceManagedEBSVolumeConfiguration(PropertyType):
    role_arn: str | None = None
    encrypted: bool | None = None
    filesystem_type: str | None = None
    iops: int | None = None
    kms_key_id: str | None = None
    size_in_gi_b: int | None = None
    snapshot_id: str | None = None
    tag_specifications: list[EBSTagSpecification] = field(default_factory=list)
    throughput: int | None = None
    volume_initialization_rate: int | None = None
    volume_type: str | None = None


@dataclass
class ServiceRegistry(PropertyType):
    container_name: str | None = None
    container_port: int | None = None
    port: int | None = None
    registry_arn: str | None = None


@dataclass
class ServiceVolumeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "managed_ebs_volume": "ManagedEBSVolume",
    }

    name: str | None = None
    managed_ebs_volume: ServiceManagedEBSVolumeConfiguration | None = None


@dataclass
class TimeoutConfiguration(PropertyType):
    idle_timeout_seconds: int | None = None
    per_request_timeout_seconds: int | None = None


@dataclass
class VpcLatticeConfiguration(PropertyType):
    port_name: str | None = None
    role_arn: str | None = None
    target_group_arn: str | None = None
