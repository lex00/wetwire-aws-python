"""PropertyTypes for AWS::AmazonMQ::Broker."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ConfigurationId(PropertyType):
    id: DslValue[str] | None = None
    revision: DslValue[int] | None = None


@dataclass
class EncryptionOptions(PropertyType):
    use_aws_owned_key: DslValue[bool] | None = None
    kms_key_id: DslValue[str] | None = None


@dataclass
class LdapServerMetadata(PropertyType):
    hosts: list[DslValue[str]] = field(default_factory=list)
    role_base: DslValue[str] | None = None
    role_search_matching: DslValue[str] | None = None
    service_account_username: DslValue[str] | None = None
    user_base: DslValue[str] | None = None
    user_search_matching: DslValue[str] | None = None
    role_name: DslValue[str] | None = None
    role_search_subtree: DslValue[bool] | None = None
    service_account_password: DslValue[str] | None = None
    user_role_name: DslValue[str] | None = None
    user_search_subtree: DslValue[bool] | None = None


@dataclass
class LogList(PropertyType):
    audit: DslValue[bool] | None = None
    general: DslValue[bool] | None = None


@dataclass
class MaintenanceWindow(PropertyType):
    day_of_week: DslValue[str] | None = None
    time_of_day: DslValue[str] | None = None
    time_zone: DslValue[str] | None = None


@dataclass
class TagsEntry(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class User(PropertyType):
    password: DslValue[str] | None = None
    username: DslValue[str] | None = None
    console_access: DslValue[bool] | None = None
    groups: list[DslValue[str]] = field(default_factory=list)
    replication_user: DslValue[bool] | None = None
