"""Template outputs."""

from . import *  # noqa: F403


class SiteURLOutput:
    resource: Output
    value = Sub('https://${SiteDistribution.DomainName}')


class RedirectURIOutput:
    resource: Output
    value = Sub('https://${SiteDistribution.DomainName}/index.html')


class AppNameOutput:
    resource: Output
    value = AppName


class RestApiInvokeURLOutput:
    resource: Output
    value = Sub('https://${RestApi}.execute-api.${AWS::Region}.amazonaws.com/${RestApiStage}')


class AppClientIdOutput:
    resource: Output
    value = CognitoClient


class CognitoDomainPrefixOutput:
    resource: Output
    value = AppName
