"""PropertyTypes for AWS::MediaPackageV2::Channel."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class IngestEndpoint(PropertyType):
    id: str | None = None
    url: str | None = None


@dataclass
class InputSwitchConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "mqcs_input_switching": "MQCSInputSwitching",
    }

    mqcs_input_switching: bool | None = None
    preferred_input: int | None = None


@dataclass
class OutputHeaderConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "publish_mqcs": "PublishMQCS",
    }

    publish_mqcs: bool | None = None
