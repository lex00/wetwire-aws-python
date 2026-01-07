"""PropertyTypes for AWS::CodePipeline::Webhook."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class WebhookAuthConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "allowed_ip_range": "AllowedIPRange",
    }

    allowed_ip_range: DslValue[str] | None = None
    secret_token: DslValue[str] | None = None


@dataclass
class WebhookFilterRule(PropertyType):
    json_path: DslValue[str] | None = None
    match_equals: DslValue[str] | None = None
