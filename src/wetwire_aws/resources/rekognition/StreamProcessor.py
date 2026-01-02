"""PropertyTypes for AWS::Rekognition::StreamProcessor."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BoundingBox(PropertyType):
    height: float | None = None
    left: float | None = None
    top: float | None = None
    width: float | None = None


@dataclass
class ConnectedHomeSettings(PropertyType):
    labels: list[String] = field(default_factory=list)
    min_confidence: float | None = None


@dataclass
class DataSharingPreference(PropertyType):
    opt_in: bool | None = None


@dataclass
class FaceSearchSettings(PropertyType):
    collection_id: str | None = None
    face_match_threshold: float | None = None


@dataclass
class KinesisDataStream(PropertyType):
    arn: str | None = None


@dataclass
class KinesisVideoStream(PropertyType):
    arn: str | None = None


@dataclass
class NotificationChannel(PropertyType):
    arn: str | None = None


@dataclass
class S3Destination(PropertyType):
    bucket_name: str | None = None
    object_key_prefix: str | None = None
