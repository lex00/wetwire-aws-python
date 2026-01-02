"""PropertyTypes for AWS::SystemsManagerSAP::Application."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ComponentInfo(PropertyType):
    component_type: str | None = None
    ec2_instance_id: str | None = None
    sid: str | None = None


@dataclass
class Credential(PropertyType):
    credential_type: str | None = None
    database_name: str | None = None
    secret_id: str | None = None
