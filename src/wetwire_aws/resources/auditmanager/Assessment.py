"""PropertyTypes for AWS::AuditManager::Assessment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AWSAccount(PropertyType):
    email_address: str | None = None
    id: str | None = None
    name: str | None = None


@dataclass
class AWSService(PropertyType):
    service_name: str | None = None


@dataclass
class AssessmentReportsDestination(PropertyType):
    destination: str | None = None
    destination_type: str | None = None


@dataclass
class Delegation(PropertyType):
    assessment_id: str | None = None
    assessment_name: str | None = None
    comment: str | None = None
    control_set_id: str | None = None
    created_by: str | None = None
    creation_time: float | None = None
    id: str | None = None
    last_updated: float | None = None
    role_arn: str | None = None
    role_type: str | None = None
    status: str | None = None


@dataclass
class Role(PropertyType):
    role_arn: str | None = None
    role_type: str | None = None


@dataclass
class Scope(PropertyType):
    aws_accounts: list[AWSAccount] = field(default_factory=list)
    aws_services: list[AWSService] = field(default_factory=list)
