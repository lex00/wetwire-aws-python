"""PropertyTypes for AWS::PaymentCryptography::Key."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class KeyAttributes(PropertyType):
    key_algorithm: DslValue[str] | None = None
    key_class: DslValue[str] | None = None
    key_modes_of_use: DslValue[KeyModesOfUse] | None = None
    key_usage: DslValue[str] | None = None


@dataclass
class KeyModesOfUse(PropertyType):
    decrypt: DslValue[bool] | None = None
    derive_key: DslValue[bool] | None = None
    encrypt: DslValue[bool] | None = None
    generate: DslValue[bool] | None = None
    no_restrictions: DslValue[bool] | None = None
    sign: DslValue[bool] | None = None
    unwrap: DslValue[bool] | None = None
    verify: DslValue[bool] | None = None
    wrap: DslValue[bool] | None = None


@dataclass
class ReplicationStatusType(PropertyType):
    status: DslValue[str] | None = None
    status_message: DslValue[str] | None = None
