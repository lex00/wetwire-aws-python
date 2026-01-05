"""Infra resources: PrivateWaitHandle, PrivateWaitCondition."""

from . import *  # noqa: F403


class PrivateWaitHandle(cloudformation.WaitConditionHandle):
    pass


class PrivateWaitCondition(cloudformation.WaitCondition):
    handle = PrivateWaitHandle
    timeout = '3600'
    count = 1
    depends_on = [PrivateInstance]
