"""PropertyTypes for AWS::AmplifyUIBuilder::Form."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class FieldConfig(PropertyType):
    excluded: DslValue[bool] | None = None
    input_type: DslValue[FieldInputConfig] | None = None
    label: DslValue[str] | None = None
    position: DslValue[FieldPosition] | None = None
    validations: list[DslValue[FieldValidationConfiguration]] = field(
        default_factory=list
    )


@dataclass
class FieldInputConfig(PropertyType):
    type_: DslValue[str] | None = None
    default_checked: DslValue[bool] | None = None
    default_country_code: DslValue[str] | None = None
    default_value: DslValue[str] | None = None
    descriptive_text: DslValue[str] | None = None
    file_uploader_config: DslValue[FileUploaderFieldConfig] | None = None
    is_array: DslValue[bool] | None = None
    max_value: DslValue[float] | None = None
    min_value: DslValue[float] | None = None
    name: DslValue[str] | None = None
    placeholder: DslValue[str] | None = None
    read_only: DslValue[bool] | None = None
    required: DslValue[bool] | None = None
    step: DslValue[float] | None = None
    value: DslValue[str] | None = None
    value_mappings: DslValue[ValueMappings] | None = None


@dataclass
class FieldPosition(PropertyType):
    below: DslValue[str] | None = None
    fixed: DslValue[str] | None = None
    right_of: DslValue[str] | None = None


@dataclass
class FieldValidationConfiguration(PropertyType):
    type_: DslValue[str] | None = None
    num_values: list[DslValue[float]] = field(default_factory=list)
    str_values: list[DslValue[str]] = field(default_factory=list)
    validation_message: DslValue[str] | None = None


@dataclass
class FileUploaderFieldConfig(PropertyType):
    accepted_file_types: list[DslValue[str]] = field(default_factory=list)
    access_level: DslValue[str] | None = None
    is_resumable: DslValue[bool] | None = None
    max_file_count: DslValue[float] | None = None
    max_size: DslValue[float] | None = None
    show_thumbnails: DslValue[bool] | None = None


@dataclass
class FormButton(PropertyType):
    children: DslValue[str] | None = None
    excluded: DslValue[bool] | None = None
    position: DslValue[FieldPosition] | None = None


@dataclass
class FormCTA(PropertyType):
    cancel: DslValue[FormButton] | None = None
    clear: DslValue[FormButton] | None = None
    position: DslValue[str] | None = None
    submit: DslValue[FormButton] | None = None


@dataclass
class FormDataTypeConfig(PropertyType):
    data_source_type: DslValue[str] | None = None
    data_type_name: DslValue[str] | None = None


@dataclass
class FormInputBindingPropertiesValue(PropertyType):
    binding_properties: DslValue[FormInputBindingPropertiesValueProperties] | None = (
        None
    )
    type_: DslValue[str] | None = None


@dataclass
class FormInputBindingPropertiesValueProperties(PropertyType):
    model: DslValue[str] | None = None


@dataclass
class FormInputValueProperty(PropertyType):
    binding_properties: DslValue[FormInputValuePropertyBindingProperties] | None = None
    concat: list[DslValue[FormInputValueProperty]] = field(default_factory=list)
    value: DslValue[str] | None = None


@dataclass
class FormInputValuePropertyBindingProperties(PropertyType):
    property: DslValue[str] | None = None
    field_: DslValue[str] | None = None


@dataclass
class FormStyle(PropertyType):
    horizontal_gap: DslValue[FormStyleConfig] | None = None
    outer_padding: DslValue[FormStyleConfig] | None = None
    vertical_gap: DslValue[FormStyleConfig] | None = None


@dataclass
class FormStyleConfig(PropertyType):
    token_reference: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class SectionalElement(PropertyType):
    type_: DslValue[str] | None = None
    excluded: DslValue[bool] | None = None
    level: DslValue[float] | None = None
    orientation: DslValue[str] | None = None
    position: DslValue[FieldPosition] | None = None
    text: DslValue[str] | None = None


@dataclass
class ValueMapping(PropertyType):
    value: DslValue[FormInputValueProperty] | None = None
    display_value: DslValue[FormInputValueProperty] | None = None


@dataclass
class ValueMappings(PropertyType):
    values: list[DslValue[ValueMapping]] = field(default_factory=list)
    binding_properties: dict[str, DslValue[FormInputBindingPropertiesValue]] = field(
        default_factory=dict
    )
