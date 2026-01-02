"""PropertyTypes for AWS::RTBFabric::InboundExternalLink."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ApplicationLogs(PropertyType):
    link_application_log_sampling: LinkApplicationLogSampling | None = None


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
class ResponderErrorMaskingForHttpCode(PropertyType):
    action: str | None = None
    http_code: str | None = None
    logging_types: list[String] = field(default_factory=list)
    response_logging_percentage: float | None = None
