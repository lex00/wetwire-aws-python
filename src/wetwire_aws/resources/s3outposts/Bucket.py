"""PropertyTypes for AWS::S3Outposts::Bucket."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AbortIncompleteMultipartUpload(PropertyType):
    days_after_initiation: DslValue[int] | None = None


@dataclass
class Filter(PropertyType):
    and_operator: DslValue[FilterAndOperator] | None = None
    prefix: DslValue[str] | None = None
    tag: DslValue[FilterTag] | None = None


@dataclass
class FilterAndOperator(PropertyType):
    tags: list[DslValue[FilterTag]] = field(default_factory=list)
    prefix: DslValue[str] | None = None


@dataclass
class FilterTag(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class LifecycleConfiguration(PropertyType):
    rules: list[DslValue[Rule]] = field(default_factory=list)


@dataclass
class Rule(PropertyType):
    status: DslValue[str] | None = None
    abort_incomplete_multipart_upload: (
        DslValue[AbortIncompleteMultipartUpload] | None
    ) = None
    expiration_date: DslValue[str] | None = None
    expiration_in_days: DslValue[int] | None = None
    filter: DslValue[Filter] | None = None
    id: DslValue[str] | None = None
