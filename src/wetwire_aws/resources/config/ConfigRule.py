"""PropertyTypes for AWS::Config::ConfigRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Compliance(PropertyType):
    type_: DslValue[str] | None = None


@dataclass
class CustomPolicyDetails(PropertyType):
    enable_debug_log_delivery: DslValue[bool] | None = None
    policy_runtime: DslValue[str] | None = None
    policy_text: DslValue[str] | None = None


@dataclass
class EvaluationModeConfiguration(PropertyType):
    mode: DslValue[str] | None = None


@dataclass
class Scope(PropertyType):
    compliance_resource_id: DslValue[str] | None = None
    compliance_resource_types: list[DslValue[str]] = field(default_factory=list)
    tag_key: DslValue[str] | None = None
    tag_value: DslValue[str] | None = None


@dataclass
class Source(PropertyType):
    owner: DslValue[str] | None = None
    custom_policy_details: DslValue[CustomPolicyDetails] | None = None
    source_details: list[DslValue[SourceDetail]] = field(default_factory=list)
    source_identifier: DslValue[str] | None = None


@dataclass
class SourceDetail(PropertyType):
    event_source: DslValue[str] | None = None
    message_type: DslValue[str] | None = None
    maximum_execution_frequency: DslValue[str] | None = None
