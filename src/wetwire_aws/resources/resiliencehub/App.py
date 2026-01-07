"""PropertyTypes for AWS::ResilienceHub::App."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EventSubscription(PropertyType):
    event_type: DslValue[str] | None = None
    name: DslValue[str] | None = None
    sns_topic_arn: DslValue[str] | None = None


@dataclass
class PermissionModel(PropertyType):
    type_: DslValue[str] | None = None
    cross_account_role_arns: list[DslValue[str]] = field(default_factory=list)
    invoker_role_name: DslValue[str] | None = None


@dataclass
class PhysicalResourceId(PropertyType):
    identifier: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    aws_account_id: DslValue[str] | None = None
    aws_region: DslValue[str] | None = None


@dataclass
class ResourceMapping(PropertyType):
    mapping_type: DslValue[str] | None = None
    physical_resource_id: DslValue[PhysicalResourceId] | None = None
    eks_source_name: DslValue[str] | None = None
    logical_stack_name: DslValue[str] | None = None
    resource_name: DslValue[str] | None = None
    terraform_source_name: DslValue[str] | None = None
