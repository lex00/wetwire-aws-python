"""PropertyTypes for AWS::SageMaker::App."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ResourceSpec(PropertyType):
    instance_type: str | None = None
    lifecycle_config_arn: str | None = None
    sage_maker_image_arn: str | None = None
    sage_maker_image_version_arn: str | None = None
