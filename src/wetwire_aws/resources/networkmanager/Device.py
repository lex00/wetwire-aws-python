"""PropertyTypes for AWS::NetworkManager::Device."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AWSLocation(PropertyType):
    subnet_arn: DslValue[str] | None = None
    zone: DslValue[str] | None = None


@dataclass
class Location(PropertyType):
    address: DslValue[str] | None = None
    latitude: DslValue[str] | None = None
    longitude: DslValue[str] | None = None
