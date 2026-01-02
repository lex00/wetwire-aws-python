"""PropertyTypes for AWS::Glue::DataCatalogEncryptionSettings."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ConnectionPasswordEncryption(PropertyType):
    kms_key_id: str | None = None
    return_connection_password_encrypted: bool | None = None


@dataclass
class DataCatalogEncryptionSettings(PropertyType):
    connection_password_encryption: ConnectionPasswordEncryption | None = None
    encryption_at_rest: EncryptionAtRest | None = None


@dataclass
class EncryptionAtRest(PropertyType):
    catalog_encryption_mode: str | None = None
    catalog_encryption_service_role: str | None = None
    sse_aws_kms_key_id: str | None = None
