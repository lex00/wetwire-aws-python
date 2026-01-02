"""PropertyTypes for AWS::ApiGateway::RestApi."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EndpointConfiguration(PropertyType):
    ip_address_type: str | None = None
    types: list[String] = field(default_factory=list)
    vpc_endpoint_ids: list[String] = field(default_factory=list)


@dataclass
class S3Location(PropertyType):
    bucket: str | None = None
    e_tag: str | None = None
    key: str | None = None
    version: str | None = None
