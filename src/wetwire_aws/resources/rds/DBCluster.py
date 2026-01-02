"""PropertyTypes for AWS::RDS::DBCluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DBClusterRole(PropertyType):
    role_arn: str | None = None
    feature_name: str | None = None


@dataclass
class Endpoint(PropertyType):
    address: str | None = None
    port: str | None = None


@dataclass
class MasterUserSecret(PropertyType):
    kms_key_id: str | None = None
    secret_arn: str | None = None


@dataclass
class ReadEndpoint(PropertyType):
    address: str | None = None


@dataclass
class ScalingConfiguration(PropertyType):
    auto_pause: bool | None = None
    max_capacity: int | None = None
    min_capacity: int | None = None
    seconds_before_timeout: int | None = None
    seconds_until_auto_pause: int | None = None
    timeout_action: str | None = None


@dataclass
class ServerlessV2ScalingConfiguration(PropertyType):
    max_capacity: float | None = None
    min_capacity: float | None = None
    seconds_until_auto_pause: int | None = None
