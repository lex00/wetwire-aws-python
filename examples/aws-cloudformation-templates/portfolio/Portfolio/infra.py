"""Infra resources: ServiceCatalogProductTagOptionsDept, ServiceCatalogPortfolio, ServiceCatalogProductTagOptionsUser, ServiceCatalogPortfolioShare, ServiceCatalogProductTagOptionsEnv, ServiceCatalogProductTagOptionsOwner."""

from . import *  # noqa: F403


class ServiceCatalogProductTagOptionsDept(servicecatalog.TagOption):
    resource: servicecatalog.TagOption
    active = ActivateProductTagOptions
    key = 'Dept'
    value = ProductDept


class ServiceCatalogPortfolioProvisioningParameter(servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter):
    key = 'Name'
    value = PortfolioDisplayName


class ServiceCatalogPortfolioProvisioningParameter1(servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter):
    key = 'Dept'
    value = Dept


class ServiceCatalogPortfolioProvisioningParameter2(servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter):
    key = 'Env'
    value = Env


class ServiceCatalogPortfolioProvisioningParameter3(servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter):
    key = 'User'
    value = User


class ServiceCatalogPortfolioProvisioningParameter4(servicecatalog.CloudFormationProvisionedProduct.ProvisioningParameter):
    key = 'Owner'
    value = Owner


class ServiceCatalogPortfolio(servicecatalog.Portfolio):
    resource: servicecatalog.Portfolio
    provider_name = PortfolioProviderName
    description = PortfolioDescription
    display_name = PortfolioDisplayName
    tags = [ServiceCatalogPortfolioProvisioningParameter, ServiceCatalogPortfolioProvisioningParameter1, ServiceCatalogPortfolioProvisioningParameter2, ServiceCatalogPortfolioProvisioningParameter3, ServiceCatalogPortfolioProvisioningParameter4]


class ServiceCatalogProductTagOptionsUser(servicecatalog.TagOption):
    resource: servicecatalog.TagOption
    active = ActivateProductTagOptions
    key = 'User'
    value = ProductUser


class ServiceCatalogPortfolioShare(servicecatalog.PortfolioShare):
    resource: servicecatalog.PortfolioShare
    account_id = AccountIdOfChildAWSAccount
    portfolio_id = ServiceCatalogPortfolio
    condition = 'ConditionShareThisPortfolio'


class ServiceCatalogProductTagOptionsEnv(servicecatalog.TagOption):
    resource: servicecatalog.TagOption
    active = ActivateProductTagOptions
    key = 'Env'
    value = ProductEnv


class ServiceCatalogProductTagOptionsOwner(servicecatalog.TagOption):
    resource: servicecatalog.TagOption
    active = ActivateProductTagOptions
    key = 'Owner'
    value = ProductOwner
