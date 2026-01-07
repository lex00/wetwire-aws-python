"""PropertyTypes for AWS::DataSync::Task."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Deleted(PropertyType):
    report_level: DslValue[str] | None = None


@dataclass
class Destination(PropertyType):
    s3: DslValue[TaskReportConfigDestinationS3] | None = None


@dataclass
class FilterRule(PropertyType):
    filter_type: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class ManifestConfig(PropertyType):
    source: DslValue[Source] | None = None
    action: DslValue[str] | None = None
    format: DslValue[str] | None = None


@dataclass
class ManifestConfigSourceS3(PropertyType):
    bucket_access_role_arn: DslValue[str] | None = None
    manifest_object_path: DslValue[str] | None = None
    manifest_object_version_id: DslValue[str] | None = None
    s3_bucket_arn: DslValue[str] | None = None


@dataclass
class Options(PropertyType):
    atime: DslValue[str] | None = None
    bytes_per_second: DslValue[int] | None = None
    gid: DslValue[str] | None = None
    log_level: DslValue[str] | None = None
    mtime: DslValue[str] | None = None
    object_tags: DslValue[str] | None = None
    overwrite_mode: DslValue[str] | None = None
    posix_permissions: DslValue[str] | None = None
    preserve_deleted_files: DslValue[str] | None = None
    preserve_devices: DslValue[str] | None = None
    security_descriptor_copy_flags: DslValue[str] | None = None
    task_queueing: DslValue[str] | None = None
    transfer_mode: DslValue[str] | None = None
    uid: DslValue[str] | None = None
    verify_mode: DslValue[str] | None = None


@dataclass
class Overrides(PropertyType):
    deleted: DslValue[Deleted] | None = None
    skipped: DslValue[Skipped] | None = None
    transferred: DslValue[Transferred] | None = None
    verified: DslValue[Verified] | None = None


@dataclass
class Skipped(PropertyType):
    report_level: DslValue[str] | None = None


@dataclass
class Source(PropertyType):
    s3: DslValue[ManifestConfigSourceS3] | None = None


@dataclass
class TaskReportConfig(PropertyType):
    destination: DslValue[Destination] | None = None
    output_type: DslValue[str] | None = None
    object_version_ids: DslValue[str] | None = None
    overrides: DslValue[Overrides] | None = None
    report_level: DslValue[str] | None = None


@dataclass
class TaskReportConfigDestinationS3(PropertyType):
    bucket_access_role_arn: DslValue[str] | None = None
    s3_bucket_arn: DslValue[str] | None = None
    subdirectory: DslValue[str] | None = None


@dataclass
class TaskSchedule(PropertyType):
    schedule_expression: DslValue[str] | None = None
    status: DslValue[str] | None = None


@dataclass
class Transferred(PropertyType):
    report_level: DslValue[str] | None = None


@dataclass
class Verified(PropertyType):
    report_level: DslValue[str] | None = None
