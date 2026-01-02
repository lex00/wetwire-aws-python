"""PropertyTypes for AWS::AmazonMQ::Broker."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ConfigurationId(PropertyType):
    id: str | None = None
    revision: int | None = None


@dataclass
class EncryptionOptions(PropertyType):
    use_aws_owned_key: bool | None = None
    kms_key_id: str | None = None


@dataclass
class LdapServerMetadata(PropertyType):
    hosts: list[String] = field(default_factory=list)
    role_base: str | None = None
    role_search_matching: str | None = None
    service_account_username: str | None = None
    user_base: str | None = None
    user_search_matching: str | None = None
    role_name: str | None = None
    role_search_subtree: bool | None = None
    service_account_password: str | None = None
    user_role_name: str | None = None
    user_search_subtree: bool | None = None


@dataclass
class LogList(PropertyType):
    audit: bool | None = None
    general: bool | None = None


@dataclass
class MaintenanceWindow(PropertyType):
    day_of_week: str | None = None
    time_of_day: str | None = None
    time_zone: str | None = None


@dataclass
class TagsEntry(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class User(PropertyType):
    password: str | None = None
    username: str | None = None
    console_access: bool | None = None
    groups: list[String] = field(default_factory=list)
    replication_user: bool | None = None
