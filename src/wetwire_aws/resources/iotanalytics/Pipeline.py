"""PropertyTypes for AWS::IoTAnalytics::Pipeline."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Activity(PropertyType):
    add_attributes: AddAttributes | None = None
    channel: Channel | None = None
    datastore: Datastore | None = None
    device_registry_enrich: DeviceRegistryEnrich | None = None
    device_shadow_enrich: DeviceShadowEnrich | None = None
    filter: Filter | None = None
    lambda_: Lambda | None = None
    math: Math | None = None
    remove_attributes: RemoveAttributes | None = None
    select_attributes: SelectAttributes | None = None


@dataclass
class AddAttributes(PropertyType):
    attributes: dict[str, String] = field(default_factory=dict)
    name: str | None = None
    next: str | None = None


@dataclass
class Channel(PropertyType):
    channel_name: str | None = None
    name: str | None = None
    next: str | None = None


@dataclass
class Datastore(PropertyType):
    datastore_name: str | None = None
    name: str | None = None


@dataclass
class DeviceRegistryEnrich(PropertyType):
    attribute: str | None = None
    name: str | None = None
    role_arn: str | None = None
    thing_name: str | None = None
    next: str | None = None


@dataclass
class DeviceShadowEnrich(PropertyType):
    attribute: str | None = None
    name: str | None = None
    role_arn: str | None = None
    thing_name: str | None = None
    next: str | None = None


@dataclass
class Filter(PropertyType):
    filter: str | None = None
    name: str | None = None
    next: str | None = None


@dataclass
class Lambda(PropertyType):
    batch_size: int | None = None
    lambda_name: str | None = None
    name: str | None = None
    next: str | None = None


@dataclass
class Math(PropertyType):
    attribute: str | None = None
    math: str | None = None
    name: str | None = None
    next: str | None = None


@dataclass
class RemoveAttributes(PropertyType):
    attributes: list[String] = field(default_factory=list)
    name: str | None = None
    next: str | None = None


@dataclass
class SelectAttributes(PropertyType):
    attributes: list[String] = field(default_factory=list)
    name: str | None = None
    next: str | None = None
