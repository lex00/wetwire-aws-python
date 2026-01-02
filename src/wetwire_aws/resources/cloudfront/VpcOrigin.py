"""PropertyTypes for AWS::CloudFront::VpcOrigin."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class VpcOriginEndpointConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "http_port": "HTTPPort",
        "https_port": "HTTPSPort",
        "origin_ssl_protocols": "OriginSSLProtocols",
    }

    arn: str | None = None
    name: str | None = None
    http_port: int | None = None
    https_port: int | None = None
    origin_protocol_policy: str | None = None
    origin_ssl_protocols: list[String] = field(default_factory=list)
