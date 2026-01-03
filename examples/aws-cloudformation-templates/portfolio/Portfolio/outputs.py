"""Template outputs."""

from . import *  # noqa: F403


class ServiceCatalogPortfolioOutput:
    resource: Output
    value = ServiceCatalogPortfolio
    export_name = Sub('${AWS::StackName}-ServiceCatalogPortfolio')


class ServiceCatalogPortfolioNameOutput:
    resource: Output
    value = ServiceCatalogPortfolio.PortfolioName
    export_name = Sub('${AWS::StackName}-ServiceCatalogPortfolioName')


class ServiceCatalogProductTagOptionsDeptOutput:
    resource: Output
    value = ServiceCatalogProductTagOptionsDept
    export_name = Sub('${AWS::StackName}-ServiceCatalogProductTagOptionsDept')
