"""PropertyTypes for AWS::EntityResolution::IdNamespace."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class IdNamespaceIdMappingWorkflowProperties(PropertyType):
    id_mapping_type: DslValue[str] | None = None
    provider_properties: DslValue[NamespaceProviderProperties] | None = None
    rule_based_properties: DslValue[NamespaceRuleBasedProperties] | None = None


@dataclass
class IdNamespaceInputSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "input_source_arn": "InputSourceARN",
    }

    input_source_arn: DslValue[str] | None = None
    schema_name: DslValue[str] | None = None


@dataclass
class NamespaceProviderProperties(PropertyType):
    provider_service_arn: DslValue[str] | None = None
    provider_configuration: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class NamespaceRuleBasedProperties(PropertyType):
    attribute_matching_model: DslValue[str] | None = None
    record_matching_models: list[DslValue[str]] = field(default_factory=list)
    rule_definition_types: list[DslValue[str]] = field(default_factory=list)
    rules: list[DslValue[Rule]] = field(default_factory=list)


@dataclass
class Rule(PropertyType):
    matching_keys: list[DslValue[str]] = field(default_factory=list)
    rule_name: DslValue[str] | None = None
