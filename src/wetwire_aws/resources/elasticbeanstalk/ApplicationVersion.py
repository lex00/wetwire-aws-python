"""PropertyTypes for AWS::ElasticBeanstalk::ApplicationVersion."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class SourceBundle(PropertyType):
    s3_bucket: DslValue[str] | None = None
    s3_key: DslValue[str] | None = None
