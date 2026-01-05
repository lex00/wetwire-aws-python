"""Infra resources: ServiceCatalogProductTagOptionsEnv, ServiceCatalogPortfolio, ServiceCatalogProductTagOptionsUser, ServiceCatalogPortfolioShare, ServiceCatalogProductTagOptionsOwner, ServiceCatalogProductTagOptionsDept."""

from . import *  # noqa: F403


class ServiceCatalogProductTagOptionsEnv(servicecatalog.TagOption):
    active = ActivateProductTagOptions
    key = 'Env'
    value = ProductEnv


class ServiceCatalogPortfolioProvisioningParameter:
    resource: servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter
    key = 'Name'
    value = PortfolioDisplayName


class ServiceCatalogPortfolioProvisioningParameter1:
    resource: servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter
    key = 'Dept'
    value = Dept


class ServiceCatalogPortfolioProvisioningParameter2:
    resource: servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter
    key = 'Env'
    value = Env


class ServiceCatalogPortfolioProvisioningParameter3:
    resource: servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter
    key = 'User'
    value = User


class ServiceCatalogPortfolioProvisioningParameter4:
    resource: servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter
    key = 'Owner'
    value = Owner


class ServiceCatalogPortfolio(servicecatalog.Portfolio):
    provider_name = PortfolioProviderName
    description = PortfolioDescription
    display_name = PortfolioDisplayName
    tags = [ServiceCatalogPortfolioProvisioningParameter, ServiceCatalogPortfolioProvisioningParameter1, ServiceCatalogPortfolioProvisioningParameter2, ServiceCatalogPortfolioProvisioningParameter3, ServiceCatalogPortfolioProvisioningParameter4]


class ServiceCatalogProductTagOptionsUser(servicecatalog.TagOption):
    active = ActivateProductTagOptions
    key = 'User'
    value = ProductUser


class ServiceCatalogPortfolioShare(servicecatalog.PortfolioShare):
    account_id = AccountIdOfChildAWSAccount
    portfolio_id = ServiceCatalogPortfolio
    condition = 'ConditionShareThisPortfolio'


class ServiceCatalogProductTagOptionsOwner(servicecatalog.TagOption):
    active = ActivateProductTagOptions
    key = 'Owner'
    value = ProductOwner


class ServiceCatalogProductTagOptionsDept(servicecatalog.TagOption):
    active = ActivateProductTagOptions
    key = 'Dept'
    value = ProductDept
