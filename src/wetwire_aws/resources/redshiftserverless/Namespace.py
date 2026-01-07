"""PropertyTypes for AWS::RedshiftServerless::Namespace."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Namespace(PropertyType):
    admin_password_secret_arn: DslValue[str] | None = None
    admin_password_secret_kms_key_id: DslValue[str] | None = None
    admin_username: DslValue[str] | None = None
    creation_date: DslValue[str] | None = None
    db_name: DslValue[str] | None = None
    default_iam_role_arn: DslValue[str] | None = None
    iam_roles: list[DslValue[str]] = field(default_factory=list)
    kms_key_id: DslValue[str] | None = None
    log_exports: list[DslValue[str]] = field(default_factory=list)
    namespace_arn: DslValue[str] | None = None
    namespace_id: DslValue[str] | None = None
    namespace_name: DslValue[str] | None = None
    status: DslValue[str] | None = None


@dataclass
class SnapshotCopyConfiguration(PropertyType):
    destination_region: DslValue[str] | None = None
    destination_kms_key_id: DslValue[str] | None = None
    snapshot_retention_period: DslValue[int] | None = None
