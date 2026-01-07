"""PropertyTypes for AWS::MPA::ApprovalTeam."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ApprovalStrategy(PropertyType):
    mof_n: DslValue[MofNApprovalStrategy] | None = None


@dataclass
class Approver(PropertyType):
    primary_identity_id: DslValue[str] | None = None
    primary_identity_source_arn: DslValue[str] | None = None
    approver_id: DslValue[str] | None = None
    primary_identity_status: DslValue[str] | None = None
    response_time: DslValue[str] | None = None


@dataclass
class MofNApprovalStrategy(PropertyType):
    min_approvals_required: DslValue[int] | None = None


@dataclass
class Policy(PropertyType):
    policy_arn: DslValue[str] | None = None
