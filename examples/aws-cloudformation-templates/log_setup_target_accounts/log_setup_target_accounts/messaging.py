"""Messaging resources: DeadLetterQueue, CloudFormationEventRule, DeadLetterQueuePolicy."""

from . import *  # noqa: F403


class DeadLetterQueue:
    resource: sqs.Queue
    queue_name = 'CloudFormation-Logs-DLQ'


class CloudFormationEventRuleDeadLetterConfig:
    resource: events.Rule.DeadLetterConfig
    arn = DeadLetterQueue.Arn


class CloudFormationEventRuleTarget:
    resource: events.Rule.Target
    arn = CentralEventBusArn
    role_arn = EventBridgeRole.Arn
    id = 'CentralEventBus'
    dead_letter_config = CloudFormationEventRuleDeadLetterConfig


class CloudFormationEventRule:
    resource: events.Rule
    name = 'CloudFormationEventRule'
    event_bus_name = Sub('arn:aws:events:${AWS::Region}:${AWS::AccountId}:event-bus/default')
    event_pattern = {
        'source': ['aws.cloudformation'],
    }
    state = events.RuleState.ENABLED
    targets = [CloudFormationEventRuleTarget]


class DeadLetterQueuePolicyAllowStatement0:
    resource: PolicyStatement
    sid = 'AllowEventBridgeToWriteLogs'
    principal = {
        'Service': 'events.amazonaws.com',
    }
    action = 'sqs:SendMessage'
    resource_arn = DeadLetterQueue.Arn
    condition = {
        ARN_LIKE: {
            'aws:SourceArn': Sub('arn:aws:events:${AWS::Region}:${AWS::AccountId}:rule/CloudFormationEventRule'),
        },
    }


class DeadLetterQueuePolicyPolicyDocument:
    resource: PolicyDocument
    statement = [DeadLetterQueuePolicyAllowStatement0]


class DeadLetterQueuePolicy:
    resource: sqs.QueuePolicy
    policy_document = DeadLetterQueuePolicyPolicyDocument
    queues = [DeadLetterQueue]
