"""PropertyTypes for AWS::RTBFabric::InboundExternalLink."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ApplicationLogs(PropertyType):
    link_application_log_sampling: DslValue[LinkApplicationLogSampling] | None = None


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
class ResponderErrorMaskingForHttpCode(PropertyType):
    action: DslValue[str] | None = None
    http_code: DslValue[str] | None = None
    logging_types: list[DslValue[str]] = field(default_factory=list)
    response_logging_percentage: DslValue[float] | None = None
