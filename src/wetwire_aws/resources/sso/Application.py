"""PropertyTypes for AWS::SSO::Application."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class PortalOptionsConfiguration(PropertyType):
    sign_in_options: DslValue[SignInOptions] | None = None
    visibility: DslValue[str] | None = None


@dataclass
class SignInOptions(PropertyType):
    origin: DslValue[str] | None = None
    application_url: DslValue[str] | None = None
