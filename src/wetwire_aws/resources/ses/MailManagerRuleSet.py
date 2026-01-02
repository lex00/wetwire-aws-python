"""PropertyTypes for AWS::SES::MailManagerRuleSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AddHeaderAction(PropertyType):
    header_name: str | None = None
    header_value: str | None = None


@dataclass
class Analysis(PropertyType):
    analyzer: str | None = None
    result_field: str | None = None


@dataclass
class ArchiveAction(PropertyType):
    target_archive: str | None = None
    action_failure_policy: str | None = None


@dataclass
class DeliverToMailboxAction(PropertyType):
    mailbox_arn: str | None = None
    role_arn: str | None = None
    action_failure_policy: str | None = None


@dataclass
class DeliverToQBusinessAction(PropertyType):
    application_id: str | None = None
    index_id: str | None = None
    role_arn: str | None = None
    action_failure_policy: str | None = None


@dataclass
class RelayAction(PropertyType):
    relay: str | None = None
    action_failure_policy: str | None = None
    mail_from: str | None = None


@dataclass
class ReplaceRecipientAction(PropertyType):
    replace_with: list[String] = field(default_factory=list)


@dataclass
class Rule(PropertyType):
    actions: list[RuleAction] = field(default_factory=list)
    conditions: list[RuleCondition] = field(default_factory=list)
    name: str | None = None
    unless: list[RuleCondition] = field(default_factory=list)


@dataclass
class RuleAction(PropertyType):
    add_header: AddHeaderAction | None = None
    archive: ArchiveAction | None = None
    deliver_to_mailbox: DeliverToMailboxAction | None = None
    deliver_to_q_business: DeliverToQBusinessAction | None = None
    drop: dict[str, Any] | None = None
    publish_to_sns: SnsAction | None = None
    relay: RelayAction | None = None
    replace_recipient: ReplaceRecipientAction | None = None
    send: SendAction | None = None
    write_to_s3: S3Action | None = None


@dataclass
class RuleBooleanExpression(PropertyType):
    evaluate: RuleBooleanToEvaluate | None = None
    operator: str | None = None


@dataclass
class RuleBooleanToEvaluate(PropertyType):
    analysis: Analysis | None = None
    attribute: str | None = None
    is_in_address_list: RuleIsInAddressList | None = None


@dataclass
class RuleCondition(PropertyType):
    boolean_expression: RuleBooleanExpression | None = None
    dmarc_expression: RuleDmarcExpression | None = None
    ip_expression: RuleIpExpression | None = None
    number_expression: RuleNumberExpression | None = None
    string_expression: RuleStringExpression | None = None
    verdict_expression: RuleVerdictExpression | None = None


@dataclass
class RuleDmarcExpression(PropertyType):
    operator: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class RuleIpExpression(PropertyType):
    evaluate: RuleIpToEvaluate | None = None
    operator: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class RuleIpToEvaluate(PropertyType):
    attribute: str | None = None


@dataclass
class RuleIsInAddressList(PropertyType):
    address_lists: list[String] = field(default_factory=list)
    attribute: str | None = None


@dataclass
class RuleNumberExpression(PropertyType):
    evaluate: RuleNumberToEvaluate | None = None
    operator: str | None = None
    value: float | None = None


@dataclass
class RuleNumberToEvaluate(PropertyType):
    attribute: str | None = None


@dataclass
class RuleStringExpression(PropertyType):
    evaluate: RuleStringToEvaluate | None = None
    operator: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class RuleStringToEvaluate(PropertyType):
    analysis: Analysis | None = None
    attribute: str | None = None
    mime_header_attribute: str | None = None


@dataclass
class RuleVerdictExpression(PropertyType):
    evaluate: RuleVerdictToEvaluate | None = None
    operator: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class RuleVerdictToEvaluate(PropertyType):
    analysis: Analysis | None = None
    attribute: str | None = None


@dataclass
class S3Action(PropertyType):
    role_arn: str | None = None
    s3_bucket: str | None = None
    action_failure_policy: str | None = None
    s3_prefix: str | None = None
    s3_sse_kms_key_id: str | None = None


@dataclass
class SendAction(PropertyType):
    role_arn: str | None = None
    action_failure_policy: str | None = None


@dataclass
class SnsAction(PropertyType):
    role_arn: str | None = None
    topic_arn: str | None = None
    action_failure_policy: str | None = None
    encoding: str | None = None
    payload_type: str | None = None
