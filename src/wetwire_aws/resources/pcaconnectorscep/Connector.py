"""PropertyTypes for AWS::PCAConnectorSCEP::Connector."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class IntuneConfiguration(PropertyType):
    azure_application_id: DslValue[str] | None = None
    domain: DslValue[str] | None = None


@dataclass
class MobileDeviceManagement(PropertyType):
    intune: DslValue[IntuneConfiguration] | None = None


@dataclass
class OpenIdConfiguration(PropertyType):
    audience: DslValue[str] | None = None
    issuer: DslValue[str] | None = None
    subject: DslValue[str] | None = None
