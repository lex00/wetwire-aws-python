"""PropertyTypes for AWS::IoTAnalytics::Pipeline."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Activity(PropertyType):
    add_attributes: DslValue[AddAttributes] | None = None
    channel: DslValue[Channel] | None = None
    datastore: DslValue[Datastore] | None = None
    device_registry_enrich: DslValue[DeviceRegistryEnrich] | None = None
    device_shadow_enrich: DslValue[DeviceShadowEnrich] | None = None
    filter: DslValue[Filter] | None = None
    lambda_: DslValue[Lambda] | None = None
    math: DslValue[Math] | None = None
    remove_attributes: DslValue[RemoveAttributes] | None = None
    select_attributes: DslValue[SelectAttributes] | None = None


@dataclass
class AddAttributes(PropertyType):
    attributes: dict[str, DslValue[str]] = field(default_factory=dict)
    name: DslValue[str] | None = None
    next: DslValue[str] | None = None


@dataclass
class Channel(PropertyType):
    channel_name: DslValue[str] | None = None
    name: DslValue[str] | None = None
    next: DslValue[str] | None = None


@dataclass
class Datastore(PropertyType):
    datastore_name: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class DeviceRegistryEnrich(PropertyType):
    attribute: DslValue[str] | None = None
    name: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    thing_name: DslValue[str] | None = None
    next: DslValue[str] | None = None


@dataclass
class DeviceShadowEnrich(PropertyType):
    attribute: DslValue[str] | None = None
    name: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    thing_name: DslValue[str] | None = None
    next: DslValue[str] | None = None


@dataclass
class Filter(PropertyType):
    filter: DslValue[str] | None = None
    name: DslValue[str] | None = None
    next: DslValue[str] | None = None


@dataclass
class Lambda(PropertyType):
    batch_size: DslValue[int] | None = None
    lambda_name: DslValue[str] | None = None
    name: DslValue[str] | None = None
    next: DslValue[str] | None = None


@dataclass
class Math(PropertyType):
    attribute: DslValue[str] | None = None
    math: DslValue[str] | None = None
    name: DslValue[str] | None = None
    next: DslValue[str] | None = None


@dataclass
class RemoveAttributes(PropertyType):
    attributes: list[DslValue[str]] = field(default_factory=list)
    name: DslValue[str] | None = None
    next: DslValue[str] | None = None


@dataclass
class SelectAttributes(PropertyType):
    attributes: list[DslValue[str]] = field(default_factory=list)
    name: DslValue[str] | None = None
    next: DslValue[str] | None = None
