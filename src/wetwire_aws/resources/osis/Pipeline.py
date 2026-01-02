"""PropertyTypes for AWS::OSIS::Pipeline."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BufferOptions(PropertyType):
    persistent_buffer_enabled: bool | None = None


@dataclass
class CloudWatchLogDestination(PropertyType):
    log_group: str | None = None


@dataclass
class EncryptionAtRestOptions(PropertyType):
    kms_key_arn: str | None = None


@dataclass
class LogPublishingOptions(PropertyType):
    cloud_watch_log_destination: CloudWatchLogDestination | None = None
    is_logging_enabled: bool | None = None


@dataclass
class ResourcePolicy(PropertyType):
    policy: dict[str, Any] | None = None


@dataclass
class VpcAttachmentOptions(PropertyType):
    attach_to_vpc: bool | None = None
    cidr_block: str | None = None


@dataclass
class VpcEndpoint(PropertyType):
    vpc_endpoint_id: str | None = None
    vpc_id: str | None = None
    vpc_options: VpcOptions | None = None


@dataclass
class VpcOptions(PropertyType):
    subnet_ids: list[String] = field(default_factory=list)
    security_group_ids: list[String] = field(default_factory=list)
    vpc_attachment_options: VpcAttachmentOptions | None = None
    vpc_endpoint_management: str | None = None
