"""Stack resources."""

from . import *  # noqa: F403


class EnableShapshotTrigger(CloudFormationResource):
    # Unknown resource type: Custom::Region
    resource: CloudFormationResource
    service_token = EnableShapshot.Arn
    ss_cluster_id = RedisReplicationGroup
    ss_window = SnapshotWindow
    ss_retention_limit = SnapshotRetentionLimit
    depends_on = [EnableShapshot, LambdaExecutePermission, RedisReplicationGroup]
    condition = 'EnableBackups'
