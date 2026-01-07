"""Infra resources: PrivateWaitHandle."""

from . import *  # noqa: F403


class PrivateWaitHandle(cloudformation.WaitConditionHandle):
    resource: cloudformation.WaitConditionHandle
