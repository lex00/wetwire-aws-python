"""Template outputs."""

from . import *  # noqa: F403


class TableNameOutput(Output):
    """Table name of the newly created DynamoDB table"""

    value = myDynamoDBTable
    description = 'Table name of the newly created DynamoDB table'
