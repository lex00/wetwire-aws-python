"""PropertyTypes for AWS::CodeDeploy::DeploymentGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Alarm(PropertyType):
    name: str | None = None


@dataclass
class AlarmConfiguration(PropertyType):
    alarms: list[Alarm] = field(default_factory=list)
    enabled: bool | None = None
    ignore_poll_alarm_failure: bool | None = None


@dataclass
class AutoRollbackConfiguration(PropertyType):
    enabled: bool | None = None
    events: list[String] = field(default_factory=list)


@dataclass
class BlueGreenDeploymentConfiguration(PropertyType):
    deployment_ready_option: DeploymentReadyOption | None = None
    green_fleet_provisioning_option: GreenFleetProvisioningOption | None = None
    terminate_blue_instances_on_deployment_success: (
        BlueInstanceTerminationOption | None
    ) = None


@dataclass
class BlueInstanceTerminationOption(PropertyType):
    action: str | None = None
    termination_wait_time_in_minutes: int | None = None


@dataclass
class Deployment(PropertyType):
    revision: RevisionLocation | None = None
    description: str | None = None
    ignore_application_stop_failures: bool | None = None


@dataclass
class DeploymentReadyOption(PropertyType):
    action_on_timeout: str | None = None
    wait_time_in_minutes: int | None = None


@dataclass
class DeploymentStyle(PropertyType):
    deployment_option: str | None = None
    deployment_type: str | None = None


@dataclass
class EC2TagFilter(PropertyType):
    key: str | None = None
    type_: str | None = None
    value: str | None = None


@dataclass
class EC2TagSet(PropertyType):
    ec2_tag_set_list: list[EC2TagSetListObject] = field(default_factory=list)


@dataclass
class EC2TagSetListObject(PropertyType):
    ec2_tag_group: list[EC2TagFilter] = field(default_factory=list)


@dataclass
class ECSService(PropertyType):
    cluster_name: str | None = None
    service_name: str | None = None


@dataclass
class ELBInfo(PropertyType):
    name: str | None = None


@dataclass
class GitHubLocation(PropertyType):
    commit_id: str | None = None
    repository: str | None = None


@dataclass
class GreenFleetProvisioningOption(PropertyType):
    action: str | None = None


@dataclass
class LoadBalancerInfo(PropertyType):
    elb_info_list: list[ELBInfo] = field(default_factory=list)
    target_group_info_list: list[TargetGroupInfo] = field(default_factory=list)
    target_group_pair_info_list: list[TargetGroupPairInfo] = field(default_factory=list)


@dataclass
class OnPremisesTagSet(PropertyType):
    on_premises_tag_set_list: list[OnPremisesTagSetListObject] = field(
        default_factory=list
    )


@dataclass
class OnPremisesTagSetListObject(PropertyType):
    on_premises_tag_group: list[TagFilter] = field(default_factory=list)


@dataclass
class RevisionLocation(PropertyType):
    git_hub_location: GitHubLocation | None = None
    revision_type: str | None = None
    s3_location: S3Location | None = None


@dataclass
class S3Location(PropertyType):
    bucket: str | None = None
    key: str | None = None
    bundle_type: str | None = None
    e_tag: str | None = None
    version: str | None = None


@dataclass
class TagFilter(PropertyType):
    key: str | None = None
    type_: str | None = None
    value: str | None = None


@dataclass
class TargetGroupInfo(PropertyType):
    name: str | None = None


@dataclass
class TargetGroupPairInfo(PropertyType):
    prod_traffic_route: TrafficRoute | None = None
    target_groups: list[TargetGroupInfo] = field(default_factory=list)
    test_traffic_route: TrafficRoute | None = None


@dataclass
class TrafficRoute(PropertyType):
    listener_arns: list[String] = field(default_factory=list)


@dataclass
class TriggerConfig(PropertyType):
    trigger_events: list[String] = field(default_factory=list)
    trigger_name: str | None = None
    trigger_target_arn: str | None = None
