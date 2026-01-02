"""PropertyTypes for AWS::SSM::Document."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AttachmentsSource(PropertyType):
    key: str | None = None
    name: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class DocumentRequires(PropertyType):
    name: str | None = None
    version: str | None = None
