"""Template outputs."""

from . import *  # noqa: F403


class DBCredentialSecretNameArnOutput:
    """Name of the secret containing the database credential"""

    resource: Output
    value = DBCredential
    description = 'Name of the secret containing the database credential'


class EC2PlatformOutput:
    """Platform in which this stack is deployed"""

    resource: Output
    value = If("IsEC2VPC", 'true', 'EC2VPC')
    description = 'Platform in which this stack is deployed'


class JDBCConnectionStringOutput:
    """JDBC connection string for the master database"""

    resource: Output
    value = Join('', [
    'jdbc:mysql://',
    MainDB.Endpoint.Address,
    ':',
    MainDB.Endpoint.Port,
    '/',
    DBName,
])
    description = 'JDBC connection string for the master database'


class ReplicaJDBCConnectionStringOutput:
    """JDBC connection string for the replica database"""

    resource: Output
    value = Join('', [
    'jdbc:mysql://',
    ReplicaDB.Endpoint.Address,
    ':',
    ReplicaDB.Endpoint.Port,
    '/',
    DBName,
])
    description = 'JDBC connection string for the replica database'
    condition = 'EnableReadReplica'
