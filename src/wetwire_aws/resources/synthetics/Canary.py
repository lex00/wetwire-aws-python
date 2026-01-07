"""PropertyTypes for AWS::Synthetics::Canary."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ArtifactConfig(PropertyType):
    s3_encryption: DslValue[S3Encryption] | None = None


@dataclass
class BaseScreenshot(PropertyType):
    screenshot_name: DslValue[str] | None = None
    ignore_coordinates: list[DslValue[str]] = field(default_factory=list)


@dataclass
class BrowserConfig(PropertyType):
    browser_type: DslValue[str] | None = None


@dataclass
class Code(PropertyType):
    blueprint_types: list[DslValue[str]] = field(default_factory=list)
    dependencies: list[DslValue[Dependency]] = field(default_factory=list)
    handler: DslValue[str] | None = None
    s3_bucket: DslValue[str] | None = None
    s3_key: DslValue[str] | None = None
    s3_object_version: DslValue[str] | None = None
    script: DslValue[str] | None = None
    source_location_arn: DslValue[str] | None = None


@dataclass
class Dependency(PropertyType):
    reference: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class RetryConfig(PropertyType):
    max_retries: DslValue[int] | None = None


@dataclass
class RunConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "memory_in_mb": "MemoryInMB",
    }

    active_tracing: DslValue[bool] | None = None
    environment_variables: dict[str, DslValue[str]] = field(default_factory=dict)
    ephemeral_storage: DslValue[int] | None = None
    memory_in_mb: DslValue[int] | None = None
    timeout_in_seconds: DslValue[int] | None = None


@dataclass
class S3Encryption(PropertyType):
    encryption_mode: DslValue[str] | None = None
    kms_key_arn: DslValue[str] | None = None


@dataclass
class Schedule(PropertyType):
    expression: DslValue[str] | None = None
    duration_in_seconds: DslValue[str] | None = None
    retry_config: DslValue[RetryConfig] | None = None


@dataclass
class VPCConfig(PropertyType):
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnet_ids: list[DslValue[str]] = field(default_factory=list)
    ipv6_allowed_for_dual_stack: DslValue[bool] | None = None
    vpc_id: DslValue[str] | None = None


@dataclass
class VisualReference(PropertyType):
    base_canary_run_id: DslValue[str] | None = None
    base_screenshots: list[DslValue[BaseScreenshot]] = field(default_factory=list)
    browser_type: DslValue[str] | None = None
