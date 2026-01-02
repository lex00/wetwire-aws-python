"""PropertyTypes for AWS::Config::OrganizationConfigRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class OrganizationCustomPolicyRuleMetadata(PropertyType):
    policy_text: str | None = None
    runtime: str | None = None
    debug_log_delivery_accounts: list[String] = field(default_factory=list)
    description: str | None = None
    input_parameters: str | None = None
    maximum_execution_frequency: str | None = None
    organization_config_rule_trigger_types: list[String] = field(default_factory=list)
    resource_id_scope: str | None = None
    resource_types_scope: list[String] = field(default_factory=list)
    tag_key_scope: str | None = None
    tag_value_scope: str | None = None


@dataclass
class OrganizationCustomRuleMetadata(PropertyType):
    lambda_function_arn: str | None = None
    organization_config_rule_trigger_types: list[String] = field(default_factory=list)
    description: str | None = None
    input_parameters: str | None = None
    maximum_execution_frequency: str | None = None
    resource_id_scope: str | None = None
    resource_types_scope: list[String] = field(default_factory=list)
    tag_key_scope: str | None = None
    tag_value_scope: str | None = None


@dataclass
class OrganizationManagedRuleMetadata(PropertyType):
    rule_identifier: str | None = None
    description: str | None = None
    input_parameters: str | None = None
    maximum_execution_frequency: str | None = None
    resource_id_scope: str | None = None
    resource_types_scope: list[String] = field(default_factory=list)
    tag_key_scope: str | None = None
    tag_value_scope: str | None = None
