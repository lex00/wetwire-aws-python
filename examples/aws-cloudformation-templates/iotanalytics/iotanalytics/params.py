"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class ProjectName:
    resource: Parameter
    type = STRING
    default = 'myIoTAnalyticsProject'


class SqlQuery:
    resource: Parameter
    type = STRING
    default = 'select * from myIoTAnalyticsProject_datastore '


class ScheduleExpression:
    resource: Parameter
    type = STRING
    default = 'cron(1/5 * * * ? *)'
