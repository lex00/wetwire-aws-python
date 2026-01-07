"""PropertyTypes for AWS::SageMaker::App."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ResourceSpec(PropertyType):
    instance_type: DslValue[str] | None = None
    lifecycle_config_arn: DslValue[str] | None = None
    sage_maker_image_arn: DslValue[str] | None = None
    sage_maker_image_version_arn: DslValue[str] | None = None
