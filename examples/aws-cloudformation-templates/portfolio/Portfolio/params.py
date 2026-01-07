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


class ProductEnv(Parameter):
    """Please specify the target Environment. Used for tagging and resource names. Mandatory LOWER CASE."""

    type = STRING
    description = 'Please specify the target Environment. Used for tagging and resource names. Mandatory LOWER CASE.'
    default = 'dev'
    allowed_values = [
    'test',
    'dev',
    'prod',
]


class ProductDept(Parameter):
    """Please specify the Department. Used for tagging"""

    type = STRING
    description = 'Please specify the Department. Used for tagging'
    default = '1234'


class ProductUser(Parameter):
    """Please specify the User. Used for tagging"""

    type = STRING
    description = 'Please specify the User. Used for tagging'
    default = 'User'


class ProductOwner(Parameter):
    """Please specify the Owner. Used for tagging"""

    type = STRING
    description = 'Please specify the Owner. Used for tagging'
    default = 'Owner'


class PortfolioProviderName(Parameter):
    """Please specify the Portfolio Provider Name."""

    type = STRING
    description = 'Please specify the Portfolio Provider Name.'
    default = 'IT Provider'


class PortfolioDescription(Parameter):
    """Please specify the Portfolio Description."""

    type = STRING
    description = 'Please specify the Portfolio Description.'
    default = 'Service Catalog Portfolio for Business Unit (BU)'


class PortfolioDisplayName(Parameter):
    """Please specify the Portfolio Description. Must satisfy regular expression pattern, (^[a-zA-Z0-9_\-]*)"""

    type = STRING
    description = 'Please specify the Portfolio Description. Must satisfy regular expression pattern, (^[a-zA-Z0-9_\\-]*)'
    default = 'Test_Portfolio'


class ActivateProductTagOptions(Parameter):
    """Activate Custom Tag Options? Used for portfolio tagging"""

    type = STRING
    description = 'Activate Custom Tag Options? Used for portfolio tagging'
    default = 'true'
    allowed_values = [
    'true',
    'false',
]


class ShareThisPortfolio(Parameter):
    """Please specify if this Portfolio will be Shared with additonal accounts?"""

    type = STRING
    description = 'Please specify if this Portfolio will be Shared with additonal accounts?'
    default = 'false'
    allowed_values = [
    'true',
    'false',
]


class AccountIdOfChildAWSAccount(Parameter):
    """Please specify the Sub AWS Account ID."""

    type = STRING
    description = 'Please specify the Sub AWS Account ID.'
    default = '1234567890'


class ConditionShareThisPortfolioCondition(TemplateCondition):
    logical_id = 'ConditionShareThisPortfolio'
    expression = Equals(ShareThisPortfolio, 'true')
