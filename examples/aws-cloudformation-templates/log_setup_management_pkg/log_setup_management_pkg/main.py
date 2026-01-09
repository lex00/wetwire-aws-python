"""Stack resources."""

from . import *  # noqa: F403


class CentralEventLog(logs.LogGroup):
    log_group_class = logs.LogGroupClass.STANDARD
    log_group_name = CentralEventLogName
    kms_key_id = CentralEventLogKey.Arn
    depends_on = [CentralEventBus]
