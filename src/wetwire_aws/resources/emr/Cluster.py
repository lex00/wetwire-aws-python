"""PropertyTypes for AWS::EMR::Cluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Application(PropertyType):
    additional_info: dict[str, DslValue[str]] = field(default_factory=dict)
    args: list[DslValue[str]] = field(default_factory=list)
    name: DslValue[str] | None = None
    version: DslValue[str] | None = None


@dataclass
class AutoScalingPolicy(PropertyType):
    constraints: DslValue[ScalingConstraints] | None = None
    rules: list[DslValue[ScalingRule]] = field(default_factory=list)


@dataclass
class AutoTerminationPolicy(PropertyType):
    idle_timeout: DslValue[int] | None = None


@dataclass
class BootstrapActionConfig(PropertyType):
    name: DslValue[str] | None = None
    script_bootstrap_action: DslValue[ScriptBootstrapActionConfig] | None = None


@dataclass
class CloudWatchAlarmDefinition(PropertyType):
    comparison_operator: DslValue[str] | None = None
    metric_name: DslValue[str] | None = None
    period: DslValue[int] | None = None
    threshold: DslValue[float] | None = None
    dimensions: list[DslValue[MetricDimension]] = field(default_factory=list)
    evaluation_periods: DslValue[int] | None = None
    namespace: DslValue[str] | None = None
    statistic: DslValue[str] | None = None
    unit: DslValue[str] | None = None


@dataclass
class ComputeLimits(PropertyType):
    maximum_capacity_units: DslValue[int] | None = None
    minimum_capacity_units: DslValue[int] | None = None
    unit_type: DslValue[str] | None = None
    maximum_core_capacity_units: DslValue[int] | None = None
    maximum_on_demand_capacity_units: DslValue[int] | None = None


@dataclass
class Configuration(PropertyType):
    classification: DslValue[str] | None = None
    configuration_properties: dict[str, DslValue[str]] = field(default_factory=dict)
    configurations: list[DslValue[Configuration]] = field(default_factory=list)


@dataclass
class EbsBlockDeviceConfig(PropertyType):
    volume_specification: DslValue[VolumeSpecification] | None = None
    volumes_per_instance: DslValue[int] | None = None


@dataclass
class EbsConfiguration(PropertyType):
    ebs_block_device_configs: list[DslValue[EbsBlockDeviceConfig]] = field(
        default_factory=list
    )
    ebs_optimized: DslValue[bool] | None = None


@dataclass
class HadoopJarStepConfig(PropertyType):
    jar: DslValue[str] | None = None
    args: list[DslValue[str]] = field(default_factory=list)
    main_class: DslValue[str] | None = None
    step_properties: list[DslValue[KeyValue]] = field(default_factory=list)


@dataclass
class InstanceFleetConfig(PropertyType):
    instance_type_configs: list[DslValue[InstanceTypeConfig]] = field(
        default_factory=list
    )
    launch_specifications: DslValue[InstanceFleetProvisioningSpecifications] | None = (
        None
    )
    name: DslValue[str] | None = None
    resize_specifications: DslValue[InstanceFleetResizingSpecifications] | None = None
    target_on_demand_capacity: DslValue[int] | None = None
    target_spot_capacity: DslValue[int] | None = None


@dataclass
class InstanceFleetProvisioningSpecifications(PropertyType):
    on_demand_specification: DslValue[OnDemandProvisioningSpecification] | None = None
    spot_specification: DslValue[SpotProvisioningSpecification] | None = None


@dataclass
class InstanceFleetResizingSpecifications(PropertyType):
    on_demand_resize_specification: DslValue[OnDemandResizingSpecification] | None = (
        None
    )
    spot_resize_specification: DslValue[SpotResizingSpecification] | None = None


@dataclass
class InstanceGroupConfig(PropertyType):
    instance_count: DslValue[int] | None = None
    instance_type: DslValue[str] | None = None
    auto_scaling_policy: DslValue[AutoScalingPolicy] | None = None
    bid_price: DslValue[str] | None = None
    configurations: list[DslValue[Configuration]] = field(default_factory=list)
    custom_ami_id: DslValue[str] | None = None
    ebs_configuration: DslValue[EbsConfiguration] | None = None
    market: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class InstanceTypeConfig(PropertyType):
    instance_type: DslValue[str] | None = None
    bid_price: DslValue[str] | None = None
    bid_price_as_percentage_of_on_demand_price: DslValue[float] | None = None
    configurations: list[DslValue[Configuration]] = field(default_factory=list)
    custom_ami_id: DslValue[str] | None = None
    ebs_configuration: DslValue[EbsConfiguration] | None = None
    priority: DslValue[float] | None = None
    weighted_capacity: DslValue[int] | None = None


@dataclass
class JobFlowInstancesConfig(PropertyType):
    additional_master_security_groups: list[DslValue[str]] = field(default_factory=list)
    additional_slave_security_groups: list[DslValue[str]] = field(default_factory=list)
    core_instance_fleet: DslValue[InstanceFleetConfig] | None = None
    core_instance_group: DslValue[InstanceGroupConfig] | None = None
    ec2_key_name: DslValue[str] | None = None
    ec2_subnet_id: DslValue[str] | None = None
    ec2_subnet_ids: list[DslValue[str]] = field(default_factory=list)
    emr_managed_master_security_group: DslValue[str] | None = None
    emr_managed_slave_security_group: DslValue[str] | None = None
    hadoop_version: DslValue[str] | None = None
    keep_job_flow_alive_when_no_steps: DslValue[bool] | None = None
    master_instance_fleet: DslValue[InstanceFleetConfig] | None = None
    master_instance_group: DslValue[InstanceGroupConfig] | None = None
    placement: DslValue[PlacementType] | None = None
    service_access_security_group: DslValue[str] | None = None
    task_instance_fleets: list[DslValue[InstanceFleetConfig]] = field(
        default_factory=list
    )
    task_instance_groups: list[DslValue[InstanceGroupConfig]] = field(
        default_factory=list
    )
    termination_protected: DslValue[bool] | None = None
    unhealthy_node_replacement: DslValue[bool] | None = None


@dataclass
class KerberosAttributes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ad_domain_join_password": "ADDomainJoinPassword",
        "ad_domain_join_user": "ADDomainJoinUser",
    }

    kdc_admin_password: DslValue[str] | None = None
    realm: DslValue[str] | None = None
    ad_domain_join_password: DslValue[str] | None = None
    ad_domain_join_user: DslValue[str] | None = None
    cross_realm_trust_principal_password: DslValue[str] | None = None


@dataclass
class KeyValue(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class ManagedScalingPolicy(PropertyType):
    compute_limits: DslValue[ComputeLimits] | None = None
    scaling_strategy: DslValue[str] | None = None
    utilization_performance_index: DslValue[int] | None = None


@dataclass
class MetricDimension(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class OnDemandCapacityReservationOptions(PropertyType):
    capacity_reservation_preference: DslValue[str] | None = None
    capacity_reservation_resource_group_arn: DslValue[str] | None = None
    usage_strategy: DslValue[str] | None = None


@dataclass
class OnDemandProvisioningSpecification(PropertyType):
    allocation_strategy: DslValue[str] | None = None
    capacity_reservation_options: (
        DslValue[OnDemandCapacityReservationOptions] | None
    ) = None


@dataclass
class OnDemandResizingSpecification(PropertyType):
    allocation_strategy: DslValue[str] | None = None
    capacity_reservation_options: (
        DslValue[OnDemandCapacityReservationOptions] | None
    ) = None
    timeout_duration_minutes: DslValue[int] | None = None


@dataclass
class PlacementGroupConfig(PropertyType):
    instance_role: DslValue[str] | None = None
    placement_strategy: DslValue[str] | None = None


@dataclass
class PlacementType(PropertyType):
    availability_zone: DslValue[str] | None = None


@dataclass
class ScalingAction(PropertyType):
    simple_scaling_policy_configuration: (
        DslValue[SimpleScalingPolicyConfiguration] | None
    ) = None
    market: DslValue[str] | None = None


@dataclass
class ScalingConstraints(PropertyType):
    max_capacity: DslValue[int] | None = None
    min_capacity: DslValue[int] | None = None


@dataclass
class ScalingRule(PropertyType):
    action: DslValue[ScalingAction] | None = None
    name: DslValue[str] | None = None
    trigger: DslValue[ScalingTrigger] | None = None
    description: DslValue[str] | None = None


@dataclass
class ScalingTrigger(PropertyType):
    cloud_watch_alarm_definition: DslValue[CloudWatchAlarmDefinition] | None = None


@dataclass
class ScriptBootstrapActionConfig(PropertyType):
    path: DslValue[str] | None = None
    args: list[DslValue[str]] = field(default_factory=list)


@dataclass
class SimpleScalingPolicyConfiguration(PropertyType):
    scaling_adjustment: DslValue[int] | None = None
    adjustment_type: DslValue[str] | None = None
    cool_down: DslValue[int] | None = None


@dataclass
class SpotProvisioningSpecification(PropertyType):
    timeout_action: DslValue[str] | None = None
    timeout_duration_minutes: DslValue[int] | None = None
    allocation_strategy: DslValue[str] | None = None
    block_duration_minutes: DslValue[int] | None = None


@dataclass
class SpotResizingSpecification(PropertyType):
    allocation_strategy: DslValue[str] | None = None
    timeout_duration_minutes: DslValue[int] | None = None


@dataclass
class StepConfig(PropertyType):
    hadoop_jar_step: DslValue[HadoopJarStepConfig] | None = None
    name: DslValue[str] | None = None
    action_on_failure: DslValue[str] | None = None


@dataclass
class VolumeSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "size_in_gb": "SizeInGB",
    }

    size_in_gb: DslValue[int] | None = None
    volume_type: DslValue[str] | None = None
    iops: DslValue[int] | None = None
    throughput: DslValue[int] | None = None
