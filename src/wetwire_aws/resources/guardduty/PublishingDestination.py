"""PropertyTypes for AWS::GuardDuty::PublishingDestination."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CFNDestinationProperties(PropertyType):
    destination_arn: DslValue[str] | None = None
    kms_key_arn: DslValue[str] | None = None


@dataclass
class TagItem(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None
