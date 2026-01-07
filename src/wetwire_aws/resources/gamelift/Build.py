"""PropertyTypes for AWS::GameLift::Build."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class StorageLocation(PropertyType):
    bucket: DslValue[str] | None = None
    key: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    object_version: DslValue[str] | None = None
