"""PropertyTypes for AWS::Config::ConfigRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Compliance(PropertyType):
    type_: str | None = None


@dataclass
class CustomPolicyDetails(PropertyType):
    enable_debug_log_delivery: bool | None = None
    policy_runtime: str | None = None
    policy_text: str | None = None


@dataclass
class EvaluationModeConfiguration(PropertyType):
    mode: str | None = None


@dataclass
class Scope(PropertyType):
    compliance_resource_id: str | None = None
    compliance_resource_types: list[String] = field(default_factory=list)
    tag_key: str | None = None
    tag_value: str | None = None


@dataclass
class Source(PropertyType):
    owner: str | None = None
    custom_policy_details: CustomPolicyDetails | None = None
    source_details: list[SourceDetail] = field(default_factory=list)
    source_identifier: str | None = None


@dataclass
class SourceDetail(PropertyType):
    event_source: str | None = None
    message_type: str | None = None
    maximum_execution_frequency: str | None = None
