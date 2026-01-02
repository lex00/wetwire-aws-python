"""PropertyTypes for AWS::RedshiftServerless::Namespace."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Namespace(PropertyType):
    admin_password_secret_arn: str | None = None
    admin_password_secret_kms_key_id: str | None = None
    admin_username: str | None = None
    creation_date: str | None = None
    db_name: str | None = None
    default_iam_role_arn: str | None = None
    iam_roles: list[String] = field(default_factory=list)
    kms_key_id: str | None = None
    log_exports: list[String] = field(default_factory=list)
    namespace_arn: str | None = None
    namespace_id: str | None = None
    namespace_name: str | None = None
    status: str | None = None


@dataclass
class SnapshotCopyConfiguration(PropertyType):
    destination_region: str | None = None
    destination_kms_key_id: str | None = None
    snapshot_retention_period: int | None = None
