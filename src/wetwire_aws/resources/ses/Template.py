"""PropertyTypes for AWS::SES::Template."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Template(PropertyType):
    subject_part: DslValue[str] | None = None
    html_part: DslValue[str] | None = None
    template_name: DslValue[str] | None = None
    text_part: DslValue[str] | None = None
