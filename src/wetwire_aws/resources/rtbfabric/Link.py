"""PropertyTypes for AWS::RTBFabric::Link."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Action(PropertyType):
    header_tag: HeaderTagAction | None = None
    no_bid: NoBidAction | None = None


@dataclass
class ApplicationLogs(PropertyType):
    link_application_log_sampling: LinkApplicationLogSampling | None = None


@dataclass
class Filter(PropertyType):
    criteria: list[FilterCriterion] = field(default_factory=list)


@dataclass
class FilterCriterion(PropertyType):
    path: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class HeaderTagAction(PropertyType):
    name: str | None = None
    value: str | None = None


@dataclass
class LinkApplicationLogSampling(PropertyType):
    error_log: float | None = None
    filter_log: float | None = None


@dataclass
class LinkAttributes(PropertyType):
    customer_provided_id: str | None = None
    responder_error_masking: list[ResponderErrorMaskingForHttpCode] = field(
        default_factory=list
    )


@dataclass
class LinkLogSettings(PropertyType):
    application_logs: ApplicationLogs | None = None


@dataclass
class ModuleConfiguration(PropertyType):
    name: str | None = None
    depends_on: list[String] = field(default_factory=list)
    module_parameters: ModuleParameters | None = None
    version: str | None = None


@dataclass
class ModuleParameters(PropertyType):
    no_bid: NoBidModuleParameters | None = None
    open_rtb_attribute: OpenRtbAttributeModuleParameters | None = None


@dataclass
class NoBidAction(PropertyType):
    no_bid_reason_code: int | None = None


@dataclass
class NoBidModuleParameters(PropertyType):
    pass_through_percentage: float | None = None
    reason: str | None = None
    reason_code: int | None = None


@dataclass
class OpenRtbAttributeModuleParameters(PropertyType):
    action: Action | None = None
    filter_configuration: list[Filter] = field(default_factory=list)
    filter_type: str | None = None
    holdback_percentage: float | None = None


@dataclass
class ResponderErrorMaskingForHttpCode(PropertyType):
    action: str | None = None
    http_code: str | None = None
    logging_types: list[String] = field(default_factory=list)
    response_logging_percentage: float | None = None
