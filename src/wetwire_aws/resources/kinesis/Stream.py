"""PropertyTypes for AWS::Kinesis::Stream."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class StreamEncryption(PropertyType):
    encryption_type: DslValue[str] | None = None
    key_id: DslValue[str] | None = None


@dataclass
class StreamModeDetails(PropertyType):
    stream_mode: DslValue[str] | None = None


@dataclass
class WarmThroughputObject(PropertyType):
    current_mi_bps: DslValue[int] | None = None
    target_mi_bps: DslValue[int] | None = None
