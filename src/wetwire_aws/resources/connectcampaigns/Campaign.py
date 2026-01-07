"""PropertyTypes for AWS::ConnectCampaigns::Campaign."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AgentlessDialerConfig(PropertyType):
    dialing_capacity: DslValue[float] | None = None


@dataclass
class AnswerMachineDetectionConfig(PropertyType):
    enable_answer_machine_detection: DslValue[bool] | None = None
    await_answer_machine_prompt: DslValue[bool] | None = None


@dataclass
class DialerConfig(PropertyType):
    agentless_dialer_config: DslValue[AgentlessDialerConfig] | None = None
    predictive_dialer_config: DslValue[PredictiveDialerConfig] | None = None
    progressive_dialer_config: DslValue[ProgressiveDialerConfig] | None = None


@dataclass
class OutboundCallConfig(PropertyType):
    connect_contact_flow_arn: DslValue[str] | None = None
    answer_machine_detection_config: DslValue[AnswerMachineDetectionConfig] | None = (
        None
    )
    connect_queue_arn: DslValue[str] | None = None
    connect_source_phone_number: DslValue[str] | None = None


@dataclass
class PredictiveDialerConfig(PropertyType):
    bandwidth_allocation: DslValue[float] | None = None
    dialing_capacity: DslValue[float] | None = None


@dataclass
class ProgressiveDialerConfig(PropertyType):
    bandwidth_allocation: DslValue[float] | None = None
    dialing_capacity: DslValue[float] | None = None
