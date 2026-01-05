"""Database resources: RedisParameterGroup, RedisSubnetGroup, RedisReplicationGroup."""

from . import *  # noqa: F403


class RedisParameterGroup(elasticache.ParameterGroup):
    cache_parameter_group_family = 'redis2.8'
    description = 'RedisParameterGroup'


class RedisSubnetGroup(elasticache.SubnetGroup):
    description = 'RedisSubnetGroup'
    subnet_ids = [PublicSubnetA, PublicSubnetB]


class RedisReplicationGroup(elasticache.ReplicationGroup):
    automatic_failover_enabled = 'true'
    cache_node_type = RedisNodeType
    cache_parameter_group_name = RedisParameterGroup
    cache_subnet_group_name = RedisSubnetGroup
    engine = 'redis'
    engine_version = '2.8.24'
    num_cache_clusters = '2'
    preferred_cache_cluster_a_zs = [FindInMap("AWSRegion2AZ", AWS_REGION, 'A'), FindInMap("AWSRegion2AZ", AWS_REGION, 'B')]
    replication_group_description = 'RedisReplicationGroup'
    security_group_ids = [RedisSecurityGroup]
