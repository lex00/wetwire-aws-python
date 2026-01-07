"""PropertyTypes for AWS::ECR::RepositoryCreationTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EncryptionConfiguration(PropertyType):
    encryption_type: DslValue[str] | None = None
    kms_key: DslValue[str] | None = None


@dataclass
class ImageTagMutabilityExclusionFilter(PropertyType):
    image_tag_mutability_exclusion_filter_type: DslValue[str] | None = None
    image_tag_mutability_exclusion_filter_value: DslValue[str] | None = None
