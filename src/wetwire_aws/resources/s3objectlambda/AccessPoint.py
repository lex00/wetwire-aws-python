"""PropertyTypes for AWS::S3ObjectLambda::AccessPoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Alias(PropertyType):
    value: DslValue[str] | None = None
    status: DslValue[str] | None = None


@dataclass
class AwsLambda(PropertyType):
    function_arn: DslValue[str] | None = None
    function_payload: DslValue[str] | None = None


@dataclass
class ContentTransformation(PropertyType):
    aws_lambda: DslValue[AwsLambda] | None = None


@dataclass
class ObjectLambdaConfiguration(PropertyType):
    supporting_access_point: DslValue[str] | None = None
    transformation_configurations: list[DslValue[TransformationConfiguration]] = field(
        default_factory=list
    )
    allowed_features: list[DslValue[str]] = field(default_factory=list)
    cloud_watch_metrics_enabled: DslValue[bool] | None = None


@dataclass
class PublicAccessBlockConfiguration(PropertyType):
    block_public_acls: DslValue[bool] | None = None
    block_public_policy: DslValue[bool] | None = None
    ignore_public_acls: DslValue[bool] | None = None
    restrict_public_buckets: DslValue[bool] | None = None


@dataclass
class TransformationConfiguration(PropertyType):
    actions: list[DslValue[str]] = field(default_factory=list)
    content_transformation: DslValue[ContentTransformation] | None = None
