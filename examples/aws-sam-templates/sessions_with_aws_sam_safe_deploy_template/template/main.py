"""Stack resources."""

from . import *  # noqa: F403


class BaseAPICorsConfiguration(serverless.HttpApi.CorsConfiguration):
    allow_methods = ['GET']
    allow_origins = ClientDomains


class BaseAPI(serverless.HttpApi):
    cors_configuration = BaseAPICorsConfiguration


class BasePostFunctionTracingConfiguration(serverless.StateMachine.TracingConfiguration):
    enabled = False


class BasePostFunctionAllowStatement0(PolicyStatement):
    action = ['codedeploy:PutLifecycleEventHookExecutionStatus']
    resource_arn = Sub('arn:${AWS::Partition}:codedeploy:${AWS::Region}:${AWS::AccountId}:deploymentgroup:${ServerlessDeploymentApplication}/*')


class BasePostFunctionPolicies0(PolicyDocument):
    statement = [BasePostFunctionAllowStatement0]


class BasePostFunction(serverless.Function):
    handler = 'src/hooks/basepost.lambdaHandler'
    function_name = 'CodeDeployHook_postTrafficHook1'
    deployment_preference = BasePostFunctionTracingConfiguration
    policies = [BasePostFunctionPolicies0]


class BasePreFunctionTracingConfiguration(serverless.StateMachine.TracingConfiguration):
    enabled = False


class BasePreFunctionEnvironment(serverless.Function.Environment):
    variables = {
        'FUNCTION_VERSION': BaseFunction.Version  # noqa: WAW019 - SAM implicit resource,
    }


class BasePreFunctionAllowStatement0(PolicyStatement):
    action = ['codedeploy:PutLifecycleEventHookExecutionStatus']
    resource_arn = Sub('arn:${AWS::Partition}:codedeploy:${AWS::Region}:${AWS::AccountId}:deploymentgroup:${ServerlessDeploymentApplication}/*')


class BasePreFunctionPolicies0(PolicyDocument):
    statement = [BasePreFunctionAllowStatement0]


class BasePreFunctionAllowStatement0_1(PolicyStatement):
    action = ['lambda:InvokeFunction']
    resource_arn = Sub('${FunctionArn}:*', {
    'FunctionArn': BaseFunction.Arn,
})


class BasePreFunctionPolicies1(PolicyDocument):
    statement = [BasePreFunctionAllowStatement0_1]


class BasePreFunction(serverless.Function):
    handler = 'src/hooks/basepre.lambdaHandler'
    function_name = 'CodeDeployHook_preTrafficHook1'
    deployment_preference = BasePreFunctionTracingConfiguration
    environment = BasePreFunctionEnvironment
    policies = [BasePreFunctionPolicies0, BasePreFunctionPolicies1]


class BaseFunction(serverless.Function):
    handler = 'src/base.lambdaHandler'
    description = 'Base lambda function'
    auto_publish_alias = 'live'
    events = {
        'ApiEvent': {
            'Type': 'HttpApi',
            'Properties': {
                'ApiId': BaseAPI,
                'Path': '/',
                'Method': 'GET',
            },
        },
    }
    deployment_preference = {
        'Type': 'AllAtOnce',
        'TriggerConfigurations': [{
            'TriggerTargetArn': AlertTopic,
            'TriggerName': 'BaseAlerts',
            'TriggerEvents': [
                'DeploymentStart',
                'DeploymentSuccess',
                'DeploymentFailure',
                'DeploymentStop',
                'DeploymentRollback',
            ],
        }],
        'Hooks': {
            'PreTraffic': BasePreFunction,
            'PostTraffic': BasePostFunction,
        },
    }


class ResourcesLayer(serverless.LayerVersion):
    layer_name = 'resources'
    content_uri = 'layer/'
    compatible_runtimes = ['nodejs16.x']
    license_info = 'MIT'
    retention_policy = 'Retain'
