"""PropertyTypes for AWS::SageMaker::NotebookInstance."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class InstanceMetadataServiceConfiguration(PropertyType):
    minimum_instance_metadata_service_version: str | None = None
