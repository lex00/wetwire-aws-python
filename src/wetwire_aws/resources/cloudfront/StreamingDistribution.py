"""PropertyTypes for AWS::CloudFront::StreamingDistribution."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Logging(PropertyType):
    bucket: DslValue[str] | None = None
    enabled: DslValue[bool] | None = None
    prefix: DslValue[str] | None = None


@dataclass
class S3Origin(PropertyType):
    domain_name: DslValue[str] | None = None
    origin_access_identity: DslValue[str] | None = None


@dataclass
class StreamingDistributionConfig(PropertyType):
    comment: DslValue[str] | None = None
    enabled: DslValue[bool] | None = None
    s3_origin: DslValue[S3Origin] | None = None
    trusted_signers: DslValue[TrustedSigners] | None = None
    aliases: list[DslValue[str]] = field(default_factory=list)
    logging: DslValue[Logging] | None = None
    price_class: DslValue[str] | None = None


@dataclass
class TrustedSigners(PropertyType):
    enabled: DslValue[bool] | None = None
    aws_account_numbers: list[DslValue[str]] = field(default_factory=list)
