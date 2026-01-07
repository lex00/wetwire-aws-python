"""PropertyTypes for AWS::B2BI::Partnership."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CapabilityOptions(PropertyType):
    inbound_edi: DslValue[InboundEdiOptions] | None = None
    outbound_edi: DslValue[OutboundEdiOptions] | None = None


@dataclass
class InboundEdiOptions(PropertyType):
    x12: DslValue[X12InboundEdiOptions] | None = None


@dataclass
class OutboundEdiOptions(PropertyType):
    x12: DslValue[X12Envelope] | None = None


@dataclass
class WrapOptions(PropertyType):
    line_length: DslValue[float] | None = None
    line_terminator: DslValue[str] | None = None
    wrap_by: DslValue[str] | None = None


@dataclass
class X12AcknowledgmentOptions(PropertyType):
    functional_acknowledgment: DslValue[str] | None = None
    technical_acknowledgment: DslValue[str] | None = None


@dataclass
class X12ControlNumbers(PropertyType):
    starting_functional_group_control_number: DslValue[float] | None = None
    starting_interchange_control_number: DslValue[float] | None = None
    starting_transaction_set_control_number: DslValue[float] | None = None


@dataclass
class X12Delimiters(PropertyType):
    component_separator: DslValue[str] | None = None
    data_element_separator: DslValue[str] | None = None
    segment_terminator: DslValue[str] | None = None


@dataclass
class X12Envelope(PropertyType):
    common: DslValue[X12OutboundEdiHeaders] | None = None
    wrap_options: DslValue[WrapOptions] | None = None


@dataclass
class X12FunctionalGroupHeaders(PropertyType):
    application_receiver_code: DslValue[str] | None = None
    application_sender_code: DslValue[str] | None = None
    responsible_agency_code: DslValue[str] | None = None


@dataclass
class X12InboundEdiOptions(PropertyType):
    acknowledgment_options: DslValue[X12AcknowledgmentOptions] | None = None


@dataclass
class X12InterchangeControlHeaders(PropertyType):
    acknowledgment_requested_code: DslValue[str] | None = None
    receiver_id: DslValue[str] | None = None
    receiver_id_qualifier: DslValue[str] | None = None
    repetition_separator: DslValue[str] | None = None
    sender_id: DslValue[str] | None = None
    sender_id_qualifier: DslValue[str] | None = None
    usage_indicator_code: DslValue[str] | None = None


@dataclass
class X12OutboundEdiHeaders(PropertyType):
    control_numbers: DslValue[X12ControlNumbers] | None = None
    delimiters: DslValue[X12Delimiters] | None = None
    functional_group_headers: DslValue[X12FunctionalGroupHeaders] | None = None
    gs05_time_format: DslValue[str] | None = None
    interchange_control_headers: DslValue[X12InterchangeControlHeaders] | None = None
    validate_edi: DslValue[bool] | None = None
