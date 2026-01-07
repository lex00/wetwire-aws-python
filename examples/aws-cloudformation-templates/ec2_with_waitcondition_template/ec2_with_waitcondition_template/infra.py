"""Infra resources: KWOSWaitHandle, KWOSWaitCondition."""

from . import *  # noqa: F403


class KWOSWaitHandle(cloudformation.WaitConditionHandle):
    pass


class KWOSWaitCondition(cloudformation.WaitCondition):
    handle = KWOSWaitHandle
    timeout = '300'
