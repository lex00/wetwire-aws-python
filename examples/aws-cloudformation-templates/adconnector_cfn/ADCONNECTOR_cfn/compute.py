"""Compute resources: ADConnectorLambdaFunction."""

from . import *  # noqa: F403


class ADConnectorLambdaFunctionEnvironment:
    resource: lambda_.Function.Environment
    variables = {
        'LOG_LEVEL': LambdaLogLevel,
    }


class ADConnectorLambdaFunctionContent:
    resource: lambda_.LayerVersion.Content
    s3_bucket = LambdaS3BucketName
    s3_key = LambdaZipFileName


class ADConnectorLambdaFunctionCapacityProviderVpcConfig:
    resource: lambda_.CapacityProvider.CapacityProviderVpcConfig
    subnet_ids = ['PrivateSubnet1ID', 'PrivateSubnet2ID']
    security_group_ids = [ADConnectorDomainMembersSG]


class ADConnectorLambdaFunction(lambda_.Function):
    function_name = LambdaFunctionName
    handler = 'adconnector_custom_resource.lambda_handler'
    role = ADConnectorLambdaRole.Arn
    runtime = lambda_.Runtime.PYTHON3_8
    memory_size = 128
    timeout = 120
    environment = ADConnectorLambdaFunctionEnvironment
    code = ADConnectorLambdaFunctionContent
    vpc_config = ADConnectorLambdaFunctionCapacityProviderVpcConfig
