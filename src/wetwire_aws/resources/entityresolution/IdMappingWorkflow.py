"""PropertyTypes for AWS::EntityResolution::IdMappingWorkflow."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class IdMappingIncrementalRunConfig(PropertyType):
    incremental_run_type: str | None = None


@dataclass
class IdMappingRuleBasedProperties(PropertyType):
    attribute_matching_model: str | None = None
    record_matching_model: str | None = None
    rule_definition_type: str | None = None
    rules: list[Rule] = field(default_factory=list)


@dataclass
class IdMappingTechniques(PropertyType):
    id_mapping_type: str | None = None
    normalization_version: str | None = None
    provider_properties: ProviderProperties | None = None
    rule_based_properties: IdMappingRuleBasedProperties | None = None


@dataclass
class IdMappingWorkflowInputSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "input_source_arn": "InputSourceARN",
    }

    input_source_arn: str | None = None
    schema_arn: str | None = None
    type_: str | None = None


@dataclass
class IdMappingWorkflowOutputSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_arn": "KMSArn",
    }

    output_s3_path: str | None = None
    kms_arn: str | None = None


@dataclass
class IntermediateSourceConfiguration(PropertyType):
    intermediate_s3_path: str | None = None


@dataclass
class ProviderProperties(PropertyType):
    provider_service_arn: str | None = None
    intermediate_source_configuration: IntermediateSourceConfiguration | None = None
    provider_configuration: dict[str, String] = field(default_factory=dict)


@dataclass
class Rule(PropertyType):
    matching_keys: list[String] = field(default_factory=list)
    rule_name: str | None = None
