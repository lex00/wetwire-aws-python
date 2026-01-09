"""Stack resources."""

from . import *  # noqa: F403


class LambdaFunctionEnvironment(serverless.Function.Environment):
    variables = {
        'DB_ENGINE': DbEngine,
        'DB_VERSION': '{{resolve:ssm:/myApp/DbVersion:1}}',
        'DB_NAME': '{{resolve:secretsmanager:/myApp/DbName}}',
        'DB_USERNAME': '{{resolve:secretsmanager:/myApp/DbCreds:SecretString:Username}}',
        'DB_PASSWORD': '{{resolve:secretsmanager:/myApp/DbCreds:SecretString:Password}}',
    }


class LambdaFunction(serverless.Function):
    code_uri = 'src/'
    runtime = 'nodejs16.x'
    handler = 'app.lambdaHandler'
    environment = LambdaFunctionEnvironment
