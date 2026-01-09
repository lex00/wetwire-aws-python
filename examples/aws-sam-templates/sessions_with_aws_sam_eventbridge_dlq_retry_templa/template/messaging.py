"""Messaging resources: DLQueue, EBRule."""

from . import *  # noqa: F403


class DLQueue(sqs.Queue):
    pass


class EBRuleDeadLetterConfig(events.Rule.DeadLetterConfig):
    arn = DLQueue.Arn


class EBRuleRetryPolicy(events.Rule.RetryPolicy):
    maximum_event_age_in_seconds = 60
    maximum_retry_attempts = 4


class EBRuleTarget(events.Rule.Target):
    arn = TriggeredFunction.Arn
    id = 'lambdaTarget'
    dead_letter_config = EBRuleDeadLetterConfig
    retry_policy = EBRuleRetryPolicy


class EBRule(events.Rule):
    role_arn = EBRuleRole.Arn
    targets = [EBRuleTarget]
    event_pattern = {
        'source': ['WebApp'],
        'detail-type': ['MyDetailType'],
    }
