"""PropertyTypes for AWS::IoTThingsGraph::FlowTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DefinitionDocument(PropertyType):
    language: str | None = None
    text: str | None = None
