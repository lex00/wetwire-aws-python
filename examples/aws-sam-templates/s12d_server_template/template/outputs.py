"""Template outputs."""

from . import *  # noqa: F403


class VueAppNameOutput(Output):
    """Name of your application"""

    value = AppName
    description = 'Name of your application'


class VueAppAPIRootOutput(Output):
    """API Gateway endpoint URL for linker"""

    value = CloudFrontDistro.DomainName
    description = 'API Gateway endpoint URL for linker'


class VueAppAuthDomainOutput(Output):
    """Domain used for authentication"""

    value = Sub('https://${AppName}-${AWS::AccountId}.auth.${AWS::Region}.amazoncognito.com')
    description = 'Domain used for authentication'


class VueAppClientIdOutput(Output):
    """Cognito User Pool Client Id"""

    value = UserPoolClient
    description = 'Cognito User Pool Client Id'
