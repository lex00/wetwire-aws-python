"""Infra resources: PrivateWaitHandle, PrivateWaitCondition."""

from . import *  # noqa: F403


class PrivateWaitHandle:
    resource: cloudformation.WaitConditionHandle


class PrivateWaitCondition:
    resource: cloudformation.WaitCondition
    handle = PrivateWaitHandle
    timeout = '3600'
    count = 1
    depends_on = [PrivateInstance]
