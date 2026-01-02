"""PropertyTypes for AWS::NetworkFirewall::FirewallPolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ActionDefinition(PropertyType):
    publish_metric_action: PublishMetricAction | None = None


@dataclass
class CustomAction(PropertyType):
    action_definition: ActionDefinition | None = None
    action_name: str | None = None


@dataclass
class Dimension(PropertyType):
    value: str | None = None


@dataclass
class FirewallPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_tls_session_holding": "EnableTLSSessionHolding",
        "tls_inspection_configuration_arn": "TLSInspectionConfigurationArn",
    }

    stateless_default_actions: list[String] = field(default_factory=list)
    stateless_fragment_default_actions: list[String] = field(default_factory=list)
    enable_tls_session_holding: bool | None = None
    policy_variables: PolicyVariables | None = None
    stateful_default_actions: list[String] = field(default_factory=list)
    stateful_engine_options: StatefulEngineOptions | None = None
    stateful_rule_group_references: list[StatefulRuleGroupReference] = field(
        default_factory=list
    )
    stateless_custom_actions: list[CustomAction] = field(default_factory=list)
    stateless_rule_group_references: list[StatelessRuleGroupReference] = field(
        default_factory=list
    )
    tls_inspection_configuration_arn: str | None = None


@dataclass
class FlowTimeouts(PropertyType):
    tcp_idle_timeout_seconds: int | None = None


@dataclass
class IPSet(PropertyType):
    definition: list[String] = field(default_factory=list)


@dataclass
class PolicyVariables(PropertyType):
    rule_variables: dict[str, IPSet] = field(default_factory=dict)


@dataclass
class PublishMetricAction(PropertyType):
    dimensions: list[Dimension] = field(default_factory=list)


@dataclass
class StatefulEngineOptions(PropertyType):
    flow_timeouts: FlowTimeouts | None = None
    rule_order: str | None = None
    stream_exception_policy: str | None = None


@dataclass
class StatefulRuleGroupOverride(PropertyType):
    action: str | None = None


@dataclass
class StatefulRuleGroupReference(PropertyType):
    resource_arn: str | None = None
    deep_threat_inspection: bool | None = None
    override: StatefulRuleGroupOverride | None = None
    priority: int | None = None


@dataclass
class StatelessRuleGroupReference(PropertyType):
    priority: int | None = None
    resource_arn: str | None = None
