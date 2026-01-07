"""PropertyTypes for AWS::CodeDeploy::DeploymentGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Alarm(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class AlarmConfiguration(PropertyType):
    alarms: list[DslValue[Alarm]] = field(default_factory=list)
    enabled: DslValue[bool] | None = None
    ignore_poll_alarm_failure: DslValue[bool] | None = None


@dataclass
class AutoRollbackConfiguration(PropertyType):
    enabled: DslValue[bool] | None = None
    events: list[DslValue[str]] = field(default_factory=list)


@dataclass
class BlueGreenDeploymentConfiguration(PropertyType):
    deployment_ready_option: DslValue[DeploymentReadyOption] | None = None
    green_fleet_provisioning_option: DslValue[GreenFleetProvisioningOption] | None = (
        None
    )
    terminate_blue_instances_on_deployment_success: (
        DslValue[BlueInstanceTerminationOption] | None
    ) = None


@dataclass
class BlueInstanceTerminationOption(PropertyType):
    action: DslValue[str] | None = None
    termination_wait_time_in_minutes: DslValue[int] | None = None


@dataclass
class Deployment(PropertyType):
    revision: DslValue[RevisionLocation] | None = None
    description: DslValue[str] | None = None
    ignore_application_stop_failures: DslValue[bool] | None = None


@dataclass
class DeploymentReadyOption(PropertyType):
    action_on_timeout: DslValue[str] | None = None
    wait_time_in_minutes: DslValue[int] | None = None


@dataclass
class DeploymentStyle(PropertyType):
    deployment_option: DslValue[str] | None = None
    deployment_type: DslValue[str] | None = None


@dataclass
class EC2TagFilter(PropertyType):
    key: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class EC2TagSet(PropertyType):
    ec2_tag_set_list: list[DslValue[EC2TagSetListObject]] = field(default_factory=list)


@dataclass
class EC2TagSetListObject(PropertyType):
    ec2_tag_group: list[DslValue[EC2TagFilter]] = field(default_factory=list)


@dataclass
class ECSService(PropertyType):
    cluster_name: DslValue[str] | None = None
    service_name: DslValue[str] | None = None


@dataclass
class ELBInfo(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class GitHubLocation(PropertyType):
    commit_id: DslValue[str] | None = None
    repository: DslValue[str] | None = None


@dataclass
class GreenFleetProvisioningOption(PropertyType):
    action: DslValue[str] | None = None


@dataclass
class LoadBalancerInfo(PropertyType):
    elb_info_list: list[DslValue[ELBInfo]] = field(default_factory=list)
    target_group_info_list: list[DslValue[TargetGroupInfo]] = field(
        default_factory=list
    )
    target_group_pair_info_list: list[DslValue[TargetGroupPairInfo]] = field(
        default_factory=list
    )


@dataclass
class OnPremisesTagSet(PropertyType):
    on_premises_tag_set_list: list[DslValue[OnPremisesTagSetListObject]] = field(
        default_factory=list
    )


@dataclass
class OnPremisesTagSetListObject(PropertyType):
    on_premises_tag_group: list[DslValue[TagFilter]] = field(default_factory=list)


@dataclass
class RevisionLocation(PropertyType):
    git_hub_location: DslValue[GitHubLocation] | None = None
    revision_type: DslValue[str] | None = None
    s3_location: DslValue[S3Location] | None = None


@dataclass
class S3Location(PropertyType):
    bucket: DslValue[str] | None = None
    key: DslValue[str] | None = None
    bundle_type: DslValue[str] | None = None
    e_tag: DslValue[str] | None = None
    version: DslValue[str] | None = None


@dataclass
class TagFilter(PropertyType):
    key: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class TargetGroupInfo(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class TargetGroupPairInfo(PropertyType):
    prod_traffic_route: DslValue[TrafficRoute] | None = None
    target_groups: list[DslValue[TargetGroupInfo]] = field(default_factory=list)
    test_traffic_route: DslValue[TrafficRoute] | None = None


@dataclass
class TrafficRoute(PropertyType):
    listener_arns: list[DslValue[str]] = field(default_factory=list)


@dataclass
class TriggerConfig(PropertyType):
    trigger_events: list[DslValue[str]] = field(default_factory=list)
    trigger_name: DslValue[str] | None = None
    trigger_target_arn: DslValue[str] | None = None
