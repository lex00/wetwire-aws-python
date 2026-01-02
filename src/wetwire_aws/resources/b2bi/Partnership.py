"""PropertyTypes for AWS::B2BI::Partnership."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CapabilityOptions(PropertyType):
    inbound_edi: InboundEdiOptions | None = None
    outbound_edi: OutboundEdiOptions | None = None


@dataclass
class InboundEdiOptions(PropertyType):
    x12: X12InboundEdiOptions | None = None


@dataclass
class OutboundEdiOptions(PropertyType):
    x12: X12Envelope | None = None


@dataclass
class WrapOptions(PropertyType):
    line_length: float | None = None
    line_terminator: str | None = None
    wrap_by: str | None = None


@dataclass
class X12AcknowledgmentOptions(PropertyType):
    functional_acknowledgment: str | None = None
    technical_acknowledgment: str | None = None


@dataclass
class X12ControlNumbers(PropertyType):
    starting_functional_group_control_number: float | None = None
    starting_interchange_control_number: float | None = None
    starting_transaction_set_control_number: float | None = None


@dataclass
class X12Delimiters(PropertyType):
    component_separator: str | None = None
    data_element_separator: str | None = None
    segment_terminator: str | None = None


@dataclass
class X12Envelope(PropertyType):
    common: X12OutboundEdiHeaders | None = None
    wrap_options: WrapOptions | None = None


@dataclass
class X12FunctionalGroupHeaders(PropertyType):
    application_receiver_code: str | None = None
    application_sender_code: str | None = None
    responsible_agency_code: str | None = None


@dataclass
class X12InboundEdiOptions(PropertyType):
    acknowledgment_options: X12AcknowledgmentOptions | None = None


@dataclass
class X12InterchangeControlHeaders(PropertyType):
    acknowledgment_requested_code: str | None = None
    receiver_id: str | None = None
    receiver_id_qualifier: str | None = None
    repetition_separator: str | None = None
    sender_id: str | None = None
    sender_id_qualifier: str | None = None
    usage_indicator_code: str | None = None


@dataclass
class X12OutboundEdiHeaders(PropertyType):
    control_numbers: X12ControlNumbers | None = None
    delimiters: X12Delimiters | None = None
    functional_group_headers: X12FunctionalGroupHeaders | None = None
    gs05_time_format: str | None = None
    interchange_control_headers: X12InterchangeControlHeaders | None = None
    validate_edi: bool | None = None
