"""Stack resources."""

from . import *  # noqa: F403


class InstanceAZ(CloudFormationResource):
    # Unknown resource type: Custom::InstanceAZ
    region = AWS_REGION
    service_token = InstanceAZFunction.Arn


class FunctionDefinitionExecution:
    resource: greengrass.FunctionDefinition.Execution
    isolation_mode = 'GreengrassContainer'


class FunctionDefinitionDefaultConfig:
    resource: greengrass.FunctionDefinition.DefaultConfig
    execution = FunctionDefinitionExecution


class FunctionDefinitionRunAs:
    resource: greengrass.FunctionDefinition.RunAs
    gid = '10'
    uid = '1'


class FunctionDefinitionExecution1:
    resource: greengrass.FunctionDefinition.Execution
    isolation_mode = 'GreengrassContainer'
    run_as = FunctionDefinitionRunAs


class FunctionDefinitionEnvironment:
    resource: greengrass.FunctionDefinition.Environment
    access_sysfs = 'false'
    execution = FunctionDefinitionExecution1
    variables = {
        'CORE_NAME': CoreName,
    }


class FunctionDefinitionFunctionConfiguration:
    resource: greengrass.FunctionDefinition.FunctionConfiguration
    encoding_type = 'binary'
    environment = FunctionDefinitionEnvironment
    executable = 'index.py'
    memory_size = '65536'
    pinned = 'true'
    timeout = '300'


class FunctionDefinitionFunction:
    resource: greengrass.FunctionDefinition.Function
    function_arn = GGSampleFunctionVersion
    function_configuration = FunctionDefinitionFunctionConfiguration
    id = Join('_', [
    CoreName,
    'sample',
])


class FunctionDefinitionFunctionDefinitionVersion:
    resource: greengrass.FunctionDefinition.FunctionDefinitionVersion
    default_config = FunctionDefinitionDefaultConfig
    functions = [FunctionDefinitionFunction]


class FunctionDefinition(greengrass.FunctionDefinition):
    initial_version = FunctionDefinitionFunctionDefinitionVersion
    name = 'FunctionDefinition'


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


class GreengrassCoreDefinitionVersionCore:
    resource: greengrass.CoreDefinition.Core
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
    id = Join('_', [
    CoreName,
    'Core',
])
    sync_shadow = 'false'
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


class GreengrassCoreDefinitionVersion(greengrass.CoreDefinitionVersion):
    core_definition_id = GreengrassCoreDefinition
    cores = [GreengrassCoreDefinitionVersionCore]


class SubscriptionDefinitionSubscription:
    resource: greengrass.SubscriptionDefinitionVersion.Subscription
    id = 'Subscription1'
    source = 'cloud'
    subject = Join('/', [
    CoreName,
    'in',
])
    target = GGSampleFunctionVersion


class SubscriptionDefinitionSubscription1:
    resource: greengrass.SubscriptionDefinitionVersion.Subscription
    id = 'Subscription2'
    source = GGSampleFunctionVersion
    subject = Join('/', [
    CoreName,
    'out',
])
    target = 'cloud'


class SubscriptionDefinitionSubscription2:
    resource: greengrass.SubscriptionDefinitionVersion.Subscription
    id = 'Subscription3'
    source = GGSampleFunctionVersion
    subject = Join('/', [
    CoreName,
    'telem',
])
    target = 'cloud'


class SubscriptionDefinitionSubscriptionDefinitionVersion:
    resource: greengrass.SubscriptionDefinition.SubscriptionDefinitionVersion
    subscriptions = [SubscriptionDefinitionSubscription, SubscriptionDefinitionSubscription1, SubscriptionDefinitionSubscription2]


class SubscriptionDefinition(greengrass.SubscriptionDefinition):
    initial_version = SubscriptionDefinitionSubscriptionDefinitionVersion
    name = 'SubscriptionDefinition'


class GreengrassGroupGroupVersion:
    resource: greengrass.Group.GroupVersion
    core_definition_version_arn = GreengrassCoreDefinitionVersion
    function_definition_version_arn = FunctionDefinition.LatestVersionArn
    subscription_definition_version_arn = SubscriptionDefinition.LatestVersionArn


class GreengrassGroup(greengrass.Group):
    initial_version = GreengrassGroupGroupVersion
    name = CoreName
    role_arn = GreengrassResourceRole.Arn


class SubnetAPublic(ec2.Subnet):
    availability_zone = InstanceAZ.AvailabilityZone
    cidr_block = '172.31.0.0/24'
    map_public_ip_on_launch = True
    vpc_id = VPC


class GroupDeploymentReset(CloudFormationResource):
    # Unknown resource type: Custom::GroupDeploymentReset
    region = AWS_REGION
    service_token = GroupDeploymentResetFunction.Arn
    thing_name = Join('_', [
    CoreName,
    'Core',
])
    depends_on = [GreengrassGroup]
