"""Messaging resources: TestQ."""

from . import *  # noqa: F403


class TestQ(sqs.Queue):
    queue_name = 'test-events17'
