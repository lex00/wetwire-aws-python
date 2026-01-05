"""Stack resources."""

from . import *  # noqa: F403


class CentralEventLog:
    resource: logs.LogGroup
    log_group_class = logs.LogGroupClass.STANDARD
    log_group_name = CentralEventLogName
    kms_key_id = CentralEventLogKey.Arn
    retention_in_days = 90
    depends_on = [CentralEventBus]
