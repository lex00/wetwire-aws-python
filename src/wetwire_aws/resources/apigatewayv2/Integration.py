"""PropertyTypes for AWS::ApiGatewayV2::Integration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ResponseParameter(PropertyType):
    destination: DslValue[str] | None = None
    source: DslValue[str] | None = None


@dataclass
class ResponseParameterMap(PropertyType):
    response_parameters: list[DslValue[ResponseParameter]] = field(default_factory=list)


@dataclass
class TlsConfig(PropertyType):
    server_name_to_verify: DslValue[str] | None = None
