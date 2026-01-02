"""PropertyTypes for AWS::IoTWireless::PartnerAccount."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class SidewalkAccountInfo(PropertyType):
    app_server_private_key: str | None = None


@dataclass
class SidewalkAccountInfoWithFingerprint(PropertyType):
    amazon_id: str | None = None
    arn: str | None = None
    fingerprint: str | None = None


@dataclass
class SidewalkUpdateAccount(PropertyType):
    app_server_private_key: str | None = None
