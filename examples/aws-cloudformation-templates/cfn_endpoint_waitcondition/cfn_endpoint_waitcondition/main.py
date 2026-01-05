"""Stack resources."""

from . import *  # noqa: F403


class PrivateWaitCondition:
    resource: cloudformation.WaitCondition
    handle = PrivateWaitHandle
    timeout = '3600'
    count = 1
    depends_on = [PrivateInstance]
