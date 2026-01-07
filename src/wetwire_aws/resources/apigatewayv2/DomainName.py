"""PropertyTypes for AWS::ApiGatewayV2::DomainName."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DomainNameConfiguration(PropertyType):
    certificate_arn: DslValue[str] | None = None
    certificate_name: DslValue[str] | None = None
    endpoint_type: DslValue[str] | None = None
    ip_address_type: DslValue[str] | None = None
    ownership_verification_certificate_arn: DslValue[str] | None = None
    security_policy: DslValue[str] | None = None


@dataclass
class MutualTlsAuthentication(PropertyType):
    truststore_uri: DslValue[str] | None = None
    truststore_version: DslValue[str] | None = None
