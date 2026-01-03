"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class Env:
    """Please specify the target Environment. Used for tagging and resource names. Mandatory LOWER CASE."""

    resource: Parameter
    type = STRING
    description = 'Please specify the target Environment. Used for tagging and resource names. Mandatory LOWER CASE.'
    default = 'dev'
    allowed_values = [
    'test',
    'dev',
    'prod',
]


class AppName:
    """Please specify the Application Name. Used for tagging and resource names. Mandatory LOWER CASE."""

    resource: Parameter
    type = STRING
    description = 'Please specify the Application Name. Used for tagging and resource names. Mandatory LOWER CASE.'
    default = 'app'


class Dept:
    """Please specify the Department. Used for tagging"""

    resource: Parameter
    type = STRING
    description = 'Please specify the Department. Used for tagging'
    default = '1234'


class User:
    """Please specify the User. Used for tagging"""

    resource: Parameter
    type = STRING
    description = 'Please specify the User. Used for tagging'
    default = 'User'


class Owner:
    """Please specify the Owner. Used for tagging"""

    resource: Parameter
    type = STRING
    description = 'Please specify the Owner. Used for tagging'
    default = 'Owner'


class ServiceCatalogPortfolioStackName:
    """Please specify the Service Catalog Portfolio Stack Name."""

    resource: Parameter
    type = STRING
    description = 'Please specify the Service Catalog Portfolio Stack Name.'
    default = ''


class SCProductName:
    """Please specify ServiceCatalog Product Name."""

    resource: Parameter
    type = STRING
    description = 'Please specify ServiceCatalog Product Name.'
    default = 'ProductName'


class SCProductDescription:
    """Please specify ServiceCatalog Product Name Description."""

    resource: Parameter
    type = STRING
    description = 'Please specify ServiceCatalog Product Name Description.'
    default = 'ProductDescription'


class SCProductOwner:
    """Please specify ServiceCatalog Product Owner."""

    resource: Parameter
    type = STRING
    description = 'Please specify ServiceCatalog Product Owner.'
    default = 'ProductOwner'


class SCProductSupport:
    """Please specify ServiceCatalog Product Support."""

    resource: Parameter
    type = STRING
    description = 'Please specify ServiceCatalog Product Support.'
    default = 'IT Support can be reached @support'


class SCProductDistributor:
    """Please specify ServiceCatalog Product Distributor."""

    resource: Parameter
    type = STRING
    description = 'Please specify ServiceCatalog Product Distributor.'
    default = 'App Vendor'


class SCSupportEmail:
    """Please specify ServiceCatalog Product Support Email."""

    resource: Parameter
    type = STRING
    description = 'Please specify ServiceCatalog Product Support Email.'
    default = 'support@example.com'


class SCSupportUrl:
    """Please specify ServiceCatalog Product Support URL."""

    resource: Parameter
    type = STRING
    description = 'Please specify ServiceCatalog Product Support URL.'
    default = 'https://www.support.example.com'


class ProvisioningArtifactTemplateUrl:
    """Please specify the S3 URL of the template"""

    resource: Parameter
    type = STRING
    description = 'Please specify the S3 URL of the template'
    default = 'https://awsdocs.s3.amazonaws.com/servicecatalog/development-environment.template'


class ProvisioningArtifactNameParameter:
    """Please specify ServiceCatalog Product Artifact Name."""

    resource: Parameter
    type = STRING
    description = 'Please specify ServiceCatalog Product Artifact Name.'
    default = 'ProductExample'


class ProvisioningArtifactDescriptionParameter:
    """Please specify ServiceCatalog Product Artifact Description."""

    resource: Parameter
    type = STRING
    description = 'Please specify ServiceCatalog Product Artifact Description.'
    default = 'ProductExample'
