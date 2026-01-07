"""PropertyTypes for AWS::AmplifyUIBuilder::Component."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ActionParameters(PropertyType):
    anchor: DslValue[ComponentProperty] | None = None
    fields: dict[str, DslValue[ComponentProperty]] = field(default_factory=dict)
    global_: DslValue[ComponentProperty] | None = None
    id: DslValue[ComponentProperty] | None = None
    model: DslValue[str] | None = None
    state: DslValue[MutationActionSetStateParameter] | None = None
    target: DslValue[ComponentProperty] | None = None
    type_: DslValue[ComponentProperty] | None = None
    url: DslValue[ComponentProperty] | None = None


@dataclass
class ComponentBindingPropertiesValue(PropertyType):
    binding_properties: DslValue[ComponentBindingPropertiesValueProperties] | None = (
        None
    )
    default_value: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class ComponentBindingPropertiesValueProperties(PropertyType):
    bucket: DslValue[str] | None = None
    default_value: DslValue[str] | None = None
    field_: DslValue[str] | None = None
    key: DslValue[str] | None = None
    model: DslValue[str] | None = None
    predicates: list[DslValue[Predicate]] = field(default_factory=list)
    slot_name: DslValue[str] | None = None
    user_attribute: DslValue[str] | None = None


@dataclass
class ComponentChild(PropertyType):
    component_type: DslValue[str] | None = None
    name: DslValue[str] | None = None
    properties: dict[str, DslValue[ComponentProperty]] = field(default_factory=dict)
    children: list[DslValue[ComponentChild]] = field(default_factory=list)
    events: dict[str, DslValue[ComponentEvent]] = field(default_factory=dict)
    source_id: DslValue[str] | None = None


@dataclass
class ComponentConditionProperty(PropertyType):
    else_: DslValue[ComponentProperty] | None = None
    field_: DslValue[str] | None = None
    operand: DslValue[str] | None = None
    operand_type: DslValue[str] | None = None
    operator: DslValue[str] | None = None
    property: DslValue[str] | None = None
    then: DslValue[ComponentProperty] | None = None


@dataclass
class ComponentDataConfiguration(PropertyType):
    model: DslValue[str] | None = None
    identifiers: list[DslValue[str]] = field(default_factory=list)
    predicate: DslValue[Predicate] | None = None
    sort: list[DslValue[SortProperty]] = field(default_factory=list)


@dataclass
class ComponentEvent(PropertyType):
    action: DslValue[str] | None = None
    binding_event: DslValue[str] | None = None
    parameters: DslValue[ActionParameters] | None = None


@dataclass
class ComponentProperty(PropertyType):
    binding_properties: DslValue[ComponentPropertyBindingProperties] | None = None
    bindings: dict[str, DslValue[FormBindingElement]] = field(default_factory=dict)
    collection_binding_properties: (
        DslValue[ComponentPropertyBindingProperties] | None
    ) = None
    component_name: DslValue[str] | None = None
    concat: list[DslValue[ComponentProperty]] = field(default_factory=list)
    condition: DslValue[ComponentConditionProperty] | None = None
    configured: DslValue[bool] | None = None
    default_value: DslValue[str] | None = None
    event: DslValue[str] | None = None
    imported_value: DslValue[str] | None = None
    model: DslValue[str] | None = None
    property: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    user_attribute: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class ComponentPropertyBindingProperties(PropertyType):
    property: DslValue[str] | None = None
    field_: DslValue[str] | None = None


@dataclass
class ComponentVariant(PropertyType):
    overrides: DslValue[dict[str, Any]] | None = None
    variant_values: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class FormBindingElement(PropertyType):
    element: DslValue[str] | None = None
    property: DslValue[str] | None = None


@dataclass
class MutationActionSetStateParameter(PropertyType):
    component_name: DslValue[str] | None = None
    property: DslValue[str] | None = None
    set: DslValue[ComponentProperty] | None = None


@dataclass
class Predicate(PropertyType):
    and_: list[DslValue[Predicate]] = field(default_factory=list)
    field_: DslValue[str] | None = None
    operand: DslValue[str] | None = None
    operand_type: DslValue[str] | None = None
    operator: DslValue[str] | None = None
    or_: list[DslValue[Predicate]] = field(default_factory=list)


@dataclass
class SortProperty(PropertyType):
    direction: DslValue[str] | None = None
    field_: DslValue[str] | None = None
