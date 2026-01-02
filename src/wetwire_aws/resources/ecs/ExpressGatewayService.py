"""PropertyTypes for AWS::ECS::ExpressGatewayService."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AutoScalingArns(PropertyType):
    application_auto_scaling_policies: list[String] = field(default_factory=list)
    scalable_target: str | None = None


@dataclass
class ECSManagedResourceArns(PropertyType):
    auto_scaling: AutoScalingArns | None = None
    ingress_path: IngressPathArns | None = None
    log_groups: list[String] = field(default_factory=list)
    metric_alarms: list[String] = field(default_factory=list)
    service_security_groups: list[String] = field(default_factory=list)


@dataclass
class ExpressGatewayContainer(PropertyType):
    image: str | None = None
    aws_logs_configuration: ExpressGatewayServiceAwsLogsConfiguration | None = None
    command: list[String] = field(default_factory=list)
    container_port: int | None = None
    environment: list[KeyValuePair] = field(default_factory=list)
    repository_credentials: ExpressGatewayRepositoryCredentials | None = None
    secrets: list[Secret] = field(default_factory=list)


@dataclass
class ExpressGatewayRepositoryCredentials(PropertyType):
    credentials_parameter: str | None = None


@dataclass
class ExpressGatewayScalingTarget(PropertyType):
    auto_scaling_metric: str | None = None
    auto_scaling_target_value: int | None = None
    max_task_count: int | None = None
    min_task_count: int | None = None


@dataclass
class ExpressGatewayServiceAwsLogsConfiguration(PropertyType):
    log_group: str | None = None
    log_stream_prefix: str | None = None


@dataclass
class ExpressGatewayServiceConfiguration(PropertyType):
    cpu: str | None = None
    created_at: str | None = None
    execution_role_arn: str | None = None
    health_check_path: str | None = None
    ingress_paths: list[IngressPathSummary] = field(default_factory=list)
    memory: str | None = None
    network_configuration: ExpressGatewayServiceNetworkConfiguration | None = None
    primary_container: ExpressGatewayContainer | None = None
    scaling_target: ExpressGatewayScalingTarget | None = None
    service_revision_arn: str | None = None
    task_role_arn: str | None = None


@dataclass
class ExpressGatewayServiceNetworkConfiguration(PropertyType):
    security_groups: list[String] = field(default_factory=list)
    subnets: list[String] = field(default_factory=list)


@dataclass
class ExpressGatewayServiceStatus(PropertyType):
    status_code: str | None = None


@dataclass
class IngressPathArns(PropertyType):
    certificate_arn: str | None = None
    listener_arn: str | None = None
    listener_rule_arn: str | None = None
    load_balancer_arn: str | None = None
    load_balancer_security_groups: list[String] = field(default_factory=list)
    target_group_arns: list[String] = field(default_factory=list)


@dataclass
class IngressPathSummary(PropertyType):
    access_type: str | None = None
    endpoint: str | None = None


@dataclass
class KeyValuePair(PropertyType):
    name: str | None = None
    value: str | None = None


@dataclass
class Secret(PropertyType):
    name: str | None = None
    value_from: str | None = None
