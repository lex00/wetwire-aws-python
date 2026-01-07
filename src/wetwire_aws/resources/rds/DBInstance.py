"""PropertyTypes for AWS::RDS::DBInstance."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CertificateDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ca_identifier": "CAIdentifier",
    }

    ca_identifier: DslValue[str] | None = None
    valid_till: DslValue[str] | None = None


@dataclass
class DBInstanceRole(PropertyType):
    feature_name: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None


@dataclass
class DBInstanceStatusInfo(PropertyType):
    message: DslValue[str] | None = None
    normal: DslValue[bool] | None = None
    status: DslValue[str] | None = None
    status_type: DslValue[str] | None = None


@dataclass
class Endpoint(PropertyType):
    address: DslValue[str] | None = None
    hosted_zone_id: DslValue[str] | None = None
    port: DslValue[str] | None = None


@dataclass
class MasterUserSecret(PropertyType):
    kms_key_id: DslValue[str] | None = None
    secret_arn: DslValue[str] | None = None


@dataclass
class ProcessorFeature(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None
