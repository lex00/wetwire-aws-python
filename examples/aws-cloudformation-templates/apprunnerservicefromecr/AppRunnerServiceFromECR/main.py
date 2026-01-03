"""Stack resources."""

from . import *  # noqa: F403


class AppRunnerAuthenticationConfiguration:
    resource: apprunner.Service.AuthenticationConfiguration
    access_role_arn = AppRunnerRole.Arn


class AppRunnerImageConfiguration:
    resource: apprunner.Service.ImageConfiguration
    port = TCPPORT


class AppRunnerImageRepository:
    resource: apprunner.Service.ImageRepository
    image_repository_type = 'ECR'
    image_identifier = ECRURL
    image_configuration = AppRunnerImageConfiguration


class AppRunnerSourceConfiguration:
    resource: apprunner.Service.SourceConfiguration
    authentication_configuration = AppRunnerAuthenticationConfiguration
    auto_deployments_enabled = True
    image_repository = AppRunnerImageRepository


class AppRunner:
    resource: apprunner.Service
    service_name = Join('', [
    AWS_STACK_NAME,
    '-service',
])
    source_configuration = AppRunnerSourceConfiguration
