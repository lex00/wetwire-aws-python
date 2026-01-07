"""PropertyTypes for AWS::SES::ReceiptRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Action(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sns_action": "SNSAction",
    }

    add_header_action: DslValue[AddHeaderAction] | None = None
    bounce_action: DslValue[BounceAction] | None = None
    connect_action: DslValue[ConnectAction] | None = None
    lambda_action: DslValue[LambdaAction] | None = None
    s3_action: DslValue[S3Action] | None = None
    sns_action: DslValue[SNSAction] | None = None
    stop_action: DslValue[StopAction] | None = None
    workmail_action: DslValue[WorkmailAction] | None = None


@dataclass
class AddHeaderAction(PropertyType):
    header_name: DslValue[str] | None = None
    header_value: DslValue[str] | None = None


@dataclass
class BounceAction(PropertyType):
    message: DslValue[str] | None = None
    sender: DslValue[str] | None = None
    smtp_reply_code: DslValue[str] | None = None
    status_code: DslValue[str] | None = None
    topic_arn: DslValue[str] | None = None


@dataclass
class ConnectAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "iam_role_arn": "IAMRoleARN",
        "instance_arn": "InstanceARN",
    }

    iam_role_arn: DslValue[str] | None = None
    instance_arn: DslValue[str] | None = None


@dataclass
class LambdaAction(PropertyType):
    function_arn: DslValue[str] | None = None
    invocation_type: DslValue[str] | None = None
    topic_arn: DslValue[str] | None = None


@dataclass
class Rule(PropertyType):
    actions: list[DslValue[Action]] = field(default_factory=list)
    enabled: DslValue[bool] | None = None
    name: DslValue[str] | None = None
    recipients: list[DslValue[str]] = field(default_factory=list)
    scan_enabled: DslValue[bool] | None = None
    tls_policy: DslValue[str] | None = None


@dataclass
class S3Action(PropertyType):
    bucket_name: DslValue[str] | None = None
    iam_role_arn: DslValue[str] | None = None
    kms_key_arn: DslValue[str] | None = None
    object_key_prefix: DslValue[str] | None = None
    topic_arn: DslValue[str] | None = None


@dataclass
class SNSAction(PropertyType):
    encoding: DslValue[str] | None = None
    topic_arn: DslValue[str] | None = None


@dataclass
class StopAction(PropertyType):
    scope: DslValue[str] | None = None
    topic_arn: DslValue[str] | None = None


@dataclass
class WorkmailAction(PropertyType):
    organization_arn: DslValue[str] | None = None
    topic_arn: DslValue[str] | None = None
