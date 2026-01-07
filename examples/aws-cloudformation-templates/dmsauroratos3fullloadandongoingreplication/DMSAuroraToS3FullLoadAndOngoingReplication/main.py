"""Stack resources."""

from . import *  # noqa: F403


class DMSReplicationSubnetGroup(dms.ReplicationSubnetGroup):
    replication_subnet_group_description = 'Subnets available for DMS'
    subnet_ids = [DBSubnet1, DBSubnet2]


class DMSReplicationInstance(dms.ReplicationInstance):
    availability_zone = DBSubnet1.AvailabilityZone
    publicly_accessible = False
    replication_instance_class = 'dms.t3.medium'
    replication_instance_identifier = 'aurora-s3-repinstance-sampledb'
    replication_subnet_group_identifier = DMSReplicationSubnetGroup
    vpc_security_group_ids = [DMSSecurityGroup]
    depends_on = [DMSReplicationSubnetGroup, DMSSecurityGroup]


class S3TargetEndpointRedshiftSettings(dms.Endpoint.RedshiftSettings):
    bucket_name = S3Bucket
    service_access_role_arn = S3TargetDMSRole.Arn


class S3TargetEndpoint(dms.Endpoint):
    endpoint_type = 'target'
    engine_name = 'S3'
    extra_connection_attributes = 'addColumnName=true'
    s3_settings = S3TargetEndpointRedshiftSettings
    depends_on = [DMSReplicationInstance, S3Bucket, S3TargetDMSRole]


class AuroraSourceEndpoint(dms.Endpoint):
    endpoint_type = 'source'
    engine_name = 'AURORA'
    password = '{{resolve:secretsmanager:aurora-source-enpoint-password:SecretString:password}}'
    port = 3306
    server_name = AuroraCluster.Endpoint.Address
    username = 'admin'
    depends_on = [DMSReplicationInstance, AuroraCluster, AuroraDB]


class DMSReplicationTask(dms.ReplicationTask):
    migration_type = 'full-load-and-cdc'
    replication_instance_arn = DMSReplicationInstance
    replication_task_settings = '{ "Logging" : { "EnableLogging" : true, "LogComponents": [ { "Id" : "SOURCE_UNLOAD", "Severity" : "LOGGER_SEVERITY_DEFAULT" }, { "Id" : "SOURCE_CAPTURE", "Severity" : "LOGGER_SEVERITY_DEFAULT" }, { "Id" : "TARGET_LOAD", "Severity" : "LOGGER_SEVERITY_DEFAULT" }, { "Id" : "TARGET_APPLY", "Severity" : "LOGGER_SEVERITY_DEFAULT" } ] } }'
    source_endpoint_arn = AuroraSourceEndpoint
    table_mappings = '{ "rules": [ { "rule-type" : "selection", "rule-id" : "1", "rule-name" : "1", "object-locator" : { "schema-name" : "dms_sample", "table-name" : "%" }, "rule-action" : "include" } ] }'
    target_endpoint_arn = S3TargetEndpoint
    depends_on = [AuroraSourceEndpoint, S3TargetEndpoint, DMSReplicationInstance]
