"""PropertyTypes for AWS::ApiGateway::Method."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Integration(PropertyType):
    type_: DslValue[str] | None = None
    cache_key_parameters: list[DslValue[str]] = field(default_factory=list)
    cache_namespace: DslValue[str] | None = None
    connection_id: DslValue[str] | None = None
    connection_type: DslValue[str] | None = None
    content_handling: DslValue[str] | None = None
    credentials: DslValue[str] | None = None
    integration_http_method: DslValue[str] | None = None
    integration_responses: list[DslValue[IntegrationResponse]] = field(
        default_factory=list
    )
    integration_target: DslValue[str] | None = None
    passthrough_behavior: DslValue[str] | None = None
    request_parameters: dict[str, DslValue[str]] = field(default_factory=dict)
    request_templates: dict[str, DslValue[str]] = field(default_factory=dict)
    response_transfer_mode: DslValue[str] | None = None
    timeout_in_millis: DslValue[int] | None = None
    uri: DslValue[str] | None = None


@dataclass
class IntegrationResponse(PropertyType):
    status_code: DslValue[str] | None = None
    content_handling: DslValue[str] | None = None
    response_parameters: dict[str, DslValue[str]] = field(default_factory=dict)
    response_templates: dict[str, DslValue[str]] = field(default_factory=dict)
    selection_pattern: DslValue[str] | None = None


@dataclass
class MethodResponse(PropertyType):
    status_code: DslValue[str] | None = None
    response_models: dict[str, DslValue[str]] = field(default_factory=dict)
    response_parameters: dict[str, DslValue[str]] = field(default_factory=dict)
