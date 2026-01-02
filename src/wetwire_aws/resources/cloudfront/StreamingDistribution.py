"""PropertyTypes for AWS::CloudFront::StreamingDistribution."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Logging(PropertyType):
    bucket: str | None = None
    enabled: bool | None = None
    prefix: str | None = None


@dataclass
class S3Origin(PropertyType):
    domain_name: str | None = None
    origin_access_identity: str | None = None


@dataclass
class StreamingDistributionConfig(PropertyType):
    comment: str | None = None
    enabled: bool | None = None
    s3_origin: S3Origin | None = None
    trusted_signers: TrustedSigners | None = None
    aliases: list[String] = field(default_factory=list)
    logging: Logging | None = None
    price_class: str | None = None


@dataclass
class TrustedSigners(PropertyType):
    enabled: bool | None = None
    aws_account_numbers: list[String] = field(default_factory=list)
