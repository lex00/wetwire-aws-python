"""Template outputs."""

from . import *  # noqa: F403


class SiteURLOutput(Output):
    value = Sub('https://${SiteDistribution.DomainName}')


class RedirectURIOutput(Output):
    value = Sub('https://${SiteDistribution.DomainName}/index.html')


class AppNameOutput(Output):
    value = AppName


class RestApiInvokeURLOutput(Output):
    value = Sub('https://${RestApi}.execute-api.${AWS::Region}.amazonaws.com/${RestApiStage}')


class AppClientIdOutput(Output):
    value = CognitoClient


class CognitoDomainPrefixOutput(Output):
    value = AppName
