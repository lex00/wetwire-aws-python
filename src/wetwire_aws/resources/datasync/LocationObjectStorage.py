"""PropertyTypes for AWS::DataSync::LocationObjectStorage."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CmkSecretConfig(PropertyType):
    kms_key_arn: DslValue[str] | None = None
    secret_arn: DslValue[str] | None = None


@dataclass
class CustomSecretConfig(PropertyType):
    secret_access_role_arn: DslValue[str] | None = None
    secret_arn: DslValue[str] | None = None


@dataclass
class ManagedSecretConfig(PropertyType):
    secret_arn: DslValue[str] | None = None
