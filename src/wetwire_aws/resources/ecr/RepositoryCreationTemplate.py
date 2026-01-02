"""PropertyTypes for AWS::ECR::RepositoryCreationTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EncryptionConfiguration(PropertyType):
    encryption_type: str | None = None
    kms_key: str | None = None


@dataclass
class ImageTagMutabilityExclusionFilter(PropertyType):
    image_tag_mutability_exclusion_filter_type: str | None = None
    image_tag_mutability_exclusion_filter_value: str | None = None
