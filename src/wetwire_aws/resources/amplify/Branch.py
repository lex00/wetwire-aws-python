"""PropertyTypes for AWS::Amplify::Branch."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Backend(PropertyType):
    stack_arn: str | None = None


@dataclass
class BasicAuthConfig(PropertyType):
    password: str | None = None
    username: str | None = None
    enable_basic_auth: bool | None = None


@dataclass
class EnvironmentVariable(PropertyType):
    name: str | None = None
    value: str | None = None
