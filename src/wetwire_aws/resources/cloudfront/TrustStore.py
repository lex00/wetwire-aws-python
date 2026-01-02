"""PropertyTypes for AWS::CloudFront::TrustStore."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CaCertificatesBundleS3Location(PropertyType):
    bucket: str | None = None
    key: str | None = None
    region: str | None = None
    version: str | None = None


@dataclass
class CaCertificatesBundleSource(PropertyType):
    ca_certificates_bundle_s3_location: CaCertificatesBundleS3Location | None = None
