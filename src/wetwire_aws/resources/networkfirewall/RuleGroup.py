"""PropertyTypes for AWS::NetworkFirewall::RuleGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ActionDefinition(PropertyType):
    publish_metric_action: DslValue[PublishMetricAction] | None = None


@dataclass
class Address(PropertyType):
    address_definition: DslValue[str] | None = None


@dataclass
class CustomAction(PropertyType):
    action_definition: DslValue[ActionDefinition] | None = None
    action_name: DslValue[str] | None = None


@dataclass
class Dimension(PropertyType):
    value: DslValue[str] | None = None


@dataclass
class Header(PropertyType):
    destination: DslValue[str] | None = None
    destination_port: DslValue[str] | None = None
    direction: DslValue[str] | None = None
    protocol: DslValue[str] | None = None
    source: DslValue[str] | None = None
    source_port: DslValue[str] | None = None


@dataclass
class IPSet(PropertyType):
    definition: list[DslValue[str]] = field(default_factory=list)


@dataclass
class IPSetReference(PropertyType):
    reference_arn: DslValue[str] | None = None


@dataclass
class MatchAttributes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "tcp_flags": "TCPFlags",
    }

    destination_ports: list[DslValue[PortRange]] = field(default_factory=list)
    destinations: list[DslValue[Address]] = field(default_factory=list)
    protocols: list[DslValue[int]] = field(default_factory=list)
    source_ports: list[DslValue[PortRange]] = field(default_factory=list)
    sources: list[DslValue[Address]] = field(default_factory=list)
    tcp_flags: list[DslValue[TCPFlagField]] = field(default_factory=list)


@dataclass
class PortRange(PropertyType):
    from_port: DslValue[int] | None = None
    to_port: DslValue[int] | None = None


@dataclass
class PortSet(PropertyType):
    definition: list[DslValue[str]] = field(default_factory=list)


@dataclass
class PublishMetricAction(PropertyType):
    dimensions: list[DslValue[Dimension]] = field(default_factory=list)


@dataclass
class ReferenceSets(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_set_references": "IPSetReferences",
    }

    ip_set_references: dict[str, DslValue[IPSetReference]] = field(default_factory=dict)


@dataclass
class RuleDefinition(PropertyType):
    actions: list[DslValue[str]] = field(default_factory=list)
    match_attributes: DslValue[MatchAttributes] | None = None


@dataclass
class RuleGroup(PropertyType):
    rules_source: DslValue[RulesSource] | None = None
    reference_sets: DslValue[ReferenceSets] | None = None
    rule_variables: DslValue[RuleVariables] | None = None
    stateful_rule_options: DslValue[StatefulRuleOptions] | None = None


@dataclass
class RuleOption(PropertyType):
    keyword: DslValue[str] | None = None
    settings: list[DslValue[str]] = field(default_factory=list)


@dataclass
class RuleVariables(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_sets": "IPSets",
    }

    ip_sets: dict[str, DslValue[IPSet]] = field(default_factory=dict)
    port_sets: dict[str, DslValue[PortSet]] = field(default_factory=dict)


@dataclass
class RulesSource(PropertyType):
    rules_source_list: DslValue[RulesSourceList] | None = None
    rules_string: DslValue[str] | None = None
    stateful_rules: list[DslValue[StatefulRule]] = field(default_factory=list)
    stateless_rules_and_custom_actions: (
        DslValue[StatelessRulesAndCustomActions] | None
    ) = None


@dataclass
class RulesSourceList(PropertyType):
    generated_rules_type: DslValue[str] | None = None
    target_types: list[DslValue[str]] = field(default_factory=list)
    targets: list[DslValue[str]] = field(default_factory=list)


@dataclass
class StatefulRule(PropertyType):
    action: DslValue[str] | None = None
    header: DslValue[Header] | None = None
    rule_options: list[DslValue[RuleOption]] = field(default_factory=list)


@dataclass
class StatefulRuleOptions(PropertyType):
    rule_order: DslValue[str] | None = None


@dataclass
class StatelessRule(PropertyType):
    priority: DslValue[int] | None = None
    rule_definition: DslValue[RuleDefinition] | None = None


@dataclass
class StatelessRulesAndCustomActions(PropertyType):
    stateless_rules: list[DslValue[StatelessRule]] = field(default_factory=list)
    custom_actions: list[DslValue[CustomAction]] = field(default_factory=list)


@dataclass
class SummaryConfiguration(PropertyType):
    rule_options: list[DslValue[str]] = field(default_factory=list)


@dataclass
class TCPFlagField(PropertyType):
    flags: list[DslValue[str]] = field(default_factory=list)
    masks: list[DslValue[str]] = field(default_factory=list)
