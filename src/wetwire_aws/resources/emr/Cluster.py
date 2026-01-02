"""PropertyTypes for AWS::EMR::Cluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Application(PropertyType):
    additional_info: dict[str, String] = field(default_factory=dict)
    args: list[String] = field(default_factory=list)
    name: str | None = None
    version: str | None = None


@dataclass
class AutoScalingPolicy(PropertyType):
    constraints: ScalingConstraints | None = None
    rules: list[ScalingRule] = field(default_factory=list)


@dataclass
class AutoTerminationPolicy(PropertyType):
    idle_timeout: int | None = None


@dataclass
class BootstrapActionConfig(PropertyType):
    name: str | None = None
    script_bootstrap_action: ScriptBootstrapActionConfig | None = None


@dataclass
class CloudWatchAlarmDefinition(PropertyType):
    comparison_operator: str | None = None
    metric_name: str | None = None
    period: int | None = None
    threshold: float | None = None
    dimensions: list[MetricDimension] = field(default_factory=list)
    evaluation_periods: int | None = None
    namespace: str | None = None
    statistic: str | None = None
    unit: str | None = None


@dataclass
class ComputeLimits(PropertyType):
    maximum_capacity_units: int | None = None
    minimum_capacity_units: int | None = None
    unit_type: str | None = None
    maximum_core_capacity_units: int | None = None
    maximum_on_demand_capacity_units: int | None = None


@dataclass
class Configuration(PropertyType):
    classification: str | None = None
    configuration_properties: dict[str, String] = field(default_factory=dict)
    configurations: list[Configuration] = field(default_factory=list)


@dataclass
class EbsBlockDeviceConfig(PropertyType):
    volume_specification: VolumeSpecification | None = None
    volumes_per_instance: int | None = None


@dataclass
class EbsConfiguration(PropertyType):
    ebs_block_device_configs: list[EbsBlockDeviceConfig] = field(default_factory=list)
    ebs_optimized: bool | None = None


@dataclass
class HadoopJarStepConfig(PropertyType):
    jar: str | None = None
    args: list[String] = field(default_factory=list)
    main_class: str | None = None
    step_properties: list[KeyValue] = field(default_factory=list)


@dataclass
class InstanceFleetConfig(PropertyType):
    instance_type_configs: list[InstanceTypeConfig] = field(default_factory=list)
    launch_specifications: InstanceFleetProvisioningSpecifications | None = None
    name: str | None = None
    resize_specifications: InstanceFleetResizingSpecifications | None = None
    target_on_demand_capacity: int | None = None
    target_spot_capacity: int | None = None


@dataclass
class InstanceFleetProvisioningSpecifications(PropertyType):
    on_demand_specification: OnDemandProvisioningSpecification | None = None
    spot_specification: SpotProvisioningSpecification | None = None


@dataclass
class InstanceFleetResizingSpecifications(PropertyType):
    on_demand_resize_specification: OnDemandResizingSpecification | None = None
    spot_resize_specification: SpotResizingSpecification | None = None


@dataclass
class InstanceGroupConfig(PropertyType):
    instance_count: int | None = None
    instance_type: str | None = None
    auto_scaling_policy: AutoScalingPolicy | None = None
    bid_price: str | None = None
    configurations: list[Configuration] = field(default_factory=list)
    custom_ami_id: str | None = None
    ebs_configuration: EbsConfiguration | None = None
    market: str | None = None
    name: str | None = None


@dataclass
class InstanceTypeConfig(PropertyType):
    instance_type: str | None = None
    bid_price: str | None = None
    bid_price_as_percentage_of_on_demand_price: float | None = None
    configurations: list[Configuration] = field(default_factory=list)
    custom_ami_id: str | None = None
    ebs_configuration: EbsConfiguration | None = None
    priority: float | None = None
    weighted_capacity: int | None = None


@dataclass
class JobFlowInstancesConfig(PropertyType):
    additional_master_security_groups: list[String] = field(default_factory=list)
    additional_slave_security_groups: list[String] = field(default_factory=list)
    core_instance_fleet: InstanceFleetConfig | None = None
    core_instance_group: InstanceGroupConfig | None = None
    ec2_key_name: str | None = None
    ec2_subnet_id: str | None = None
    ec2_subnet_ids: list[String] = field(default_factory=list)
    emr_managed_master_security_group: str | None = None
    emr_managed_slave_security_group: str | None = None
    hadoop_version: str | None = None
    keep_job_flow_alive_when_no_steps: bool | None = None
    master_instance_fleet: InstanceFleetConfig | None = None
    master_instance_group: InstanceGroupConfig | None = None
    placement: PlacementType | None = None
    service_access_security_group: str | None = None
    task_instance_fleets: list[InstanceFleetConfig] = field(default_factory=list)
    task_instance_groups: list[InstanceGroupConfig] = field(default_factory=list)
    termination_protected: bool | None = None
    unhealthy_node_replacement: bool | None = None


@dataclass
class KerberosAttributes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ad_domain_join_password": "ADDomainJoinPassword",
        "ad_domain_join_user": "ADDomainJoinUser",
    }

    kdc_admin_password: str | None = None
    realm: str | None = None
    ad_domain_join_password: str | None = None
    ad_domain_join_user: str | None = None
    cross_realm_trust_principal_password: str | None = None


@dataclass
class KeyValue(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class ManagedScalingPolicy(PropertyType):
    compute_limits: ComputeLimits | None = None
    scaling_strategy: str | None = None
    utilization_performance_index: int | None = None


@dataclass
class MetricDimension(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class OnDemandCapacityReservationOptions(PropertyType):
    capacity_reservation_preference: str | None = None
    capacity_reservation_resource_group_arn: str | None = None
    usage_strategy: str | None = None


@dataclass
class OnDemandProvisioningSpecification(PropertyType):
    allocation_strategy: str | None = None
    capacity_reservation_options: OnDemandCapacityReservationOptions | None = None


@dataclass
class OnDemandResizingSpecification(PropertyType):
    allocation_strategy: str | None = None
    capacity_reservation_options: OnDemandCapacityReservationOptions | None = None
    timeout_duration_minutes: int | None = None


@dataclass
class PlacementGroupConfig(PropertyType):
    instance_role: str | None = None
    placement_strategy: str | None = None


@dataclass
class PlacementType(PropertyType):
    availability_zone: str | None = None


@dataclass
class ScalingAction(PropertyType):
    simple_scaling_policy_configuration: SimpleScalingPolicyConfiguration | None = None
    market: str | None = None


@dataclass
class ScalingConstraints(PropertyType):
    max_capacity: int | None = None
    min_capacity: int | None = None


@dataclass
class ScalingRule(PropertyType):
    action: ScalingAction | None = None
    name: str | None = None
    trigger: ScalingTrigger | None = None
    description: str | None = None


@dataclass
class ScalingTrigger(PropertyType):
    cloud_watch_alarm_definition: CloudWatchAlarmDefinition | None = None


@dataclass
class ScriptBootstrapActionConfig(PropertyType):
    path: str | None = None
    args: list[String] = field(default_factory=list)


@dataclass
class SimpleScalingPolicyConfiguration(PropertyType):
    scaling_adjustment: int | None = None
    adjustment_type: str | None = None
    cool_down: int | None = None


@dataclass
class SpotProvisioningSpecification(PropertyType):
    timeout_action: str | None = None
    timeout_duration_minutes: int | None = None
    allocation_strategy: str | None = None
    block_duration_minutes: int | None = None


@dataclass
class SpotResizingSpecification(PropertyType):
    allocation_strategy: str | None = None
    timeout_duration_minutes: int | None = None


@dataclass
class StepConfig(PropertyType):
    hadoop_jar_step: HadoopJarStepConfig | None = None
    name: str | None = None
    action_on_failure: str | None = None


@dataclass
class VolumeSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "size_in_gb": "SizeInGB",
    }

    size_in_gb: int | None = None
    volume_type: str | None = None
    iops: int | None = None
    throughput: int | None = None
