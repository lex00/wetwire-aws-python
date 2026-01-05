"""Messaging resources: EventRule."""

from . import *  # noqa: F403


class EventRuleTarget:
    resource: events.Rule.Target
    arn = Join('', [
    'arn:aws:codepipeline:',
    AWS_REGION,
    ':',
    AWS_ACCOUNT_ID,
    ':',
    Pipeline,
])
    role_arn = EventRole.Arn
    id = 'codepipeline-Pipeline'


class EventRule(events.Rule):
    event_pattern = {
        'source': ['aws.codecommit'],
        'detail-type': ['CodeCommit Repository State Change'],
        'resources': [ImportValue(Sub('${CodeBuildStack}-CodeCommitArn'))],
        'detail': {
            'event': [
                'referenceCreated',
                'referenceUpdated',
            ],
            'referenceType': ['branch'],
            'referenceName': ['main'],
        },
    }
    targets = [EventRuleTarget]
