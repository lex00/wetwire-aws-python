"""PropertyTypes for AWS::EntityResolution::MatchingWorkflow."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CustomerProfilesIntegrationConfig(PropertyType):
    domain_arn: DslValue[str] | None = None
    object_type_arn: DslValue[str] | None = None


@dataclass
class IncrementalRunConfig(PropertyType):
    incremental_run_type: DslValue[str] | None = None


@dataclass
class InputSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "input_source_arn": "InputSourceARN",
    }

    input_source_arn: DslValue[str] | None = None
    schema_arn: DslValue[str] | None = None
    apply_normalization: DslValue[bool] | None = None


@dataclass
class IntermediateSourceConfiguration(PropertyType):
    intermediate_s3_path: DslValue[str] | None = None


@dataclass
class OutputAttribute(PropertyType):
    name: DslValue[str] | None = None
    hashed: DslValue[bool] | None = None


@dataclass
class OutputSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_arn": "KMSArn",
    }

    output: list[DslValue[OutputAttribute]] = field(default_factory=list)
    apply_normalization: DslValue[bool] | None = None
    customer_profiles_integration_config: (
        DslValue[CustomerProfilesIntegrationConfig] | None
    ) = None
    kms_arn: DslValue[str] | None = None
    output_s3_path: DslValue[str] | None = None


@dataclass
class ProviderProperties(PropertyType):
    provider_service_arn: DslValue[str] | None = None
    intermediate_source_configuration: (
        DslValue[IntermediateSourceConfiguration] | None
    ) = None
    provider_configuration: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class ResolutionTechniques(PropertyType):
    provider_properties: DslValue[ProviderProperties] | None = None
    resolution_type: DslValue[str] | None = None
    rule_based_properties: DslValue[RuleBasedProperties] | None = None
    rule_condition_properties: DslValue[RuleConditionProperties] | None = None


@dataclass
class Rule(PropertyType):
    matching_keys: list[DslValue[str]] = field(default_factory=list)
    rule_name: DslValue[str] | None = None


@dataclass
class RuleBasedProperties(PropertyType):
    attribute_matching_model: DslValue[str] | None = None
    rules: list[DslValue[Rule]] = field(default_factory=list)
    match_purpose: DslValue[str] | None = None


@dataclass
class RuleCondition(PropertyType):
    condition: DslValue[str] | None = None
    rule_name: DslValue[str] | None = None


@dataclass
class RuleConditionProperties(PropertyType):
    rules: list[DslValue[RuleCondition]] = field(default_factory=list)
