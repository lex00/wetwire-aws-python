"""Stack resources."""

from . import *  # noqa: F403


class CentralEventRuleDeadLetterConfig:
    resource: events.Rule.DeadLetterConfig
    arn = DeadLetterQueue.Arn


class CentralEventRuleTarget:
    resource: events.Rule.Target
    arn = CentralEventLog.Arn
    id = 'CloudFormationLogsToCentralGroup'
    dead_letter_config = CentralEventRuleDeadLetterConfig


class CentralEventRule:
    resource: events.Rule
    name = 'CloudFormationLogs'
    event_bus_name = CentralEventBusName
    state = events.RuleState.ENABLED
    event_pattern = {
        'source': [{
            'prefix': '',
        }],
    }
    targets = [CentralEventRuleTarget]
    depends_on = [CentralEventLog]
