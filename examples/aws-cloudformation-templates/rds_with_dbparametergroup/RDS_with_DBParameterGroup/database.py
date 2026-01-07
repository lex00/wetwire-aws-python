"""Database resources: MyRDSParamGroup, MyDB."""

from . import *  # noqa: F403


class MyRDSParamGroup(rds.DBParameterGroup):
    resource: rds.DBParameterGroup
    family = 'MySQL8.0'
    description = 'CloudFormation Sample Database Parameter Group'
    parameters = {
        'autocommit': '1',
        'general_log': '1',
    }


class MyDB(rds.DBInstance):
    resource: rds.DBInstance
    db_name = DBName
    allocated_storage = '5'
    db_instance_class = 'db.t3.small'
    backup_retention_period = 7
    engine = 'MySQL'
    engine_version = '8.0.36'
    master_username = DBUser
    manage_master_user_password = True
    db_parameter_group_name = MyRDSParamGroup
    publicly_accessible = False
    storage_encrypted = True
    deletion_policy = 'Snapshot'
