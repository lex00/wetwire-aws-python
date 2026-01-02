"""PropertyTypes for AWS::VoiceID::Domain."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ServerSideEncryptionConfiguration(PropertyType):
    kms_key_id: str | None = None
