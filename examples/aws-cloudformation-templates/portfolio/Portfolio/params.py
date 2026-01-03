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


class ProductEnv:
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


class ProductDept:
    """Please specify the Department. Used for tagging"""

    resource: Parameter
    type = STRING
    description = 'Please specify the Department. Used for tagging'
    default = '1234'


class ProductUser:
    """Please specify the User. Used for tagging"""

    resource: Parameter
    type = STRING
    description = 'Please specify the User. Used for tagging'
    default = 'User'


class ProductOwner:
    """Please specify the Owner. Used for tagging"""

    resource: Parameter
    type = STRING
    description = 'Please specify the Owner. Used for tagging'
    default = 'Owner'


class PortfolioProviderName:
    """Please specify the Portfolio Provider Name."""

    resource: Parameter
    type = STRING
    description = 'Please specify the Portfolio Provider Name.'
    default = 'IT Provider'


class PortfolioDescription:
    """Please specify the Portfolio Description."""

    resource: Parameter
    type = STRING
    description = 'Please specify the Portfolio Description.'
    default = 'Service Catalog Portfolio for Business Unit (BU)'


class PortfolioDisplayName:
    """Please specify the Portfolio Description. Must satisfy regular expression pattern, (^[a-zA-Z0-9_\-]*)"""

    resource: Parameter
    type = STRING
    description = 'Please specify the Portfolio Description. Must satisfy regular expression pattern, (^[a-zA-Z0-9_\\-]*)'
    default = 'Test_Portfolio'


class ActivateProductTagOptions:
    """Activate Custom Tag Options? Used for portfolio tagging"""

    resource: Parameter
    type = STRING
    description = 'Activate Custom Tag Options? Used for portfolio tagging'
    default = 'true'
    allowed_values = [
    'true',
    'false',
]


class ShareThisPortfolio:
    """Please specify if this Portfolio will be Shared with additonal accounts?"""

    resource: Parameter
    type = STRING
    description = 'Please specify if this Portfolio will be Shared with additonal accounts?'
    default = 'false'
    allowed_values = [
    'true',
    'false',
]


class AccountIdOfChildAWSAccount:
    """Please specify the Sub AWS Account ID."""

    resource: Parameter
    type = STRING
    description = 'Please specify the Sub AWS Account ID.'
    default = '1234567890'


class ConditionShareThisPortfolioCondition:
    resource: TemplateCondition
    logical_id = 'ConditionShareThisPortfolio'
    expression = Equals(ShareThisPortfolio, 'true')
