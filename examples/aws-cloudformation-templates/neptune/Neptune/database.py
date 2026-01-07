"""Database resources: NeptuneDBSubnetGroup, NeptuneDBClusterParameterGroup, NeptuneDBCluster, NeptuneDBParameterGroup, NeptuneDBInstance."""

from . import *  # noqa: F403


class NeptuneDBSubnetGroup(neptune.DBSubnetGroup):
    resource: neptune.DBSubnetGroup
    db_subnet_group_description = Sub('CloudFormation managed Neptune DB Subnet Group - ${Env}-${AppName}-subnet-group')
    db_subnet_group_name = NeptuneDBSubnetGroupName
    subnet_ids = [ImportValue(Sub('${VPCStack}-PrivateSubnet1')), ImportValue(Sub('${VPCStack}-PrivateSubnet2'))]
    tags = [{
        'Key': 'Name',
        'Value': Sub('${Env}-${AppName}-subnet-group'),
    }, {
        'Key': 'App',
        'Value': AppName,
    }, {
        'Key': 'Compliance',
        'Value': 'Compliance',
    }, {
        'Key': 'Env',
        'Value': Env,
    }, {
        'Key': 'User',
        'Value': User,
    }, {
        'Key': 'Owner',
        'Value': Owner,
    }, {
        'Key': 'Tier',
        'Value': Tier,
    }, {
        'Key': 'Version',
        'Value': Version,
    }, {
        'Key': 'Storage',
        'Value': Storage,
    }]


class NeptuneDBClusterParameterGroup(neptune.DBClusterParameterGroup):
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
        'Value': AppName,
    }, {
        'Key': 'Compliance',
        'Value': 'Compliance',
    }, {
        'Key': 'Env',
        'Value': Env,
    }, {
        'Key': 'User',
        'Value': User,
    }, {
        'Key': 'Owner',
        'Value': Owner,
    }, {
        'Key': 'Tier',
        'Value': Tier,
    }, {
        'Key': 'Version',
        'Value': Version,
    }, {
        'Key': 'Storage',
        'Value': Storage,
    }]


class NeptuneDBCluster(neptune.DBCluster):
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
        'Value': AppName,
    }, {
        'Key': 'Compliance',
        'Value': 'Compliance',
    }, {
        'Key': 'Env',
        'Value': Env,
    }, {
        'Key': 'User',
        'Value': User,
    }, {
        'Key': 'Owner',
        'Value': Owner,
    }, {
        'Key': 'Tier',
        'Value': Tier,
    }, {
        'Key': 'Version',
        'Value': Version,
    }, {
        'Key': 'Storage',
        'Value': Storage,
    }]
    depends_on = [NeptuneDBSG]


class NeptuneDBParameterGroup(neptune.DBParameterGroup):
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
        'Value': AppName,
    }, {
        'Key': 'Compliance',
        'Value': 'Compliance',
    }, {
        'Key': 'Env',
        'Value': Env,
    }, {
        'Key': 'User',
        'Value': User,
    }, {
        'Key': 'Owner',
        'Value': Owner,
    }, {
        'Key': 'Tier',
        'Value': Tier,
    }, {
        'Key': 'Version',
        'Value': Version,
    }, {
        'Key': 'Storage',
        'Value': Storage,
    }]


class NeptuneDBInstance(neptune.DBInstance):
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
        'Value': AppName,
    }, {
        'Key': 'Compliance',
        'Value': 'Compliance',
    }, {
        'Key': 'Env',
        'Value': Env,
    }, {
        'Key': 'User',
        'Value': User,
    }, {
        'Key': 'Owner',
        'Value': Owner,
    }, {
        'Key': 'Tier',
        'Value': Tier,
    }, {
        'Key': 'Version',
        'Value': Version,
    }, {
        'Key': 'Storage',
        'Value': Storage,
    }]
