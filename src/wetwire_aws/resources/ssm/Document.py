"""PropertyTypes for AWS::SSM::Document."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AttachmentsSource(PropertyType):
    key: DslValue[str] | None = None
    name: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class DocumentRequires(PropertyType):
    name: DslValue[str] | None = None
    version: DslValue[str] | None = None
