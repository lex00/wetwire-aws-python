"""PropertyTypes for AWS::XRay::SamplingRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class SamplingRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "http_method": "HTTPMethod",
        "resource_arn": "ResourceARN",
        "rule_arn": "RuleARN",
        "url_path": "URLPath",
    }

    fixed_rate: float | None = None
    host: str | None = None
    http_method: str | None = None
    priority: int | None = None
    reservoir_size: int | None = None
    resource_arn: str | None = None
    service_name: str | None = None
    service_type: str | None = None
    url_path: str | None = None
    attributes: dict[str, String] = field(default_factory=dict)
    rule_arn: str | None = None
    rule_name: str | None = None
    version: int | None = None
