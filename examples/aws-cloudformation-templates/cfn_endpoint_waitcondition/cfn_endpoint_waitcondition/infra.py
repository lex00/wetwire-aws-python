"""Infra resources: PrivateWaitHandle."""

from . import *  # noqa: F403


class PrivateWaitHandle:
    resource: cloudformation.WaitConditionHandle
