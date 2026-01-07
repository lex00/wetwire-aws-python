"""PropertyTypes for AWS::Route53RecoveryReadiness::ResourceSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DNSTargetResource(PropertyType):
    domain_name: DslValue[str] | None = None
    hosted_zone_arn: DslValue[str] | None = None
    record_set_id: DslValue[str] | None = None
    record_type: DslValue[str] | None = None
    target_resource: DslValue[TargetResource] | None = None


@dataclass
class NLBResource(PropertyType):
    arn: DslValue[str] | None = None


@dataclass
class R53ResourceRecord(PropertyType):
    domain_name: DslValue[str] | None = None
    record_set_id: DslValue[str] | None = None


@dataclass
class Resource(PropertyType):
    component_id: DslValue[str] | None = None
    dns_target_resource: DslValue[DNSTargetResource] | None = None
    readiness_scopes: list[DslValue[str]] = field(default_factory=list)
    resource_arn: DslValue[str] | None = None


@dataclass
class TargetResource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "nlb_resource": "NLBResource",
    }

    nlb_resource: DslValue[NLBResource] | None = None
    r53_resource: DslValue[R53ResourceRecord] | None = None
