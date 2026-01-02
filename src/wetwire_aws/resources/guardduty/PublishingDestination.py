"""PropertyTypes for AWS::GuardDuty::PublishingDestination."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CFNDestinationProperties(PropertyType):
    destination_arn: str | None = None
    kms_key_arn: str | None = None


@dataclass
class TagItem(PropertyType):
    key: str | None = None
    value: str | None = None
