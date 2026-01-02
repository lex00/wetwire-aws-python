"""PropertyTypes for AWS::S3Vectors::VectorBucket."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EncryptionConfiguration(PropertyType):
    kms_key_arn: str | None = None
    sse_type: str | None = None
