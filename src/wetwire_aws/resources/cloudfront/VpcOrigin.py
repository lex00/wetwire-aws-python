"""PropertyTypes for AWS::CloudFront::VpcOrigin."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class VpcOriginEndpointConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "http_port": "HTTPPort",
        "https_port": "HTTPSPort",
        "origin_ssl_protocols": "OriginSSLProtocols",
    }

    arn: DslValue[str] | None = None
    name: DslValue[str] | None = None
    http_port: DslValue[int] | None = None
    https_port: DslValue[int] | None = None
    origin_protocol_policy: DslValue[str] | None = None
    origin_ssl_protocols: list[DslValue[str]] = field(default_factory=list)
