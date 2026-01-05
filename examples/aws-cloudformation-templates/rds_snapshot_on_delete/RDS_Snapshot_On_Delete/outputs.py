"""Template outputs."""

from . import *  # noqa: F403


class JDBCConnectionStringOutput:
    """JDBC connection string for the database"""

    resource: Output
    value = Join('', [
    'jdbc:mysql://',
    MyDB.Endpoint.Address,
    ':',
    MyDB.Endpoint.Port,
    '/MyDatabase',
])
    description = 'JDBC connection string for the database'
