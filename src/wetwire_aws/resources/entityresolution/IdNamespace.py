"""PropertyTypes for AWS::EntityResolution::IdNamespace."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class IdNamespaceIdMappingWorkflowProperties(PropertyType):
    id_mapping_type: str | None = None
    provider_properties: NamespaceProviderProperties | None = None
    rule_based_properties: NamespaceRuleBasedProperties | None = None


@dataclass
class IdNamespaceInputSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "input_source_arn": "InputSourceARN",
    }

    input_source_arn: str | None = None
    schema_name: str | None = None


@dataclass
class NamespaceProviderProperties(PropertyType):
    provider_service_arn: str | None = None
    provider_configuration: dict[str, String] = field(default_factory=dict)


@dataclass
class NamespaceRuleBasedProperties(PropertyType):
    attribute_matching_model: str | None = None
    record_matching_models: list[String] = field(default_factory=list)
    rule_definition_types: list[String] = field(default_factory=list)
    rules: list[Rule] = field(default_factory=list)


@dataclass
class Rule(PropertyType):
    matching_keys: list[String] = field(default_factory=list)
    rule_name: str | None = None
