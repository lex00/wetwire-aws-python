"""PropertyTypes for AWS::Serverless::Api."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ApiAuth(PropertyType):
    api_key_required: bool | None = None
    authorizers: dict[str, ApiAuthorizer] = field(default_factory=dict)
    default_authorizer: str | None = None


@dataclass
class ApiAuthorizer(PropertyType):
    authorization_scopes: list[str] = field(default_factory=list)
    function_arn: str | None = None
    function_payload_type: str | None = None
    identity: dict[str, Any] | None = None
    user_pool_arn: str | None = None


@dataclass
class EndpointConfiguration(PropertyType):
    type_: str | None = None
    vpc_endpoint_ids: list[str] = field(default_factory=list)
