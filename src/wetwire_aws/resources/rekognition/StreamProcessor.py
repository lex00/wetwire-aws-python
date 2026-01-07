"""PropertyTypes for AWS::Rekognition::StreamProcessor."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BoundingBox(PropertyType):
    height: DslValue[float] | None = None
    left: DslValue[float] | None = None
    top: DslValue[float] | None = None
    width: DslValue[float] | None = None


@dataclass
class ConnectedHomeSettings(PropertyType):
    labels: list[DslValue[str]] = field(default_factory=list)
    min_confidence: DslValue[float] | None = None


@dataclass
class DataSharingPreference(PropertyType):
    opt_in: DslValue[bool] | None = None


@dataclass
class FaceSearchSettings(PropertyType):
    collection_id: DslValue[str] | None = None
    face_match_threshold: DslValue[float] | None = None


@dataclass
class KinesisDataStream(PropertyType):
    arn: DslValue[str] | None = None


@dataclass
class KinesisVideoStream(PropertyType):
    arn: DslValue[str] | None = None


@dataclass
class NotificationChannel(PropertyType):
    arn: DslValue[str] | None = None


@dataclass
class S3Destination(PropertyType):
    bucket_name: DslValue[str] | None = None
    object_key_prefix: DslValue[str] | None = None
