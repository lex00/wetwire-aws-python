"""PropertyTypes for AWS::Panorama::Package."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class StorageLocation(PropertyType):
    binary_prefix_location: DslValue[str] | None = None
    bucket: DslValue[str] | None = None
    generated_prefix_location: DslValue[str] | None = None
    manifest_prefix_location: DslValue[str] | None = None
    repo_prefix_location: DslValue[str] | None = None
