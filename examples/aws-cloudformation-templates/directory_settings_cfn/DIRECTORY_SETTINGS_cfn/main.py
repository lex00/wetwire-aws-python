"""Stack resources."""

from . import *  # noqa: F403


class DirectorySettingsResource:
    # Unknown resource type: Custom::DirectorySettingsResource
    resource: CloudFormationResource
    service_token = DirectorySettingsLambdaFunction.Arn
    directory_id = DirectoryID
    create_directory_alias = CreateDirectoryAlias
    enable_directory_sso = EnableDirectorySSO
    directory_alias = DirectoryAlias
    directory_monitoring_topic_name = DirectoryMonitoringTopic.TopicName
