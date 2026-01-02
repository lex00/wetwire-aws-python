"""PropertyTypes for AWS::Route53Resolver::FirewallRuleGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class FirewallRule(PropertyType):
    action: str | None = None
    priority: int | None = None
    block_override_dns_type: str | None = None
    block_override_domain: str | None = None
    block_override_ttl: int | None = None
    block_response: str | None = None
    confidence_threshold: str | None = None
    dns_threat_protection: str | None = None
    firewall_domain_list_id: str | None = None
    firewall_domain_redirection_action: str | None = None
    firewall_threat_protection_id: str | None = None
    qtype: str | None = None
