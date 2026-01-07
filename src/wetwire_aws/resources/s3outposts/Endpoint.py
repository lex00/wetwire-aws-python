"""PropertyTypes for AWS::S3Outposts::Endpoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class FailedReason(PropertyType):
    error_code: DslValue[str] | None = None
    message: DslValue[str] | None = None


@dataclass
class NetworkInterface(PropertyType):
    network_interface_id: DslValue[str] | None = None
