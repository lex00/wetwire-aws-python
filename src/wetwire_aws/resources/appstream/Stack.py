"""PropertyTypes for AWS::AppStream::Stack."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AccessEndpoint(PropertyType):
    endpoint_type: str | None = None
    vpce_id: str | None = None


@dataclass
class ApplicationSettings(PropertyType):
    enabled: bool | None = None
    settings_group: str | None = None


@dataclass
class StorageConnector(PropertyType):
    connector_type: str | None = None
    domains: list[String] = field(default_factory=list)
    resource_identifier: str | None = None


@dataclass
class StreamingExperienceSettings(PropertyType):
    preferred_protocol: str | None = None


@dataclass
class UserSetting(PropertyType):
    action: str | None = None
    permission: str | None = None
    maximum_length: int | None = None
