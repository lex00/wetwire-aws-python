"""PropertyTypes for AWS::IoTSiteWise::Asset."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AssetHierarchy(PropertyType):
    child_asset_id: str | None = None
    external_id: str | None = None
    id: str | None = None
    logical_id: str | None = None


@dataclass
class AssetProperty(PropertyType):
    alias: str | None = None
    external_id: str | None = None
    id: str | None = None
    logical_id: str | None = None
    notification_state: str | None = None
    unit: str | None = None
