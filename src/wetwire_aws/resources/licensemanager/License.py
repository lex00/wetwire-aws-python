"""PropertyTypes for AWS::LicenseManager::License."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BorrowConfiguration(PropertyType):
    allow_early_check_in: bool | None = None
    max_time_to_live_in_minutes: int | None = None


@dataclass
class ConsumptionConfiguration(PropertyType):
    borrow_configuration: BorrowConfiguration | None = None
    provisional_configuration: ProvisionalConfiguration | None = None
    renew_type: str | None = None


@dataclass
class Entitlement(PropertyType):
    name: str | None = None
    unit: str | None = None
    allow_check_in: bool | None = None
    max_count: int | None = None
    overage: bool | None = None
    value: str | None = None


@dataclass
class IssuerData(PropertyType):
    name: str | None = None
    sign_key: str | None = None


@dataclass
class Metadata(PropertyType):
    name: str | None = None
    value: str | None = None


@dataclass
class ProvisionalConfiguration(PropertyType):
    max_time_to_live_in_minutes: int | None = None


@dataclass
class ValidityDateFormat(PropertyType):
    begin: str | None = None
    end: str | None = None
