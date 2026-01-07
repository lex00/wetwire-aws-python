"""PropertyTypes for AWS::Amplify::Domain."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Certificate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "certificate_verification_dns_record": "CertificateVerificationDNSRecord",
    }

    certificate_arn: DslValue[str] | None = None
    certificate_type: DslValue[str] | None = None
    certificate_verification_dns_record: DslValue[str] | None = None


@dataclass
class CertificateSettings(PropertyType):
    certificate_type: DslValue[str] | None = None
    custom_certificate_arn: DslValue[str] | None = None


@dataclass
class SubDomainSetting(PropertyType):
    branch_name: DslValue[str] | None = None
    prefix: DslValue[str] | None = None
