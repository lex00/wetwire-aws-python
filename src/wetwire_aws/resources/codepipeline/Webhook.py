"""PropertyTypes for AWS::CodePipeline::Webhook."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class WebhookAuthConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "allowed_ip_range": "AllowedIPRange",
    }

    allowed_ip_range: str | None = None
    secret_token: str | None = None


@dataclass
class WebhookFilterRule(PropertyType):
    json_path: str | None = None
    match_equals: str | None = None
