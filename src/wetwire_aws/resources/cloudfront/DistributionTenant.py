"""PropertyTypes for AWS::CloudFront::DistributionTenant."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Certificate(PropertyType):
    arn: str | None = None


@dataclass
class Customizations(PropertyType):
    certificate: Certificate | None = None
    geo_restrictions: GeoRestrictionCustomization | None = None
    web_acl: WebAclCustomization | None = None


@dataclass
class DomainResult(PropertyType):
    domain: str | None = None
    status: str | None = None


@dataclass
class GeoRestrictionCustomization(PropertyType):
    locations: list[String] = field(default_factory=list)
    restriction_type: str | None = None


@dataclass
class ManagedCertificateRequest(PropertyType):
    certificate_transparency_logging_preference: str | None = None
    primary_domain_name: str | None = None
    validation_token_host: str | None = None


@dataclass
class Parameter(PropertyType):
    name: str | None = None
    value: str | None = None


@dataclass
class WebAclCustomization(PropertyType):
    action: str | None = None
    arn: str | None = None
