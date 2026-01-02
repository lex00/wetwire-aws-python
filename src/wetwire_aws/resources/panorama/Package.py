"""PropertyTypes for AWS::Panorama::Package."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class StorageLocation(PropertyType):
    binary_prefix_location: str | None = None
    bucket: str | None = None
    generated_prefix_location: str | None = None
    manifest_prefix_location: str | None = None
    repo_prefix_location: str | None = None
