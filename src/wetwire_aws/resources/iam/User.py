"""PropertyTypes for AWS::IAM::User."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class LoginProfile(PropertyType):
    password: str | None = None
    password_reset_required: bool | None = None


@dataclass
class Policy(PropertyType):
    policy_document: dict[str, Any] | None = None
    policy_name: str | None = None
