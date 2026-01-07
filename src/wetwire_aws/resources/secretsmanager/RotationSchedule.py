"""PropertyTypes for AWS::SecretsManager::RotationSchedule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ExternalSecretRotationMetadataItem(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class HostedRotationLambda(PropertyType):
    rotation_type: DslValue[str] | None = None
    exclude_characters: DslValue[str] | None = None
    kms_key_arn: DslValue[str] | None = None
    master_secret_arn: DslValue[str] | None = None
    master_secret_kms_key_arn: DslValue[str] | None = None
    rotation_lambda_name: DslValue[str] | None = None
    runtime: DslValue[str] | None = None
    superuser_secret_arn: DslValue[str] | None = None
    superuser_secret_kms_key_arn: DslValue[str] | None = None
    vpc_security_group_ids: DslValue[str] | None = None
    vpc_subnet_ids: DslValue[str] | None = None


@dataclass
class RotationRules(PropertyType):
    automatically_after_days: DslValue[int] | None = None
    duration: DslValue[str] | None = None
    schedule_expression: DslValue[str] | None = None
