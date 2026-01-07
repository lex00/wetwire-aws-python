"""PropertyTypes for AWS::SystemsManagerSAP::Application."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ComponentInfo(PropertyType):
    component_type: DslValue[str] | None = None
    ec2_instance_id: DslValue[str] | None = None
    sid: DslValue[str] | None = None


@dataclass
class Credential(PropertyType):
    credential_type: DslValue[str] | None = None
    database_name: DslValue[str] | None = None
    secret_id: DslValue[str] | None = None
