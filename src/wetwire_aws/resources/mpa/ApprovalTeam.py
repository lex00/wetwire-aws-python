"""PropertyTypes for AWS::MPA::ApprovalTeam."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ApprovalStrategy(PropertyType):
    mof_n: MofNApprovalStrategy | None = None


@dataclass
class Approver(PropertyType):
    primary_identity_id: str | None = None
    primary_identity_source_arn: str | None = None
    approver_id: str | None = None
    primary_identity_status: str | None = None
    response_time: str | None = None


@dataclass
class MofNApprovalStrategy(PropertyType):
    min_approvals_required: int | None = None


@dataclass
class Policy(PropertyType):
    policy_arn: str | None = None
