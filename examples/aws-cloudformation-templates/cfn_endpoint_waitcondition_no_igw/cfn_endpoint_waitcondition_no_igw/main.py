"""Stack resources."""

from . import *  # noqa: F403


class PrivateWaitCondition(cloudformation.WaitCondition):
    handle = PrivateWaitHandle
    timeout = '3600'
    count = 1
    depends_on = [PrivateInstance]
