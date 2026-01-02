"""PropertyTypes for AWS::DataSync::LocationObjectStorage."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CmkSecretConfig(PropertyType):
    kms_key_arn: str | None = None
    secret_arn: str | None = None


@dataclass
class CustomSecretConfig(PropertyType):
    secret_access_role_arn: str | None = None
    secret_arn: str | None = None


@dataclass
class ManagedSecretConfig(PropertyType):
    secret_arn: str | None = None
