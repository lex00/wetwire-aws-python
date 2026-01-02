"""PropertyTypes for AWS::S3ObjectLambda::AccessPoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Alias(PropertyType):
    value: str | None = None
    status: str | None = None


@dataclass
class AwsLambda(PropertyType):
    function_arn: str | None = None
    function_payload: str | None = None


@dataclass
class ContentTransformation(PropertyType):
    aws_lambda: AwsLambda | None = None


@dataclass
class ObjectLambdaConfiguration(PropertyType):
    supporting_access_point: str | None = None
    transformation_configurations: list[TransformationConfiguration] = field(
        default_factory=list
    )
    allowed_features: list[String] = field(default_factory=list)
    cloud_watch_metrics_enabled: bool | None = None


@dataclass
class PublicAccessBlockConfiguration(PropertyType):
    block_public_acls: bool | None = None
    block_public_policy: bool | None = None
    ignore_public_acls: bool | None = None
    restrict_public_buckets: bool | None = None


@dataclass
class TransformationConfiguration(PropertyType):
    actions: list[String] = field(default_factory=list)
    content_transformation: ContentTransformation | None = None
