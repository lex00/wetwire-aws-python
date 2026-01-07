"""PropertyTypes for AWS::IoTWireless::PartnerAccount."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class SidewalkAccountInfo(PropertyType):
    app_server_private_key: DslValue[str] | None = None


@dataclass
class SidewalkAccountInfoWithFingerprint(PropertyType):
    amazon_id: DslValue[str] | None = None
    arn: DslValue[str] | None = None
    fingerprint: DslValue[str] | None = None


@dataclass
class SidewalkUpdateAccount(PropertyType):
    app_server_private_key: DslValue[str] | None = None
