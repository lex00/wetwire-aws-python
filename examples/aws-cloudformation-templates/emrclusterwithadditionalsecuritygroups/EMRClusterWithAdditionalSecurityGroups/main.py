"""Stack resources."""

from . import *  # noqa: F403


class EMRClusterBootstrapActionConfig(emr.Cluster.BootstrapActionConfig):
    name = 'Ganglia'


class EMRClusterConfiguration(emr.InstanceGroupConfig.Configuration):
    classification = 'hbase-site'
    configuration_properties = {
        'hbase.rootdir': S3DataUri,
    }


class EMRClusterConfiguration1(emr.InstanceGroupConfig.Configuration):
    classification = 'hbase'
    configuration_properties = {
        'hbase.emr.storageMode': 's3',
    }


class EMRClusterInstanceGroupConfig(emr.Cluster.InstanceGroupConfig):
    instance_count = 1
    instance_type = MasterInstanceType
    market = 'ON_DEMAND'
    name = 'Master'


class EMRClusterInstanceGroupConfig1(emr.Cluster.InstanceGroupConfig):
    instance_count = NumberOfCoreInstances
    instance_type = CoreInstanceType
    market = 'ON_DEMAND'
    name = 'Core'


class EMRClusterJobFlowInstancesConfig(emr.Cluster.JobFlowInstancesConfig):
    ec2_key_name = KeyName
    ec2_subnet_id = SubnetID
    additional_master_security_groups = AdditionalPrimaryNodeSecurityGroups
    additional_slave_security_groups = AdditionalCoreNodeSecurityGroups
    master_instance_group = EMRClusterInstanceGroupConfig
    core_instance_group = EMRClusterInstanceGroupConfig1
    termination_protected = False


class EMRCluster(emr.Cluster):
    resource: emr.Cluster
    applications = [EMRClusterBootstrapActionConfig, If("Spark", {
    'Name': 'Spark',
}, AWS_NO_VALUE), If("Hbase", {
    'Name': 'Hbase',
}, AWS_NO_VALUE)]
    configurations = [EMRClusterConfiguration, EMRClusterConfiguration1]
    instances = EMRClusterJobFlowInstancesConfig
    visible_to_all_users = True
    job_flow_role = EMRClusterinstanceProfile
    release_label = ReleaseLabel
    log_uri = LogUri
    name = EMRClusterName
    auto_scaling_role = 'EMR_AutoScaling_DefaultRole'
    service_role = EMRClusterServiceRole
    depends_on = [EMRClusterServiceRole, EMRClusterinstanceProfileRole, EMRClusterinstanceProfile]
