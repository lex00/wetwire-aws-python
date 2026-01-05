"""Messaging resources: DeadLetterQueue, CentralEventBus, CentralEventRule, CentralEventBusPolicy."""

from . import *  # noqa: F403


class DeadLetterQueue(sqs.Queue):
    queue_name = Sub('${CentralEventBusName}-DLQ')


class CentralEventBusDeadLetterConfig:
    resource: events.Rule.DeadLetterConfig
    arn = DeadLetterQueue.Arn


class CentralEventBus(events.EventBus):
    description = 'A custom event bus in the central account to be used as a destination for events from a rule in target accounts'
    name = CentralEventBusName
    dead_letter_config = CentralEventBusDeadLetterConfig


class CentralEventRuleDeadLetterConfig:
    resource: events.Rule.DeadLetterConfig
    arn = DeadLetterQueue.Arn


class CentralEventRuleTarget:
    resource: events.Rule.Target
    arn = CentralEventLog.Arn
    id = 'CloudFormationLogsToCentralGroup'
    dead_letter_config = CentralEventRuleDeadLetterConfig


class CentralEventRule(events.Rule):
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


class CentralEventBusPolicy(events.EventBusPolicy):
    event_bus_name = CentralEventBus
    statement_id = 'CentralEventBusPolicyStatement'
    statement = {
        'Effect': 'Allow',
        'Principal': '*',
        'Action': 'events:PutEvents',
        'Resource': Sub('arn:aws:events:${AWS::Region}:${AWS::AccountId}:event-bus/${CentralEventBusName}'),
        'Condition': {
            'StringEquals': {
                'aws:PrincipalOrgID': OrgID,
            },
        },
    }
