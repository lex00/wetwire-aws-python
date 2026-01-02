"""PropertyTypes for AWS::S3Outposts::Endpoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class FailedReason(PropertyType):
    error_code: str | None = None
    message: str | None = None


@dataclass
class NetworkInterface(PropertyType):
    network_interface_id: str | None = None
