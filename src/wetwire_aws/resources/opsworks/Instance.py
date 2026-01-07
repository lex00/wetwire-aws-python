"""PropertyTypes for AWS::OpsWorks::Instance."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BlockDeviceMapping(PropertyType):
    device_name: DslValue[str] | None = None
    ebs: DslValue[EbsBlockDevice] | None = None
    no_device: DslValue[str] | None = None
    virtual_name: DslValue[str] | None = None


@dataclass
class EbsBlockDevice(PropertyType):
    delete_on_termination: DslValue[bool] | None = None
    iops: DslValue[int] | None = None
    snapshot_id: DslValue[str] | None = None
    volume_size: DslValue[int] | None = None
    volume_type: DslValue[str] | None = None


@dataclass
class TimeBasedAutoScaling(PropertyType):
    friday: dict[str, DslValue[str]] = field(default_factory=dict)
    monday: dict[str, DslValue[str]] = field(default_factory=dict)
    saturday: dict[str, DslValue[str]] = field(default_factory=dict)
    sunday: dict[str, DslValue[str]] = field(default_factory=dict)
    thursday: dict[str, DslValue[str]] = field(default_factory=dict)
    tuesday: dict[str, DslValue[str]] = field(default_factory=dict)
    wednesday: dict[str, DslValue[str]] = field(default_factory=dict)
