"""PropertyTypes for AWS::IoTThingsGraph::FlowTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DefinitionDocument(PropertyType):
    language: DslValue[str] | None = None
    text: DslValue[str] | None = None
