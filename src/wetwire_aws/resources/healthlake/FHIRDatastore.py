"""PropertyTypes for AWS::HealthLake::FHIRDatastore."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CreatedAt(PropertyType):
    nanos: int | None = None
    seconds: str | None = None


@dataclass
class IdentityProviderConfiguration(PropertyType):
    authorization_strategy: str | None = None
    fine_grained_authorization_enabled: bool | None = None
    idp_lambda_arn: str | None = None
    metadata: str | None = None


@dataclass
class KmsEncryptionConfig(PropertyType):
    cmk_type: str | None = None
    kms_key_id: str | None = None


@dataclass
class PreloadDataConfig(PropertyType):
    preload_data_type: str | None = None


@dataclass
class SseConfiguration(PropertyType):
    kms_encryption_config: KmsEncryptionConfig | None = None
