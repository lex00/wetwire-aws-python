"""PropertyTypes for AWS::MediaTailor::SourceLocation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AccessConfiguration(PropertyType):
    access_type: DslValue[str] | None = None
    secrets_manager_access_token_configuration: (
        DslValue[SecretsManagerAccessTokenConfiguration] | None
    ) = None


@dataclass
class DefaultSegmentDeliveryConfiguration(PropertyType):
    base_url: DslValue[str] | None = None


@dataclass
class HttpConfiguration(PropertyType):
    base_url: DslValue[str] | None = None


@dataclass
class SecretsManagerAccessTokenConfiguration(PropertyType):
    header_name: DslValue[str] | None = None
    secret_arn: DslValue[str] | None = None
    secret_string_key: DslValue[str] | None = None


@dataclass
class SegmentDeliveryConfiguration(PropertyType):
    base_url: DslValue[str] | None = None
    name: DslValue[str] | None = None
