"""PropertyTypes for AWS::Amplify::Branch."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Backend(PropertyType):
    stack_arn: DslValue[str] | None = None


@dataclass
class BasicAuthConfig(PropertyType):
    password: DslValue[str] | None = None
    username: DslValue[str] | None = None
    enable_basic_auth: DslValue[bool] | None = None


@dataclass
class EnvironmentVariable(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None
