"""PropertyTypes for AWS::SSO::Application."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class PortalOptionsConfiguration(PropertyType):
    sign_in_options: SignInOptions | None = None
    visibility: str | None = None


@dataclass
class SignInOptions(PropertyType):
    origin: str | None = None
    application_url: str | None = None
