"""PropertyTypes for AWS::ElasticBeanstalk::ApplicationVersion."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class SourceBundle(PropertyType):
    s3_bucket: str | None = None
    s3_key: str | None = None
