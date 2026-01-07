"""PropertyTypes for AWS::Transfer::WebApp."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class IdentityProviderDetails(PropertyType):
    application_arn: DslValue[str] | None = None
    instance_arn: DslValue[str] | None = None
    role: DslValue[str] | None = None


@dataclass
class WebAppCustomization(PropertyType):
    favicon_file: DslValue[str] | None = None
    logo_file: DslValue[str] | None = None
    title: DslValue[str] | None = None


@dataclass
class WebAppUnits(PropertyType):
    provisioned: DslValue[int] | None = None
