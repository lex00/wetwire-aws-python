"""PropertyTypes for AWS::ApiGateway::Method."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Integration(PropertyType):
    type_: str | None = None
    cache_key_parameters: list[String] = field(default_factory=list)
    cache_namespace: str | None = None
    connection_id: str | None = None
    connection_type: str | None = None
    content_handling: str | None = None
    credentials: str | None = None
    integration_http_method: str | None = None
    integration_responses: list[IntegrationResponse] = field(default_factory=list)
    integration_target: str | None = None
    passthrough_behavior: str | None = None
    request_parameters: dict[str, String] = field(default_factory=dict)
    request_templates: dict[str, String] = field(default_factory=dict)
    response_transfer_mode: str | None = None
    timeout_in_millis: int | None = None
    uri: str | None = None


@dataclass
class IntegrationResponse(PropertyType):
    status_code: str | None = None
    content_handling: str | None = None
    response_parameters: dict[str, String] = field(default_factory=dict)
    response_templates: dict[str, String] = field(default_factory=dict)
    selection_pattern: str | None = None


@dataclass
class MethodResponse(PropertyType):
    status_code: str | None = None
    response_models: dict[str, String] = field(default_factory=dict)
    response_parameters: dict[str, String] = field(default_factory=dict)
