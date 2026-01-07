"""PropertyTypes for AWS::AmazonMQ::ConfigurationAssociation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ConfigurationId(PropertyType):
    id: DslValue[str] | None = None
    revision: DslValue[int] | None = None
