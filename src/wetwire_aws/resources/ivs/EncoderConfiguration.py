"""PropertyTypes for AWS::IVS::EncoderConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Video(PropertyType):
    bitrate: int | None = None
    framerate: float | None = None
    height: int | None = None
    width: int | None = None
