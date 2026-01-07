"""PropertyTypes for AWS::ECS::ExpressGatewayService."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AutoScalingArns(PropertyType):
    application_auto_scaling_policies: list[DslValue[str]] = field(default_factory=list)
    scalable_target: DslValue[str] | None = None


@dataclass
class ECSManagedResourceArns(PropertyType):
    auto_scaling: DslValue[AutoScalingArns] | None = None
    ingress_path: DslValue[IngressPathArns] | None = None
    log_groups: list[DslValue[str]] = field(default_factory=list)
    metric_alarms: list[DslValue[str]] = field(default_factory=list)
    service_security_groups: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ExpressGatewayContainer(PropertyType):
    image: DslValue[str] | None = None
    aws_logs_configuration: (
        DslValue[ExpressGatewayServiceAwsLogsConfiguration] | None
    ) = None
    command: list[DslValue[str]] = field(default_factory=list)
    container_port: DslValue[int] | None = None
    environment: list[DslValue[KeyValuePair]] = field(default_factory=list)
    repository_credentials: DslValue[ExpressGatewayRepositoryCredentials] | None = None
    secrets: list[DslValue[Secret]] = field(default_factory=list)


@dataclass
class ExpressGatewayRepositoryCredentials(PropertyType):
    credentials_parameter: DslValue[str] | None = None


@dataclass
class ExpressGatewayScalingTarget(PropertyType):
    auto_scaling_metric: DslValue[str] | None = None
    auto_scaling_target_value: DslValue[int] | None = None
    max_task_count: DslValue[int] | None = None
    min_task_count: DslValue[int] | None = None


@dataclass
class ExpressGatewayServiceAwsLogsConfiguration(PropertyType):
    log_group: DslValue[str] | None = None
    log_stream_prefix: DslValue[str] | None = None


@dataclass
class ExpressGatewayServiceConfiguration(PropertyType):
    cpu: DslValue[str] | None = None
    created_at: DslValue[str] | None = None
    execution_role_arn: DslValue[str] | None = None
    health_check_path: DslValue[str] | None = None
    ingress_paths: list[DslValue[IngressPathSummary]] = field(default_factory=list)
    memory: DslValue[str] | None = None
    network_configuration: (
        DslValue[ExpressGatewayServiceNetworkConfiguration] | None
    ) = None
    primary_container: DslValue[ExpressGatewayContainer] | None = None
    scaling_target: DslValue[ExpressGatewayScalingTarget] | None = None
    service_revision_arn: DslValue[str] | None = None
    task_role_arn: DslValue[str] | None = None


@dataclass
class ExpressGatewayServiceNetworkConfiguration(PropertyType):
    security_groups: list[DslValue[str]] = field(default_factory=list)
    subnets: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ExpressGatewayServiceStatus(PropertyType):
    status_code: DslValue[str] | None = None


@dataclass
class IngressPathArns(PropertyType):
    certificate_arn: DslValue[str] | None = None
    listener_arn: DslValue[str] | None = None
    listener_rule_arn: DslValue[str] | None = None
    load_balancer_arn: DslValue[str] | None = None
    load_balancer_security_groups: list[DslValue[str]] = field(default_factory=list)
    target_group_arns: list[DslValue[str]] = field(default_factory=list)


@dataclass
class IngressPathSummary(PropertyType):
    access_type: DslValue[str] | None = None
    endpoint: DslValue[str] | None = None


@dataclass
class KeyValuePair(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class Secret(PropertyType):
    name: DslValue[str] | None = None
    value_from: DslValue[str] | None = None
