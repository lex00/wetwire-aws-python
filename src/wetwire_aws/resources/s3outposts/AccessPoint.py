"""PropertyTypes for AWS::S3Outposts::AccessPoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class VpcConfiguration(PropertyType):
    vpc_id: str | None = None
