"""PropertyTypes for AWS::DataSync::Task."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Deleted(PropertyType):
    report_level: str | None = None


@dataclass
class Destination(PropertyType):
    s3: TaskReportConfigDestinationS3 | None = None


@dataclass
class FilterRule(PropertyType):
    filter_type: str | None = None
    value: str | None = None


@dataclass
class ManifestConfig(PropertyType):
    source: Source | None = None
    action: str | None = None
    format: str | None = None


@dataclass
class ManifestConfigSourceS3(PropertyType):
    bucket_access_role_arn: str | None = None
    manifest_object_path: str | None = None
    manifest_object_version_id: str | None = None
    s3_bucket_arn: str | None = None


@dataclass
class Options(PropertyType):
    atime: str | None = None
    bytes_per_second: int | None = None
    gid: str | None = None
    log_level: str | None = None
    mtime: str | None = None
    object_tags: str | None = None
    overwrite_mode: str | None = None
    posix_permissions: str | None = None
    preserve_deleted_files: str | None = None
    preserve_devices: str | None = None
    security_descriptor_copy_flags: str | None = None
    task_queueing: str | None = None
    transfer_mode: str | None = None
    uid: str | None = None
    verify_mode: str | None = None


@dataclass
class Overrides(PropertyType):
    deleted: Deleted | None = None
    skipped: Skipped | None = None
    transferred: Transferred | None = None
    verified: Verified | None = None


@dataclass
class Skipped(PropertyType):
    report_level: str | None = None


@dataclass
class Source(PropertyType):
    s3: ManifestConfigSourceS3 | None = None


@dataclass
class TaskReportConfig(PropertyType):
    destination: Destination | None = None
    output_type: str | None = None
    object_version_ids: str | None = None
    overrides: Overrides | None = None
    report_level: str | None = None


@dataclass
class TaskReportConfigDestinationS3(PropertyType):
    bucket_access_role_arn: str | None = None
    s3_bucket_arn: str | None = None
    subdirectory: str | None = None


@dataclass
class TaskSchedule(PropertyType):
    schedule_expression: str | None = None
    status: str | None = None


@dataclass
class Transferred(PropertyType):
    report_level: str | None = None


@dataclass
class Verified(PropertyType):
    report_level: str | None = None
