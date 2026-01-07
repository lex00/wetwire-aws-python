"""PropertyTypes for AWS::Macie::AllowList."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Criteria(PropertyType):
    regex: DslValue[str] | None = None
    s3_words_list: DslValue[S3WordsList] | None = None


@dataclass
class S3WordsList(PropertyType):
    bucket_name: DslValue[str] | None = None
    object_key: DslValue[str] | None = None
