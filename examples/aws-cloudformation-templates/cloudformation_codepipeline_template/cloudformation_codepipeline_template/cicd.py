"""Cicd resources: Pipeline."""

from . import *  # noqa: F403


class PipelineArtifactStore(codepipeline.Pipeline.ArtifactStore):
    type_ = 'S3'
    location = ImportValue(Sub('${CodeBuildStack}-PipelineS3Bucket'))


class PipelineActionTypeId(codepipeline.Pipeline.ActionTypeId):
    category = 'Source'
    owner = 'AWS'
    provider = 'CodeCommit'
    version = 1


class PipelineOutputArtifact(codepipeline.Pipeline.OutputArtifact):
    name = 'Source'


class PipelineActionDeclaration(codepipeline.Pipeline.ActionDeclaration):
    name = 'Source'
    action_type_id = PipelineActionTypeId
    configuration = {
        'RepositoryName': ImportValue(Sub('${CodeBuildStack}-CodeCommitName')),
        'BranchName': 'main',
        'PollForSourceChanges': False,
    }
    output_artifacts = [PipelineOutputArtifact]


class PipelineStageDeclaration(codepipeline.Pipeline.StageDeclaration):
    name = 'Source'
    actions = [PipelineActionDeclaration]


class PipelineActionTypeId1(codepipeline.Pipeline.ActionTypeId):
    category = 'Build'
    owner = 'AWS'
    provider = 'CodeBuild'
    version = 1


class PipelineInputArtifact(codepipeline.Pipeline.InputArtifact):
    name = 'Source'


class PipelineOutputArtifact1(codepipeline.Pipeline.OutputArtifact):
    name = 'FullZip'


class PipelineActionDeclaration1(codepipeline.Pipeline.ActionDeclaration):
    name = 'App-Build'
    action_type_id = PipelineActionTypeId1
    configuration = {
        'ProjectName': ImportValue(Sub('${CodeBuildStack}-AppBuild')),
    }
    input_artifacts = [PipelineInputArtifact]
    output_artifacts = [PipelineOutputArtifact1]
    run_order = 1


class PipelineStageDeclaration1(codepipeline.Pipeline.StageDeclaration):
    name = 'Build-AppBuild'
    actions = [PipelineActionDeclaration1]


class PipelineActionTypeId2(codepipeline.Pipeline.ActionTypeId):
    category = 'Approval'
    owner = 'AWS'
    provider = 'Manual'
    version = 1


class PipelineActionDeclaration2(codepipeline.Pipeline.ActionDeclaration):
    name = 'Approval'
    action_type_id = PipelineActionTypeId2
    configuration = {
        'CustomData': 'Review the build output and approve to deploy',
    }
    run_order = 2


class PipelineActionTypeId3(codepipeline.Pipeline.ActionTypeId):
    category = 'Build'
    owner = 'AWS'
    provider = 'CodeBuild'
    version = 1


class PipelineInputArtifact1(codepipeline.Pipeline.InputArtifact):
    name = 'Source'


class PipelineInputArtifact2(codepipeline.Pipeline.InputArtifact):
    name = 'FullZip'


class PipelineActionDeclaration3(codepipeline.Pipeline.ActionDeclaration):
    name = 'App-Deploy'
    action_type_id = PipelineActionTypeId3
    configuration = {
        'ProjectName': ImportValue(Sub('${CodeBuildStack}-AppDeploy')),
        'PrimarySource': 'Source',
        'EnvironmentVariables': '[{"name":"ENVIRONMENT","value":"SampleEnv","type":"PLAINTEXT"}]',
    }
    input_artifacts = [PipelineInputArtifact1, PipelineInputArtifact2]
    run_order = 3


class PipelineStageDeclaration2(codepipeline.Pipeline.StageDeclaration):
    name = 'Deploy-App'
    actions = [PipelineActionDeclaration2, PipelineActionDeclaration3]


class Pipeline(codepipeline.Pipeline):
    resource: codepipeline.Pipeline
    name = Sub('${AWS::StackName}-Code-Pipeline')
    artifact_store = PipelineArtifactStore
    restart_execution_on_update = False
    role_arn = PipelineRole.Arn
    stages = [PipelineStageDeclaration, PipelineStageDeclaration1, PipelineStageDeclaration2]
