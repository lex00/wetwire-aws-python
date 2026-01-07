"""PropertyTypes for AWS::MediaPackage::Asset."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EgressEndpoint(PropertyType):
    packaging_configuration_id: DslValue[str] | None = None
    url: DslValue[str] | None = None
