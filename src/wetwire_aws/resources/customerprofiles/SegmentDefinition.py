"""PropertyTypes for AWS::CustomerProfiles::SegmentDefinition."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AddressDimension(PropertyType):
    city: DslValue[ProfileDimension] | None = None
    country: DslValue[ProfileDimension] | None = None
    county: DslValue[ProfileDimension] | None = None
    postal_code: DslValue[ProfileDimension] | None = None
    province: DslValue[ProfileDimension] | None = None
    state: DslValue[ProfileDimension] | None = None


@dataclass
class AttributeDimension(PropertyType):
    dimension_type: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class CalculatedAttributeDimension(PropertyType):
    dimension_type: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)
    condition_overrides: DslValue[ConditionOverrides] | None = None


@dataclass
class ConditionOverrides(PropertyType):
    range: DslValue[RangeOverride] | None = None


@dataclass
class DateDimension(PropertyType):
    dimension_type: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Dimension(PropertyType):
    calculated_attributes: dict[str, DslValue[CalculatedAttributeDimension]] = field(
        default_factory=dict
    )
    profile_attributes: DslValue[ProfileAttributes] | None = None


@dataclass
class ExtraLengthValueProfileDimension(PropertyType):
    dimension_type: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Group(PropertyType):
    dimensions: list[DslValue[Dimension]] = field(default_factory=list)
    source_segments: list[DslValue[SourceSegment]] = field(default_factory=list)
    source_type: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class ProfileAttributes(PropertyType):
    account_number: DslValue[ProfileDimension] | None = None
    additional_information: DslValue[ExtraLengthValueProfileDimension] | None = None
    address: DslValue[AddressDimension] | None = None
    attributes: dict[str, DslValue[AttributeDimension]] = field(default_factory=dict)
    billing_address: DslValue[AddressDimension] | None = None
    birth_date: DslValue[DateDimension] | None = None
    business_email_address: DslValue[ProfileDimension] | None = None
    business_name: DslValue[ProfileDimension] | None = None
    business_phone_number: DslValue[ProfileDimension] | None = None
    email_address: DslValue[ProfileDimension] | None = None
    first_name: DslValue[ProfileDimension] | None = None
    gender_string: DslValue[ProfileDimension] | None = None
    home_phone_number: DslValue[ProfileDimension] | None = None
    last_name: DslValue[ProfileDimension] | None = None
    mailing_address: DslValue[AddressDimension] | None = None
    middle_name: DslValue[ProfileDimension] | None = None
    mobile_phone_number: DslValue[ProfileDimension] | None = None
    party_type_string: DslValue[ProfileDimension] | None = None
    personal_email_address: DslValue[ProfileDimension] | None = None
    phone_number: DslValue[ProfileDimension] | None = None
    profile_type: DslValue[ProfileTypeDimension] | None = None
    shipping_address: DslValue[AddressDimension] | None = None


@dataclass
class ProfileDimension(PropertyType):
    dimension_type: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ProfileTypeDimension(PropertyType):
    dimension_type: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class RangeOverride(PropertyType):
    start: DslValue[int] | None = None
    unit: DslValue[str] | None = None
    end: DslValue[int] | None = None


@dataclass
class SegmentGroup(PropertyType):
    groups: list[DslValue[Group]] = field(default_factory=list)
    include: DslValue[str] | None = None


@dataclass
class SourceSegment(PropertyType):
    segment_definition_name: DslValue[str] | None = None
