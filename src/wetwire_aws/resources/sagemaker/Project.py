"""PropertyTypes for AWS::SageMaker::Project."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CfnStackParameter(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class CfnTemplateProviderDetail(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role_arn": "RoleARN",
        "template_url": "TemplateURL",
    }

    template_name: DslValue[str] | None = None
    template_url: DslValue[str] | None = None
    parameters: list[DslValue[CfnStackParameter]] = field(default_factory=list)
    role_arn: DslValue[str] | None = None


@dataclass
class ProvisioningParameter(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class ServiceCatalogProvisionedProductDetails(PropertyType):
    provisioned_product_id: DslValue[str] | None = None
    provisioned_product_status_message: DslValue[str] | None = None


@dataclass
class ServiceCatalogProvisioningDetails(PropertyType):
    product_id: DslValue[str] | None = None
    path_id: DslValue[str] | None = None
    provisioning_artifact_id: DslValue[str] | None = None
    provisioning_parameters: list[DslValue[ProvisioningParameter]] = field(
        default_factory=list
    )


@dataclass
class TemplateProviderDetail(PropertyType):
    cfn_template_provider_detail: DslValue[CfnTemplateProviderDetail] | None = None
