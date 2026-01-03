"""Template outputs."""

from . import *  # noqa: F403


class CodeCommitNameOutput:
    """The code commit repository name"""

    resource: Output
    value = CodeCommitRepo.Name
    description = 'The code commit repository name'
    export_name = Sub('${AWS::StackName}-CodeCommitName')


class CodeCommitArnOutput:
    """The code commit repository arn"""

    resource: Output
    value = CodeCommitRepo.Arn
    description = 'The code commit repository arn'
    export_name = Sub('${AWS::StackName}-CodeCommitArn')


class PipelineS3BucketOutput:
    """The s3 bucket used by the deployment codepipelines"""

    resource: Output
    value = PipelineS3Bucket
    description = 'The s3 bucket used by the deployment codepipelines'
    export_name = Sub('${AWS::StackName}-PipelineS3Bucket')


class PipelineS3BucketArnOutput:
    """The s3 bucket used by the deployment codepipelines"""

    resource: Output
    value = PipelineS3Bucket.Arn
    description = 'The s3 bucket used by the deployment codepipelines'
    export_name = Sub('${AWS::StackName}-PipelineS3BucketArn')


class CodeBuildRoleOutput:
    """IAM Role ARN associated with CodeBuild projects"""

    resource: Output
    value = CodeBuildRole
    description = 'IAM Role ARN associated with CodeBuild projects'
    export_name = Sub('${AWS::StackName}-CodeBuildRole')


class CodeBuildRoleArnOutput:
    """IAM Role ARN associated with CodeBuild projects"""

    resource: Output
    value = CodeBuildRole.Arn
    description = 'IAM Role ARN associated with CodeBuild projects'
    export_name = Sub('${AWS::StackName}-CodeBuildRoleArn')


class AppDeployOutput:
    resource: Output
    value = AppDeploy
    export_name = Sub('${AWS::StackName}-AppDeploy')


class AppDeploydArnOutput:
    resource: Output
    value = AppDeploy.Arn
    export_name = Sub('${AWS::StackName}-AppDeployArn')


class AppBuildOutput:
    resource: Output
    value = AppBuild
    export_name = Sub('${AWS::StackName}-AppBuild')


class AppBuildArnOutput:
    resource: Output
    value = AppBuild.Arn
    export_name = Sub('${AWS::StackName}-AppBuildArn')
