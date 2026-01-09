"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class MainRegion(Parameter):
    """Main region for the account"""

    type = STRING
    description = 'Main region for the account'
    default = 'us-west-2'


class IsMainRegionCondition(TemplateCondition):
    logical_id = 'IsMainRegion'
    expression = Equals(MainRegion, AWS_REGION)
