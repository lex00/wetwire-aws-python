"""PropertyTypes for AWS::Cognito::ManagedLoginBranding."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AssetType(PropertyType):
    category: str | None = None
    color_mode: str | None = None
    extension: str | None = None
    bytes: str | None = None
    resource_id: str | None = None
