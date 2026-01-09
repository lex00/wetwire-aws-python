"""Template outputs."""

from . import *  # noqa: F403


class APIUrlOutput(Output):
    """HTTP API endpoint URL"""

    value = Sub('https://${ServerlessHttpApi}.execute-api.${AWS::Region}.amazonaws.com')
    description = 'HTTP API endpoint URL'


class MyNotificationArnOutput(Output):
    """Topic ARN"""

    value = AWS_NOTIFICATION_ARNS
    description = 'Topic ARN'
