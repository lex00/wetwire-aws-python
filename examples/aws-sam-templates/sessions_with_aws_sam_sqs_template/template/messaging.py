"""Messaging resources: DeadLetter, RawQueue, RawQueuePolicy."""

from . import *  # noqa: F403


class DeadLetter(sqs.Queue):
    pass


class RawQueue(sqs.Queue):
    delay_seconds = 0
    redrive_policy = {
        'deadLetterTargetArn': DeadLetter.Arn,
        'maxReceiveCount': 4,
    }
    tags = [{
        'Key': 'Series',
        'Value': 'SWS',
    }]
    visibility_timeout = 120


class RawQueuePolicyAllowStatement0(PolicyStatement):
    principal = {
        'AWS': [
            ['desired account number'],
            ['desired user or role ARN'],
        ],
    }
    action = ['sqs:SendMessage']
    resource_arn = RawQueue.Arn
    condition = {
        DATE_GREATER_THAN: {
            'aws:CurrentTime': '2020-04-28T12:00Z',
        },
        DATE_LESS_THAN: {
            'aws:CurrentTime': '2020-05-01T12:00Z',
        },
    }


class RawQueuePolicyPolicyDocument(PolicyDocument):
    statement = [RawQueuePolicyAllowStatement0]


class RawQueuePolicy(sqs.QueuePolicy):
    policy_document = RawQueuePolicyPolicyDocument
    queues = [RawQueue]
