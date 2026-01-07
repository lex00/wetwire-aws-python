"""PropertyTypes for AWS::Kendra::Index."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CapacityUnitsConfiguration(PropertyType):
    query_capacity_units: DslValue[int] | None = None
    storage_capacity_units: DslValue[int] | None = None


@dataclass
class DocumentMetadataConfiguration(PropertyType):
    name: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    relevance: DslValue[Relevance] | None = None
    search: DslValue[Search] | None = None


@dataclass
class JsonTokenTypeConfiguration(PropertyType):
    group_attribute_field: DslValue[str] | None = None
    user_name_attribute_field: DslValue[str] | None = None


@dataclass
class JwtTokenTypeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "url": "URL",
    }

    key_location: DslValue[str] | None = None
    claim_regex: DslValue[str] | None = None
    group_attribute_field: DslValue[str] | None = None
    issuer: DslValue[str] | None = None
    secret_manager_arn: DslValue[str] | None = None
    url: DslValue[str] | None = None
    user_name_attribute_field: DslValue[str] | None = None


@dataclass
class Relevance(PropertyType):
    duration: DslValue[str] | None = None
    freshness: DslValue[bool] | None = None
    importance: DslValue[int] | None = None
    rank_order: DslValue[str] | None = None
    value_importance_items: list[DslValue[ValueImportanceItem]] = field(
        default_factory=list
    )


@dataclass
class Search(PropertyType):
    displayable: DslValue[bool] | None = None
    facetable: DslValue[bool] | None = None
    searchable: DslValue[bool] | None = None
    sortable: DslValue[bool] | None = None


@dataclass
class ServerSideEncryptionConfiguration(PropertyType):
    kms_key_id: DslValue[str] | None = None


@dataclass
class UserTokenConfiguration(PropertyType):
    json_token_type_configuration: DslValue[JsonTokenTypeConfiguration] | None = None
    jwt_token_type_configuration: DslValue[JwtTokenTypeConfiguration] | None = None


@dataclass
class ValueImportanceItem(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[int] | None = None
