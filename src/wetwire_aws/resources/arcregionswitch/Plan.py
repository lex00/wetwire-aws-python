"""PropertyTypes for AWS::ARCRegionSwitch::Plan."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ArcRoutingControlConfiguration(PropertyType):
    region_and_routing_controls: DslValue[dict[str, Any]] | None = None
    cross_account_role: DslValue[str] | None = None
    external_id: DslValue[str] | None = None
    timeout_minutes: DslValue[float] | None = None


@dataclass
class Asg(PropertyType):
    arn: DslValue[str] | None = None
    cross_account_role: DslValue[str] | None = None
    external_id: DslValue[str] | None = None


@dataclass
class AssociatedAlarm(PropertyType):
    alarm_type: DslValue[str] | None = None
    resource_identifier: DslValue[str] | None = None
    cross_account_role: DslValue[str] | None = None
    external_id: DslValue[str] | None = None


@dataclass
class CustomActionLambdaConfiguration(PropertyType):
    lambdas: list[DslValue[Lambdas]] = field(default_factory=list)
    region_to_run: DslValue[str] | None = None
    retry_interval_minutes: DslValue[float] | None = None
    timeout_minutes: DslValue[float] | None = None
    ungraceful: DslValue[LambdaUngraceful] | None = None


@dataclass
class DocumentDbConfiguration(PropertyType):
    behavior: DslValue[dict[str, Any]] | None = None
    database_cluster_arns: list[DslValue[str]] = field(default_factory=list)
    global_cluster_identifier: DslValue[str] | None = None
    cross_account_role: DslValue[str] | None = None
    external_id: DslValue[str] | None = None
    timeout_minutes: DslValue[float] | None = None
    ungraceful: DslValue[DocumentDbUngraceful] | None = None


@dataclass
class DocumentDbUngraceful(PropertyType):
    ungraceful: DslValue[str] | None = None


@dataclass
class Ec2AsgCapacityIncreaseConfiguration(PropertyType):
    asgs: list[DslValue[Asg]] = field(default_factory=list)
    capacity_monitoring_approach: DslValue[dict[str, Any]] | None = None
    target_percent: DslValue[float] | None = None
    timeout_minutes: DslValue[float] | None = None
    ungraceful: DslValue[Ec2Ungraceful] | None = None


@dataclass
class Ec2Ungraceful(PropertyType):
    minimum_success_percentage: DslValue[float] | None = None


@dataclass
class EcsCapacityIncreaseConfiguration(PropertyType):
    services: list[DslValue[Service]] = field(default_factory=list)
    capacity_monitoring_approach: DslValue[dict[str, Any]] | None = None
    target_percent: DslValue[float] | None = None
    timeout_minutes: DslValue[float] | None = None
    ungraceful: DslValue[EcsUngraceful] | None = None


@dataclass
class EcsUngraceful(PropertyType):
    minimum_success_percentage: DslValue[float] | None = None


@dataclass
class EksCluster(PropertyType):
    cluster_arn: DslValue[str] | None = None
    cross_account_role: DslValue[str] | None = None
    external_id: DslValue[str] | None = None


@dataclass
class EksResourceScalingConfiguration(PropertyType):
    kubernetes_resource_type: DslValue[KubernetesResourceType] | None = None
    capacity_monitoring_approach: DslValue[dict[str, Any]] | None = None
    eks_clusters: list[DslValue[EksCluster]] = field(default_factory=list)
    scaling_resources: DslValue[dict[str, Any]] | None = None
    target_percent: DslValue[float] | None = None
    timeout_minutes: DslValue[float] | None = None
    ungraceful: DslValue[EksResourceScalingUngraceful] | None = None


@dataclass
class EksResourceScalingUngraceful(PropertyType):
    minimum_success_percentage: DslValue[float] | None = None


@dataclass
class ExecutionApprovalConfiguration(PropertyType):
    approval_role: DslValue[str] | None = None
    timeout_minutes: DslValue[float] | None = None


@dataclass
class ExecutionBlockConfiguration(PropertyType):
    arc_routing_control_config: DslValue[ArcRoutingControlConfiguration] | None = None
    custom_action_lambda_config: DslValue[CustomActionLambdaConfiguration] | None = None
    document_db_config: DslValue[DocumentDbConfiguration] | None = None
    ec2_asg_capacity_increase_config: (
        DslValue[Ec2AsgCapacityIncreaseConfiguration] | None
    ) = None
    ecs_capacity_increase_config: DslValue[EcsCapacityIncreaseConfiguration] | None = (
        None
    )
    eks_resource_scaling_config: DslValue[EksResourceScalingConfiguration] | None = None
    execution_approval_config: DslValue[ExecutionApprovalConfiguration] | None = None
    global_aurora_config: DslValue[GlobalAuroraConfiguration] | None = None
    parallel_config: DslValue[ParallelExecutionBlockConfiguration] | None = None
    region_switch_plan_config: DslValue[RegionSwitchPlanConfiguration] | None = None
    route53_health_check_config: DslValue[Route53HealthCheckConfiguration] | None = None


@dataclass
class GlobalAuroraConfiguration(PropertyType):
    behavior: DslValue[dict[str, Any]] | None = None
    database_cluster_arns: list[DslValue[str]] = field(default_factory=list)
    global_cluster_identifier: DslValue[str] | None = None
    cross_account_role: DslValue[str] | None = None
    external_id: DslValue[str] | None = None
    timeout_minutes: DslValue[float] | None = None
    ungraceful: DslValue[GlobalAuroraUngraceful] | None = None


@dataclass
class GlobalAuroraUngraceful(PropertyType):
    ungraceful: DslValue[str] | None = None


@dataclass
class KubernetesResourceType(PropertyType):
    api_version: DslValue[str] | None = None
    kind: DslValue[str] | None = None


@dataclass
class LambdaUngraceful(PropertyType):
    behavior: DslValue[dict[str, Any]] | None = None


@dataclass
class Lambdas(PropertyType):
    arn: DslValue[str] | None = None
    cross_account_role: DslValue[str] | None = None
    external_id: DslValue[str] | None = None


@dataclass
class ParallelExecutionBlockConfiguration(PropertyType):
    steps: list[DslValue[Step]] = field(default_factory=list)


@dataclass
class RegionSwitchPlanConfiguration(PropertyType):
    arn: DslValue[str] | None = None
    cross_account_role: DslValue[str] | None = None
    external_id: DslValue[str] | None = None


@dataclass
class ReportConfiguration(PropertyType):
    report_output: list[DslValue[ReportOutputConfiguration]] = field(
        default_factory=list
    )


@dataclass
class ReportOutputConfiguration(PropertyType):
    s3_configuration: DslValue[S3ReportOutputConfiguration] | None = None


@dataclass
class Route53HealthCheckConfiguration(PropertyType):
    hosted_zone_id: DslValue[str] | None = None
    record_name: DslValue[str] | None = None
    cross_account_role: DslValue[str] | None = None
    external_id: DslValue[str] | None = None
    record_sets: list[DslValue[Route53ResourceRecordSet]] = field(default_factory=list)
    timeout_minutes: DslValue[float] | None = None


@dataclass
class Route53ResourceRecordSet(PropertyType):
    record_set_identifier: DslValue[str] | None = None
    region: DslValue[str] | None = None


@dataclass
class S3ReportOutputConfiguration(PropertyType):
    bucket_owner: DslValue[str] | None = None
    bucket_path: DslValue[str] | None = None


@dataclass
class Service(PropertyType):
    cluster_arn: DslValue[str] | None = None
    cross_account_role: DslValue[str] | None = None
    external_id: DslValue[str] | None = None
    service_arn: DslValue[str] | None = None


@dataclass
class Step(PropertyType):
    execution_block_configuration: DslValue[ExecutionBlockConfiguration] | None = None
    execution_block_type: DslValue[str] | None = None
    name: DslValue[str] | None = None
    description: DslValue[str] | None = None


@dataclass
class Trigger(PropertyType):
    action: DslValue[str] | None = None
    conditions: list[DslValue[TriggerCondition]] = field(default_factory=list)
    min_delay_minutes_between_executions: DslValue[float] | None = None
    target_region: DslValue[str] | None = None
    description: DslValue[str] | None = None


@dataclass
class TriggerCondition(PropertyType):
    associated_alarm_name: DslValue[str] | None = None
    condition: DslValue[str] | None = None


@dataclass
class Workflow(PropertyType):
    workflow_target_action: DslValue[str] | None = None
    steps: list[DslValue[Step]] = field(default_factory=list)
    workflow_description: DslValue[str] | None = None
    workflow_target_region: DslValue[str] | None = None
