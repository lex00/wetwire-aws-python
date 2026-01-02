"""PropertyTypes for AWS::DataSync::LocationHDFS."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class NameNode(PropertyType):
    hostname: str | None = None
    port: int | None = None


@dataclass
class QopConfiguration(PropertyType):
    data_transfer_protection: str | None = None
    rpc_protection: str | None = None
