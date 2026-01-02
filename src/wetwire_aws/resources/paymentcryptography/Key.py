"""PropertyTypes for AWS::PaymentCryptography::Key."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class KeyAttributes(PropertyType):
    key_algorithm: str | None = None
    key_class: str | None = None
    key_modes_of_use: KeyModesOfUse | None = None
    key_usage: str | None = None


@dataclass
class KeyModesOfUse(PropertyType):
    decrypt: bool | None = None
    derive_key: bool | None = None
    encrypt: bool | None = None
    generate: bool | None = None
    no_restrictions: bool | None = None
    sign: bool | None = None
    unwrap: bool | None = None
    verify: bool | None = None
    wrap: bool | None = None


@dataclass
class ReplicationStatusType(PropertyType):
    status: str | None = None
    status_message: str | None = None
