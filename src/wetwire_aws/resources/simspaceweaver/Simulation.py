"""PropertyTypes for AWS::SimSpaceWeaver::Simulation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class S3Location(PropertyType):
    bucket_name: str | None = None
    object_key: str | None = None
