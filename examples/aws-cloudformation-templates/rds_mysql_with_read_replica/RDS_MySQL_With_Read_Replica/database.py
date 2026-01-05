"""Database resources: MainDB, ReplicaDB."""

from . import *  # noqa: F403


class MainDBTagFormat:
    resource: rds.DBProxyEndpoint.TagFormat
    key = 'Name'
    value = 'Master Database'


class MainDB(rds.DBInstance):
    db_name = DBName
    allocated_storage = DBAllocatedStorage
    backup_retention_period = 7
    db_instance_class = DBInstanceClass
    engine = 'MySQL'
    master_username = DBUser
    master_user_password = Sub('{{resolve:secretsmanager:${DBCredential}}}')
    multi_az = MultiAZ
    publicly_accessible = False
    storage_encrypted = True
    tags = [MainDBTagFormat]
    vpc_security_groups = If("IsEC2VPC", [DBEC2SecurityGroup.GroupId], AWS_NO_VALUE)
    depends_on = [DBCredential]
    deletion_policy = 'Snapshot'


class ReplicaDBTagFormat:
    resource: rds.DBProxyEndpoint.TagFormat
    key = 'Name'
    value = 'Read Replica Database'


class ReplicaDB(rds.DBInstance):
    source_db_instance_identifier = MainDB
    publicly_accessible = False
    db_instance_class = DBInstanceClass
    tags = [ReplicaDBTagFormat]
    condition = 'EnableReadReplica'
    deletion_policy = 'Retain'
