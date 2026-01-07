"""PropertyTypes for AWS::Transfer::Agreement."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CustomDirectories(PropertyType):
    failed_files_directory: DslValue[str] | None = None
    mdn_files_directory: DslValue[str] | None = None
    payload_files_directory: DslValue[str] | None = None
    status_files_directory: DslValue[str] | None = None
    temporary_files_directory: DslValue[str] | None = None
