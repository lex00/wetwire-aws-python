"""PropertyTypes for AWS::Amplify::Domain."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Certificate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "certificate_verification_dns_record": "CertificateVerificationDNSRecord",
    }

    certificate_arn: str | None = None
    certificate_type: str | None = None
    certificate_verification_dns_record: str | None = None


@dataclass
class CertificateSettings(PropertyType):
    certificate_type: str | None = None
    custom_certificate_arn: str | None = None


@dataclass
class SubDomainSetting(PropertyType):
    branch_name: str | None = None
    prefix: str | None = None
