"""PropertyTypes for AWS::AmazonMQ::ConfigurationAssociation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ConfigurationId(PropertyType):
    id: str | None = None
    revision: int | None = None
