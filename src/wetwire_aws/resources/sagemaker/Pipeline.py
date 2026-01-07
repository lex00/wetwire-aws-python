"""PropertyTypes for AWS::SageMaker::Pipeline."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ParallelismConfiguration(PropertyType):
    max_parallel_execution_steps: DslValue[int] | None = None


@dataclass
class PipelineDefinition(PropertyType):
    pipeline_definition_body: DslValue[str] | None = None
    pipeline_definition_s3_location: DslValue[S3Location] | None = None


@dataclass
class S3Location(PropertyType):
    bucket: DslValue[str] | None = None
    key: DslValue[str] | None = None
    e_tag: DslValue[str] | None = None
    version: DslValue[str] | None = None
