"""Template outputs."""

from . import *  # noqa: F403


class HelloWorldApiOutput(Output):
    """API Gateway endpoint URL for Prod stage for Hello World function"""

    value = Sub('https://${MyHttpApi}.execute-api.${AWS::Region}.amazonaws.com')
    description = 'API Gateway endpoint URL for Prod stage for Hello World function'
