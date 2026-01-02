"""PropertyTypes for AWS::OpenSearchServerless::SecurityConfig."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class IamFederationConfigOptions(PropertyType):
    group_attribute: str | None = None
    user_attribute: str | None = None


@dataclass
class IamIdentityCenterConfigOptions(PropertyType):
    instance_arn: str | None = None
    application_arn: str | None = None
    application_description: str | None = None
    application_name: str | None = None
    group_attribute: str | None = None
    user_attribute: str | None = None


@dataclass
class SamlConfigOptions(PropertyType):
    metadata: str | None = None
    group_attribute: str | None = None
    open_search_serverless_entity_id: str | None = None
    session_timeout: int | None = None
    user_attribute: str | None = None
