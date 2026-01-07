"""PropertyTypes for AWS::OSIS::Pipeline."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BufferOptions(PropertyType):
    persistent_buffer_enabled: DslValue[bool] | None = None


@dataclass
class CloudWatchLogDestination(PropertyType):
    log_group: DslValue[str] | None = None


@dataclass
class EncryptionAtRestOptions(PropertyType):
    kms_key_arn: DslValue[str] | None = None


@dataclass
class LogPublishingOptions(PropertyType):
    cloud_watch_log_destination: DslValue[CloudWatchLogDestination] | None = None
    is_logging_enabled: DslValue[bool] | None = None


@dataclass
class ResourcePolicy(PropertyType):
    policy: DslValue[dict[str, Any]] | None = None


@dataclass
class VpcAttachmentOptions(PropertyType):
    attach_to_vpc: DslValue[bool] | None = None
    cidr_block: DslValue[str] | None = None


@dataclass
class VpcEndpoint(PropertyType):
    vpc_endpoint_id: DslValue[str] | None = None
    vpc_id: DslValue[str] | None = None
    vpc_options: DslValue[VpcOptions] | None = None


@dataclass
class VpcOptions(PropertyType):
    subnet_ids: list[DslValue[str]] = field(default_factory=list)
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    vpc_attachment_options: DslValue[VpcAttachmentOptions] | None = None
    vpc_endpoint_management: DslValue[str] | None = None
