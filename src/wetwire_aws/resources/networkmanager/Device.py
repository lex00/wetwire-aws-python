"""PropertyTypes for AWS::NetworkManager::Device."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AWSLocation(PropertyType):
    subnet_arn: str | None = None
    zone: str | None = None


@dataclass
class Location(PropertyType):
    address: str | None = None
    latitude: str | None = None
    longitude: str | None = None
