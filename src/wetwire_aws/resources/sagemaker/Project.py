"""PropertyTypes for AWS::SageMaker::Project."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CfnStackParameter(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class CfnTemplateProviderDetail(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role_arn": "RoleARN",
        "template_url": "TemplateURL",
    }

    template_name: str | None = None
    template_url: str | None = None
    parameters: list[CfnStackParameter] = field(default_factory=list)
    role_arn: str | None = None


@dataclass
class ProvisioningParameter(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class ServiceCatalogProvisionedProductDetails(PropertyType):
    provisioned_product_id: str | None = None
    provisioned_product_status_message: str | None = None


@dataclass
class ServiceCatalogProvisioningDetails(PropertyType):
    product_id: str | None = None
    path_id: str | None = None
    provisioning_artifact_id: str | None = None
    provisioning_parameters: list[ProvisioningParameter] = field(default_factory=list)


@dataclass
class TemplateProviderDetail(PropertyType):
    cfn_template_provider_detail: CfnTemplateProviderDetail | None = None
