"""PropertyTypes for AWS::EC2::VPCEndpoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DnsOptionsSpecification(PropertyType):
    dns_record_ip_type: DslValue[str] | None = None
    private_dns_only_for_inbound_resolver_endpoint: DslValue[str] | None = None
    private_dns_preference: DslValue[str] | None = None
    private_dns_specified_domains: list[DslValue[str]] = field(default_factory=list)
