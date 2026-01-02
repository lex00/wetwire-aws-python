"""PropertyTypes for AWS::Synthetics::Canary."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ArtifactConfig(PropertyType):
    s3_encryption: S3Encryption | None = None


@dataclass
class BaseScreenshot(PropertyType):
    screenshot_name: str | None = None
    ignore_coordinates: list[String] = field(default_factory=list)


@dataclass
class BrowserConfig(PropertyType):
    browser_type: str | None = None


@dataclass
class Code(PropertyType):
    blueprint_types: list[String] = field(default_factory=list)
    dependencies: list[Dependency] = field(default_factory=list)
    handler: str | None = None
    s3_bucket: str | None = None
    s3_key: str | None = None
    s3_object_version: str | None = None
    script: str | None = None
    source_location_arn: str | None = None


@dataclass
class Dependency(PropertyType):
    reference: str | None = None
    type_: str | None = None


@dataclass
class RetryConfig(PropertyType):
    max_retries: int | None = None


@dataclass
class RunConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "memory_in_mb": "MemoryInMB",
    }

    active_tracing: bool | None = None
    environment_variables: dict[str, String] = field(default_factory=dict)
    ephemeral_storage: int | None = None
    memory_in_mb: int | None = None
    timeout_in_seconds: int | None = None


@dataclass
class S3Encryption(PropertyType):
    encryption_mode: str | None = None
    kms_key_arn: str | None = None


@dataclass
class Schedule(PropertyType):
    expression: str | None = None
    duration_in_seconds: str | None = None
    retry_config: RetryConfig | None = None


@dataclass
class VPCConfig(PropertyType):
    security_group_ids: list[String] = field(default_factory=list)
    subnet_ids: list[String] = field(default_factory=list)
    ipv6_allowed_for_dual_stack: bool | None = None
    vpc_id: str | None = None


@dataclass
class VisualReference(PropertyType):
    base_canary_run_id: str | None = None
    base_screenshots: list[BaseScreenshot] = field(default_factory=list)
    browser_type: str | None = None
