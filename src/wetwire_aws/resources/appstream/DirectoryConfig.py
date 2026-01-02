"""PropertyTypes for AWS::AppStream::DirectoryConfig."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CertificateBasedAuthProperties(PropertyType):
    certificate_authority_arn: str | None = None
    status: str | None = None


@dataclass
class ServiceAccountCredentials(PropertyType):
    account_name: str | None = None
    account_password: str | None = None
