"""Template outputs."""

from . import *  # noqa: F403


class HelloWorldApiOutput(Output):
    """API Gateway endpoint URL for Prod stage for Hello World function"""

    value = Sub('https://${ServerlessRestApi}.execute-api.${AWS::Region}.amazonaws.com/')
    description = 'API Gateway endpoint URL for Prod stage for Hello World function'


class HelloWorldFunctionOutput(Output):
    """Hello World Lambda Function ARN"""

    value = HelloWorldFunction.Arn
    description = 'Hello World Lambda Function ARN'


class HelloWorldFunctionIamRoleOutput(Output):
    """Implicit IAM Role created for Hello World function"""

    value = HelloWorldFunctionRole.Arn  # noqa: WAW020 - SAM implicit resource
    description = 'Implicit IAM Role created for Hello World function'
