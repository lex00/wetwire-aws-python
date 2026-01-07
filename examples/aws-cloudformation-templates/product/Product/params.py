"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class Env(Parameter):
    """Please specify the target Environment. Used for tagging and resource names. Mandatory LOWER CASE."""

    type = STRING
    description = 'Please specify the target Environment. Used for tagging and resource names. Mandatory LOWER CASE.'
    default = 'dev'
    allowed_values = [
    'test',
    'dev',
    'prod',
]


class AppName(Parameter):
    """Please specify the Application Name. Used for tagging and resource names. Mandatory LOWER CASE."""

    type = STRING
    description = 'Please specify the Application Name. Used for tagging and resource names. Mandatory LOWER CASE.'
    default = 'app'


class Dept(Parameter):
    """Please specify the Department. Used for tagging"""

    type = STRING
    description = 'Please specify the Department. Used for tagging'
    default = '1234'


class User(Parameter):
    """Please specify the User. Used for tagging"""

    type = STRING
    description = 'Please specify the User. Used for tagging'
    default = 'User'


class Owner(Parameter):
    """Please specify the Owner. Used for tagging"""

    type = STRING
    description = 'Please specify the Owner. Used for tagging'
    default = 'Owner'


class ServiceCatalogPortfolioStackName(Parameter):
    """Please specify the Service Catalog Portfolio Stack Name."""

    type = STRING
    description = 'Please specify the Service Catalog Portfolio Stack Name.'
    default = ''


class SCProductName(Parameter):
    """Please specify ServiceCatalog Product Name."""

    type = STRING
    description = 'Please specify ServiceCatalog Product Name.'
    default = 'ProductName'


class SCProductDescription(Parameter):
    """Please specify ServiceCatalog Product Name Description."""

    type = STRING
    description = 'Please specify ServiceCatalog Product Name Description.'
    default = 'ProductDescription'


class SCProductOwner(Parameter):
    """Please specify ServiceCatalog Product Owner."""

    type = STRING
    description = 'Please specify ServiceCatalog Product Owner.'
    default = 'ProductOwner'


class SCProductSupport(Parameter):
    """Please specify ServiceCatalog Product Support."""

    type = STRING
    description = 'Please specify ServiceCatalog Product Support.'
    default = 'IT Support can be reached @support'


class SCProductDistributor(Parameter):
    """Please specify ServiceCatalog Product Distributor."""

    type = STRING
    description = 'Please specify ServiceCatalog Product Distributor.'
    default = 'App Vendor'


class SCSupportEmail(Parameter):
    """Please specify ServiceCatalog Product Support Email."""

    type = STRING
    description = 'Please specify ServiceCatalog Product Support Email.'
    default = 'support@example.com'


class SCSupportUrl(Parameter):
    """Please specify ServiceCatalog Product Support URL."""

    type = STRING
    description = 'Please specify ServiceCatalog Product Support URL.'
    default = 'https://www.support.example.com'


class ProvisioningArtifactTemplateUrl(Parameter):
    """Please specify the S3 URL of the template"""

    type = STRING
    description = 'Please specify the S3 URL of the template'
    default = 'https://awsdocs.s3.amazonaws.com/servicecatalog/development-environment.template'


class ProvisioningArtifactNameParameter(Parameter):
    """Please specify ServiceCatalog Product Artifact Name."""

    type = STRING
    description = 'Please specify ServiceCatalog Product Artifact Name.'
    default = 'ProductExample'


class ProvisioningArtifactDescriptionParameter(Parameter):
    """Please specify ServiceCatalog Product Artifact Description."""

    type = STRING
    description = 'Please specify ServiceCatalog Product Artifact Description.'
    default = 'ProductExample'
