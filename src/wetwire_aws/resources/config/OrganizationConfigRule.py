"""PropertyTypes for AWS::Config::OrganizationConfigRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class OrganizationCustomPolicyRuleMetadata(PropertyType):
    policy_text: DslValue[str] | None = None
    runtime: DslValue[str] | None = None
    debug_log_delivery_accounts: list[DslValue[str]] = field(default_factory=list)
    description: DslValue[str] | None = None
    input_parameters: DslValue[str] | None = None
    maximum_execution_frequency: DslValue[str] | None = None
    organization_config_rule_trigger_types: list[DslValue[str]] = field(
        default_factory=list
    )
    resource_id_scope: DslValue[str] | None = None
    resource_types_scope: list[DslValue[str]] = field(default_factory=list)
    tag_key_scope: DslValue[str] | None = None
    tag_value_scope: DslValue[str] | None = None


@dataclass
class OrganizationCustomRuleMetadata(PropertyType):
    lambda_function_arn: DslValue[str] | None = None
    organization_config_rule_trigger_types: list[DslValue[str]] = field(
        default_factory=list
    )
    description: DslValue[str] | None = None
    input_parameters: DslValue[str] | None = None
    maximum_execution_frequency: DslValue[str] | None = None
    resource_id_scope: DslValue[str] | None = None
    resource_types_scope: list[DslValue[str]] = field(default_factory=list)
    tag_key_scope: DslValue[str] | None = None
    tag_value_scope: DslValue[str] | None = None


@dataclass
class OrganizationManagedRuleMetadata(PropertyType):
    rule_identifier: DslValue[str] | None = None
    description: DslValue[str] | None = None
    input_parameters: DslValue[str] | None = None
    maximum_execution_frequency: DslValue[str] | None = None
    resource_id_scope: DslValue[str] | None = None
    resource_types_scope: list[DslValue[str]] = field(default_factory=list)
    tag_key_scope: DslValue[str] | None = None
    tag_value_scope: DslValue[str] | None = None
