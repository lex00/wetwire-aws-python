"""Template outputs."""

from . import *  # noqa: F403


class TableNameOutput:
    """Name of the newly created DynamoDB table"""

    resource: Output
    value = TableOfBooks
    description = 'Name of the newly created DynamoDB table'
