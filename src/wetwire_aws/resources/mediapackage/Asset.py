"""PropertyTypes for AWS::MediaPackage::Asset."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EgressEndpoint(PropertyType):
    packaging_configuration_id: str | None = None
    url: str | None = None
