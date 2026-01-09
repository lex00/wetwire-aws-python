"""Template outputs."""

from . import *  # noqa: F403


class HttpApiUrlOutput(Output):
    """URL of your API endpoint"""

    value = Sub('https://${HttpApi}.execute-api.${AWS::Region}.${AWS::URLSuffix}/')
    description = 'URL of your API endpoint'


class AppConfigUrlOutput(Output):
    """URL to your application in AppConfig"""

    value = Sub('https://${AWS::Region}.console.aws.amazon.com/systems-manager/appconfig/applications/${AppConfigLambdaApplication}/')
    description = 'URL to your application in AppConfig'


class AppConfigHostedConfigurationUrlOutput(Output):
    """URL to your hosted configuration in AppConfig"""

    value = Sub('https://${AWS::Region}.console.aws.amazon.com/systems-manager/appconfig/applications/${AppConfigLambdaApplication}/configurationprofiles/${AppConfigLambdaConfigurationProfile}/versions')
    description = 'URL to your hosted configuration in AppConfig'
