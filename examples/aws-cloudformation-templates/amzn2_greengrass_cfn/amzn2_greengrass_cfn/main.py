"""Stack resources."""

from . import *  # noqa: F403


class InstanceAZ(CloudFormationResource):
    # Unknown resource type: Custom::InstanceAZ
    resource: CloudFormationResource
    service_token = InstanceAZFunction.Arn
    region = AWS_REGION


class SubnetAPublic(ec2.Subnet):
    resource: ec2.Subnet
    availability_zone = InstanceAZ.AvailabilityZone
    cidr_block = '172.31.0.0/24'
    map_public_ip_on_launch = True
    vpc_id = VPC


class IoTThing(CloudFormationResource):
    # Unknown resource type: Custom::IoTThing
    resource: CloudFormationResource
    service_token = CreateThingFunction.Arn
    thing_name = Join('_', [
    CoreName,
    'Core',
])


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
    resource: greengrass.FunctionDefinition
    name = 'FunctionDefinition'
    initial_version = FunctionDefinitionFunctionDefinitionVersion


class GreengrassCoreDefinition(greengrass.CoreDefinition):
    resource: greengrass.CoreDefinition
    name = Join('_', [
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
    resource: greengrass.CoreDefinitionVersion
    core_definition_id = GreengrassCoreDefinition
    cores = [GreengrassCoreDefinitionVersionCore]


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
    resource: greengrass.SubscriptionDefinition
    name = 'SubscriptionDefinition'
    initial_version = SubscriptionDefinitionSubscriptionDefinitionVersion


class GreengrassGroupGroupVersion(greengrass.Group.GroupVersion):
    core_definition_version_arn = GreengrassCoreDefinitionVersion
    function_definition_version_arn = FunctionDefinition.LatestVersionArn
    subscription_definition_version_arn = SubscriptionDefinition.LatestVersionArn


class GreengrassGroup(greengrass.Group):
    resource: greengrass.Group
    name = CoreName
    role_arn = GreengrassResourceRole.Arn
    initial_version = GreengrassGroupGroupVersion


class GroupDeploymentReset(CloudFormationResource):
    # Unknown resource type: Custom::GroupDeploymentReset
    resource: CloudFormationResource
    service_token = GroupDeploymentResetFunction.Arn
    region = AWS_REGION
    thing_name = Join('_', [
    CoreName,
    'Core',
])
    depends_on = [GreengrassGroup]
