"""PropertyTypes for AWS::SageMaker::NotebookInstance."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class InstanceMetadataServiceConfiguration(PropertyType):
    minimum_instance_metadata_service_version: DslValue[str] | None = None
