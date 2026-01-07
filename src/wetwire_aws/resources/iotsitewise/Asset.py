"""PropertyTypes for AWS::IoTSiteWise::Asset."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AssetHierarchy(PropertyType):
    child_asset_id: DslValue[str] | None = None
    external_id: DslValue[str] | None = None
    id: DslValue[str] | None = None
    logical_id: DslValue[str] | None = None


@dataclass
class AssetProperty(PropertyType):
    alias: DslValue[str] | None = None
    external_id: DslValue[str] | None = None
    id: DslValue[str] | None = None
    logical_id: DslValue[str] | None = None
    notification_state: DslValue[str] | None = None
    unit: DslValue[str] | None = None
