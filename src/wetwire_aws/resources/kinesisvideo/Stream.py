"""PropertyTypes for AWS::KinesisVideo::Stream."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class StreamStorageConfiguration(PropertyType):
    default_storage_tier: DslValue[str] | None = None
