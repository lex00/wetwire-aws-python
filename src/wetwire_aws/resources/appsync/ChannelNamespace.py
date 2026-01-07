"""PropertyTypes for AWS::AppSync::ChannelNamespace."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AuthMode(PropertyType):
    auth_type: DslValue[str] | None = None


@dataclass
class HandlerConfig(PropertyType):
    behavior: DslValue[str] | None = None
    integration: DslValue[Integration] | None = None


@dataclass
class HandlerConfigs(PropertyType):
    on_publish: DslValue[HandlerConfig] | None = None
    on_subscribe: DslValue[HandlerConfig] | None = None


@dataclass
class Integration(PropertyType):
    data_source_name: DslValue[str] | None = None
    lambda_config: DslValue[LambdaConfig] | None = None


@dataclass
class LambdaConfig(PropertyType):
    invoke_type: DslValue[str] | None = None
