"""PropertyTypes for AWS::B2BI::Transformer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AdvancedOptions(PropertyType):
    x12: DslValue[X12AdvancedOptions] | None = None


@dataclass
class FormatOptions(PropertyType):
    x12: DslValue[X12Details] | None = None


@dataclass
class InputConversion(PropertyType):
    from_format: DslValue[str] | None = None
    advanced_options: DslValue[AdvancedOptions] | None = None
    format_options: DslValue[FormatOptions] | None = None


@dataclass
class Mapping(PropertyType):
    template_language: DslValue[str] | None = None
    template: DslValue[str] | None = None


@dataclass
class OutputConversion(PropertyType):
    to_format: DslValue[str] | None = None
    advanced_options: DslValue[AdvancedOptions] | None = None
    format_options: DslValue[FormatOptions] | None = None


@dataclass
class SampleDocumentKeys(PropertyType):
    input: DslValue[str] | None = None
    output: DslValue[str] | None = None


@dataclass
class SampleDocuments(PropertyType):
    bucket_name: DslValue[str] | None = None
    keys: list[DslValue[SampleDocumentKeys]] = field(default_factory=list)


@dataclass
class X12AdvancedOptions(PropertyType):
    split_options: DslValue[X12SplitOptions] | None = None
    validation_options: DslValue[X12ValidationOptions] | None = None


@dataclass
class X12CodeListValidationRule(PropertyType):
    element_id: DslValue[str] | None = None
    codes_to_add: list[DslValue[str]] = field(default_factory=list)
    codes_to_remove: list[DslValue[str]] = field(default_factory=list)


@dataclass
class X12Details(PropertyType):
    transaction_set: DslValue[str] | None = None
    version: DslValue[str] | None = None


@dataclass
class X12ElementLengthValidationRule(PropertyType):
    element_id: DslValue[str] | None = None
    max_length: DslValue[float] | None = None
    min_length: DslValue[float] | None = None


@dataclass
class X12ElementRequirementValidationRule(PropertyType):
    element_position: DslValue[str] | None = None
    requirement: DslValue[str] | None = None


@dataclass
class X12SplitOptions(PropertyType):
    split_by: DslValue[str] | None = None


@dataclass
class X12ValidationOptions(PropertyType):
    validation_rules: list[DslValue[X12ValidationRule]] = field(default_factory=list)


@dataclass
class X12ValidationRule(PropertyType):
    code_list_validation_rule: DslValue[X12CodeListValidationRule] | None = None
    element_length_validation_rule: DslValue[X12ElementLengthValidationRule] | None = (
        None
    )
    element_requirement_validation_rule: (
        DslValue[X12ElementRequirementValidationRule] | None
    ) = None
