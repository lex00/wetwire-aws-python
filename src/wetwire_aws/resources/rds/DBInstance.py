"""PropertyTypes for AWS::RDS::DBInstance."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CertificateDetails(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ca_identifier": "CAIdentifier",
    }

    ca_identifier: str | None = None
    valid_till: str | None = None


@dataclass
class DBInstanceRole(PropertyType):
    feature_name: str | None = None
    role_arn: str | None = None


@dataclass
class DBInstanceStatusInfo(PropertyType):
    message: str | None = None
    normal: bool | None = None
    status: str | None = None
    status_type: str | None = None


@dataclass
class Endpoint(PropertyType):
    address: str | None = None
    hosted_zone_id: str | None = None
    port: str | None = None


@dataclass
class MasterUserSecret(PropertyType):
    kms_key_id: str | None = None
    secret_arn: str | None = None


@dataclass
class ProcessorFeature(PropertyType):
    name: str | None = None
    value: str | None = None
