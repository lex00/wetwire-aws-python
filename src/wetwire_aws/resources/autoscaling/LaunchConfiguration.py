"""PropertyTypes for AWS::AutoScaling::LaunchConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BlockDevice(PropertyType):
    delete_on_termination: DslValue[bool] | None = None
    encrypted: DslValue[bool] | None = None
    iops: DslValue[int] | None = None
    snapshot_id: DslValue[str] | None = None
    throughput: DslValue[int] | None = None
    volume_size: DslValue[int] | None = None
    volume_type: DslValue[str] | None = None


@dataclass
class BlockDeviceMapping(PropertyType):
    device_name: DslValue[str] | None = None
    ebs: DslValue[BlockDevice] | None = None
    no_device: DslValue[bool] | None = None
    virtual_name: DslValue[str] | None = None


@dataclass
class MetadataOptions(PropertyType):
    http_endpoint: DslValue[str] | None = None
    http_put_response_hop_limit: DslValue[int] | None = None
    http_tokens: DslValue[str] | None = None
