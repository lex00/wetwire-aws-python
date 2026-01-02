"""PropertyTypes for AWS::B2BI::Transformer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AdvancedOptions(PropertyType):
    x12: X12AdvancedOptions | None = None


@dataclass
class FormatOptions(PropertyType):
    x12: X12Details | None = None


@dataclass
class InputConversion(PropertyType):
    from_format: str | None = None
    advanced_options: AdvancedOptions | None = None
    format_options: FormatOptions | None = None


@dataclass
class Mapping(PropertyType):
    template_language: str | None = None
    template: str | None = None


@dataclass
class OutputConversion(PropertyType):
    to_format: str | None = None
    advanced_options: AdvancedOptions | None = None
    format_options: FormatOptions | None = None


@dataclass
class SampleDocumentKeys(PropertyType):
    input: str | None = None
    output: str | None = None


@dataclass
class SampleDocuments(PropertyType):
    bucket_name: str | None = None
    keys: list[SampleDocumentKeys] = field(default_factory=list)


@dataclass
class X12AdvancedOptions(PropertyType):
    split_options: X12SplitOptions | None = None
    validation_options: X12ValidationOptions | None = None


@dataclass
class X12CodeListValidationRule(PropertyType):
    element_id: str | None = None
    codes_to_add: list[String] = field(default_factory=list)
    codes_to_remove: list[String] = field(default_factory=list)


@dataclass
class X12Details(PropertyType):
    transaction_set: str | None = None
    version: str | None = None


@dataclass
class X12ElementLengthValidationRule(PropertyType):
    element_id: str | None = None
    max_length: float | None = None
    min_length: float | None = None


@dataclass
class X12ElementRequirementValidationRule(PropertyType):
    element_position: str | None = None
    requirement: str | None = None


@dataclass
class X12SplitOptions(PropertyType):
    split_by: str | None = None


@dataclass
class X12ValidationOptions(PropertyType):
    validation_rules: list[X12ValidationRule] = field(default_factory=list)


@dataclass
class X12ValidationRule(PropertyType):
    code_list_validation_rule: X12CodeListValidationRule | None = None
    element_length_validation_rule: X12ElementLengthValidationRule | None = None
    element_requirement_validation_rule: X12ElementRequirementValidationRule | None = (
        None
    )
