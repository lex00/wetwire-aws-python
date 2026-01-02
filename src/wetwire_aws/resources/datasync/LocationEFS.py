"""PropertyTypes for AWS::DataSync::LocationEFS."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Ec2Config(PropertyType):
    security_group_arns: list[String] = field(default_factory=list)
    subnet_arn: str | None = None
