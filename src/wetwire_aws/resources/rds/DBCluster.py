"""PropertyTypes for AWS::RDS::DBCluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DBClusterRole(PropertyType):
    role_arn: DslValue[str] | None = None
    feature_name: DslValue[str] | None = None


@dataclass
class Endpoint(PropertyType):
    address: DslValue[str] | None = None
    port: DslValue[str] | None = None


@dataclass
class MasterUserSecret(PropertyType):
    kms_key_id: DslValue[str] | None = None
    secret_arn: DslValue[str] | None = None


@dataclass
class ReadEndpoint(PropertyType):
    address: DslValue[str] | None = None


@dataclass
class ScalingConfiguration(PropertyType):
    auto_pause: DslValue[bool] | None = None
    max_capacity: DslValue[int] | None = None
    min_capacity: DslValue[int] | None = None
    seconds_before_timeout: DslValue[int] | None = None
    seconds_until_auto_pause: DslValue[int] | None = None
    timeout_action: DslValue[str] | None = None


@dataclass
class ServerlessV2ScalingConfiguration(PropertyType):
    max_capacity: DslValue[float] | None = None
    min_capacity: DslValue[float] | None = None
    seconds_until_auto_pause: DslValue[int] | None = None
