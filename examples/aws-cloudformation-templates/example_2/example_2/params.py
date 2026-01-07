"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class PermissionBoundaryArn(Parameter):
    """ARN for the Permission Boundary Policy"""

    type = STRING
    description = 'ARN for the Permission Boundary Policy'
