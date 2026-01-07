"""Template outputs."""

from . import *  # noqa: F403


class ServiceCatalogPortfolioOutput(Output):
    value = ServiceCatalogPortfolio
    export_name = Sub('${AWS::StackName}-ServiceCatalogPortfolio')


class ServiceCatalogPortfolioNameOutput(Output):
    value = ServiceCatalogPortfolio.PortfolioName
    export_name = Sub('${AWS::StackName}-ServiceCatalogPortfolioName')


class ServiceCatalogProductTagOptionsDeptOutput(Output):
    value = ServiceCatalogProductTagOptionsDept
    export_name = Sub('${AWS::StackName}-ServiceCatalogProductTagOptionsDept')
