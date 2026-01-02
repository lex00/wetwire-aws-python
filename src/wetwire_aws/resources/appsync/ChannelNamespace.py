"""PropertyTypes for AWS::AppSync::ChannelNamespace."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AuthMode(PropertyType):
    auth_type: str | None = None


@dataclass
class HandlerConfig(PropertyType):
    behavior: str | None = None
    integration: Integration | None = None


@dataclass
class HandlerConfigs(PropertyType):
    on_publish: HandlerConfig | None = None
    on_subscribe: HandlerConfig | None = None


@dataclass
class Integration(PropertyType):
    data_source_name: str | None = None
    lambda_config: LambdaConfig | None = None


@dataclass
class LambdaConfig(PropertyType):
    invoke_type: str | None = None
