"""PropertyTypes for AWS::AuditManager::Assessment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AWSAccount(PropertyType):
    email_address: DslValue[str] | None = None
    id: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class AWSService(PropertyType):
    service_name: DslValue[str] | None = None


@dataclass
class AssessmentReportsDestination(PropertyType):
    destination: DslValue[str] | None = None
    destination_type: DslValue[str] | None = None


@dataclass
class Delegation(PropertyType):
    assessment_id: DslValue[str] | None = None
    assessment_name: DslValue[str] | None = None
    comment: DslValue[str] | None = None
    control_set_id: DslValue[str] | None = None
    created_by: DslValue[str] | None = None
    creation_time: DslValue[float] | None = None
    id: DslValue[str] | None = None
    last_updated: DslValue[float] | None = None
    role_arn: DslValue[str] | None = None
    role_type: DslValue[str] | None = None
    status: DslValue[str] | None = None


@dataclass
class Role(PropertyType):
    role_arn: DslValue[str] | None = None
    role_type: DslValue[str] | None = None


@dataclass
class Scope(PropertyType):
    aws_accounts: list[DslValue[AWSAccount]] = field(default_factory=list)
    aws_services: list[DslValue[AWSService]] = field(default_factory=list)
