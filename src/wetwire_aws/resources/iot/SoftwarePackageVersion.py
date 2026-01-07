"""PropertyTypes for AWS::IoT::SoftwarePackageVersion."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class PackageVersionArtifact(PropertyType):
    s3_location: DslValue[S3Location] | None = None


@dataclass
class S3Location(PropertyType):
    bucket: DslValue[str] | None = None
    key: DslValue[str] | None = None
    version: DslValue[str] | None = None


@dataclass
class Sbom(PropertyType):
    s3_location: DslValue[S3Location] | None = None
