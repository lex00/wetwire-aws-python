"""Infra resources: KWOSWaitHandle, KWOSWaitCondition."""

from . import *  # noqa: F403


class KWOSWaitHandle:
    resource: cloudformation.WaitConditionHandle


class KWOSWaitCondition:
    resource: cloudformation.WaitCondition
    handle = KWOSWaitHandle
    timeout = '300'
