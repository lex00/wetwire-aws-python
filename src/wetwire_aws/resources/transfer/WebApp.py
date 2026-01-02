"""PropertyTypes for AWS::Transfer::WebApp."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class IdentityProviderDetails(PropertyType):
    application_arn: str | None = None
    instance_arn: str | None = None
    role: str | None = None


@dataclass
class WebAppCustomization(PropertyType):
    favicon_file: str | None = None
    logo_file: str | None = None
    title: str | None = None


@dataclass
class WebAppUnits(PropertyType):
    provisioned: int | None = None
