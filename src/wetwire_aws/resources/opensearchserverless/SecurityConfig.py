"""PropertyTypes for AWS::OpenSearchServerless::SecurityConfig."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class IamFederationConfigOptions(PropertyType):
    group_attribute: DslValue[str] | None = None
    user_attribute: DslValue[str] | None = None


@dataclass
class IamIdentityCenterConfigOptions(PropertyType):
    instance_arn: DslValue[str] | None = None
    application_arn: DslValue[str] | None = None
    application_description: DslValue[str] | None = None
    application_name: DslValue[str] | None = None
    group_attribute: DslValue[str] | None = None
    user_attribute: DslValue[str] | None = None


@dataclass
class SamlConfigOptions(PropertyType):
    metadata: DslValue[str] | None = None
    group_attribute: DslValue[str] | None = None
    open_search_serverless_entity_id: DslValue[str] | None = None
    session_timeout: DslValue[int] | None = None
    user_attribute: DslValue[str] | None = None
