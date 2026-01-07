"""PropertyTypes for AWS::S3Vectors::Index."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EncryptionConfiguration(PropertyType):
    kms_key_arn: DslValue[str] | None = None
    sse_type: DslValue[str] | None = None


@dataclass
class MetadataConfiguration(PropertyType):
    non_filterable_metadata_keys: list[DslValue[str]] = field(default_factory=list)
