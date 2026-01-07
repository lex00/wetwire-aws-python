"""PropertyTypes for AWS::AppStream::Stack."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AccessEndpoint(PropertyType):
    endpoint_type: DslValue[str] | None = None
    vpce_id: DslValue[str] | None = None


@dataclass
class ApplicationSettings(PropertyType):
    enabled: DslValue[bool] | None = None
    settings_group: DslValue[str] | None = None


@dataclass
class StorageConnector(PropertyType):
    connector_type: DslValue[str] | None = None
    domains: list[DslValue[str]] = field(default_factory=list)
    resource_identifier: DslValue[str] | None = None


@dataclass
class StreamingExperienceSettings(PropertyType):
    preferred_protocol: DslValue[str] | None = None


@dataclass
class UserSetting(PropertyType):
    action: DslValue[str] | None = None
    permission: DslValue[str] | None = None
    maximum_length: DslValue[int] | None = None
