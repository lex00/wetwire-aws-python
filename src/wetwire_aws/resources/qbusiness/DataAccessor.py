"""PropertyTypes for AWS::QBusiness::DataAccessor."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ActionConfiguration(PropertyType):
    action: DslValue[str] | None = None
    filter_configuration: DslValue[ActionFilterConfiguration] | None = None


@dataclass
class ActionFilterConfiguration(PropertyType):
    document_attribute_filter: DslValue[AttributeFilter] | None = None


@dataclass
class AttributeFilter(PropertyType):
    and_all_filters: list[DslValue[AttributeFilter]] = field(default_factory=list)
    contains_all: DslValue[DocumentAttribute] | None = None
    contains_any: DslValue[DocumentAttribute] | None = None
    equals_to: DslValue[DocumentAttribute] | None = None
    greater_than: DslValue[DocumentAttribute] | None = None
    greater_than_or_equals: DslValue[DocumentAttribute] | None = None
    less_than: DslValue[DocumentAttribute] | None = None
    less_than_or_equals: DslValue[DocumentAttribute] | None = None
    not_filter: DslValue[AttributeFilter] | None = None
    or_all_filters: list[DslValue[AttributeFilter]] = field(default_factory=list)


@dataclass
class DataAccessorAuthenticationConfiguration(PropertyType):
    idc_trusted_token_issuer_configuration: (
        DslValue[DataAccessorIdcTrustedTokenIssuerConfiguration] | None
    ) = None


@dataclass
class DataAccessorAuthenticationDetail(PropertyType):
    authentication_type: DslValue[str] | None = None
    authentication_configuration: (
        DslValue[DataAccessorAuthenticationConfiguration] | None
    ) = None
    external_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class DataAccessorIdcTrustedTokenIssuerConfiguration(PropertyType):
    idc_trusted_token_issuer_arn: DslValue[str] | None = None


@dataclass
class DocumentAttribute(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[DocumentAttributeValue] | None = None


@dataclass
class DocumentAttributeValue(PropertyType):
    date_value: DslValue[str] | None = None
    long_value: DslValue[float] | None = None
    string_list_value: list[DslValue[str]] = field(default_factory=list)
    string_value: DslValue[str] | None = None
