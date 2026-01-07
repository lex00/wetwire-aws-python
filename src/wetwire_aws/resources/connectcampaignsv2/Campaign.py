"""PropertyTypes for AWS::ConnectCampaignsV2::Campaign."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AnswerMachineDetectionConfig(PropertyType):
    enable_answer_machine_detection: DslValue[bool] | None = None
    await_answer_machine_prompt: DslValue[bool] | None = None


@dataclass
class ChannelSubtypeConfig(PropertyType):
    email: DslValue[EmailChannelSubtypeConfig] | None = None
    sms: DslValue[SmsChannelSubtypeConfig] | None = None
    telephony: DslValue[TelephonyChannelSubtypeConfig] | None = None
    whats_app: DslValue[WhatsAppChannelSubtypeConfig] | None = None


@dataclass
class CommunicationLimit(PropertyType):
    frequency: DslValue[int] | None = None
    max_count_per_recipient: DslValue[int] | None = None
    unit: DslValue[str] | None = None


@dataclass
class CommunicationLimits(PropertyType):
    communication_limit_list: list[DslValue[CommunicationLimit]] = field(
        default_factory=list
    )


@dataclass
class CommunicationLimitsConfig(PropertyType):
    all_channels_subtypes: DslValue[CommunicationLimits] | None = None
    instance_limits_handling: DslValue[str] | None = None


@dataclass
class CommunicationTimeConfig(PropertyType):
    local_time_zone_config: DslValue[LocalTimeZoneConfig] | None = None
    email: DslValue[TimeWindow] | None = None
    sms: DslValue[TimeWindow] | None = None
    telephony: DslValue[TimeWindow] | None = None
    whats_app: DslValue[TimeWindow] | None = None


@dataclass
class DailyHour(PropertyType):
    key: DslValue[str] | None = None
    value: list[DslValue[TimeRange]] = field(default_factory=list)


@dataclass
class EmailChannelSubtypeConfig(PropertyType):
    default_outbound_config: DslValue[EmailOutboundConfig] | None = None
    outbound_mode: DslValue[EmailOutboundMode] | None = None
    capacity: DslValue[float] | None = None


@dataclass
class EmailOutboundConfig(PropertyType):
    connect_source_email_address: DslValue[str] | None = None
    wisdom_template_arn: DslValue[str] | None = None
    source_email_address_display_name: DslValue[str] | None = None


@dataclass
class EmailOutboundMode(PropertyType):
    agentless_config: DslValue[dict[str, Any]] | None = None


@dataclass
class EventTrigger(PropertyType):
    customer_profiles_domain_arn: DslValue[str] | None = None


@dataclass
class LocalTimeZoneConfig(PropertyType):
    default_time_zone: DslValue[str] | None = None
    local_time_zone_detection: list[DslValue[str]] = field(default_factory=list)


@dataclass
class OpenHours(PropertyType):
    daily_hours: list[DslValue[DailyHour]] = field(default_factory=list)


@dataclass
class PredictiveConfig(PropertyType):
    bandwidth_allocation: DslValue[float] | None = None


@dataclass
class PreviewConfig(PropertyType):
    bandwidth_allocation: DslValue[float] | None = None
    timeout_config: DslValue[TimeoutConfig] | None = None
    agent_actions: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ProgressiveConfig(PropertyType):
    bandwidth_allocation: DslValue[float] | None = None


@dataclass
class RestrictedPeriod(PropertyType):
    end_date: DslValue[str] | None = None
    start_date: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class RestrictedPeriods(PropertyType):
    restricted_period_list: list[DslValue[RestrictedPeriod]] = field(
        default_factory=list
    )


@dataclass
class Schedule(PropertyType):
    end_time: DslValue[str] | None = None
    start_time: DslValue[str] | None = None
    refresh_frequency: DslValue[str] | None = None


@dataclass
class SmsChannelSubtypeConfig(PropertyType):
    default_outbound_config: DslValue[SmsOutboundConfig] | None = None
    outbound_mode: DslValue[SmsOutboundMode] | None = None
    capacity: DslValue[float] | None = None


@dataclass
class SmsOutboundConfig(PropertyType):
    connect_source_phone_number_arn: DslValue[str] | None = None
    wisdom_template_arn: DslValue[str] | None = None


@dataclass
class SmsOutboundMode(PropertyType):
    agentless_config: DslValue[dict[str, Any]] | None = None


@dataclass
class Source(PropertyType):
    customer_profiles_segment_arn: DslValue[str] | None = None
    event_trigger: DslValue[EventTrigger] | None = None


@dataclass
class TelephonyChannelSubtypeConfig(PropertyType):
    default_outbound_config: DslValue[TelephonyOutboundConfig] | None = None
    outbound_mode: DslValue[TelephonyOutboundMode] | None = None
    capacity: DslValue[float] | None = None
    connect_queue_id: DslValue[str] | None = None


@dataclass
class TelephonyOutboundConfig(PropertyType):
    connect_contact_flow_id: DslValue[str] | None = None
    answer_machine_detection_config: DslValue[AnswerMachineDetectionConfig] | None = (
        None
    )
    connect_source_phone_number: DslValue[str] | None = None
    ring_timeout: DslValue[int] | None = None


@dataclass
class TelephonyOutboundMode(PropertyType):
    agentless_config: DslValue[dict[str, Any]] | None = None
    predictive_config: DslValue[PredictiveConfig] | None = None
    preview_config: DslValue[PreviewConfig] | None = None
    progressive_config: DslValue[ProgressiveConfig] | None = None


@dataclass
class TimeRange(PropertyType):
    end_time: DslValue[str] | None = None
    start_time: DslValue[str] | None = None


@dataclass
class TimeWindow(PropertyType):
    open_hours: DslValue[OpenHours] | None = None
    restricted_periods: DslValue[RestrictedPeriods] | None = None


@dataclass
class TimeoutConfig(PropertyType):
    duration_in_seconds: DslValue[int] | None = None


@dataclass
class WhatsAppChannelSubtypeConfig(PropertyType):
    default_outbound_config: DslValue[WhatsAppOutboundConfig] | None = None
    outbound_mode: DslValue[WhatsAppOutboundMode] | None = None
    capacity: DslValue[float] | None = None


@dataclass
class WhatsAppOutboundConfig(PropertyType):
    connect_source_phone_number_arn: DslValue[str] | None = None
    wisdom_template_arn: DslValue[str] | None = None


@dataclass
class WhatsAppOutboundMode(PropertyType):
    agentless_config: DslValue[dict[str, Any]] | None = None
