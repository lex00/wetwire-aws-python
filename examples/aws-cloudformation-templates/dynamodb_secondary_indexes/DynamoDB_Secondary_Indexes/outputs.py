"""Template outputs."""

from . import *  # noqa: F403


class TableNameOutput(Output):
    """Name of the newly created DynamoDB table"""

    value = TableOfBooks
    description = 'Name of the newly created DynamoDB table'
