"""Infra resources: ServiceCatalogCloudFormationProduct, ServiceCatalogCustomTagOptionsAssociation, ServiceCatalogPortfolioProductAssociation."""

from . import *  # noqa: F403


class ServiceCatalogCloudFormationProductProvisioningParameter:
    resource: servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter
    key = 'Name'
    value = Sub('${AppName}')


class ServiceCatalogCloudFormationProductProvisioningParameter1:
    resource: servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter
    key = 'App'
    value = Sub('${AppName}')


class ServiceCatalogCloudFormationProductProvisioningParameter2:
    resource: servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter
    key = 'Dept'
    value = Sub('${Dept}')


class ServiceCatalogCloudFormationProductProvisioningParameter3:
    resource: servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter
    key = 'Env'
    value = Sub('${Env}')


class ServiceCatalogCloudFormationProductProvisioningParameter4:
    resource: servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter
    key = 'User'
    value = Sub('${User}')


class ServiceCatalogCloudFormationProductProvisioningParameter5:
    resource: servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter
    key = 'Owner'
    value = Sub('${Owner}')


class ServiceCatalogCloudFormationProductProvisioningArtifactProperties:
    resource: servicecatalog.CloudFormationProduct.ProvisioningArtifactProperties
    name = Sub('${ProvisioningArtifactNameParameter}')
    description = Sub('${ProvisioningArtifactDescriptionParameter}')
    info = {
        'LoadTemplateFromURL': Sub('${ProvisioningArtifactTemplateUrl}'),
    }


class ServiceCatalogCloudFormationProduct:
    resource: servicecatalog.CloudFormationProduct
    name = SCProductName
    description = SCProductDescription
    owner = SCProductOwner
    support_description = SCProductSupport
    distributor = SCProductDistributor
    support_email = SCSupportEmail
    support_url = Sub('${SCSupportUrl}')
    tags = [ServiceCatalogCloudFormationProductProvisioningParameter, ServiceCatalogCloudFormationProductProvisioningParameter1, ServiceCatalogCloudFormationProductProvisioningParameter2, ServiceCatalogCloudFormationProductProvisioningParameter3, ServiceCatalogCloudFormationProductProvisioningParameter4, ServiceCatalogCloudFormationProductProvisioningParameter5]
    provisioning_artifact_parameters = [ServiceCatalogCloudFormationProductProvisioningArtifactProperties]


class ServiceCatalogCustomTagOptionsAssociation:
    resource: servicecatalog.TagOptionAssociation
    tag_option_id = ImportValue(Sub('${ServiceCatalogPortfolioStackName}-ServiceCatalogProductTagOptionsDept'))
    resource_id = ServiceCatalogCloudFormationProduct


class ServiceCatalogPortfolioProductAssociation:
    resource: servicecatalog.PortfolioProductAssociation
    portfolio_id = ImportValue(Sub('${ServiceCatalogPortfolioStackName}-ServiceCatalogPortfolio'))
    product_id = ServiceCatalogCloudFormationProduct
    depends_on = [ServiceCatalogCloudFormationProduct]
