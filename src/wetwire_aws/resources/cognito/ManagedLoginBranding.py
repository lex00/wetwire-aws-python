"""PropertyTypes for AWS::Cognito::ManagedLoginBranding."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AssetType(PropertyType):
    category: DslValue[str] | None = None
    color_mode: DslValue[str] | None = None
    extension: DslValue[str] | None = None
    bytes: DslValue[str] | None = None
    resource_id: DslValue[str] | None = None
