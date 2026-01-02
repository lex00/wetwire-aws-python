"""PropertyTypes for AWS::IoT::TopicRuleDestination."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class HttpUrlDestinationSummary(PropertyType):
    confirmation_url: str | None = None


@dataclass
class VpcDestinationProperties(PropertyType):
    role_arn: str | None = None
    security_groups: list[String] = field(default_factory=list)
    subnet_ids: list[String] = field(default_factory=list)
    vpc_id: str | None = None
