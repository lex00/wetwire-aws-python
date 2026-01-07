"""PropertyTypes for AWS::DataSync::LocationEFS."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Ec2Config(PropertyType):
    security_group_arns: list[DslValue[str]] = field(default_factory=list)
    subnet_arn: DslValue[str] | None = None
