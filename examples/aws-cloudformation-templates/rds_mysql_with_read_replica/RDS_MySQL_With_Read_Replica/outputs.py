"""Template outputs."""

from . import *  # noqa: F403


class DBCredentialSecretNameArnOutput(Output):
    """Name of the secret containing the database credential"""

    value = DBCredential
    description = 'Name of the secret containing the database credential'


class EC2PlatformOutput(Output):
    """Platform in which this stack is deployed"""

    value = If("IsEC2VPC", 'true', 'EC2VPC')
    description = 'Platform in which this stack is deployed'


class JDBCConnectionStringOutput(Output):
    """JDBC connection string for the master database"""

    value = Join('', [
    'jdbc:mysql://',
    MainDB.Endpoint.Address,
    ':',
    MainDB.Endpoint.Port,
    '/',
    DBName,
])
    description = 'JDBC connection string for the master database'


class ReplicaJDBCConnectionStringOutput(Output):
    """JDBC connection string for the replica database"""

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
