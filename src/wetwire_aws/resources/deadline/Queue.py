"""PropertyTypes for AWS::Deadline::Queue."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class JobAttachmentSettings(PropertyType):
    root_prefix: DslValue[str] | None = None
    s3_bucket_name: DslValue[str] | None = None


@dataclass
class JobRunAsUser(PropertyType):
    run_as: DslValue[str] | None = None
    posix: DslValue[PosixUser] | None = None
    windows: DslValue[WindowsUser] | None = None


@dataclass
class PosixUser(PropertyType):
    group: DslValue[str] | None = None
    user: DslValue[str] | None = None


@dataclass
class WindowsUser(PropertyType):
    password_arn: DslValue[str] | None = None
    user: DslValue[str] | None = None
