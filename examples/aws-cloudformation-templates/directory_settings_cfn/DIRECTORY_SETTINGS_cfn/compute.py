"""Compute resources: DirectorySettingsLambdaFunction."""

from . import *  # noqa: F403


class DirectorySettingsLambdaFunctionEnvironment:
    resource: lambda_.Function.Environment
    variables = {
        'LOG_LEVEL': LambdaLogLevel,
    }


class DirectorySettingsLambdaFunctionContent:
    resource: lambda_.LayerVersion.Content
    s3_bucket = LambdaS3BucketName
    s3_key = LambdaZipFileName


class DirectorySettingsLambdaFunctionCapacityProviderVpcConfig:
    resource: lambda_.CapacityProvider.CapacityProviderVpcConfig
    subnet_ids = Subnets
    security_group_ids = SecurityGroups


class DirectorySettingsLambdaFunction(lambda_.Function):
    function_name = LambdaFunctionName
    handler = 'directory_settings_custom_resource.lambda_handler'
    role = DirectorySettingsLambdaRole.Arn
    runtime = lambda_.Runtime.PYTHON3_12
    memory_size = 128
    timeout = 120
    environment = DirectorySettingsLambdaFunctionEnvironment
    code = DirectorySettingsLambdaFunctionContent
    vpc_config = DirectorySettingsLambdaFunctionCapacityProviderVpcConfig
