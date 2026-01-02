"""PropertyTypes for AWS::M2::Environment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EfsStorageConfiguration(PropertyType):
    file_system_id: str | None = None
    mount_point: str | None = None


@dataclass
class FsxStorageConfiguration(PropertyType):
    file_system_id: str | None = None
    mount_point: str | None = None


@dataclass
class HighAvailabilityConfig(PropertyType):
    desired_capacity: int | None = None


@dataclass
class StorageConfiguration(PropertyType):
    efs: EfsStorageConfiguration | None = None
    fsx: FsxStorageConfiguration | None = None
