"""Infra resources: PrivateWaitHandle, PrivateWaitCondition."""

from . import *  # noqa: F403


class PrivateWaitHandle(cloudformation.WaitConditionHandle):
    resource: cloudformation.WaitConditionHandle


class PrivateWaitCondition(cloudformation.WaitCondition):
    resource: cloudformation.WaitCondition
    handle = PrivateWaitHandle
    timeout = '3600'
    count = 1
    depends_on = [PrivateInstance]
