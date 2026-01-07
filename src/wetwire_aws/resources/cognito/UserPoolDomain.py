"""PropertyTypes for AWS::Cognito::UserPoolDomain."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CustomDomainConfigType(PropertyType):
    certificate_arn: DslValue[str] | None = None
