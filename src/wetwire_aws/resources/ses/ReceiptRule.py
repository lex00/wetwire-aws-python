"""PropertyTypes for AWS::SES::ReceiptRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Action(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sns_action": "SNSAction",
    }

    add_header_action: AddHeaderAction | None = None
    bounce_action: BounceAction | None = None
    connect_action: ConnectAction | None = None
    lambda_action: LambdaAction | None = None
    s3_action: S3Action | None = None
    sns_action: SNSAction | None = None
    stop_action: StopAction | None = None
    workmail_action: WorkmailAction | None = None


@dataclass
class AddHeaderAction(PropertyType):
    header_name: str | None = None
    header_value: str | None = None


@dataclass
class BounceAction(PropertyType):
    message: str | None = None
    sender: str | None = None
    smtp_reply_code: str | None = None
    status_code: str | None = None
    topic_arn: str | None = None


@dataclass
class ConnectAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "iam_role_arn": "IAMRoleARN",
        "instance_arn": "InstanceARN",
    }

    iam_role_arn: str | None = None
    instance_arn: str | None = None


@dataclass
class LambdaAction(PropertyType):
    function_arn: str | None = None
    invocation_type: str | None = None
    topic_arn: str | None = None


@dataclass
class Rule(PropertyType):
    actions: list[Action] = field(default_factory=list)
    enabled: bool | None = None
    name: str | None = None
    recipients: list[String] = field(default_factory=list)
    scan_enabled: bool | None = None
    tls_policy: str | None = None


@dataclass
class S3Action(PropertyType):
    bucket_name: str | None = None
    iam_role_arn: str | None = None
    kms_key_arn: str | None = None
    object_key_prefix: str | None = None
    topic_arn: str | None = None


@dataclass
class SNSAction(PropertyType):
    encoding: str | None = None
    topic_arn: str | None = None


@dataclass
class StopAction(PropertyType):
    scope: str | None = None
    topic_arn: str | None = None


@dataclass
class WorkmailAction(PropertyType):
    organization_arn: str | None = None
    topic_arn: str | None = None
