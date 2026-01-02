"""PropertyTypes for AWS::S3Outposts::Bucket."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AbortIncompleteMultipartUpload(PropertyType):
    days_after_initiation: int | None = None


@dataclass
class Filter(PropertyType):
    and_operator: FilterAndOperator | None = None
    prefix: str | None = None
    tag: FilterTag | None = None


@dataclass
class FilterAndOperator(PropertyType):
    tags: list[FilterTag] = field(default_factory=list)
    prefix: str | None = None


@dataclass
class FilterTag(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class LifecycleConfiguration(PropertyType):
    rules: list[Rule] = field(default_factory=list)


@dataclass
class Rule(PropertyType):
    status: str | None = None
    abort_incomplete_multipart_upload: AbortIncompleteMultipartUpload | None = None
    expiration_date: str | None = None
    expiration_in_days: int | None = None
    filter: Filter | None = None
    id: str | None = None
