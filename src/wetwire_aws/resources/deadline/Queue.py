"""PropertyTypes for AWS::Deadline::Queue."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class JobAttachmentSettings(PropertyType):
    root_prefix: str | None = None
    s3_bucket_name: str | None = None


@dataclass
class JobRunAsUser(PropertyType):
    run_as: str | None = None
    posix: PosixUser | None = None
    windows: WindowsUser | None = None


@dataclass
class PosixUser(PropertyType):
    group: str | None = None
    user: str | None = None


@dataclass
class WindowsUser(PropertyType):
    password_arn: str | None = None
    user: str | None = None
