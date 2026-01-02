"""PropertyTypes for AWS::Cognito::UserPoolResourceServer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ResourceServerScopeType(PropertyType):
    scope_description: str | None = None
    scope_name: str | None = None
