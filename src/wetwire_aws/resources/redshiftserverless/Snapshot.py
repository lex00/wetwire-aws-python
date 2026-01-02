"""PropertyTypes for AWS::RedshiftServerless::Snapshot."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Snapshot(PropertyType):
    admin_username: str | None = None
    kms_key_id: str | None = None
    namespace_arn: str | None = None
    namespace_name: str | None = None
    owner_account: str | None = None
    retention_period: int | None = None
    snapshot_arn: str | None = None
    snapshot_create_time: str | None = None
    snapshot_name: str | None = None
    status: str | None = None
