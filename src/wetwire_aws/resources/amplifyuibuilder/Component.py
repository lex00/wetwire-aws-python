"""PropertyTypes for AWS::AmplifyUIBuilder::Component."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ActionParameters(PropertyType):
    anchor: ComponentProperty | None = None
    fields: dict[str, ComponentProperty] = field(default_factory=dict)
    global_: ComponentProperty | None = None
    id: ComponentProperty | None = None
    model: str | None = None
    state: MutationActionSetStateParameter | None = None
    target: ComponentProperty | None = None
    type_: ComponentProperty | None = None
    url: ComponentProperty | None = None


@dataclass
class ComponentBindingPropertiesValue(PropertyType):
    binding_properties: ComponentBindingPropertiesValueProperties | None = None
    default_value: str | None = None
    type_: str | None = None


@dataclass
class ComponentBindingPropertiesValueProperties(PropertyType):
    bucket: str | None = None
    default_value: str | None = None
    field_: str | None = None
    key: str | None = None
    model: str | None = None
    predicates: list[Predicate] = field(default_factory=list)
    slot_name: str | None = None
    user_attribute: str | None = None


@dataclass
class ComponentChild(PropertyType):
    component_type: str | None = None
    name: str | None = None
    properties: dict[str, ComponentProperty] = field(default_factory=dict)
    children: list[ComponentChild] = field(default_factory=list)
    events: dict[str, ComponentEvent] = field(default_factory=dict)
    source_id: str | None = None


@dataclass
class ComponentConditionProperty(PropertyType):
    else_: ComponentProperty | None = None
    field_: str | None = None
    operand: str | None = None
    operand_type: str | None = None
    operator: str | None = None
    property: str | None = None
    then: ComponentProperty | None = None


@dataclass
class ComponentDataConfiguration(PropertyType):
    model: str | None = None
    identifiers: list[String] = field(default_factory=list)
    predicate: Predicate | None = None
    sort: list[SortProperty] = field(default_factory=list)


@dataclass
class ComponentEvent(PropertyType):
    action: str | None = None
    binding_event: str | None = None
    parameters: ActionParameters | None = None


@dataclass
class ComponentProperty(PropertyType):
    binding_properties: ComponentPropertyBindingProperties | None = None
    bindings: dict[str, FormBindingElement] = field(default_factory=dict)
    collection_binding_properties: ComponentPropertyBindingProperties | None = None
    component_name: str | None = None
    concat: list[ComponentProperty] = field(default_factory=list)
    condition: ComponentConditionProperty | None = None
    configured: bool | None = None
    default_value: str | None = None
    event: str | None = None
    imported_value: str | None = None
    model: str | None = None
    property: str | None = None
    type_: str | None = None
    user_attribute: str | None = None
    value: str | None = None


@dataclass
class ComponentPropertyBindingProperties(PropertyType):
    property: str | None = None
    field_: str | None = None


@dataclass
class ComponentVariant(PropertyType):
    overrides: dict[str, Any] | None = None
    variant_values: dict[str, String] = field(default_factory=dict)


@dataclass
class FormBindingElement(PropertyType):
    element: str | None = None
    property: str | None = None


@dataclass
class MutationActionSetStateParameter(PropertyType):
    component_name: str | None = None
    property: str | None = None
    set: ComponentProperty | None = None


@dataclass
class Predicate(PropertyType):
    and_: list[Predicate] = field(default_factory=list)
    field_: str | None = None
    operand: str | None = None
    operand_type: str | None = None
    operator: str | None = None
    or_: list[Predicate] = field(default_factory=list)


@dataclass
class SortProperty(PropertyType):
    direction: str | None = None
    field_: str | None = None
