"""PropertyTypes for AWS::ApiGatewayV2::Integration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ResponseParameter(PropertyType):
    destination: str | None = None
    source: str | None = None


@dataclass
class ResponseParameterMap(PropertyType):
    response_parameters: list[ResponseParameter] = field(default_factory=list)


@dataclass
class TlsConfig(PropertyType):
    server_name_to_verify: str | None = None
