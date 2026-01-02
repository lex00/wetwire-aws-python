"""PropertyTypes for AWS::MediaLive::InputSecurityGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class InputWhitelistRuleCidr(PropertyType):
    cidr: str | None = None
