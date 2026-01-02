"""PropertyTypes for AWS::EC2::VPCEndpoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DnsOptionsSpecification(PropertyType):
    dns_record_ip_type: str | None = None
    private_dns_only_for_inbound_resolver_endpoint: str | None = None
    private_dns_preference: str | None = None
    private_dns_specified_domains: list[String] = field(default_factory=list)
