"""Template outputs."""

from . import *  # noqa: F403


class UserPoolIdOutput(Output):
    """User pool ID"""

    value = UserPool
    description = 'User pool ID'
    export_name = Sub('${AppName}:UserPoolId')


class UserPoolClientIdOutput(Output):
    """Application client ID"""

    value = UserPoolClient
    description = 'Application client ID'


class AuthUrlOutput(Output):
    """URL used for authentication"""

    value = Sub('https://${UserPoolDomain}.auth.${AWS::Region}.amazoncognito.com')
    description = 'URL used for authentication'
