"""PropertyTypes for AWS::Transfer::Workflow."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CopyStepDetails(PropertyType):
    destination_file_location: S3FileLocation | None = None
    name: str | None = None
    overwrite_existing: str | None = None
    source_file_location: str | None = None


@dataclass
class CustomStepDetails(PropertyType):
    name: str | None = None
    source_file_location: str | None = None
    target: str | None = None
    timeout_seconds: int | None = None


@dataclass
class DecryptStepDetails(PropertyType):
    destination_file_location: InputFileLocation | None = None
    type_: str | None = None
    name: str | None = None
    overwrite_existing: str | None = None
    source_file_location: str | None = None


@dataclass
class DeleteStepDetails(PropertyType):
    name: str | None = None
    source_file_location: str | None = None


@dataclass
class EfsInputFileLocation(PropertyType):
    file_system_id: str | None = None
    path: str | None = None


@dataclass
class InputFileLocation(PropertyType):
    efs_file_location: EfsInputFileLocation | None = None
    s3_file_location: S3InputFileLocation | None = None


@dataclass
class S3FileLocation(PropertyType):
    s3_file_location: S3InputFileLocation | None = None


@dataclass
class S3InputFileLocation(PropertyType):
    bucket: str | None = None
    key: str | None = None


@dataclass
class S3Tag(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class TagStepDetails(PropertyType):
    name: str | None = None
    source_file_location: str | None = None
    tags: list[S3Tag] = field(default_factory=list)


@dataclass
class WorkflowStep(PropertyType):
    copy_step_details: CopyStepDetails | None = None
    custom_step_details: CustomStepDetails | None = None
    decrypt_step_details: DecryptStepDetails | None = None
    delete_step_details: DeleteStepDetails | None = None
    tag_step_details: TagStepDetails | None = None
    type_: str | None = None
