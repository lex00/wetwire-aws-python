"""PropertyTypes for AWS::Kendra::Index."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CapacityUnitsConfiguration(PropertyType):
    query_capacity_units: int | None = None
    storage_capacity_units: int | None = None


@dataclass
class DocumentMetadataConfiguration(PropertyType):
    name: str | None = None
    type_: str | None = None
    relevance: Relevance | None = None
    search: Search | None = None


@dataclass
class JsonTokenTypeConfiguration(PropertyType):
    group_attribute_field: str | None = None
    user_name_attribute_field: str | None = None


@dataclass
class JwtTokenTypeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "url": "URL",
    }

    key_location: str | None = None
    claim_regex: str | None = None
    group_attribute_field: str | None = None
    issuer: str | None = None
    secret_manager_arn: str | None = None
    url: str | None = None
    user_name_attribute_field: str | None = None


@dataclass
class Relevance(PropertyType):
    duration: str | None = None
    freshness: bool | None = None
    importance: int | None = None
    rank_order: str | None = None
    value_importance_items: list[ValueImportanceItem] = field(default_factory=list)


@dataclass
class Search(PropertyType):
    displayable: bool | None = None
    facetable: bool | None = None
    searchable: bool | None = None
    sortable: bool | None = None


@dataclass
class ServerSideEncryptionConfiguration(PropertyType):
    kms_key_id: str | None = None


@dataclass
class UserTokenConfiguration(PropertyType):
    json_token_type_configuration: JsonTokenTypeConfiguration | None = None
    jwt_token_type_configuration: JwtTokenTypeConfiguration | None = None


@dataclass
class ValueImportanceItem(PropertyType):
    key: str | None = None
    value: int | None = None
