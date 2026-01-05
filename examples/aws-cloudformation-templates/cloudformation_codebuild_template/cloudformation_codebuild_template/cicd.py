"""Cicd resources: AppDeploy, AppBuild, CodeCommitRepo."""

from . import *  # noqa: F403


class AppDeployArtifacts:
    resource: codebuild.Project.Artifacts
    type_ = 'CODEPIPELINE'
    encryption_disabled = True


class AppDeployEnvironmentVariable:
    resource: codebuild.Project.EnvironmentVariable
    name = 'SAMPLEENVVAR'
    type_ = 'PLAINTEXT'
    value = 'test'


class AppDeployEnvironment:
    resource: codebuild.Project.Environment
    compute_type = 'BUILD_GENERAL1_SMALL'
    environment_variables = [AppDeployEnvironmentVariable]
    image = DockerImage
    type_ = 'LINUX_CONTAINER'


class AppDeploySource:
    resource: codebuild.Project.Source
    type_ = 'CODEPIPELINE'
    build_spec = 'codebuild-app-deploy.yml'


class AppDeploy(codebuild.Project):
    name = Sub('${AWS::StackName}-app-deploy')
    artifacts = AppDeployArtifacts
    environment = AppDeployEnvironment
    service_role = CodeBuildRole
    source = AppDeploySource


class AppBuildArtifacts:
    resource: codebuild.Project.Artifacts
    type_ = 'CODEPIPELINE'
    encryption_disabled = True


class AppBuildEnvironmentVariable:
    resource: codebuild.Project.EnvironmentVariable
    name = 'SAMPLEENVVAR'
    type_ = 'PLAINTEXT'
    value = 'test'


class AppBuildEnvironment:
    resource: codebuild.Project.Environment
    compute_type = 'BUILD_GENERAL1_SMALL'
    environment_variables = [AppBuildEnvironmentVariable]
    image = DockerImage
    type_ = 'LINUX_CONTAINER'


class AppBuildSource:
    resource: codebuild.Project.Source
    type_ = 'CODEPIPELINE'
    build_spec = 'codebuild-app-build.yml'


class AppBuild(codebuild.Project):
    name = Sub('${AWS::StackName}-app-build')
    artifacts = AppBuildArtifacts
    environment = AppBuildEnvironment
    service_role = CodeBuildRole
    source = AppBuildSource


class CodeCommitRepo(codecommit.Repository):
    repository_name = Sub('${AWS::StackName}-repo')
    repository_description = Sub('This is a repository for the ${AWS::StackName} project.')
