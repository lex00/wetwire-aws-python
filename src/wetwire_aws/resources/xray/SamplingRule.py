"""PropertyTypes for AWS::XRay::SamplingRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class SamplingRule(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "http_method": "HTTPMethod",
        "resource_arn": "ResourceARN",
        "rule_arn": "RuleARN",
        "url_path": "URLPath",
    }

    fixed_rate: DslValue[float] | None = None
    host: DslValue[str] | None = None
    http_method: DslValue[str] | None = None
    priority: DslValue[int] | None = None
    reservoir_size: DslValue[int] | None = None
    resource_arn: DslValue[str] | None = None
    service_name: DslValue[str] | None = None
    service_type: DslValue[str] | None = None
    url_path: DslValue[str] | None = None
    attributes: dict[str, DslValue[str]] = field(default_factory=dict)
    rule_arn: DslValue[str] | None = None
    rule_name: DslValue[str] | None = None
    version: DslValue[int] | None = None
