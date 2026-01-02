"""PropertyTypes for AWS::Transfer::Server."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EndpointDetails(PropertyType):
    address_allocation_ids: list[String] = field(default_factory=list)
    security_group_ids: list[String] = field(default_factory=list)
    subnet_ids: list[String] = field(default_factory=list)
    vpc_endpoint_id: str | None = None
    vpc_id: str | None = None


@dataclass
class IdentityProviderDetails(PropertyType):
    directory_id: str | None = None
    function: str | None = None
    invocation_role: str | None = None
    sftp_authentication_methods: str | None = None
    url: str | None = None


@dataclass
class ProtocolDetails(PropertyType):
    as2_transports: list[String] = field(default_factory=list)
    passive_ip: str | None = None
    set_stat_option: str | None = None
    tls_session_resumption_mode: str | None = None


@dataclass
class S3StorageOptions(PropertyType):
    directory_listing_optimization: str | None = None


@dataclass
class WorkflowDetail(PropertyType):
    execution_role: str | None = None
    workflow_id: str | None = None


@dataclass
class WorkflowDetails(PropertyType):
    on_partial_upload: list[WorkflowDetail] = field(default_factory=list)
    on_upload: list[WorkflowDetail] = field(default_factory=list)
