"""PropertyTypes for AWS::FinSpace::Environment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AttributeMapItems(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class FederationParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "application_call_back_url": "ApplicationCallBackURL",
        "federation_urn": "FederationURN",
        "saml_metadata_url": "SamlMetadataURL",
    }

    application_call_back_url: DslValue[str] | None = None
    attribute_map: list[DslValue[AttributeMapItems]] = field(default_factory=list)
    federation_provider_name: DslValue[str] | None = None
    federation_urn: DslValue[str] | None = None
    saml_metadata_document: DslValue[str] | None = None
    saml_metadata_url: DslValue[str] | None = None


@dataclass
class SuperuserParameters(PropertyType):
    email_address: DslValue[str] | None = None
    first_name: DslValue[str] | None = None
    last_name: DslValue[str] | None = None
