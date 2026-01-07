"""PropertyTypes for AWS::CloudFront::DistributionTenant."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Certificate(PropertyType):
    arn: DslValue[str] | None = None


@dataclass
class Customizations(PropertyType):
    certificate: DslValue[Certificate] | None = None
    geo_restrictions: DslValue[GeoRestrictionCustomization] | None = None
    web_acl: DslValue[WebAclCustomization] | None = None


@dataclass
class DomainResult(PropertyType):
    domain: DslValue[str] | None = None
    status: DslValue[str] | None = None


@dataclass
class GeoRestrictionCustomization(PropertyType):
    locations: list[DslValue[str]] = field(default_factory=list)
    restriction_type: DslValue[str] | None = None


@dataclass
class ManagedCertificateRequest(PropertyType):
    certificate_transparency_logging_preference: DslValue[str] | None = None
    primary_domain_name: DslValue[str] | None = None
    validation_token_host: DslValue[str] | None = None


@dataclass
class Parameter(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class WebAclCustomization(PropertyType):
    action: DslValue[str] | None = None
    arn: DslValue[str] | None = None
