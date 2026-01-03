"""Database resources: AuroraDBSubnetGroup, AuroraCluster, AuroraDB."""

from . import *  # noqa: F403


class AuroraDBSubnetGroup:
    resource: rds.DBSubnetGroup
    db_subnet_group_description = 'Subnets available for the Aurora SampleDB DB Instance'
    subnet_ids = [DBSubnet1, DBSubnet2]


class AuroraCluster:
    resource: rds.DBCluster
    database_name = 'dms_sample'
    backup_retention_period = 7
    db_subnet_group_name = AuroraDBSubnetGroup
    engine = 'aurora-postgresql'
    snapshot_identifier = SnapshotIdentifier
    vpc_security_group_ids = [AuroraSecurityGroup]
    storage_encrypted = True
    deletion_policy = 'Retain'


class AuroraDBTagFormat:
    resource: rds.DBProxy.TagFormat
    key = 'Application'
    value = AWS_STACK_ID


class AuroraDB:
    resource: rds.DBInstance
    db_cluster_identifier = AuroraCluster
    db_instance_class = 'db.t3.medium'
    db_instance_identifier = 'dms-sample'
    db_subnet_group_name = AuroraDBSubnetGroup
    engine = 'aurora-postgresql'
    multi_az = False
    publicly_accessible = False
    tags = [AuroraDBTagFormat]
    depends_on = [AuroraCluster]
    deletion_policy = 'Retain'
