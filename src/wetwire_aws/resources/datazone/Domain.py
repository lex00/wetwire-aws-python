"""PropertyTypes for AWS::DataZone::Domain."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class SingleSignOn(PropertyType):
    idc_instance_arn: str | None = None
    type_: str | None = None
    user_assignment: str | None = None
