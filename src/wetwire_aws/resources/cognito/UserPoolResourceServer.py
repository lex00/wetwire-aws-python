"""PropertyTypes for AWS::Cognito::UserPoolResourceServer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ResourceServerScopeType(PropertyType):
    scope_description: DslValue[str] | None = None
    scope_name: DslValue[str] | None = None
