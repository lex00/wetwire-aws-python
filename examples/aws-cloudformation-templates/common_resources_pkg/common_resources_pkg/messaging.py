"""Messaging resources: TestQ."""

from . import *  # noqa: F403


class TestQ:
    resource: sqs.Queue
    queue_name = 'test-events17'
