"""PropertyTypes for AWS::EntityResolution::IdMappingWorkflow."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class IdMappingIncrementalRunConfig(PropertyType):
    incremental_run_type: DslValue[str] | None = None


@dataclass
class IdMappingRuleBasedProperties(PropertyType):
    attribute_matching_model: DslValue[str] | None = None
    record_matching_model: DslValue[str] | None = None
    rule_definition_type: DslValue[str] | None = None
    rules: list[DslValue[Rule]] = field(default_factory=list)


@dataclass
class IdMappingTechniques(PropertyType):
    id_mapping_type: DslValue[str] | None = None
    normalization_version: DslValue[str] | None = None
    provider_properties: DslValue[ProviderProperties] | None = None
    rule_based_properties: DslValue[IdMappingRuleBasedProperties] | None = None


@dataclass
class IdMappingWorkflowInputSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "input_source_arn": "InputSourceARN",
    }

    input_source_arn: DslValue[str] | None = None
    schema_arn: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class IdMappingWorkflowOutputSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_arn": "KMSArn",
    }

    output_s3_path: DslValue[str] | None = None
    kms_arn: DslValue[str] | None = None


@dataclass
class IntermediateSourceConfiguration(PropertyType):
    intermediate_s3_path: DslValue[str] | None = None


@dataclass
class ProviderProperties(PropertyType):
    provider_service_arn: DslValue[str] | None = None
    intermediate_source_configuration: (
        DslValue[IntermediateSourceConfiguration] | None
    ) = None
    provider_configuration: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class Rule(PropertyType):
    matching_keys: list[DslValue[str]] = field(default_factory=list)
    rule_name: DslValue[str] | None = None
