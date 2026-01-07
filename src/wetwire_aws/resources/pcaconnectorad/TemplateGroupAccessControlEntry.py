"""PropertyTypes for AWS::PCAConnectorAD::TemplateGroupAccessControlEntry."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AccessRights(PropertyType):
    auto_enroll: DslValue[str] | None = None
    enroll: DslValue[str] | None = None
