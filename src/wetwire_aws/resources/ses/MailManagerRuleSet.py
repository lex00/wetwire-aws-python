"""PropertyTypes for AWS::SES::MailManagerRuleSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AddHeaderAction(PropertyType):
    header_name: DslValue[str] | None = None
    header_value: DslValue[str] | None = None


@dataclass
class Analysis(PropertyType):
    analyzer: DslValue[str] | None = None
    result_field: DslValue[str] | None = None


@dataclass
class ArchiveAction(PropertyType):
    target_archive: DslValue[str] | None = None
    action_failure_policy: DslValue[str] | None = None


@dataclass
class DeliverToMailboxAction(PropertyType):
    mailbox_arn: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    action_failure_policy: DslValue[str] | None = None


@dataclass
class DeliverToQBusinessAction(PropertyType):
    application_id: DslValue[str] | None = None
    index_id: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    action_failure_policy: DslValue[str] | None = None


@dataclass
class RelayAction(PropertyType):
    relay: DslValue[str] | None = None
    action_failure_policy: DslValue[str] | None = None
    mail_from: DslValue[str] | None = None


@dataclass
class ReplaceRecipientAction(PropertyType):
    replace_with: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Rule(PropertyType):
    actions: list[DslValue[RuleAction]] = field(default_factory=list)
    conditions: list[DslValue[RuleCondition]] = field(default_factory=list)
    name: DslValue[str] | None = None
    unless: list[DslValue[RuleCondition]] = field(default_factory=list)


@dataclass
class RuleAction(PropertyType):
    add_header: DslValue[AddHeaderAction] | None = None
    archive: DslValue[ArchiveAction] | None = None
    deliver_to_mailbox: DslValue[DeliverToMailboxAction] | None = None
    deliver_to_q_business: DslValue[DeliverToQBusinessAction] | None = None
    drop: DslValue[dict[str, Any]] | None = None
    publish_to_sns: DslValue[SnsAction] | None = None
    relay: DslValue[RelayAction] | None = None
    replace_recipient: DslValue[ReplaceRecipientAction] | None = None
    send: DslValue[SendAction] | None = None
    write_to_s3: DslValue[S3Action] | None = None


@dataclass
class RuleBooleanExpression(PropertyType):
    evaluate: DslValue[RuleBooleanToEvaluate] | None = None
    operator: DslValue[str] | None = None


@dataclass
class RuleBooleanToEvaluate(PropertyType):
    analysis: DslValue[Analysis] | None = None
    attribute: DslValue[str] | None = None
    is_in_address_list: DslValue[RuleIsInAddressList] | None = None


@dataclass
class RuleCondition(PropertyType):
    boolean_expression: DslValue[RuleBooleanExpression] | None = None
    dmarc_expression: DslValue[RuleDmarcExpression] | None = None
    ip_expression: DslValue[RuleIpExpression] | None = None
    number_expression: DslValue[RuleNumberExpression] | None = None
    string_expression: DslValue[RuleStringExpression] | None = None
    verdict_expression: DslValue[RuleVerdictExpression] | None = None


@dataclass
class RuleDmarcExpression(PropertyType):
    operator: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class RuleIpExpression(PropertyType):
    evaluate: DslValue[RuleIpToEvaluate] | None = None
    operator: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class RuleIpToEvaluate(PropertyType):
    attribute: DslValue[str] | None = None


@dataclass
class RuleIsInAddressList(PropertyType):
    address_lists: list[DslValue[str]] = field(default_factory=list)
    attribute: DslValue[str] | None = None


@dataclass
class RuleNumberExpression(PropertyType):
    evaluate: DslValue[RuleNumberToEvaluate] | None = None
    operator: DslValue[str] | None = None
    value: DslValue[float] | None = None


@dataclass
class RuleNumberToEvaluate(PropertyType):
    attribute: DslValue[str] | None = None


@dataclass
class RuleStringExpression(PropertyType):
    evaluate: DslValue[RuleStringToEvaluate] | None = None
    operator: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class RuleStringToEvaluate(PropertyType):
    analysis: DslValue[Analysis] | None = None
    attribute: DslValue[str] | None = None
    mime_header_attribute: DslValue[str] | None = None


@dataclass
class RuleVerdictExpression(PropertyType):
    evaluate: DslValue[RuleVerdictToEvaluate] | None = None
    operator: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class RuleVerdictToEvaluate(PropertyType):
    analysis: DslValue[Analysis] | None = None
    attribute: DslValue[str] | None = None


@dataclass
class S3Action(PropertyType):
    role_arn: DslValue[str] | None = None
    s3_bucket: DslValue[str] | None = None
    action_failure_policy: DslValue[str] | None = None
    s3_prefix: DslValue[str] | None = None
    s3_sse_kms_key_id: DslValue[str] | None = None


@dataclass
class SendAction(PropertyType):
    role_arn: DslValue[str] | None = None
    action_failure_policy: DslValue[str] | None = None


@dataclass
class SnsAction(PropertyType):
    role_arn: DslValue[str] | None = None
    topic_arn: DslValue[str] | None = None
    action_failure_policy: DslValue[str] | None = None
    encoding: DslValue[str] | None = None
    payload_type: DslValue[str] | None = None
