"""PropertyTypes for AWS::CustomerProfiles::SegmentDefinition."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AddressDimension(PropertyType):
    city: ProfileDimension | None = None
    country: ProfileDimension | None = None
    county: ProfileDimension | None = None
    postal_code: ProfileDimension | None = None
    province: ProfileDimension | None = None
    state: ProfileDimension | None = None


@dataclass
class AttributeDimension(PropertyType):
    dimension_type: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class CalculatedAttributeDimension(PropertyType):
    dimension_type: str | None = None
    values: list[String] = field(default_factory=list)
    condition_overrides: ConditionOverrides | None = None


@dataclass
class ConditionOverrides(PropertyType):
    range: RangeOverride | None = None


@dataclass
class DateDimension(PropertyType):
    dimension_type: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class Dimension(PropertyType):
    calculated_attributes: dict[str, CalculatedAttributeDimension] = field(
        default_factory=dict
    )
    profile_attributes: ProfileAttributes | None = None


@dataclass
class ExtraLengthValueProfileDimension(PropertyType):
    dimension_type: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class Group(PropertyType):
    dimensions: list[Dimension] = field(default_factory=list)
    source_segments: list[SourceSegment] = field(default_factory=list)
    source_type: str | None = None
    type_: str | None = None


@dataclass
class ProfileAttributes(PropertyType):
    account_number: ProfileDimension | None = None
    additional_information: ExtraLengthValueProfileDimension | None = None
    address: AddressDimension | None = None
    attributes: dict[str, AttributeDimension] = field(default_factory=dict)
    billing_address: AddressDimension | None = None
    birth_date: DateDimension | None = None
    business_email_address: ProfileDimension | None = None
    business_name: ProfileDimension | None = None
    business_phone_number: ProfileDimension | None = None
    email_address: ProfileDimension | None = None
    first_name: ProfileDimension | None = None
    gender_string: ProfileDimension | None = None
    home_phone_number: ProfileDimension | None = None
    last_name: ProfileDimension | None = None
    mailing_address: AddressDimension | None = None
    middle_name: ProfileDimension | None = None
    mobile_phone_number: ProfileDimension | None = None
    party_type_string: ProfileDimension | None = None
    personal_email_address: ProfileDimension | None = None
    phone_number: ProfileDimension | None = None
    profile_type: ProfileTypeDimension | None = None
    shipping_address: AddressDimension | None = None


@dataclass
class ProfileDimension(PropertyType):
    dimension_type: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class ProfileTypeDimension(PropertyType):
    dimension_type: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class RangeOverride(PropertyType):
    start: int | None = None
    unit: str | None = None
    end: int | None = None


@dataclass
class SegmentGroup(PropertyType):
    groups: list[Group] = field(default_factory=list)
    include: str | None = None


@dataclass
class SourceSegment(PropertyType):
    segment_definition_name: str | None = None
