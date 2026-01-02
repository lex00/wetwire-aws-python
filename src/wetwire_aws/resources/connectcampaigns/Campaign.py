"""PropertyTypes for AWS::ConnectCampaigns::Campaign."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AgentlessDialerConfig(PropertyType):
    dialing_capacity: float | None = None


@dataclass
class AnswerMachineDetectionConfig(PropertyType):
    enable_answer_machine_detection: bool | None = None
    await_answer_machine_prompt: bool | None = None


@dataclass
class DialerConfig(PropertyType):
    agentless_dialer_config: AgentlessDialerConfig | None = None
    predictive_dialer_config: PredictiveDialerConfig | None = None
    progressive_dialer_config: ProgressiveDialerConfig | None = None


@dataclass
class OutboundCallConfig(PropertyType):
    connect_contact_flow_arn: str | None = None
    answer_machine_detection_config: AnswerMachineDetectionConfig | None = None
    connect_queue_arn: str | None = None
    connect_source_phone_number: str | None = None


@dataclass
class PredictiveDialerConfig(PropertyType):
    bandwidth_allocation: float | None = None
    dialing_capacity: float | None = None


@dataclass
class ProgressiveDialerConfig(PropertyType):
    bandwidth_allocation: float | None = None
    dialing_capacity: float | None = None
