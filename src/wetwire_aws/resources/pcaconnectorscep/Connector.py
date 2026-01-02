"""PropertyTypes for AWS::PCAConnectorSCEP::Connector."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class IntuneConfiguration(PropertyType):
    azure_application_id: str | None = None
    domain: str | None = None


@dataclass
class MobileDeviceManagement(PropertyType):
    intune: IntuneConfiguration | None = None


@dataclass
class OpenIdConfiguration(PropertyType):
    audience: str | None = None
    issuer: str | None = None
    subject: str | None = None
