"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class ProjectName(Parameter):
    type = STRING
    default = 'myIoTAnalyticsProject'


class SqlQuery(Parameter):
    type = STRING
    default = 'select * from myIoTAnalyticsProject_datastore '


class ScheduleExpression(Parameter):
    type = STRING
    default = 'cron(1/5 * * * ? *)'
