"""Database resources: NeptuneDBSubnetGroup, NeptuneDBParameterGroup, NeptuneDBClusterParameterGroup, NeptuneDBCluster, NeptuneDBInstance."""

from . import *  # noqa: F403


class NeptuneDBSubnetGroup:
    resource: neptune.DBSubnetGroup
    db_subnet_group_description = Sub('CloudFormation managed Neptune DB Subnet Group - ${Env}-${AppName}-subnet-group')
    db_subnet_group_name = NeptuneDBSubnetGroupName
    subnet_ids = [ImportValue(Sub('${VPCStack}-PrivateSubnet1')), ImportValue(Sub('${VPCStack}-PrivateSubnet2'))]
    tags = [{
        'Key': 'Name',
        'Value': Sub('${Env}-${AppName}-subnet-group'),
    }, {
        'Key': 'App',
        'Value': Sub('${AppName}'),
    }, {
        'Key': 'Compliance',
        'Value': 'Compliance',
    }, {
        'Key': 'Env',
        'Value': Sub('${Env}'),
    }, {
        'Key': 'User',
        'Value': Sub('${User}'),
    }, {
        'Key': 'Owner',
        'Value': Sub('${Owner}'),
    }, {
        'Key': 'Tier',
        'Value': Sub('${Tier}'),
    }, {
        'Key': 'Version',
        'Value': Sub('${Version}'),
    }, {
        'Key': 'Storage',
        'Value': Sub('${Storage}'),
    }]


class NeptuneDBParameterGroup:
    resource: neptune.DBParameterGroup
    description = Sub('CloudFormation managed Neptune DB Parameter Group - ${Env}-${AppName}-parameter-group')
    parameters = {
        'neptune_query_timeout': NeptuneQueryTimeout,
    }
    family = 'neptune1'
    name = Sub('${Env}-${AppName}-parameter-group')
    tags = [{
        'Key': 'Name',
        'Value': Sub('${Env}-${AppName}-parameter-group'),
    }, {
        'Key': 'App',
        'Value': Sub('${AppName}'),
    }, {
        'Key': 'Compliance',
        'Value': 'Compliance',
    }, {
        'Key': 'Env',
        'Value': Sub('${Env}'),
    }, {
        'Key': 'User',
        'Value': Sub('${User}'),
    }, {
        'Key': 'Owner',
        'Value': Sub('${Owner}'),
    }, {
        'Key': 'Tier',
        'Value': Sub('${Tier}'),
    }, {
        'Key': 'Version',
        'Value': Sub('${Version}'),
    }, {
        'Key': 'Storage',
        'Value': Sub('${Storage}'),
    }]


class NeptuneDBClusterParameterGroup:
    resource: neptune.DBClusterParameterGroup
    description = Sub('CloudFormation managed Neptune DB Cluster Parameter Group - ${Env}-${AppName}-cluster-parameter-group')
    parameters = {
        'neptune_enable_audit_log': If("EnableAuditLogUpload", 1, 0),
    }
    family = 'neptune1'
    name = Sub('${Env}-${AppName}-neptune-cluster-parameter-group')
    tags = [{
        'Key': 'Name',
        'Value': Sub('${Env}-${AppName}-cluster-parameter-group'),
    }, {
        'Key': 'App',
        'Value': Sub('${AppName}'),
    }, {
        'Key': 'Compliance',
        'Value': 'Compliance',
    }, {
        'Key': 'Env',
        'Value': Sub('${Env}'),
    }, {
        'Key': 'User',
        'Value': Sub('${User}'),
    }, {
        'Key': 'Owner',
        'Value': Sub('${Owner}'),
    }, {
        'Key': 'Tier',
        'Value': Sub('${Tier}'),
    }, {
        'Key': 'Version',
        'Value': Sub('${Version}'),
    }, {
        'Key': 'Storage',
        'Value': Sub('${Storage}'),
    }]


class NeptuneDBCluster:
    resource: neptune.DBCluster
    backup_retention_period = BackupRetentionPeriod
    db_cluster_identifier = DBClusterIdentifier
    db_cluster_parameter_group_name = NeptuneDBClusterParameterGroup
    db_subnet_group_name = NeptuneDBSubnetGroup
    iam_auth_enabled = IAMAuthEnabled
    db_port = Port
    preferred_backup_window = NeptuneDBClusterPreferredBackupWindow
    preferred_maintenance_window = NeptuneDBClusterPreferredMaintenanceWindow
    storage_encrypted = StorageEncrypted
    vpc_security_group_ids = [NeptuneDBSG]
    tags = [{
        'Key': 'Name',
        'Value': Sub('${Env}-${AppName}-Cluster'),
    }, {
        'Key': 'App',
        'Value': Sub('${AppName}'),
    }, {
        'Key': 'Compliance',
        'Value': 'Compliance',
    }, {
        'Key': 'Env',
        'Value': Sub('${Env}'),
    }, {
        'Key': 'User',
        'Value': Sub('${User}'),
    }, {
        'Key': 'Owner',
        'Value': Sub('${Owner}'),
    }, {
        'Key': 'Tier',
        'Value': Sub('${Tier}'),
    }, {
        'Key': 'Version',
        'Value': Sub('${Version}'),
    }, {
        'Key': 'Storage',
        'Value': Sub('${Storage}'),
    }]
    depends_on = [NeptuneDBSG]


class NeptuneDBInstance:
    resource: neptune.DBInstance
    allow_major_version_upgrade = MajorVersionUpgrade
    auto_minor_version_upgrade = MinorVersionUpgrade
    db_cluster_identifier = NeptuneDBCluster
    db_instance_class = DBInstanceClass
    db_parameter_group_name = NeptuneDBParameterGroup
    db_subnet_group_name = NeptuneDBSubnetGroup
    preferred_maintenance_window = NeptuneDBInstancePreferredMaintenanceWindow
    tags = [{
        'Key': 'Name',
        'Value': Sub('${Env}-${AppName}-Instance'),
    }, {
        'Key': 'App',
        'Value': Sub('${AppName}'),
    }, {
        'Key': 'Compliance',
        'Value': 'Compliance',
    }, {
        'Key': 'Env',
        'Value': Sub('${Env}'),
    }, {
        'Key': 'User',
        'Value': Sub('${User}'),
    }, {
        'Key': 'Owner',
        'Value': Sub('${Owner}'),
    }, {
        'Key': 'Tier',
        'Value': Sub('${Tier}'),
    }, {
        'Key': 'Version',
        'Value': Sub('${Version}'),
    }, {
        'Key': 'Storage',
        'Value': Sub('${Storage}'),
    }]
