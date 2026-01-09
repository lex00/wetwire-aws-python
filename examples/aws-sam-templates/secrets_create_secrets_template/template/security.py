"""Security resources: DbNameParameter, DbEngineParameter, DbVersionParameter, DbCredsParameter."""

from . import *  # noqa: F403


class DbNameParameter(secretsmanager.Secret):
    name = '/myApp/DbName'
    secret_string = DbName


class DbEngineParameter(ssm.Parameter):
    name = '/myApp/DbEngine'
    type_ = 'String'
    value = DbEngine


class DbVersionParameter(ssm.Parameter):
    name = '/myApp/DbVersion'
    type_ = 'String'
    value = DbVersion


class DbCredsParameter(secretsmanager.Secret):
    name = '/myApp/DbCreds'
    secret_string = Sub('{"Username":"${DbUsername}","Password":"${DbPassword}"}')
