"""PropertyTypes for AWS::HealthLake::FHIRDatastore."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CreatedAt(PropertyType):
    nanos: DslValue[int] | None = None
    seconds: DslValue[str] | None = None


@dataclass
class IdentityProviderConfiguration(PropertyType):
    authorization_strategy: DslValue[str] | None = None
    fine_grained_authorization_enabled: DslValue[bool] | None = None
    idp_lambda_arn: DslValue[str] | None = None
    metadata: DslValue[str] | None = None


@dataclass
class KmsEncryptionConfig(PropertyType):
    cmk_type: DslValue[str] | None = None
    kms_key_id: DslValue[str] | None = None


@dataclass
class PreloadDataConfig(PropertyType):
    preload_data_type: DslValue[str] | None = None


@dataclass
class SseConfiguration(PropertyType):
    kms_encryption_config: DslValue[KmsEncryptionConfig] | None = None
