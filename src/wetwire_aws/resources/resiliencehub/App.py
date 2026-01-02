"""PropertyTypes for AWS::ResilienceHub::App."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EventSubscription(PropertyType):
    event_type: str | None = None
    name: str | None = None
    sns_topic_arn: str | None = None


@dataclass
class PermissionModel(PropertyType):
    type_: str | None = None
    cross_account_role_arns: list[String] = field(default_factory=list)
    invoker_role_name: str | None = None


@dataclass
class PhysicalResourceId(PropertyType):
    identifier: str | None = None
    type_: str | None = None
    aws_account_id: str | None = None
    aws_region: str | None = None


@dataclass
class ResourceMapping(PropertyType):
    mapping_type: str | None = None
    physical_resource_id: PhysicalResourceId | None = None
    eks_source_name: str | None = None
    logical_stack_name: str | None = None
    resource_name: str | None = None
    terraform_source_name: str | None = None
