"""PropertyTypes for AWS::NetworkFirewall::FirewallPolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ActionDefinition(PropertyType):
    publish_metric_action: DslValue[PublishMetricAction] | None = None


@dataclass
class CustomAction(PropertyType):
    action_definition: DslValue[ActionDefinition] | None = None
    action_name: DslValue[str] | None = None


@dataclass
class Dimension(PropertyType):
    value: DslValue[str] | None = None


@dataclass
class FirewallPolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_tls_session_holding": "EnableTLSSessionHolding",
        "tls_inspection_configuration_arn": "TLSInspectionConfigurationArn",
    }

    stateless_default_actions: list[DslValue[str]] = field(default_factory=list)
    stateless_fragment_default_actions: list[DslValue[str]] = field(
        default_factory=list
    )
    enable_tls_session_holding: DslValue[bool] | None = None
    policy_variables: DslValue[PolicyVariables] | None = None
    stateful_default_actions: list[DslValue[str]] = field(default_factory=list)
    stateful_engine_options: DslValue[StatefulEngineOptions] | None = None
    stateful_rule_group_references: list[DslValue[StatefulRuleGroupReference]] = field(
        default_factory=list
    )
    stateless_custom_actions: list[DslValue[CustomAction]] = field(default_factory=list)
    stateless_rule_group_references: list[DslValue[StatelessRuleGroupReference]] = (
        field(default_factory=list)
    )
    tls_inspection_configuration_arn: DslValue[str] | None = None


@dataclass
class FlowTimeouts(PropertyType):
    tcp_idle_timeout_seconds: DslValue[int] | None = None


@dataclass
class IPSet(PropertyType):
    definition: list[DslValue[str]] = field(default_factory=list)


@dataclass
class PolicyVariables(PropertyType):
    rule_variables: dict[str, DslValue[IPSet]] = field(default_factory=dict)


@dataclass
class PublishMetricAction(PropertyType):
    dimensions: list[DslValue[Dimension]] = field(default_factory=list)


@dataclass
class StatefulEngineOptions(PropertyType):
    flow_timeouts: DslValue[FlowTimeouts] | None = None
    rule_order: DslValue[str] | None = None
    stream_exception_policy: DslValue[str] | None = None


@dataclass
class StatefulRuleGroupOverride(PropertyType):
    action: DslValue[str] | None = None


@dataclass
class StatefulRuleGroupReference(PropertyType):
    resource_arn: DslValue[str] | None = None
    deep_threat_inspection: DslValue[bool] | None = None
    override: DslValue[StatefulRuleGroupOverride] | None = None
    priority: DslValue[int] | None = None


@dataclass
class StatelessRuleGroupReference(PropertyType):
    priority: DslValue[int] | None = None
    resource_arn: DslValue[str] | None = None
