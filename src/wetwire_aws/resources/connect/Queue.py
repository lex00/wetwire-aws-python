"""PropertyTypes for AWS::Connect::Queue."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class OutboundCallerConfig(PropertyType):
    outbound_caller_id_name: DslValue[str] | None = None
    outbound_caller_id_number_arn: DslValue[str] | None = None
    outbound_flow_arn: DslValue[str] | None = None


@dataclass
class OutboundEmailConfig(PropertyType):
    outbound_email_address_id: DslValue[str] | None = None
