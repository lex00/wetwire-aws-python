"""PropertyTypes for AWS::ECR::Repository."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EncryptionConfiguration(PropertyType):
    encryption_type: str | None = None
    kms_key: str | None = None


@dataclass
class ImageScanningConfiguration(PropertyType):
    scan_on_push: bool | None = None


@dataclass
class ImageTagMutabilityExclusionFilter(PropertyType):
    image_tag_mutability_exclusion_filter_type: str | None = None
    image_tag_mutability_exclusion_filter_value: str | None = None


@dataclass
class LifecyclePolicy(PropertyType):
    lifecycle_policy_text: str | None = None
    registry_id: str | None = None
