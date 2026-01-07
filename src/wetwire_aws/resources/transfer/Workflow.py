"""PropertyTypes for AWS::Transfer::Workflow."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CopyStepDetails(PropertyType):
    destination_file_location: DslValue[S3FileLocation] | None = None
    name: DslValue[str] | None = None
    overwrite_existing: DslValue[str] | None = None
    source_file_location: DslValue[str] | None = None


@dataclass
class CustomStepDetails(PropertyType):
    name: DslValue[str] | None = None
    source_file_location: DslValue[str] | None = None
    target: DslValue[str] | None = None
    timeout_seconds: DslValue[int] | None = None


@dataclass
class DecryptStepDetails(PropertyType):
    destination_file_location: DslValue[InputFileLocation] | None = None
    type_: DslValue[str] | None = None
    name: DslValue[str] | None = None
    overwrite_existing: DslValue[str] | None = None
    source_file_location: DslValue[str] | None = None


@dataclass
class DeleteStepDetails(PropertyType):
    name: DslValue[str] | None = None
    source_file_location: DslValue[str] | None = None


@dataclass
class EfsInputFileLocation(PropertyType):
    file_system_id: DslValue[str] | None = None
    path: DslValue[str] | None = None


@dataclass
class InputFileLocation(PropertyType):
    efs_file_location: DslValue[EfsInputFileLocation] | None = None
    s3_file_location: DslValue[S3InputFileLocation] | None = None


@dataclass
class S3FileLocation(PropertyType):
    s3_file_location: DslValue[S3InputFileLocation] | None = None


@dataclass
class S3InputFileLocation(PropertyType):
    bucket: DslValue[str] | None = None
    key: DslValue[str] | None = None


@dataclass
class S3Tag(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class TagStepDetails(PropertyType):
    name: DslValue[str] | None = None
    source_file_location: DslValue[str] | None = None
    tags: list[DslValue[S3Tag]] = field(default_factory=list)


@dataclass
class WorkflowStep(PropertyType):
    copy_step_details: DslValue[CopyStepDetails] | None = None
    custom_step_details: DslValue[CustomStepDetails] | None = None
    decrypt_step_details: DslValue[DecryptStepDetails] | None = None
    delete_step_details: DslValue[DeleteStepDetails] | None = None
    tag_step_details: DslValue[TagStepDetails] | None = None
    type_: DslValue[str] | None = None
