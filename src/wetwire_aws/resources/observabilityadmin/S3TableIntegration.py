"""PropertyTypes for AWS::ObservabilityAdmin::S3TableIntegration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EncryptionConfig(PropertyType):
    sse_algorithm: str | None = None
    kms_key_arn: str | None = None


@dataclass
class LogSource(PropertyType):
    name: str | None = None
    type_: str | None = None
    identifier: str | None = None
