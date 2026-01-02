"""PropertyTypes for AWS::Panorama::ApplicationInstance."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ManifestOverridesPayload(PropertyType):
    payload_data: str | None = None


@dataclass
class ManifestPayload(PropertyType):
    payload_data: str | None = None
