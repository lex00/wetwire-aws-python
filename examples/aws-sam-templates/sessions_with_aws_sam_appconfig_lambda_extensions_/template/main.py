"""Stack resources."""

from . import *  # noqa: F403


class AppConfigLambdaDeploymentStrategy(appconfig.DeploymentStrategy):
    name = AppName
    deployment_duration_in_minutes = 0
    final_bake_time_in_minutes = 0
    growth_factor = 100
    growth_type = 'LINEAR'
    replicate_to = 'NONE'


class AppConfigLambdaApplication(appconfig.Application):
    name = AppName


class AppConfigLambdaEnvironment(appconfig.Environment):
    name = AppName
    application_id = AppConfigLambdaApplication


class AppConfigLambdaConfigurationProfileValidators(appconfig.ConfigurationProfile.Validators):
    content = '{ "$schema": "http://json-schema.org/draft-04/schema#", "type": "object", "properties": { "isEnabled": { "type": "boolean" }, "messageOption": { "type": "string", "minimum": 0 } }, "required": ["isEnabled", "messageOption"] }'
    type_ = 'JSON_SCHEMA'


class AppConfigLambdaConfigurationProfile(appconfig.ConfigurationProfile):
    name = AppName
    application_id = AppConfigLambdaApplication
    location_uri = 'hosted'
    validators = [AppConfigLambdaConfigurationProfileValidators]


class HttpApi(serverless.HttpApi):
    fail_on_warnings = True


class AppConfigLambdaFunctionAllowStatement0(PolicyStatement):
    action = ['appconfig:GetConfiguration']
    resource_arn = [
        Join('', [
    'arn:aws:appconfig:*:*:application/',
    AppConfigLambdaApplication,
]),
        Join('', [
    'arn:aws:appconfig:*:*:application/',
    AppConfigLambdaApplication,
    '/configurationprofile/',
    AppConfigLambdaConfigurationProfile,
]),
        Join('', [
    'arn:aws:appconfig:*:*:application/',
    AppConfigLambdaApplication,
    '/environment/',
    AppConfigLambdaEnvironment,
]),
    ]


class AppConfigLambdaFunctionPolicies0(PolicyDocument):
    statement = [AppConfigLambdaFunctionAllowStatement0]


class AppConfigLambdaFunctionEnvironment(serverless.Function.Environment):
    variables = {
        'APPCONFIG_APPLICATION': AppConfigLambdaApplication,
        'APPCONFIG_ENVIRONMENT': AppConfigLambdaEnvironment,
        'APPCONFIG_CONFIGURATION': AppConfigLambdaConfigurationProfile,
    }


class AppConfigLambdaFunction(serverless.Function):
    code_uri = 'src/'
    handler = 'app.handler'
    runtime = 'nodejs16.x'
    layers = [FindInMap("AppConfigLayer", AWS_REGION, 'ARN')]
    policies = [AppConfigLambdaFunctionPolicies0]
    environment = AppConfigLambdaFunctionEnvironment
    events = {
        'AppConfigLambda': {
            'Type': 'HttpApi',
            'Properties': {
                'ApiId': HttpApi,
                'Path': '/',
                'Method': 'GET',
            },
        },
    }


class AppConfigLambdaConfigurationVersion(appconfig.HostedConfigurationVersion):
    application_id = AppConfigLambdaApplication
    configuration_profile_id = AppConfigLambdaConfigurationProfile
    content = '{ "isEnabled": false, "messageOption": "AppConfig" }'
    content_type = 'application/json'


class AppConfigLambdaDeployment(appconfig.Deployment):
    application_id = AppConfigLambdaApplication
    configuration_profile_id = AppConfigLambdaConfigurationProfile
    configuration_version = AppConfigLambdaConfigurationVersion
    deployment_strategy_id = AppConfigLambdaDeploymentStrategy
    environment_id = AppConfigLambdaEnvironment
