"""PropertyTypes for AWS::DataSync::LocationAzureBlob."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AzureBlobSasConfiguration(PropertyType):
    azure_blob_sas_token: DslValue[str] | None = None


@dataclass
class CmkSecretConfig(PropertyType):
    kms_key_arn: DslValue[str] | None = None
    secret_arn: DslValue[str] | None = None


@dataclass
class CustomSecretConfig(PropertyType):
    secret_access_role_arn: DslValue[str] | None = None
    secret_arn: DslValue[str] | None = None


@dataclass
class ManagedSecretConfig(PropertyType):
    secret_arn: DslValue[str] | None = None
