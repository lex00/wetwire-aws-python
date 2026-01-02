"""PropertyTypes for AWS::NetworkFirewall::RuleGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ActionDefinition(PropertyType):
    publish_metric_action: PublishMetricAction | None = None


@dataclass
class Address(PropertyType):
    address_definition: str | None = None


@dataclass
class CustomAction(PropertyType):
    action_definition: ActionDefinition | None = None
    action_name: str | None = None


@dataclass
class Dimension(PropertyType):
    value: str | None = None


@dataclass
class Header(PropertyType):
    destination: str | None = None
    destination_port: str | None = None
    direction: str | None = None
    protocol: str | None = None
    source: str | None = None
    source_port: str | None = None


@dataclass
class IPSet(PropertyType):
    definition: list[String] = field(default_factory=list)


@dataclass
class IPSetReference(PropertyType):
    reference_arn: str | None = None


@dataclass
class MatchAttributes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "tcp_flags": "TCPFlags",
    }

    destination_ports: list[PortRange] = field(default_factory=list)
    destinations: list[Address] = field(default_factory=list)
    protocols: list[Integer] = field(default_factory=list)
    source_ports: list[PortRange] = field(default_factory=list)
    sources: list[Address] = field(default_factory=list)
    tcp_flags: list[TCPFlagField] = field(default_factory=list)


@dataclass
class PortRange(PropertyType):
    from_port: int | None = None
    to_port: int | None = None


@dataclass
class PortSet(PropertyType):
    definition: list[String] = field(default_factory=list)


@dataclass
class PublishMetricAction(PropertyType):
    dimensions: list[Dimension] = field(default_factory=list)


@dataclass
class ReferenceSets(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_set_references": "IPSetReferences",
    }

    ip_set_references: dict[str, IPSetReference] = field(default_factory=dict)


@dataclass
class RuleDefinition(PropertyType):
    actions: list[String] = field(default_factory=list)
    match_attributes: MatchAttributes | None = None


@dataclass
class RuleGroup(PropertyType):
    rules_source: RulesSource | None = None
    reference_sets: ReferenceSets | None = None
    rule_variables: RuleVariables | None = None
    stateful_rule_options: StatefulRuleOptions | None = None


@dataclass
class RuleOption(PropertyType):
    keyword: str | None = None
    settings: list[String] = field(default_factory=list)


@dataclass
class RuleVariables(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_sets": "IPSets",
    }

    ip_sets: dict[str, IPSet] = field(default_factory=dict)
    port_sets: dict[str, PortSet] = field(default_factory=dict)


@dataclass
class RulesSource(PropertyType):
    rules_source_list: RulesSourceList | None = None
    rules_string: str | None = None
    stateful_rules: list[StatefulRule] = field(default_factory=list)
    stateless_rules_and_custom_actions: StatelessRulesAndCustomActions | None = None


@dataclass
class RulesSourceList(PropertyType):
    generated_rules_type: str | None = None
    target_types: list[String] = field(default_factory=list)
    targets: list[String] = field(default_factory=list)


@dataclass
class StatefulRule(PropertyType):
    action: str | None = None
    header: Header | None = None
    rule_options: list[RuleOption] = field(default_factory=list)


@dataclass
class StatefulRuleOptions(PropertyType):
    rule_order: str | None = None


@dataclass
class StatelessRule(PropertyType):
    priority: int | None = None
    rule_definition: RuleDefinition | None = None


@dataclass
class StatelessRulesAndCustomActions(PropertyType):
    stateless_rules: list[StatelessRule] = field(default_factory=list)
    custom_actions: list[CustomAction] = field(default_factory=list)


@dataclass
class SummaryConfiguration(PropertyType):
    rule_options: list[String] = field(default_factory=list)


@dataclass
class TCPFlagField(PropertyType):
    flags: list[String] = field(default_factory=list)
    masks: list[String] = field(default_factory=list)
