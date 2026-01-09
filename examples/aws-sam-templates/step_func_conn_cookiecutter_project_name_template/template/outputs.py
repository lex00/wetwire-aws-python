"""Template outputs."""

from . import *  # noqa: F403


class StockTradingStateMachineArnOutput(Output):
    """Stock Trading State machine ARN"""

    value = StockTradingStateMachine
    description = 'Stock Trading State machine ARN'


class StockTradingStateMachineRoleArnOutput(Output):
    """IAM Role created for Stock Trading State machine based on the specified SAM Policy Templates"""

    value = StockTradingStateMachineRole.Arn  # noqa: WAW020 - SAM implicit resource
    description = 'IAM Role created for Stock Trading State machine based on the specified SAM Policy Templates'
