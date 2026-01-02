"""PropertyTypes for AWS::SageMaker::Pipeline."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ParallelismConfiguration(PropertyType):
    max_parallel_execution_steps: int | None = None


@dataclass
class PipelineDefinition(PropertyType):
    pipeline_definition_body: str | None = None
    pipeline_definition_s3_location: S3Location | None = None


@dataclass
class S3Location(PropertyType):
    bucket: str | None = None
    key: str | None = None
    e_tag: str | None = None
    version: str | None = None
