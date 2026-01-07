"""Auto-generated stub for IDE type checking."""

# Core exports injected by setup_params() and setup_resources()
from wetwire_aws import (
    # Decorator
    wetwire_aws,
    # Base classes
    CloudFormationResource,
    PropertyType,
    # Policy helpers
    PolicyStatement,
    DenyStatement,
    PolicyDocument,
    # Template components
    CloudFormationTemplate,
    Parameter,
    Output,
    Mapping,
    TemplateCondition,
    # Reference types (from dataclass-dsl)
    Ref,
    RefList,
    RefDict,
    # Reference helpers
    ref,
    get_att,
    ARN,
    # Intrinsic functions
    GetAtt,
    Sub,
    Join,
    Select,
    Split,
    If,
    Equals,
    And,
    Or,
    Not,
    Base64,
    GetAZs,
    ImportValue,
    FindInMap,
    Transform,
    Cidr,
    Condition,
    # Parameter type constants
    STRING,
    NUMBER,
    LIST_NUMBER,
    COMMA_DELIMITED_LIST,
    SSM_PARAMETER_STRING,
    SSM_PARAMETER_STRING_LIST,
    # AWS-specific parameter types
    AVAILABILITY_ZONE,
    LIST_AVAILABILITY_ZONE,
    AMI_ID,
    INSTANCE_ID,
    KEY_PAIR,
    SECURITY_GROUP_ID,
    LIST_SECURITY_GROUP_ID,
    SUBNET_ID,
    LIST_SUBNET_ID,
    VPC_ID,
    VOLUME_ID,
    HOSTED_ZONE_ID,
    # Pseudo-parameters
    AWS_ACCOUNT_ID,
    AWS_NOTIFICATION_ARNS,
    AWS_NO_VALUE,
    AWS_PARTITION,
    AWS_REGION,
    AWS_STACK_ID,
    AWS_STACK_NAME,
    AWS_URL_SUFFIX,
)
from wetwire_aws.resources import (
    accessanalyzer,
    acmpca,
    aiops,
    amazonmq,
    amplify,
    amplifyuibuilder,
    apigateway,
    apigatewayv2,
    appconfig,
    appflow,
    appintegrations,
    applicationautoscaling,
    applicationinsights,
    applicationsignals,
    appmesh,
    apprunner,
    appstream,
    appsync,
    apptest,
    aps,
    arcregionswitch,
    arczonalshift,
    ask,
    athena,
    auditmanager,
    autoscaling,
    autoscalingplans,
    b2bi,
    backup,
    backupgateway,
    batch,
    bcmdataexports,
    bedrock,
    bedrockagentcore,
    billing,
    billingconductor,
    budgets,
    cases,
    cassandra,
    ce,
    certificatemanager,
    chatbot,
    cleanrooms,
    cleanroomsml,
    cloud9,
    cloudformation,
    cloudfront,
    cloudtrail,
    cloudwatch,
    codeartifact,
    codebuild,
    codecommit,
    codeconnections,
    codedeploy,
    codeguruprofiler,
    codegurureviewer,
    codepipeline,
    codestar,
    codestarconnections,
    codestarnotifications,
    cognito,
    comprehend,
    config,
    connect,
    connectcampaigns,
    connectcampaignsv2,
    controltower,
    cur,
    customerprofiles,
    databrew,
    datapipeline,
    datasync,
    datazone,
    dax,
    deadline,
    detective,
    devopsagent,
    devopsguru,
    directoryservice,
    dlm,
    dms,
    docdb,
    docdbelastic,
    dsql,
    dynamodb,
    ec2,
    ecr,
    ecs,
    efs,
    eks,
    elasticache,
    elasticbeanstalk,
    elasticloadbalancing,
    elasticloadbalancingv2,
    elasticsearch,
    emr,
    emrcontainers,
    emrserverless,
    entityresolution,
    events,
    eventschemas,
    evidently,
    evs,
    finspace,
    fis,
    fms,
    forecast,
    frauddetector,
    fsx,
    gamelift,
    globalaccelerator,
    glue,
    grafana,
    greengrass,
    greengrassv2,
    groundstation,
    guardduty,
    healthimaging,
    healthlake,
    iam,
    identitystore,
    imagebuilder,
    inspector,
    inspectorv2,
    internetmonitor,
    invoicing,
    iot,
    iotanalytics,
    iotcoredeviceadvisor,
    iotevents,
    iotfleetwise,
    iotsitewise,
    iotthingsgraph,
    iottwinmaker,
    iotwireless,
    ivs,
    ivschat,
    kafkaconnect,
    kendra,
    kendraranking,
    kinesis,
    kinesisanalytics,
    kinesisanalyticsv2,
    kinesisfirehose,
    kinesisvideo,
    kms,
    lakeformation,
    lambda_,
    launchwizard,
    lex,
    licensemanager,
    lightsail,
    location,
    logs,
    lookoutequipment,
    lookoutvision,
    m2,
    macie,
    managedblockchain,
    mediaconnect,
    mediaconvert,
    medialive,
    mediapackage,
    mediapackagev2,
    mediastore,
    mediatailor,
    memorydb,
    mpa,
    msk,
    mwaa,
    neptune,
    neptunegraph,
    networkfirewall,
    networkmanager,
    notifications,
    notificationscontacts,
    oam,
    observabilityadmin,
    odb,
    omics,
    opensearchserverless,
    opensearchservice,
    opsworks,
    organizations,
    osis,
    panorama,
    paymentcryptography,
    pcaconnectorad,
    pcaconnectorscep,
    pcs,
    personalize,
    pinpoint,
    pinpointemail,
    pipes,
    proton,
    qbusiness,
    qldb,
    quicksight,
    ram,
    rbin,
    rds,
    redshift,
    redshiftserverless,
    refactorspaces,
    rekognition,
    resiliencehub,
    resourceexplorer2,
    resourcegroups,
    robomaker,
    rolesanywhere,
    route53,
    route53profiles,
    route53recoverycontrol,
    route53recoveryreadiness,
    route53resolver,
    rtbfabric,
    rum,
    s3,
    s3express,
    s3objectlambda,
    s3outposts,
    s3tables,
    s3vectors,
    sagemaker,
    scheduler,
    sdb,
    secretsmanager,
    securityhub,
    securitylake,
    serverless,
    servicecatalog,
    servicecatalogappregistry,
    servicediscovery,
    ses,
    shield,
    signer,
    simspaceweaver,
    smsvoice,
    sns,
    sqs,
    ssm,
    ssmcontacts,
    ssmguiconnect,
    ssmincidents,
    ssmquicksetup,
    sso,
    stepfunctions,
    supportapp,
    synthetics,
    systemsmanagersap,
    timestream,
    transfer,
    verifiedpermissions,
    voiceid,
    vpclattice,
    waf,
    wafregional,
    wafv2,
    wisdom,
    workspaces,
    workspacesinstances,
    workspacesthinclient,
    workspacesweb,
    xray,
)

from wetwire_aws.loader import setup_params, setup_resources

from .compute import ContainerInstances as ContainerInstances
from .compute import ECSAutoScalingGroup as ECSAutoScalingGroup
from .compute import ECSCluster as ECSCluster
from .main import Service as Service
from .main import ServiceLoadBalancer as ServiceLoadBalancer
from .main import ServiceScalingPolicy as ServiceScalingPolicy
from .main import ServiceScalingPolicyStepAdjustment as ServiceScalingPolicyStepAdjustment
from .main import ServiceScalingPolicyStepScalingPolicyConfiguration as ServiceScalingPolicyStepScalingPolicyConfiguration
from .main import ServiceScalingTarget as ServiceScalingTarget
from .main import TaskDefinition as TaskDefinition
from .main import TaskDefinitionContainerDefinition as TaskDefinitionContainerDefinition
from .main import TaskDefinitionContainerDefinition1 as TaskDefinitionContainerDefinition1
from .main import TaskDefinitionKeyValuePair as TaskDefinitionKeyValuePair
from .main import TaskDefinitionLogConfiguration as TaskDefinitionLogConfiguration
from .main import TaskDefinitionLogConfiguration1 as TaskDefinitionLogConfiguration1
from .main import TaskDefinitionMountPoint as TaskDefinitionMountPoint
from .main import TaskDefinitionPortMapping as TaskDefinitionPortMapping
from .main import TaskDefinitionVolumeFrom as TaskDefinitionVolumeFrom
from .messaging import ECSScheduledTask as ECSScheduledTask
from .messaging import ECSScheduledTaskEcsParameters as ECSScheduledTaskEcsParameters
from .messaging import ECSScheduledTaskTarget as ECSScheduledTaskTarget
from .monitoring import ALB500sAlarmScaleUp as ALB500sAlarmScaleUp
from .monitoring import ALB500sAlarmScaleUpDimension as ALB500sAlarmScaleUpDimension
from .monitoring import CloudwatchLogsGroup as CloudwatchLogsGroup
from .network import ALBListener as ALBListener
from .network import ALBListenerAction as ALBListenerAction
from .network import ECSALB as ECSALB
from .network import ECSALBListenerRule as ECSALBListenerRule
from .network import ECSALBListenerRuleAction as ECSALBListenerRuleAction
from .network import ECSALBListenerRuleRuleCondition as ECSALBListenerRuleRuleCondition
from .network import ECSALBTargetGroupAttribute as ECSALBTargetGroupAttribute
from .network import ECSTG as ECSTG
from .network import EcsSecurityGroup as EcsSecurityGroup
from .network import EcsSecurityGroupALBports as EcsSecurityGroupALBports
from .network import EcsSecurityGroupHTTPinbound as EcsSecurityGroupHTTPinbound
from .network import EcsSecurityGroupSSHinbound as EcsSecurityGroupSSHinbound
from .outputs import ECSALBOutput as ECSALBOutput
from .outputs import EcsClusterOutput as EcsClusterOutput
from .outputs import EcsServiceOutput as EcsServiceOutput
from .outputs import EcsTaskDefOutput as EcsTaskDefOutput
from .params import CronOrRate as CronOrRate
from .params import CronRateCondition as CronRateCondition
from .params import CronSchedule as CronSchedule
from .params import DesiredCapacity as DesiredCapacity
from .params import InstanceType as InstanceType
from .params import KeyName as KeyName
from .params import LatestAmiId as LatestAmiId
from .params import MaxSize as MaxSize
from .params import RateSchedule as RateSchedule
from .params import SchedulerTasksCount as SchedulerTasksCount
from .params import SubnetId as SubnetId
from .params import VpcId as VpcId
from .security import AutoscalingRole as AutoscalingRole
from .security import AutoscalingRoleAllowStatement0 as AutoscalingRoleAllowStatement0
from .security import AutoscalingRoleAllowStatement0_1 as AutoscalingRoleAllowStatement0_1
from .security import AutoscalingRoleAssumeRolePolicyDocument as AutoscalingRoleAssumeRolePolicyDocument
from .security import AutoscalingRolePolicies0PolicyDocument as AutoscalingRolePolicies0PolicyDocument
from .security import AutoscalingRolePolicy as AutoscalingRolePolicy
from .security import EC2InstanceProfile as EC2InstanceProfile
from .security import EC2Role as EC2Role
from .security import EC2RoleAllowStatement0 as EC2RoleAllowStatement0
from .security import EC2RoleAllowStatement0_1 as EC2RoleAllowStatement0_1
from .security import EC2RoleAssumeRolePolicyDocument as EC2RoleAssumeRolePolicyDocument
from .security import EC2RolePolicies0PolicyDocument as EC2RolePolicies0PolicyDocument
from .security import EC2RolePolicy as EC2RolePolicy
from .security import ECSEventRole as ECSEventRole
from .security import ECSEventRoleAllowStatement0 as ECSEventRoleAllowStatement0
from .security import ECSEventRoleAllowStatement0_1 as ECSEventRoleAllowStatement0_1
from .security import ECSEventRoleAssumeRolePolicyDocument as ECSEventRoleAssumeRolePolicyDocument
from .security import ECSEventRolePolicies0PolicyDocument as ECSEventRolePolicies0PolicyDocument
from .security import ECSEventRolePolicy as ECSEventRolePolicy
from .security import ECSServiceRole as ECSServiceRole
from .security import ECSServiceRoleAllowStatement0 as ECSServiceRoleAllowStatement0
from .security import ECSServiceRoleAllowStatement0_1 as ECSServiceRoleAllowStatement0_1
from .security import ECSServiceRoleAssumeRolePolicyDocument as ECSServiceRoleAssumeRolePolicyDocument
from .security import ECSServiceRolePolicies0PolicyDocument as ECSServiceRolePolicies0PolicyDocument
from .security import ECSServiceRolePolicy as ECSServiceRolePolicy
from .security import LogsKmsKey as LogsKmsKey

__all__: list[str] = ['ALB500sAlarmScaleUp', 'ALB500sAlarmScaleUpDimension', 'ALBListener', 'ALBListenerAction', 'AMI_ID', 'ARN', 'AVAILABILITY_ZONE', 'AWS_ACCOUNT_ID', 'AWS_NOTIFICATION_ARNS', 'AWS_NO_VALUE', 'AWS_PARTITION', 'AWS_REGION', 'AWS_STACK_ID', 'AWS_STACK_NAME', 'AWS_URL_SUFFIX', 'And', 'AutoscalingRole', 'AutoscalingRoleAllowStatement0', 'AutoscalingRoleAllowStatement0_1', 'AutoscalingRoleAssumeRolePolicyDocument', 'AutoscalingRolePolicies0PolicyDocument', 'AutoscalingRolePolicy', 'Base64', 'COMMA_DELIMITED_LIST', 'Cidr', 'CloudFormationResource', 'CloudFormationTemplate', 'CloudwatchLogsGroup', 'Condition', 'ContainerInstances', 'CronOrRate', 'CronRateCondition', 'CronSchedule', 'DenyStatement', 'DesiredCapacity', 'EC2InstanceProfile', 'EC2Role', 'EC2RoleAllowStatement0', 'EC2RoleAllowStatement0_1', 'EC2RoleAssumeRolePolicyDocument', 'EC2RolePolicies0PolicyDocument', 'EC2RolePolicy', 'ECSALB', 'ECSALBListenerRule', 'ECSALBListenerRuleAction', 'ECSALBListenerRuleRuleCondition', 'ECSALBOutput', 'ECSALBTargetGroupAttribute', 'ECSAutoScalingGroup', 'ECSCluster', 'ECSEventRole', 'ECSEventRoleAllowStatement0', 'ECSEventRoleAllowStatement0_1', 'ECSEventRoleAssumeRolePolicyDocument', 'ECSEventRolePolicies0PolicyDocument', 'ECSEventRolePolicy', 'ECSScheduledTask', 'ECSScheduledTaskEcsParameters', 'ECSScheduledTaskTarget', 'ECSServiceRole', 'ECSServiceRoleAllowStatement0', 'ECSServiceRoleAllowStatement0_1', 'ECSServiceRoleAssumeRolePolicyDocument', 'ECSServiceRolePolicies0PolicyDocument', 'ECSServiceRolePolicy', 'ECSTG', 'EcsClusterOutput', 'EcsSecurityGroup', 'EcsSecurityGroupALBports', 'EcsSecurityGroupHTTPinbound', 'EcsSecurityGroupSSHinbound', 'EcsServiceOutput', 'EcsTaskDefOutput', 'Equals', 'FindInMap', 'GetAZs', 'GetAtt', 'HOSTED_ZONE_ID', 'INSTANCE_ID', 'If', 'ImportValue', 'InstanceType', 'Join', 'KEY_PAIR', 'KeyName', 'LIST_AVAILABILITY_ZONE', 'LIST_NUMBER', 'LIST_SECURITY_GROUP_ID', 'LIST_SUBNET_ID', 'LatestAmiId', 'LogsKmsKey', 'Mapping', 'MaxSize', 'NUMBER', 'Not', 'Or', 'Output', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'PropertyType', 'RateSchedule', 'Ref', 'RefDict', 'RefList', 'SECURITY_GROUP_ID', 'SSM_PARAMETER_STRING', 'SSM_PARAMETER_STRING_LIST', 'STRING', 'SUBNET_ID', 'SchedulerTasksCount', 'Select', 'Service', 'ServiceLoadBalancer', 'ServiceScalingPolicy', 'ServiceScalingPolicyStepAdjustment', 'ServiceScalingPolicyStepScalingPolicyConfiguration', 'ServiceScalingTarget', 'Split', 'Sub', 'SubnetId', 'TaskDefinition', 'TaskDefinitionContainerDefinition', 'TaskDefinitionContainerDefinition1', 'TaskDefinitionKeyValuePair', 'TaskDefinitionLogConfiguration', 'TaskDefinitionLogConfiguration1', 'TaskDefinitionMountPoint', 'TaskDefinitionPortMapping', 'TaskDefinitionVolumeFrom', 'TemplateCondition', 'Transform', 'VOLUME_ID', 'VPC_ID', 'VpcId', 'accessanalyzer', 'acmpca', 'aiops', 'amazonmq', 'amplify', 'amplifyuibuilder', 'apigateway', 'apigatewayv2', 'appconfig', 'appflow', 'appintegrations', 'applicationautoscaling', 'applicationinsights', 'applicationsignals', 'appmesh', 'apprunner', 'appstream', 'appsync', 'apptest', 'aps', 'arcregionswitch', 'arczonalshift', 'ask', 'athena', 'auditmanager', 'autoscaling', 'autoscalingplans', 'b2bi', 'backup', 'backupgateway', 'batch', 'bcmdataexports', 'bedrock', 'bedrockagentcore', 'billing', 'billingconductor', 'budgets', 'cases', 'cassandra', 'ce', 'certificatemanager', 'chatbot', 'cleanrooms', 'cleanroomsml', 'cloud9', 'cloudformation', 'cloudfront', 'cloudtrail', 'cloudwatch', 'codeartifact', 'codebuild', 'codecommit', 'codeconnections', 'codedeploy', 'codeguruprofiler', 'codegurureviewer', 'codepipeline', 'codestar', 'codestarconnections', 'codestarnotifications', 'cognito', 'comprehend', 'config', 'connect', 'connectcampaigns', 'connectcampaignsv2', 'controltower', 'cur', 'customerprofiles', 'databrew', 'datapipeline', 'datasync', 'datazone', 'dax', 'deadline', 'detective', 'devopsagent', 'devopsguru', 'directoryservice', 'dlm', 'dms', 'docdb', 'docdbelastic', 'dsql', 'dynamodb', 'ec2', 'ecr', 'ecs', 'efs', 'eks', 'elasticache', 'elasticbeanstalk', 'elasticloadbalancing', 'elasticloadbalancingv2', 'elasticsearch', 'emr', 'emrcontainers', 'emrserverless', 'entityresolution', 'events', 'eventschemas', 'evidently', 'evs', 'finspace', 'fis', 'fms', 'forecast', 'frauddetector', 'fsx', 'gamelift', 'get_att', 'globalaccelerator', 'glue', 'grafana', 'greengrass', 'greengrassv2', 'groundstation', 'guardduty', 'healthimaging', 'healthlake', 'iam', 'identitystore', 'imagebuilder', 'inspector', 'inspectorv2', 'internetmonitor', 'invoicing', 'iot', 'iotanalytics', 'iotcoredeviceadvisor', 'iotevents', 'iotfleetwise', 'iotsitewise', 'iotthingsgraph', 'iottwinmaker', 'iotwireless', 'ivs', 'ivschat', 'kafkaconnect', 'kendra', 'kendraranking', 'kinesis', 'kinesisanalytics', 'kinesisanalyticsv2', 'kinesisfirehose', 'kinesisvideo', 'kms', 'lakeformation', 'lambda_', 'launchwizard', 'lex', 'licensemanager', 'lightsail', 'location', 'logs', 'lookoutequipment', 'lookoutvision', 'm2', 'macie', 'managedblockchain', 'mediaconnect', 'mediaconvert', 'medialive', 'mediapackage', 'mediapackagev2', 'mediastore', 'mediatailor', 'memorydb', 'mpa', 'msk', 'mwaa', 'neptune', 'neptunegraph', 'networkfirewall', 'networkmanager', 'notifications', 'notificationscontacts', 'oam', 'observabilityadmin', 'odb', 'omics', 'opensearchserverless', 'opensearchservice', 'opsworks', 'organizations', 'osis', 'panorama', 'paymentcryptography', 'pcaconnectorad', 'pcaconnectorscep', 'pcs', 'personalize', 'pinpoint', 'pinpointemail', 'pipes', 'proton', 'qbusiness', 'qldb', 'quicksight', 'ram', 'rbin', 'rds', 'redshift', 'redshiftserverless', 'ref', 'refactorspaces', 'rekognition', 'resiliencehub', 'resourceexplorer2', 'resourcegroups', 'robomaker', 'rolesanywhere', 'route53', 'route53profiles', 'route53recoverycontrol', 'route53recoveryreadiness', 'route53resolver', 'rtbfabric', 'rum', 's3', 's3express', 's3objectlambda', 's3outposts', 's3tables', 's3vectors', 'sagemaker', 'scheduler', 'sdb', 'secretsmanager', 'securityhub', 'securitylake', 'serverless', 'servicecatalog', 'servicecatalogappregistry', 'servicediscovery', 'ses', 'setup_params', 'setup_resources', 'shield', 'signer', 'simspaceweaver', 'smsvoice', 'sns', 'sqs', 'ssm', 'ssmcontacts', 'ssmguiconnect', 'ssmincidents', 'ssmquicksetup', 'sso', 'stepfunctions', 'supportapp', 'synthetics', 'systemsmanagersap', 'timestream', 'transfer', 'verifiedpermissions', 'voiceid', 'vpclattice', 'waf', 'wafregional', 'wafv2', 'wetwire_aws', 'wisdom', 'workspaces', 'workspacesinstances', 'workspacesthinclient', 'workspacesweb', 'xray']
