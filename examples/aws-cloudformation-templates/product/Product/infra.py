"""Infra resources: ServiceCatalogCloudFormationProduct, ServiceCatalogPortfolioProductAssociation, ServiceCatalogCustomTagOptionsAssociation."""

from . import *  # noqa: F403


class ServiceCatalogCloudFormationProductProvisioningParameter:
    resource: servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter
    key = 'Name'
    value = AppName


class ServiceCatalogCloudFormationProductProvisioningParameter1:
    resource: servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter
    key = 'App'
    value = AppName


class ServiceCatalogCloudFormationProductProvisioningParameter2:
    resource: servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter
    key = 'Dept'
    value = Dept


class ServiceCatalogCloudFormationProductProvisioningParameter3:
    resource: servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter
    key = 'Env'
    value = Env


class ServiceCatalogCloudFormationProductProvisioningParameter4:
    resource: servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter
    key = 'User'
    value = User


class ServiceCatalogCloudFormationProductProvisioningParameter5:
    resource: servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter
    key = 'Owner'
    value = Owner


class ServiceCatalogCloudFormationProductProvisioningArtifactProperties:
    resource: servicecatalog.CloudFormationProduct.ProvisioningArtifactProperties
    name = ProvisioningArtifactNameParameter
    description = ProvisioningArtifactDescriptionParameter
    info = {
        'LoadTemplateFromURL': ProvisioningArtifactTemplateUrl,
    }


class ServiceCatalogCloudFormationProduct(servicecatalog.CloudFormationProduct):
    name = SCProductName
    description = SCProductDescription
    owner = SCProductOwner
    support_description = SCProductSupport
    distributor = SCProductDistributor
    support_email = SCSupportEmail
    support_url = SCSupportUrl
    tags = [ServiceCatalogCloudFormationProductProvisioningParameter, ServiceCatalogCloudFormationProductProvisioningParameter1, ServiceCatalogCloudFormationProductProvisioningParameter2, ServiceCatalogCloudFormationProductProvisioningParameter3, ServiceCatalogCloudFormationProductProvisioningParameter4, ServiceCatalogCloudFormationProductProvisioningParameter5]
    provisioning_artifact_parameters = [ServiceCatalogCloudFormationProductProvisioningArtifactProperties]


class ServiceCatalogPortfolioProductAssociation(servicecatalog.PortfolioProductAssociation):
    portfolio_id = ImportValue(Sub('${ServiceCatalogPortfolioStackName}-ServiceCatalogPortfolio'))
    product_id = ServiceCatalogCloudFormationProduct
    depends_on = [ServiceCatalogCloudFormationProduct]


class ServiceCatalogCustomTagOptionsAssociation(servicecatalog.TagOptionAssociation):
    tag_option_id = ImportValue(Sub('${ServiceCatalogPortfolioStackName}-ServiceCatalogProductTagOptionsDept'))
    resource_id = ServiceCatalogCloudFormationProduct
