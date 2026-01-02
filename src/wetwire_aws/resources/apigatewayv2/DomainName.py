"""PropertyTypes for AWS::ApiGatewayV2::DomainName."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DomainNameConfiguration(PropertyType):
    certificate_arn: str | None = None
    certificate_name: str | None = None
    endpoint_type: str | None = None
    ip_address_type: str | None = None
    ownership_verification_certificate_arn: str | None = None
    security_policy: str | None = None


@dataclass
class MutualTlsAuthentication(PropertyType):
    truststore_uri: str | None = None
    truststore_version: str | None = None
