"""PropertyTypes for AWS::DataZone::Domain."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class SingleSignOn(PropertyType):
    idc_instance_arn: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    user_assignment: DslValue[str] | None = None
