"""PropertyTypes for AWS::CloudFront::TrustStore."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CaCertificatesBundleS3Location(PropertyType):
    bucket: DslValue[str] | None = None
    key: DslValue[str] | None = None
    region: DslValue[str] | None = None
    version: DslValue[str] | None = None


@dataclass
class CaCertificatesBundleSource(PropertyType):
    ca_certificates_bundle_s3_location: (
        DslValue[CaCertificatesBundleS3Location] | None
    ) = None
