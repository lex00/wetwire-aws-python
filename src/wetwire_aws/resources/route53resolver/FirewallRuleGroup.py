"""PropertyTypes for AWS::Route53Resolver::FirewallRuleGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class FirewallRule(PropertyType):
    action: DslValue[str] | None = None
    priority: DslValue[int] | None = None
    block_override_dns_type: DslValue[str] | None = None
    block_override_domain: DslValue[str] | None = None
    block_override_ttl: DslValue[int] | None = None
    block_response: DslValue[str] | None = None
    confidence_threshold: DslValue[str] | None = None
    dns_threat_protection: DslValue[str] | None = None
    firewall_domain_list_id: DslValue[str] | None = None
    firewall_domain_redirection_action: DslValue[str] | None = None
    firewall_threat_protection_id: DslValue[str] | None = None
    qtype: DslValue[str] | None = None
