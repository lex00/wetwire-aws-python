"""PropertyTypes for AWS::Serverless::Api."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ApiAuth(PropertyType):
    api_key_required: DslValue[bool] | None = None
    authorizers: dict[str, DslValue[ApiAuthorizer]] = field(default_factory=dict)
    default_authorizer: DslValue[str] | None = None


@dataclass
class ApiAuthorizer(PropertyType):
    authorization_scopes: list[DslValue[str]] = field(default_factory=list)
    function_arn: DslValue[str] | None = None
    function_payload_type: DslValue[str] | None = None
    identity: DslValue[dict[str, Any]] | None = None
    user_pool_arn: DslValue[str] | None = None


@dataclass
class EndpointConfiguration(PropertyType):
    type_: DslValue[str] | None = None
    vpc_endpoint_ids: list[DslValue[str]] = field(default_factory=list)
