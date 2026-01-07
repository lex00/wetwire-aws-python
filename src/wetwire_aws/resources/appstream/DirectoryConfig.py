"""PropertyTypes for AWS::AppStream::DirectoryConfig."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CertificateBasedAuthProperties(PropertyType):
    certificate_authority_arn: DslValue[str] | None = None
    status: DslValue[str] | None = None


@dataclass
class ServiceAccountCredentials(PropertyType):
    account_name: DslValue[str] | None = None
    account_password: DslValue[str] | None = None
