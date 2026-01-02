"""PropertyTypes for AWS::QBusiness::DataAccessor."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ActionConfiguration(PropertyType):
    action: str | None = None
    filter_configuration: ActionFilterConfiguration | None = None


@dataclass
class ActionFilterConfiguration(PropertyType):
    document_attribute_filter: AttributeFilter | None = None


@dataclass
class AttributeFilter(PropertyType):
    and_all_filters: list[AttributeFilter] = field(default_factory=list)
    contains_all: DocumentAttribute | None = None
    contains_any: DocumentAttribute | None = None
    equals_to: DocumentAttribute | None = None
    greater_than: DocumentAttribute | None = None
    greater_than_or_equals: DocumentAttribute | None = None
    less_than: DocumentAttribute | None = None
    less_than_or_equals: DocumentAttribute | None = None
    not_filter: AttributeFilter | None = None
    or_all_filters: list[AttributeFilter] = field(default_factory=list)


@dataclass
class DataAccessorAuthenticationConfiguration(PropertyType):
    idc_trusted_token_issuer_configuration: (
        DataAccessorIdcTrustedTokenIssuerConfiguration | None
    ) = None


@dataclass
class DataAccessorAuthenticationDetail(PropertyType):
    authentication_type: str | None = None
    authentication_configuration: DataAccessorAuthenticationConfiguration | None = None
    external_ids: list[String] = field(default_factory=list)


@dataclass
class DataAccessorIdcTrustedTokenIssuerConfiguration(PropertyType):
    idc_trusted_token_issuer_arn: str | None = None


@dataclass
class DocumentAttribute(PropertyType):
    name: str | None = None
    value: DocumentAttributeValue | None = None


@dataclass
class DocumentAttributeValue(PropertyType):
    date_value: str | None = None
    long_value: float | None = None
    string_list_value: list[String] = field(default_factory=list)
    string_value: str | None = None
