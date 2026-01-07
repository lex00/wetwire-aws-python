"""Messaging resources: TestQ."""

from . import *  # noqa: F403


class TestQ(sqs.Queue):
    resource: sqs.Queue
    queue_name = 'test-events17'
