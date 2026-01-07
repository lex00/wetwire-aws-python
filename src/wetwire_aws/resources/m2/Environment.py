"""PropertyTypes for AWS::M2::Environment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EfsStorageConfiguration(PropertyType):
    file_system_id: DslValue[str] | None = None
    mount_point: DslValue[str] | None = None


@dataclass
class FsxStorageConfiguration(PropertyType):
    file_system_id: DslValue[str] | None = None
    mount_point: DslValue[str] | None = None


@dataclass
class HighAvailabilityConfig(PropertyType):
    desired_capacity: DslValue[int] | None = None


@dataclass
class StorageConfiguration(PropertyType):
    efs: DslValue[EfsStorageConfiguration] | None = None
    fsx: DslValue[FsxStorageConfiguration] | None = None
