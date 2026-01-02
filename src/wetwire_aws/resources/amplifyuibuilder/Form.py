"""PropertyTypes for AWS::AmplifyUIBuilder::Form."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class FieldConfig(PropertyType):
    excluded: bool | None = None
    input_type: FieldInputConfig | None = None
    label: str | None = None
    position: FieldPosition | None = None
    validations: list[FieldValidationConfiguration] = field(default_factory=list)


@dataclass
class FieldInputConfig(PropertyType):
    type_: str | None = None
    default_checked: bool | None = None
    default_country_code: str | None = None
    default_value: str | None = None
    descriptive_text: str | None = None
    file_uploader_config: FileUploaderFieldConfig | None = None
    is_array: bool | None = None
    max_value: float | None = None
    min_value: float | None = None
    name: str | None = None
    placeholder: str | None = None
    read_only: bool | None = None
    required: bool | None = None
    step: float | None = None
    value: str | None = None
    value_mappings: ValueMappings | None = None


@dataclass
class FieldPosition(PropertyType):
    below: str | None = None
    fixed: str | None = None
    right_of: str | None = None


@dataclass
class FieldValidationConfiguration(PropertyType):
    type_: str | None = None
    num_values: list[Double] = field(default_factory=list)
    str_values: list[String] = field(default_factory=list)
    validation_message: str | None = None


@dataclass
class FileUploaderFieldConfig(PropertyType):
    accepted_file_types: list[String] = field(default_factory=list)
    access_level: str | None = None
    is_resumable: bool | None = None
    max_file_count: float | None = None
    max_size: float | None = None
    show_thumbnails: bool | None = None


@dataclass
class FormButton(PropertyType):
    children: str | None = None
    excluded: bool | None = None
    position: FieldPosition | None = None


@dataclass
class FormCTA(PropertyType):
    cancel: FormButton | None = None
    clear: FormButton | None = None
    position: str | None = None
    submit: FormButton | None = None


@dataclass
class FormDataTypeConfig(PropertyType):
    data_source_type: str | None = None
    data_type_name: str | None = None


@dataclass
class FormInputBindingPropertiesValue(PropertyType):
    binding_properties: FormInputBindingPropertiesValueProperties | None = None
    type_: str | None = None


@dataclass
class FormInputBindingPropertiesValueProperties(PropertyType):
    model: str | None = None


@dataclass
class FormInputValueProperty(PropertyType):
    binding_properties: FormInputValuePropertyBindingProperties | None = None
    concat: list[FormInputValueProperty] = field(default_factory=list)
    value: str | None = None


@dataclass
class FormInputValuePropertyBindingProperties(PropertyType):
    property: str | None = None
    field_: str | None = None


@dataclass
class FormStyle(PropertyType):
    horizontal_gap: FormStyleConfig | None = None
    outer_padding: FormStyleConfig | None = None
    vertical_gap: FormStyleConfig | None = None


@dataclass
class FormStyleConfig(PropertyType):
    token_reference: str | None = None
    value: str | None = None


@dataclass
class SectionalElement(PropertyType):
    type_: str | None = None
    excluded: bool | None = None
    level: float | None = None
    orientation: str | None = None
    position: FieldPosition | None = None
    text: str | None = None


@dataclass
class ValueMapping(PropertyType):
    value: FormInputValueProperty | None = None
    display_value: FormInputValueProperty | None = None


@dataclass
class ValueMappings(PropertyType):
    values: list[ValueMapping] = field(default_factory=list)
    binding_properties: dict[str, FormInputBindingPropertiesValue] = field(
        default_factory=dict
    )
