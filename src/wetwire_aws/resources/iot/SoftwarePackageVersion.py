"""PropertyTypes for AWS::IoT::SoftwarePackageVersion."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class PackageVersionArtifact(PropertyType):
    s3_location: S3Location | None = None


@dataclass
class S3Location(PropertyType):
    bucket: str | None = None
    key: str | None = None
    version: str | None = None


@dataclass
class Sbom(PropertyType):
    s3_location: S3Location | None = None
