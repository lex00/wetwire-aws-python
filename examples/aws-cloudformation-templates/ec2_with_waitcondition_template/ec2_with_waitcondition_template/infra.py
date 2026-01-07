"""Infra resources: KWOSWaitHandle, KWOSWaitCondition."""

from . import *  # noqa: F403


class KWOSWaitHandle(cloudformation.WaitConditionHandle):
    resource: cloudformation.WaitConditionHandle


class KWOSWaitCondition(cloudformation.WaitCondition):
    resource: cloudformation.WaitCondition
    handle = KWOSWaitHandle
    timeout = '300'
