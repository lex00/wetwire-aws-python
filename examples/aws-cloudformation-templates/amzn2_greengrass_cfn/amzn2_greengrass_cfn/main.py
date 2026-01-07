"""Stack resources."""

from . import *  # noqa: F403


class InstanceAZ(CloudFormationResource):
    # Unknown resource type: Custom::InstanceAZ
    service_token = InstanceAZFunction.Arn
    region = AWS_REGION


class SubnetAPublic(ec2.Subnet):
    availability_zone = InstanceAZ.AvailabilityZone
    cidr_block = '172.31.0.0/24'
    map_public_ip_on_launch = True
    vpc_id = VPC


class GreengrassCoreDefinition(greengrass.CoreDefinition):
    name = Join('_', [
    CoreName,
    'Core',
])


class IoTThing(CloudFormationResource):
    # Unknown resource type: Custom::IoTThing
    service_token = CreateThingFunction.Arn
    thing_name = Join('_', [
    CoreName,
    'Core',
])


class GreengrassCoreDefinitionVersionCore(greengrass.CoreDefinition.Core):
    id = Join('_', [
    CoreName,
    'Core',
])
    thing_arn = Join(':', [
    'arn:',
    AWS_PARTITION,
    ':iot',
    AWS_REGION,
    AWS_ACCOUNT_ID,
    Join('/', [
    'thing',
    Join('_', [
    CoreName,
    'Core',
]),
]),
])
    certificate_arn = Join(':', [
    'arn:',
    AWS_PARTITION,
    ':iot',
    AWS_REGION,
    AWS_ACCOUNT_ID,
    Join('/', [
    'cert',
    IoTThing.certificateId,
]),
])
    sync_shadow = 'false'


class GreengrassCoreDefinitionVersion(greengrass.CoreDefinitionVersion):
    core_definition_id = GreengrassCoreDefinition
    cores = [GreengrassCoreDefinitionVersionCore]


class RouteTableAssociationAPublic(ec2.SubnetRouteTableAssociation):
    subnet_id = SubnetAPublic
    route_table_id = RouteTablePublic


class SubscriptionDefinitionSubscription(greengrass.SubscriptionDefinitionVersion.Subscription):
    id = 'Subscription1'
    source = 'cloud'
    subject = Join('/', [
    CoreName,
    'in',
])
    target = GGSampleFunctionVersion


class SubscriptionDefinitionSubscription1(greengrass.SubscriptionDefinitionVersion.Subscription):
    id = 'Subscription2'
    source = GGSampleFunctionVersion
    subject = Join('/', [
    CoreName,
    'out',
])
    target = 'cloud'


class SubscriptionDefinitionSubscription2(greengrass.SubscriptionDefinitionVersion.Subscription):
    id = 'Subscription3'
    source = GGSampleFunctionVersion
    subject = Join('/', [
    CoreName,
    'telem',
])
    target = 'cloud'


class SubscriptionDefinitionSubscriptionDefinitionVersion(greengrass.SubscriptionDefinition.SubscriptionDefinitionVersion):
    subscriptions = [SubscriptionDefinitionSubscription, SubscriptionDefinitionSubscription1, SubscriptionDefinitionSubscription2]


class SubscriptionDefinition(greengrass.SubscriptionDefinition):
    name = 'SubscriptionDefinition'
    initial_version = SubscriptionDefinitionSubscriptionDefinitionVersion


class FunctionDefinitionExecution(greengrass.FunctionDefinition.Execution):
    isolation_mode = 'GreengrassContainer'


class FunctionDefinitionDefaultConfig(greengrass.FunctionDefinition.DefaultConfig):
    execution = FunctionDefinitionExecution


class FunctionDefinitionRunAs(greengrass.FunctionDefinition.RunAs):
    uid = '1'
    gid = '10'


class FunctionDefinitionExecution1(greengrass.FunctionDefinition.Execution):
    isolation_mode = 'GreengrassContainer'
    run_as = FunctionDefinitionRunAs


class FunctionDefinitionEnvironment(greengrass.FunctionDefinition.Environment):
    variables = {
        'CORE_NAME': CoreName,
    }
    access_sysfs = 'false'
    execution = FunctionDefinitionExecution1


class FunctionDefinitionFunctionConfiguration(greengrass.FunctionDefinition.FunctionConfiguration):
    pinned = 'true'
    executable = 'index.py'
    memory_size = '65536'
    timeout = '300'
    encoding_type = 'binary'
    environment = FunctionDefinitionEnvironment


class FunctionDefinitionFunction(greengrass.FunctionDefinition.Function):
    id = Join('_', [
    CoreName,
    'sample',
])
    function_arn = GGSampleFunctionVersion
    function_configuration = FunctionDefinitionFunctionConfiguration


class FunctionDefinitionFunctionDefinitionVersion(greengrass.FunctionDefinition.FunctionDefinitionVersion):
    default_config = FunctionDefinitionDefaultConfig
    functions = [FunctionDefinitionFunction]


class FunctionDefinition(greengrass.FunctionDefinition):
    name = 'FunctionDefinition'
    initial_version = FunctionDefinitionFunctionDefinitionVersion


class GreengrassGroupGroupVersion(greengrass.Group.GroupVersion):
    core_definition_version_arn = GreengrassCoreDefinitionVersion
    function_definition_version_arn = FunctionDefinition.LatestVersionArn
    subscription_definition_version_arn = SubscriptionDefinition.LatestVersionArn


class GreengrassGroup(greengrass.Group):
    name = CoreName
    role_arn = GreengrassResourceRole.Arn
    initial_version = GreengrassGroupGroupVersion


class GroupDeploymentReset(CloudFormationResource):
    # Unknown resource type: Custom::GroupDeploymentReset
    service_token = GroupDeploymentResetFunction.Arn
    region = AWS_REGION
    thing_name = Join('_', [
    CoreName,
    'Core',
])
    depends_on = [GreengrassGroup]


class GreengrassInstanceAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = Join('-', [
    'Greengrass Core Blog ',
    CoreName,
])


class GreengrassInstance(ec2.Instance):
    image_id = LatestAmiId
    instance_type = InstanceType
    key_name = myKeyPair
    security_group_ids = Split(',', InstanceSecurityGroup.GroupId)
    tags = [GreengrassInstanceAssociationParameter]
    subnet_id = SubnetAPublic
    user_data = Base64(Sub("""#!/bin/bash
yum -y install python3-pip
pip3 install greengrasssdk
adduser --system ggc_user
groupadd --system ggc_group

# https://docs.aws.amazon.com/greengrass/latest/developerguide/what-is-gg.html#gg-core-download-tab
curl -O https://d1onfpft10uf5o.cloudfront.net/greengrass-core/downloads/1.9.1/greengrass-linux-x86-64-1.9.1.tar.gz
tar xf greengrass-linux-x86*.gz -C /
echo -n "${IoTThing.certificatePem}" > /greengrass/certs/${IoTThing.certificateId}.pem
echo -n "${IoTThing.privateKey}" > /greengrass/certs/${IoTThing.certificateId}.key
cd /greengrass/config
# Create Greengrass config file from inputs and parameters
# Can be enhanced to manage complete installation of Greengrass and credentials
cat <<EOT > config.json          
{
  "coreThing" : {
    "caPath" : "root.ca.pem",
    "certPath" : "${IoTThing.certificateId}.pem",
    "keyPath" : "${IoTThing.certificateId}.key",
    "thingArn" : "arn:${AWS::Partition}:iot:${AWS::Region}:${AWS::AccountId}:thing/${CoreName}_Core",
    "iotHost" : "${IoTThing.iotEndpoint}",
    "ggHost" : "greengrass-ats.iot.${AWS::Region}.amazonaws.com"
  },
  "runtime" : {
    "cgroup" : {
      "useSystemd" : "yes"
    }
  },
  "managedRespawn" : false,
  "crypto" : {
    "principals" : {
      "SecretsManager" : {
        "privateKeyPath" : "file:///greengrass/certs/${IoTThing.certificateId}.key"
      },
      "IoTCertificate" : {
        "privateKeyPath" : "file:///greengrass/certs/${IoTThing.certificateId}.key",
        "certificatePath" : "file:///greengrass/certs/${IoTThing.certificateId}.pem"
      }
    },
    "caPath" : "file:///greengrass/certs/root.ca.pem"
  }
}
EOT

cd /greengrass/certs/
curl -o root.ca.pem https://www.amazontrust.com/repository/AmazonRootCA1.pem
cd /tmp
# Create Greengrass systemd file - thanks to: https://gist.github.com/matthewberryman/fa21ca796c3a2e0dfe8224934b7b055c
cat <<EOT > greengrass.service
[Unit]
Description=greengrass daemon
After=network.target

[Service]
ExecStart=/greengrass/ggc/core/greengrassd start
Type=simple
RestartSec=2
Restart=always
User=root
PIDFile=/var/run/greengrassd.pid

[Install]
WantedBy=multi-user.target
EOT
cp greengrass.service /etc/systemd/system
systemctl enable greengrass.service
reboot
"""))
    depends_on = [GreengrassGroup]
