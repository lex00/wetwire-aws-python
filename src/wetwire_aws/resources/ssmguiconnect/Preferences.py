"""PropertyTypes for AWS::SSMGuiConnect::Preferences."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ConnectionRecordingPreferences(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_key_arn": "KMSKeyArn",
    }

    kms_key_arn: DslValue[str] | None = None
    recording_destinations: DslValue[RecordingDestinations] | None = None


@dataclass
class RecordingDestinations(PropertyType):
    s3_buckets: list[DslValue[S3Bucket]] = field(default_factory=list)


@dataclass
class S3Bucket(PropertyType):
    bucket_name: DslValue[str] | None = None
    bucket_owner: DslValue[str] | None = None
