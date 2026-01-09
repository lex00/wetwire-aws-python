"""Security resources: DbEngineParameter, DbCredsParameter, DbVersionParameter, DbNameParameter."""

from . import *  # noqa: F403


class DbEngineParameter(ssm.Parameter):
    name = '/myApp/DbEngine'
    type_ = 'String'
    value = DbEngine


class DbCredsParameter(secretsmanager.Secret):
    name = '/myApp/DbCreds'
    secret_string = Sub('{"Username":"${DbUsername}","Password":"${DbPassword}"}')


class DbVersionParameter(ssm.Parameter):
    name = '/myApp/DbVersion'
    type_ = 'String'
    value = DbVersion


class DbNameParameter(secretsmanager.Secret):
    name = '/myApp/DbName'
    secret_string = DbName
