"""PropertyTypes for AWS::OpsWorks::Instance."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BlockDeviceMapping(PropertyType):
    device_name: str | None = None
    ebs: EbsBlockDevice | None = None
    no_device: str | None = None
    virtual_name: str | None = None


@dataclass
class EbsBlockDevice(PropertyType):
    delete_on_termination: bool | None = None
    iops: int | None = None
    snapshot_id: str | None = None
    volume_size: int | None = None
    volume_type: str | None = None


@dataclass
class TimeBasedAutoScaling(PropertyType):
    friday: dict[str, String] = field(default_factory=dict)
    monday: dict[str, String] = field(default_factory=dict)
    saturday: dict[str, String] = field(default_factory=dict)
    sunday: dict[str, String] = field(default_factory=dict)
    thursday: dict[str, String] = field(default_factory=dict)
    tuesday: dict[str, String] = field(default_factory=dict)
    wednesday: dict[str, String] = field(default_factory=dict)
