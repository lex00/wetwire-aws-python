"""Template outputs."""

from . import *  # noqa: F403


class TableNameOutput:
    """Table name of the newly created DynamoDB table"""

    resource: Output
    value = myDynamoDBTable
    description = 'Table name of the newly created DynamoDB table'
