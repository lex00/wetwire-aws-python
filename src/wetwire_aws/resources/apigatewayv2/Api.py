"""PropertyTypes for AWS::ApiGatewayV2::Api."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BodyS3Location(PropertyType):
    bucket: DslValue[str] | None = None
    etag: DslValue[str] | None = None
    key: DslValue[str] | None = None
    version: DslValue[str] | None = None


@dataclass
class Cors(PropertyType):
    allow_credentials: DslValue[bool] | None = None
    allow_headers: list[DslValue[str]] = field(default_factory=list)
    allow_methods: list[DslValue[str]] = field(default_factory=list)
    allow_origins: list[DslValue[str]] = field(default_factory=list)
    expose_headers: list[DslValue[str]] = field(default_factory=list)
    max_age: DslValue[int] | None = None
