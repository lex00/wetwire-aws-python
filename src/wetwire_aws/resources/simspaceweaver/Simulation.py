"""PropertyTypes for AWS::SimSpaceWeaver::Simulation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class S3Location(PropertyType):
    bucket_name: DslValue[str] | None = None
    object_key: DslValue[str] | None = None
