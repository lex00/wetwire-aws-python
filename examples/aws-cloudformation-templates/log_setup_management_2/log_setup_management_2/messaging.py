"""Messaging resources: DeadLetterQueue, CentralEventBus, CentralEventBusPolicy."""

from . import *  # noqa: F403


class DeadLetterQueue(sqs.Queue):
    resource: sqs.Queue
    queue_name = Sub('${CentralEventBusName}-DLQ')
    kms_master_key_id = KmsKeyId


class CentralEventBusDeadLetterConfig(events.Rule.DeadLetterConfig):
    arn = DeadLetterQueue.Arn


class CentralEventBus(events.EventBus):
    resource: events.EventBus
    description = 'A custom event bus in the central account to be used as a destination for events from a rule in target accounts'
    name = CentralEventBusName
    dead_letter_config = CentralEventBusDeadLetterConfig


class CentralEventBusPolicy(events.EventBusPolicy):
    resource: events.EventBusPolicy
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
