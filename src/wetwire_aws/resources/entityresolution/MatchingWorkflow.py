"""PropertyTypes for AWS::EntityResolution::MatchingWorkflow."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CustomerProfilesIntegrationConfig(PropertyType):
    domain_arn: str | None = None
    object_type_arn: str | None = None


@dataclass
class IncrementalRunConfig(PropertyType):
    incremental_run_type: str | None = None


@dataclass
class InputSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "input_source_arn": "InputSourceARN",
    }

    input_source_arn: str | None = None
    schema_arn: str | None = None
    apply_normalization: bool | None = None


@dataclass
class IntermediateSourceConfiguration(PropertyType):
    intermediate_s3_path: str | None = None


@dataclass
class OutputAttribute(PropertyType):
    name: str | None = None
    hashed: bool | None = None


@dataclass
class OutputSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_arn": "KMSArn",
    }

    output: list[OutputAttribute] = field(default_factory=list)
    apply_normalization: bool | None = None
    customer_profiles_integration_config: CustomerProfilesIntegrationConfig | None = (
        None
    )
    kms_arn: str | None = None
    output_s3_path: str | None = None


@dataclass
class ProviderProperties(PropertyType):
    provider_service_arn: str | None = None
    intermediate_source_configuration: IntermediateSourceConfiguration | None = None
    provider_configuration: dict[str, String] = field(default_factory=dict)


@dataclass
class ResolutionTechniques(PropertyType):
    provider_properties: ProviderProperties | None = None
    resolution_type: str | None = None
    rule_based_properties: RuleBasedProperties | None = None
    rule_condition_properties: RuleConditionProperties | None = None


@dataclass
class Rule(PropertyType):
    matching_keys: list[String] = field(default_factory=list)
    rule_name: str | None = None


@dataclass
class RuleBasedProperties(PropertyType):
    attribute_matching_model: str | None = None
    rules: list[Rule] = field(default_factory=list)
    match_purpose: str | None = None


@dataclass
class RuleCondition(PropertyType):
    condition: str | None = None
    rule_name: str | None = None


@dataclass
class RuleConditionProperties(PropertyType):
    rules: list[RuleCondition] = field(default_factory=list)
