"""PropertyTypes for AWS::RTBFabric::Link."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Action(PropertyType):
    header_tag: DslValue[HeaderTagAction] | None = None
    no_bid: DslValue[NoBidAction] | None = None


@dataclass
class ApplicationLogs(PropertyType):
    link_application_log_sampling: DslValue[LinkApplicationLogSampling] | None = None


@dataclass
class Filter(PropertyType):
    criteria: list[DslValue[FilterCriterion]] = field(default_factory=list)


@dataclass
class FilterCriterion(PropertyType):
    path: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class HeaderTagAction(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class LinkApplicationLogSampling(PropertyType):
    error_log: DslValue[float] | None = None
    filter_log: DslValue[float] | None = None


@dataclass
class LinkAttributes(PropertyType):
    customer_provided_id: DslValue[str] | None = None
    responder_error_masking: list[DslValue[ResponderErrorMaskingForHttpCode]] = field(
        default_factory=list
    )


@dataclass
class LinkLogSettings(PropertyType):
    application_logs: DslValue[ApplicationLogs] | None = None


@dataclass
class ModuleConfiguration(PropertyType):
    name: DslValue[str] | None = None
    depends_on: list[DslValue[str]] = field(default_factory=list)
    module_parameters: DslValue[ModuleParameters] | None = None
    version: DslValue[str] | None = None


@dataclass
class ModuleParameters(PropertyType):
    no_bid: DslValue[NoBidModuleParameters] | None = None
    open_rtb_attribute: DslValue[OpenRtbAttributeModuleParameters] | None = None


@dataclass
class NoBidAction(PropertyType):
    no_bid_reason_code: DslValue[int] | None = None


@dataclass
class NoBidModuleParameters(PropertyType):
    pass_through_percentage: DslValue[float] | None = None
    reason: DslValue[str] | None = None
    reason_code: DslValue[int] | None = None


@dataclass
class OpenRtbAttributeModuleParameters(PropertyType):
    action: DslValue[Action] | None = None
    filter_configuration: list[DslValue[Filter]] = field(default_factory=list)
    filter_type: DslValue[str] | None = None
    holdback_percentage: DslValue[float] | None = None


@dataclass
class ResponderErrorMaskingForHttpCode(PropertyType):
    action: DslValue[str] | None = None
    http_code: DslValue[str] | None = None
    logging_types: list[DslValue[str]] = field(default_factory=list)
    response_logging_percentage: DslValue[float] | None = None
