"""PropertyTypes for AWS::DataSync::LocationHDFS."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class NameNode(PropertyType):
    hostname: DslValue[str] | None = None
    port: DslValue[int] | None = None


@dataclass
class QopConfiguration(PropertyType):
    data_transfer_protection: DslValue[str] | None = None
    rpc_protection: DslValue[str] | None = None
