"""PropertyTypes for AWS::Route53RecoveryReadiness::ResourceSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DNSTargetResource(PropertyType):
    domain_name: str | None = None
    hosted_zone_arn: str | None = None
    record_set_id: str | None = None
    record_type: str | None = None
    target_resource: TargetResource | None = None


@dataclass
class NLBResource(PropertyType):
    arn: str | None = None


@dataclass
class R53ResourceRecord(PropertyType):
    domain_name: str | None = None
    record_set_id: str | None = None


@dataclass
class Resource(PropertyType):
    component_id: str | None = None
    dns_target_resource: DNSTargetResource | None = None
    readiness_scopes: list[String] = field(default_factory=list)
    resource_arn: str | None = None


@dataclass
class TargetResource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "nlb_resource": "NLBResource",
    }

    nlb_resource: NLBResource | None = None
    r53_resource: R53ResourceRecord | None = None
