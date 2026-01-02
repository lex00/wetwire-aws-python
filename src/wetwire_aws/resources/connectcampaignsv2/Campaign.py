"""PropertyTypes for AWS::ConnectCampaignsV2::Campaign."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AnswerMachineDetectionConfig(PropertyType):
    enable_answer_machine_detection: bool | None = None
    await_answer_machine_prompt: bool | None = None


@dataclass
class ChannelSubtypeConfig(PropertyType):
    email: EmailChannelSubtypeConfig | None = None
    sms: SmsChannelSubtypeConfig | None = None
    telephony: TelephonyChannelSubtypeConfig | None = None
    whats_app: WhatsAppChannelSubtypeConfig | None = None


@dataclass
class CommunicationLimit(PropertyType):
    frequency: int | None = None
    max_count_per_recipient: int | None = None
    unit: str | None = None


@dataclass
class CommunicationLimits(PropertyType):
    communication_limit_list: list[CommunicationLimit] = field(default_factory=list)


@dataclass
class CommunicationLimitsConfig(PropertyType):
    all_channels_subtypes: CommunicationLimits | None = None
    instance_limits_handling: str | None = None


@dataclass
class CommunicationTimeConfig(PropertyType):
    local_time_zone_config: LocalTimeZoneConfig | None = None
    email: TimeWindow | None = None
    sms: TimeWindow | None = None
    telephony: TimeWindow | None = None
    whats_app: TimeWindow | None = None


@dataclass
class DailyHour(PropertyType):
    key: str | None = None
    value: list[TimeRange] = field(default_factory=list)


@dataclass
class EmailChannelSubtypeConfig(PropertyType):
    default_outbound_config: EmailOutboundConfig | None = None
    outbound_mode: EmailOutboundMode | None = None
    capacity: float | None = None


@dataclass
class EmailOutboundConfig(PropertyType):
    connect_source_email_address: str | None = None
    wisdom_template_arn: str | None = None
    source_email_address_display_name: str | None = None


@dataclass
class EmailOutboundMode(PropertyType):
    agentless_config: dict[str, Any] | None = None


@dataclass
class EventTrigger(PropertyType):
    customer_profiles_domain_arn: str | None = None


@dataclass
class LocalTimeZoneConfig(PropertyType):
    default_time_zone: str | None = None
    local_time_zone_detection: list[String] = field(default_factory=list)


@dataclass
class OpenHours(PropertyType):
    daily_hours: list[DailyHour] = field(default_factory=list)


@dataclass
class PredictiveConfig(PropertyType):
    bandwidth_allocation: float | None = None


@dataclass
class PreviewConfig(PropertyType):
    bandwidth_allocation: float | None = None
    timeout_config: TimeoutConfig | None = None
    agent_actions: list[String] = field(default_factory=list)


@dataclass
class ProgressiveConfig(PropertyType):
    bandwidth_allocation: float | None = None


@dataclass
class RestrictedPeriod(PropertyType):
    end_date: str | None = None
    start_date: str | None = None
    name: str | None = None


@dataclass
class RestrictedPeriods(PropertyType):
    restricted_period_list: list[RestrictedPeriod] = field(default_factory=list)


@dataclass
class Schedule(PropertyType):
    end_time: str | None = None
    start_time: str | None = None
    refresh_frequency: str | None = None


@dataclass
class SmsChannelSubtypeConfig(PropertyType):
    default_outbound_config: SmsOutboundConfig | None = None
    outbound_mode: SmsOutboundMode | None = None
    capacity: float | None = None


@dataclass
class SmsOutboundConfig(PropertyType):
    connect_source_phone_number_arn: str | None = None
    wisdom_template_arn: str | None = None


@dataclass
class SmsOutboundMode(PropertyType):
    agentless_config: dict[str, Any] | None = None


@dataclass
class Source(PropertyType):
    customer_profiles_segment_arn: str | None = None
    event_trigger: EventTrigger | None = None


@dataclass
class TelephonyChannelSubtypeConfig(PropertyType):
    default_outbound_config: TelephonyOutboundConfig | None = None
    outbound_mode: TelephonyOutboundMode | None = None
    capacity: float | None = None
    connect_queue_id: str | None = None


@dataclass
class TelephonyOutboundConfig(PropertyType):
    connect_contact_flow_id: str | None = None
    answer_machine_detection_config: AnswerMachineDetectionConfig | None = None
    connect_source_phone_number: str | None = None
    ring_timeout: int | None = None


@dataclass
class TelephonyOutboundMode(PropertyType):
    agentless_config: dict[str, Any] | None = None
    predictive_config: PredictiveConfig | None = None
    preview_config: PreviewConfig | None = None
    progressive_config: ProgressiveConfig | None = None


@dataclass
class TimeRange(PropertyType):
    end_time: str | None = None
    start_time: str | None = None


@dataclass
class TimeWindow(PropertyType):
    open_hours: OpenHours | None = None
    restricted_periods: RestrictedPeriods | None = None


@dataclass
class TimeoutConfig(PropertyType):
    duration_in_seconds: int | None = None


@dataclass
class WhatsAppChannelSubtypeConfig(PropertyType):
    default_outbound_config: WhatsAppOutboundConfig | None = None
    outbound_mode: WhatsAppOutboundMode | None = None
    capacity: float | None = None


@dataclass
class WhatsAppOutboundConfig(PropertyType):
    connect_source_phone_number_arn: str | None = None
    wisdom_template_arn: str | None = None


@dataclass
class WhatsAppOutboundMode(PropertyType):
    agentless_config: dict[str, Any] | None = None
