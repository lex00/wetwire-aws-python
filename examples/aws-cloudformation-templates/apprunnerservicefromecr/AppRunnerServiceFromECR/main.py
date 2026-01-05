"""Stack resources."""

from . import *  # noqa: F403


class AppRunnerAuthenticationConfiguration(apprunner.Service.AuthenticationConfiguration):
    access_role_arn = AppRunnerRole.Arn


class AppRunnerImageConfiguration(apprunner.Service.ImageConfiguration):
    port = TCPPORT


class AppRunnerImageRepository(apprunner.Service.ImageRepository):
    image_repository_type = 'ECR'
    image_identifier = ECRURL
    image_configuration = AppRunnerImageConfiguration


class AppRunnerSourceConfiguration(apprunner.Service.SourceConfiguration):
    authentication_configuration = AppRunnerAuthenticationConfiguration
    auto_deployments_enabled = True
    image_repository = AppRunnerImageRepository


class AppRunner(apprunner.Service):
    service_name = Join('', [
    AWS_STACK_NAME,
    '-service',
])
    source_configuration = AppRunnerSourceConfiguration
