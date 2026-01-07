"""Database resources: myDB."""

from . import *  # noqa: F403


class myDB(rds.DBInstance):
    resource: rds.DBInstance
    allocated_storage = '100'
    db_instance_class = 'db.t3.small'
    backup_retention_period = 7
    engine = 'MySQL'
    iops = '1000'
    master_username = DBUser
    master_user_password = Sub('{{resolve:secretsmanager:${DBCredential}}}')
    publicly_accessible = False
    storage_encrypted = True
    depends_on = [DBCredential]
