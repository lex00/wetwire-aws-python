"""PropertyTypes for AWS::Macie::AllowList."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Criteria(PropertyType):
    regex: str | None = None
    s3_words_list: S3WordsList | None = None


@dataclass
class S3WordsList(PropertyType):
    bucket_name: str | None = None
    object_key: str | None = None
