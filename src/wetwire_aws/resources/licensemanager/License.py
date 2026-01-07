"""PropertyTypes for AWS::LicenseManager::License."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BorrowConfiguration(PropertyType):
    allow_early_check_in: DslValue[bool] | None = None
    max_time_to_live_in_minutes: DslValue[int] | None = None


@dataclass
class ConsumptionConfiguration(PropertyType):
    borrow_configuration: DslValue[BorrowConfiguration] | None = None
    provisional_configuration: DslValue[ProvisionalConfiguration] | None = None
    renew_type: DslValue[str] | None = None


@dataclass
class Entitlement(PropertyType):
    name: DslValue[str] | None = None
    unit: DslValue[str] | None = None
    allow_check_in: DslValue[bool] | None = None
    max_count: DslValue[int] | None = None
    overage: DslValue[bool] | None = None
    value: DslValue[str] | None = None


@dataclass
class IssuerData(PropertyType):
    name: DslValue[str] | None = None
    sign_key: DslValue[str] | None = None


@dataclass
class Metadata(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class ProvisionalConfiguration(PropertyType):
    max_time_to_live_in_minutes: DslValue[int] | None = None


@dataclass
class ValidityDateFormat(PropertyType):
    begin: DslValue[str] | None = None
    end: DslValue[str] | None = None
