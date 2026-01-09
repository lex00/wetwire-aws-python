"""Template outputs."""

from . import *  # noqa: F403


class HelloWorldAPIOutput(Output):
    """API Gateway endpoint URL for Prod environment for First Function"""

    value = Sub('https://${ServerlessRestApi}.execute-api.${AWS::Region}.amazonaws.com/Prod/hello/')
    description = 'API Gateway endpoint URL for Prod environment for First Function'


class HelloWorldFunctionOutput(Output):
    """First Lambda Function ARN"""

    value = HelloWorldFunction.Arn
    description = 'First Lambda Function ARN'


class HelloWorldFunctionIamRoleOutput(Output):
    """Implicit IAM Role created for Hello World function"""

    value = HelloWorldFunctionRole.Arn  # noqa: WAW020 - SAM implicit resource
    description = 'Implicit IAM Role created for Hello World function'
