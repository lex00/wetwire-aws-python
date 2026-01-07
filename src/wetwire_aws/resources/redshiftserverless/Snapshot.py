"""PropertyTypes for AWS::RedshiftServerless::Snapshot."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Snapshot(PropertyType):
    admin_username: DslValue[str] | None = None
    kms_key_id: DslValue[str] | None = None
    namespace_arn: DslValue[str] | None = None
    namespace_name: DslValue[str] | None = None
    owner_account: DslValue[str] | None = None
    retention_period: DslValue[int] | None = None
    snapshot_arn: DslValue[str] | None = None
    snapshot_create_time: DslValue[str] | None = None
    snapshot_name: DslValue[str] | None = None
    status: DslValue[str] | None = None
