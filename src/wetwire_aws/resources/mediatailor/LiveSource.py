"""PropertyTypes for AWS::MediaTailor::LiveSource."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class HttpPackageConfiguration(PropertyType):
    path: str | None = None
    source_group: str | None = None
    type_: str | None = None
