"""PropertyTypes for AWS::MediaTailor::SourceLocation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AccessConfiguration(PropertyType):
    access_type: str | None = None
    secrets_manager_access_token_configuration: (
        SecretsManagerAccessTokenConfiguration | None
    ) = None


@dataclass
class DefaultSegmentDeliveryConfiguration(PropertyType):
    base_url: str | None = None


@dataclass
class HttpConfiguration(PropertyType):
    base_url: str | None = None


@dataclass
class SecretsManagerAccessTokenConfiguration(PropertyType):
    header_name: str | None = None
    secret_arn: str | None = None
    secret_string_key: str | None = None


@dataclass
class SegmentDeliveryConfiguration(PropertyType):
    base_url: str | None = None
    name: str | None = None
