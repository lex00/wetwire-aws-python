"""PropertyTypes for AWS::ApiGateway::RestApi."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EndpointConfiguration(PropertyType):
    ip_address_type: DslValue[str] | None = None
    types: list[DslValue[str]] = field(default_factory=list)
    vpc_endpoint_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class S3Location(PropertyType):
    bucket: DslValue[str] | None = None
    e_tag: DslValue[str] | None = None
    key: DslValue[str] | None = None
    version: DslValue[str] | None = None
