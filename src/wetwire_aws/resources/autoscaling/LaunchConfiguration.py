"""PropertyTypes for AWS::AutoScaling::LaunchConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BlockDevice(PropertyType):
    delete_on_termination: bool | None = None
    encrypted: bool | None = None
    iops: int | None = None
    snapshot_id: str | None = None
    throughput: int | None = None
    volume_size: int | None = None
    volume_type: str | None = None


@dataclass
class BlockDeviceMapping(PropertyType):
    device_name: str | None = None
    ebs: BlockDevice | None = None
    no_device: bool | None = None
    virtual_name: str | None = None


@dataclass
class MetadataOptions(PropertyType):
    http_endpoint: str | None = None
    http_put_response_hop_limit: int | None = None
    http_tokens: str | None = None
