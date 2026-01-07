"""PropertyTypes for AWS::Glue::DataCatalogEncryptionSettings."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ConnectionPasswordEncryption(PropertyType):
    kms_key_id: DslValue[str] | None = None
    return_connection_password_encrypted: DslValue[bool] | None = None


@dataclass
class DataCatalogEncryptionSettings(PropertyType):
    connection_password_encryption: DslValue[ConnectionPasswordEncryption] | None = None
    encryption_at_rest: DslValue[EncryptionAtRest] | None = None


@dataclass
class EncryptionAtRest(PropertyType):
    catalog_encryption_mode: DslValue[str] | None = None
    catalog_encryption_service_role: DslValue[str] | None = None
    sse_aws_kms_key_id: DslValue[str] | None = None
