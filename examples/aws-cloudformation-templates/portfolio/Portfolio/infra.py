"""Infra resources: ServiceCatalogPortfolio, ServiceCatalogProductTagOptionsDept, ServiceCatalogPortfolioShare, ServiceCatalogProductTagOptionsUser, ServiceCatalogProductTagOptionsEnv, ServiceCatalogProductTagOptionsOwner."""

from . import *  # noqa: F403


class ServiceCatalogPortfolioProvisioningParameter:
    resource: servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter
    key = 'Name'
    value = Sub('${PortfolioDisplayName}')


class ServiceCatalogPortfolioProvisioningParameter1:
    resource: servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter
    key = 'Dept'
    value = Sub('${Dept}')


class ServiceCatalogPortfolioProvisioningParameter2:
    resource: servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter
    key = 'Env'
    value = Sub('${Env}')


class ServiceCatalogPortfolioProvisioningParameter3:
    resource: servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter
    key = 'User'
    value = Sub('${User}')


class ServiceCatalogPortfolioProvisioningParameter4:
    resource: servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter
    key = 'Owner'
    value = Sub('${Owner}')


class ServiceCatalogPortfolio:
    resource: servicecatalog.Portfolio
    provider_name = PortfolioProviderName
    description = PortfolioDescription
    display_name = PortfolioDisplayName
    tags = [ServiceCatalogPortfolioProvisioningParameter, ServiceCatalogPortfolioProvisioningParameter1, ServiceCatalogPortfolioProvisioningParameter2, ServiceCatalogPortfolioProvisioningParameter3, ServiceCatalogPortfolioProvisioningParameter4]


class ServiceCatalogProductTagOptionsDept:
    resource: servicecatalog.TagOption
    active = ActivateProductTagOptions
    key = 'Dept'
    value = Sub('${ProductDept}')


class ServiceCatalogPortfolioShare:
    resource: servicecatalog.PortfolioShare
    account_id = AccountIdOfChildAWSAccount
    portfolio_id = ServiceCatalogPortfolio
    condition = 'ConditionShareThisPortfolio'


class ServiceCatalogProductTagOptionsUser:
    resource: servicecatalog.TagOption
    active = ActivateProductTagOptions
    key = 'User'
    value = Sub('${ProductUser}')


class ServiceCatalogProductTagOptionsEnv:
    resource: servicecatalog.TagOption
    active = ActivateProductTagOptions
    key = 'Env'
    value = Sub('${ProductEnv}')


class ServiceCatalogProductTagOptionsOwner:
    resource: servicecatalog.TagOption
    active = ActivateProductTagOptions
    key = 'Owner'
    value = Sub('${ProductOwner}')
