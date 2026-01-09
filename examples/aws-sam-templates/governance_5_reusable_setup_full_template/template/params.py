"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class MainRegion(Parameter):
    """Main region for the account"""

    type = STRING
    description = 'Main region for the account'
    default = 'us-west-2'


class AggregateAccount(Parameter):
    """Aggregate account ID"""

    type = STRING
    description = 'Aggregate account ID'
    no_echo = True


class SubAccountList(Parameter):
    """List of sub accounts to be monitored"""

    type = COMMA_DELIMITED_LIST
    description = 'List of sub accounts to be monitored'
    no_echo = True


class IsMainRegionCondition(TemplateCondition):
    logical_id = 'IsMainRegion'
    expression = Equals(MainRegion, AWS_REGION)


class IsAggregateAccountCondition(TemplateCondition):
    logical_id = 'IsAggregateAccount'
    expression = Equals(AggregateAccount, AWS_ACCOUNT_ID)
