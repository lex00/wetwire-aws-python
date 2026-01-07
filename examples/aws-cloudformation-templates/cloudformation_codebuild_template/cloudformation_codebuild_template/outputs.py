"""Template outputs."""

from . import *  # noqa: F403


class CodeCommitNameOutput(Output):
    """The code commit repository name"""

    value = CodeCommitRepo.Name
    description = 'The code commit repository name'
    export_name = Sub('${AWS::StackName}-CodeCommitName')


class CodeCommitArnOutput(Output):
    """The code commit repository arn"""

    value = CodeCommitRepo.Arn
    description = 'The code commit repository arn'
    export_name = Sub('${AWS::StackName}-CodeCommitArn')


class PipelineS3BucketOutput(Output):
    """The s3 bucket used by the deployment codepipelines"""

    value = PipelineS3Bucket
    description = 'The s3 bucket used by the deployment codepipelines'
    export_name = Sub('${AWS::StackName}-PipelineS3Bucket')


class PipelineS3BucketArnOutput(Output):
    """The s3 bucket used by the deployment codepipelines"""

    value = PipelineS3Bucket.Arn
    description = 'The s3 bucket used by the deployment codepipelines'
    export_name = Sub('${AWS::StackName}-PipelineS3BucketArn')


class CodeBuildRoleOutput(Output):
    """IAM Role ARN associated with CodeBuild projects"""

    value = CodeBuildRole
    description = 'IAM Role ARN associated with CodeBuild projects'
    export_name = Sub('${AWS::StackName}-CodeBuildRole')


class CodeBuildRoleArnOutput(Output):
    """IAM Role ARN associated with CodeBuild projects"""

    value = CodeBuildRole.Arn
    description = 'IAM Role ARN associated with CodeBuild projects'
    export_name = Sub('${AWS::StackName}-CodeBuildRoleArn')


class AppDeployOutput(Output):
    value = AppDeploy
    export_name = Sub('${AWS::StackName}-AppDeploy')


class AppDeploydArnOutput(Output):
    value = AppDeploy.Arn
    export_name = Sub('${AWS::StackName}-AppDeployArn')


class AppBuildOutput(Output):
    value = AppBuild
    export_name = Sub('${AWS::StackName}-AppBuild')


class AppBuildArnOutput(Output):
    value = AppBuild.Arn
    export_name = Sub('${AWS::StackName}-AppBuildArn')
