"""PropertyTypes for AWS::Lambda::CodeSigningConfig."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AllowedPublishers(PropertyType):
    signing_profile_version_arns: list[DslValue[str]] = field(default_factory=list)


@dataclass
class CodeSigningPolicies(PropertyType):
    untrusted_artifact_on_deployment: DslValue[str] | None = None
