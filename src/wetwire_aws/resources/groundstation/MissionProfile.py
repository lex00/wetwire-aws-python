"""PropertyTypes for AWS::GroundStation::MissionProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DataflowEdge(PropertyType):
    destination: str | None = None
    source: str | None = None


@dataclass
class StreamsKmsKey(PropertyType):
    kms_alias_arn: str | None = None
    kms_alias_name: str | None = None
    kms_key_arn: str | None = None
