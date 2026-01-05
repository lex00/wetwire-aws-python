"""PropertyTypes for AWS::ARCRegionSwitch::Plan."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ArcRoutingControlConfiguration(PropertyType):
    region_and_routing_controls: dict[str, Any] | None = None
    cross_account_role: str | None = None
    external_id: str | None = None
    timeout_minutes: float | None = None


@dataclass
class Asg(PropertyType):
    arn: str | None = None
    cross_account_role: str | None = None
    external_id: str | None = None


@dataclass
class AssociatedAlarm(PropertyType):
    alarm_type: str | None = None
    resource_identifier: str | None = None
    cross_account_role: str | None = None
    external_id: str | None = None


@dataclass
class CustomActionLambdaConfiguration(PropertyType):
    lambdas: list[Lambdas] = field(default_factory=list)
    region_to_run: str | None = None
    retry_interval_minutes: float | None = None
    timeout_minutes: float | None = None
    ungraceful: LambdaUngraceful | None = None


@dataclass
class DocumentDbConfiguration(PropertyType):
    behavior: dict[str, Any] | None = None
    database_cluster_arns: list[String] = field(default_factory=list)
    global_cluster_identifier: str | None = None
    cross_account_role: str | None = None
    external_id: str | None = None
    timeout_minutes: float | None = None
    ungraceful: DocumentDbUngraceful | None = None


@dataclass
class DocumentDbUngraceful(PropertyType):
    ungraceful: str | None = None


@dataclass
class Ec2AsgCapacityIncreaseConfiguration(PropertyType):
    asgs: list[Asg] = field(default_factory=list)
    capacity_monitoring_approach: dict[str, Any] | None = None
    target_percent: float | None = None
    timeout_minutes: float | None = None
    ungraceful: Ec2Ungraceful | None = None


@dataclass
class Ec2Ungraceful(PropertyType):
    minimum_success_percentage: float | None = None


@dataclass
class EcsCapacityIncreaseConfiguration(PropertyType):
    services: list[Service] = field(default_factory=list)
    capacity_monitoring_approach: dict[str, Any] | None = None
    target_percent: float | None = None
    timeout_minutes: float | None = None
    ungraceful: EcsUngraceful | None = None


@dataclass
class EcsUngraceful(PropertyType):
    minimum_success_percentage: float | None = None


@dataclass
class EksCluster(PropertyType):
    cluster_arn: str | None = None
    cross_account_role: str | None = None
    external_id: str | None = None


@dataclass
class EksResourceScalingConfiguration(PropertyType):
    kubernetes_resource_type: KubernetesResourceType | None = None
    capacity_monitoring_approach: dict[str, Any] | None = None
    eks_clusters: list[EksCluster] = field(default_factory=list)
    scaling_resources: dict[str, Any] | None = None
    target_percent: float | None = None
    timeout_minutes: float | None = None
    ungraceful: EksResourceScalingUngraceful | None = None


@dataclass
class EksResourceScalingUngraceful(PropertyType):
    minimum_success_percentage: float | None = None


@dataclass
class ExecutionApprovalConfiguration(PropertyType):
    approval_role: str | None = None
    timeout_minutes: float | None = None


@dataclass
class ExecutionBlockConfiguration(PropertyType):
    arc_routing_control_config: ArcRoutingControlConfiguration | None = None
    custom_action_lambda_config: CustomActionLambdaConfiguration | None = None
    document_db_config: DocumentDbConfiguration | None = None
    ec2_asg_capacity_increase_config: Ec2AsgCapacityIncreaseConfiguration | None = None
    ecs_capacity_increase_config: EcsCapacityIncreaseConfiguration | None = None
    eks_resource_scaling_config: EksResourceScalingConfiguration | None = None
    execution_approval_config: ExecutionApprovalConfiguration | None = None
    global_aurora_config: GlobalAuroraConfiguration | None = None
    parallel_config: ParallelExecutionBlockConfiguration | None = None
    region_switch_plan_config: RegionSwitchPlanConfiguration | None = None
    route53_health_check_config: Route53HealthCheckConfiguration | None = None


@dataclass
class GlobalAuroraConfiguration(PropertyType):
    behavior: dict[str, Any] | None = None
    database_cluster_arns: list[String] = field(default_factory=list)
    global_cluster_identifier: str | None = None
    cross_account_role: str | None = None
    external_id: str | None = None
    timeout_minutes: float | None = None
    ungraceful: GlobalAuroraUngraceful | None = None


@dataclass
class GlobalAuroraUngraceful(PropertyType):
    ungraceful: str | None = None


@dataclass
class KubernetesResourceType(PropertyType):
    api_version: str | None = None
    kind: str | None = None


@dataclass
class LambdaUngraceful(PropertyType):
    behavior: dict[str, Any] | None = None


@dataclass
class Lambdas(PropertyType):
    arn: str | None = None
    cross_account_role: str | None = None
    external_id: str | None = None


@dataclass
class ParallelExecutionBlockConfiguration(PropertyType):
    steps: list[Step] = field(default_factory=list)


@dataclass
class RegionSwitchPlanConfiguration(PropertyType):
    arn: str | None = None
    cross_account_role: str | None = None
    external_id: str | None = None


@dataclass
class ReportConfiguration(PropertyType):
    report_output: list[ReportOutputConfiguration] = field(default_factory=list)


@dataclass
class ReportOutputConfiguration(PropertyType):
    s3_configuration: S3ReportOutputConfiguration | None = None


@dataclass
class Route53HealthCheckConfiguration(PropertyType):
    hosted_zone_id: str | None = None
    record_name: str | None = None
    cross_account_role: str | None = None
    external_id: str | None = None
    record_sets: list[Route53ResourceRecordSet] = field(default_factory=list)
    timeout_minutes: float | None = None


@dataclass
class Route53ResourceRecordSet(PropertyType):
    record_set_identifier: str | None = None
    region: str | None = None


@dataclass
class S3ReportOutputConfiguration(PropertyType):
    bucket_owner: str | None = None
    bucket_path: str | None = None


@dataclass
class Service(PropertyType):
    cluster_arn: str | None = None
    cross_account_role: str | None = None
    external_id: str | None = None
    service_arn: str | None = None


@dataclass
class Step(PropertyType):
    execution_block_configuration: ExecutionBlockConfiguration | None = None
    execution_block_type: str | None = None
    name: str | None = None
    description: str | None = None


@dataclass
class Trigger(PropertyType):
    action: str | None = None
    conditions: list[TriggerCondition] = field(default_factory=list)
    min_delay_minutes_between_executions: float | None = None
    target_region: str | None = None
    description: str | None = None


@dataclass
class TriggerCondition(PropertyType):
    associated_alarm_name: str | None = None
    condition: str | None = None


@dataclass
class Workflow(PropertyType):
    workflow_target_action: str | None = None
    steps: list[Step] = field(default_factory=list)
    workflow_description: str | None = None
    workflow_target_region: str | None = None
