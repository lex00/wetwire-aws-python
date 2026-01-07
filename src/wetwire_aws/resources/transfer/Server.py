"""PropertyTypes for AWS::Transfer::Server."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EndpointDetails(PropertyType):
    address_allocation_ids: list[DslValue[str]] = field(default_factory=list)
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnet_ids: list[DslValue[str]] = field(default_factory=list)
    vpc_endpoint_id: DslValue[str] | None = None
    vpc_id: DslValue[str] | None = None


@dataclass
class IdentityProviderDetails(PropertyType):
    directory_id: DslValue[str] | None = None
    function: DslValue[str] | None = None
    invocation_role: DslValue[str] | None = None
    sftp_authentication_methods: DslValue[str] | None = None
    url: DslValue[str] | None = None


@dataclass
class ProtocolDetails(PropertyType):
    as2_transports: list[DslValue[str]] = field(default_factory=list)
    passive_ip: DslValue[str] | None = None
    set_stat_option: DslValue[str] | None = None
    tls_session_resumption_mode: DslValue[str] | None = None


@dataclass
class S3StorageOptions(PropertyType):
    directory_listing_optimization: DslValue[str] | None = None


@dataclass
class WorkflowDetail(PropertyType):
    execution_role: DslValue[str] | None = None
    workflow_id: DslValue[str] | None = None


@dataclass
class WorkflowDetails(PropertyType):
    on_partial_upload: list[DslValue[WorkflowDetail]] = field(default_factory=list)
    on_upload: list[DslValue[WorkflowDetail]] = field(default_factory=list)
