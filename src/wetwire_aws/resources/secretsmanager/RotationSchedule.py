"""PropertyTypes for AWS::SecretsManager::RotationSchedule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ExternalSecretRotationMetadataItem(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class HostedRotationLambda(PropertyType):
    rotation_type: str | None = None
    exclude_characters: str | None = None
    kms_key_arn: str | None = None
    master_secret_arn: str | None = None
    master_secret_kms_key_arn: str | None = None
    rotation_lambda_name: str | None = None
    runtime: str | None = None
    superuser_secret_arn: str | None = None
    superuser_secret_kms_key_arn: str | None = None
    vpc_security_group_ids: str | None = None
    vpc_subnet_ids: str | None = None


@dataclass
class RotationRules(PropertyType):
    automatically_after_days: int | None = None
    duration: str | None = None
    schedule_expression: str | None = None
