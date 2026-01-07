"""PropertyTypes for AWS::IVS::EncoderConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Video(PropertyType):
    bitrate: DslValue[int] | None = None
    framerate: DslValue[float] | None = None
    height: DslValue[int] | None = None
    width: DslValue[int] | None = None
