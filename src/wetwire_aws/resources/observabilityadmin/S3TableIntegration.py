"""PropertyTypes for AWS::ObservabilityAdmin::S3TableIntegration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EncryptionConfig(PropertyType):
    sse_algorithm: DslValue[str] | None = None
    kms_key_arn: DslValue[str] | None = None


@dataclass
class LogSource(PropertyType):
    name: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    identifier: DslValue[str] | None = None
