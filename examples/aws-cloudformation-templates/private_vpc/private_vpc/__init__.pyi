"""Auto-generated stub for IDE type checking."""

# Core exports injected by setup_params() and setup_resources()
from wetwire_aws import (
    # Decorator
    wetwire_aws,
    # Base classes
    CloudFormationResource,
    PropertyType,
    Tag,
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
    Attr,
    RefList,
    RefDict,
    # Reference helpers
    ref,
    get_att,
    ARN,
    # Intrinsic functions
    RefIntrinsic,
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
    # Condition operator constants
    BOOL,
    STRING_EQUALS,
    STRING_NOT_EQUALS,
    STRING_EQUALS_IGNORE_CASE,
    STRING_NOT_EQUALS_IGNORE_CASE,
    STRING_LIKE,
    STRING_NOT_LIKE,
    NUMERIC_EQUALS,
    NUMERIC_NOT_EQUALS,
    NUMERIC_LESS_THAN,
    NUMERIC_LESS_THAN_EQUALS,
    NUMERIC_GREATER_THAN,
    NUMERIC_GREATER_THAN_EQUALS,
    DATE_EQUALS,
    DATE_NOT_EQUALS,
    DATE_LESS_THAN,
    DATE_LESS_THAN_EQUALS,
    DATE_GREATER_THAN,
    DATE_GREATER_THAN_EQUALS,
    IP_ADDRESS,
    NOT_IP_ADDRESS,
    ARN_EQUALS,
    ARN_NOT_EQUALS,
    ARN_LIKE,
    ARN_NOT_LIKE,
    NULL,
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
from .network import DummyTargetGroupPrivate as DummyTargetGroupPrivate
from .network import DummyTargetGroupPublic as DummyTargetGroupPublic
from .network import DynamoDBEndpoint as DynamoDBEndpoint
from .network import DynamoDBEndpointAllowStatement0 as DynamoDBEndpointAllowStatement0
from .network import DynamoDBEndpointPolicyDocument as DynamoDBEndpointPolicyDocument
from .network import EcsHostSecurityGroup as EcsHostSecurityGroup
from .network import EcsSecurityGroupIngressFromPrivateALB as EcsSecurityGroupIngressFromPrivateALB
from .network import EcsSecurityGroupIngressFromPublicALB as EcsSecurityGroupIngressFromPublicALB
from .network import EcsSecurityGroupIngressFromSelf as EcsSecurityGroupIngressFromSelf
from .network import GatewayAttachement as GatewayAttachement
from .network import InternetGateway as InternetGateway
from .network import NatGatewayOne as NatGatewayOne
from .network import NatGatewayOneAttachment as NatGatewayOneAttachment
from .network import NatGatewayTwo as NatGatewayTwo
from .network import NatGatewayTwoAttachment as NatGatewayTwoAttachment
from .network import PrivateLoadBalancer as PrivateLoadBalancer
from .network import PrivateLoadBalancerIngressFromECS as PrivateLoadBalancerIngressFromECS
from .network import PrivateLoadBalancerListener as PrivateLoadBalancerListener
from .network import PrivateLoadBalancerListenerAction as PrivateLoadBalancerListenerAction
from .network import PrivateLoadBalancerSG as PrivateLoadBalancerSG
from .network import PrivateLoadBalancerTargetGroupAttribute as PrivateLoadBalancerTargetGroupAttribute
from .network import PrivateRouteOne as PrivateRouteOne
from .network import PrivateRouteTableOne as PrivateRouteTableOne
from .network import PrivateRouteTableOneAssociation as PrivateRouteTableOneAssociation
from .network import PrivateRouteTableTwo as PrivateRouteTableTwo
from .network import PrivateRouteTableTwoAssociation as PrivateRouteTableTwoAssociation
from .network import PrivateRouteTwo as PrivateRouteTwo
from .network import PrivateSubnetOne as PrivateSubnetOne
from .network import PrivateSubnetTwo as PrivateSubnetTwo
from .network import PublicLoadBalancer as PublicLoadBalancer
from .network import PublicLoadBalancerListener as PublicLoadBalancerListener
from .network import PublicLoadBalancerListenerAction as PublicLoadBalancerListenerAction
from .network import PublicLoadBalancerSG as PublicLoadBalancerSG
from .network import PublicLoadBalancerSGEgress as PublicLoadBalancerSGEgress
from .network import PublicLoadBalancerTargetGroupAttribute as PublicLoadBalancerTargetGroupAttribute
from .network import PublicRoute as PublicRoute
from .network import PublicRouteTable as PublicRouteTable
from .network import PublicSubnetOne as PublicSubnetOne
from .network import PublicSubnetOneRouteTableAssociation as PublicSubnetOneRouteTableAssociation
from .network import PublicSubnetTwo as PublicSubnetTwo
from .network import PublicSubnetTwoRouteTableAssociation as PublicSubnetTwoRouteTableAssociation
from .network import VPC as VPC
from .outputs import ClusterNameOutput as ClusterNameOutput
from .outputs import ECSRoleOutput as ECSRoleOutput
from .outputs import EcsHostSecurityGroupOutput as EcsHostSecurityGroupOutput
from .outputs import ExternalUrlOutput as ExternalUrlOutput
from .outputs import InternalUrlOutput as InternalUrlOutput
from .outputs import PrivateListenerOutput as PrivateListenerOutput
from .outputs import PrivateSubnetOneOutput as PrivateSubnetOneOutput
from .outputs import PrivateSubnetTwoOutput as PrivateSubnetTwoOutput
from .outputs import PublicListenerOutput as PublicListenerOutput
from .outputs import PublicSubnetOneOutput as PublicSubnetOneOutput
from .outputs import PublicSubnetTwoOutput as PublicSubnetTwoOutput
from .outputs import VPCIdOutput as VPCIdOutput
from .params import DesiredCapacity as DesiredCapacity
from .params import ECSAMI as ECSAMI
from .params import InstanceType as InstanceType
from .params import MaxSize as MaxSize
from .params import SubnetConfigMapping as SubnetConfigMapping
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
from .security import ECSRole as ECSRole
from .security import ECSRoleAllowStatement0 as ECSRoleAllowStatement0
from .security import ECSRoleAllowStatement0_1 as ECSRoleAllowStatement0_1
from .security import ECSRoleAssumeRolePolicyDocument as ECSRoleAssumeRolePolicyDocument
from .security import ECSRolePolicies0PolicyDocument as ECSRolePolicies0PolicyDocument
from .security import ECSRolePolicy as ECSRolePolicy

__all__: list[str] = ['AMI_ID', 'ARN', 'ARN_EQUALS', 'ARN_LIKE', 'ARN_NOT_EQUALS', 'ARN_NOT_LIKE', 'AVAILABILITY_ZONE', 'AWS_ACCOUNT_ID', 'AWS_NOTIFICATION_ARNS', 'AWS_NO_VALUE', 'AWS_PARTITION', 'AWS_REGION', 'AWS_STACK_ID', 'AWS_STACK_NAME', 'AWS_URL_SUFFIX', 'And', 'Attr', 'AutoscalingRole', 'AutoscalingRoleAllowStatement0', 'AutoscalingRoleAllowStatement0_1', 'AutoscalingRoleAssumeRolePolicyDocument', 'AutoscalingRolePolicies0PolicyDocument', 'AutoscalingRolePolicy', 'BOOL', 'Base64', 'COMMA_DELIMITED_LIST', 'Cidr', 'CloudFormationResource', 'CloudFormationTemplate', 'ClusterNameOutput', 'Condition', 'ContainerInstances', 'DATE_EQUALS', 'DATE_GREATER_THAN', 'DATE_GREATER_THAN_EQUALS', 'DATE_LESS_THAN', 'DATE_LESS_THAN_EQUALS', 'DATE_NOT_EQUALS', 'DenyStatement', 'DesiredCapacity', 'DummyTargetGroupPrivate', 'DummyTargetGroupPublic', 'DynamoDBEndpoint', 'DynamoDBEndpointAllowStatement0', 'DynamoDBEndpointPolicyDocument', 'EC2InstanceProfile', 'EC2Role', 'EC2RoleAllowStatement0', 'EC2RoleAllowStatement0_1', 'EC2RoleAssumeRolePolicyDocument', 'EC2RolePolicies0PolicyDocument', 'EC2RolePolicy', 'ECSAMI', 'ECSAutoScalingGroup', 'ECSCluster', 'ECSRole', 'ECSRoleAllowStatement0', 'ECSRoleAllowStatement0_1', 'ECSRoleAssumeRolePolicyDocument', 'ECSRoleOutput', 'ECSRolePolicies0PolicyDocument', 'ECSRolePolicy', 'EcsHostSecurityGroup', 'EcsHostSecurityGroupOutput', 'EcsSecurityGroupIngressFromPrivateALB', 'EcsSecurityGroupIngressFromPublicALB', 'EcsSecurityGroupIngressFromSelf', 'Equals', 'ExternalUrlOutput', 'FindInMap', 'GatewayAttachement', 'GetAZs', 'GetAtt', 'HOSTED_ZONE_ID', 'INSTANCE_ID', 'IP_ADDRESS', 'If', 'ImportValue', 'InstanceType', 'InternalUrlOutput', 'InternetGateway', 'Join', 'KEY_PAIR', 'LIST_AVAILABILITY_ZONE', 'LIST_NUMBER', 'LIST_SECURITY_GROUP_ID', 'LIST_SUBNET_ID', 'Mapping', 'MaxSize', 'NOT_IP_ADDRESS', 'NULL', 'NUMBER', 'NUMERIC_EQUALS', 'NUMERIC_GREATER_THAN', 'NUMERIC_GREATER_THAN_EQUALS', 'NUMERIC_LESS_THAN', 'NUMERIC_LESS_THAN_EQUALS', 'NUMERIC_NOT_EQUALS', 'NatGatewayOne', 'NatGatewayOneAttachment', 'NatGatewayTwo', 'NatGatewayTwoAttachment', 'Not', 'Or', 'Output', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'PrivateListenerOutput', 'PrivateLoadBalancer', 'PrivateLoadBalancerIngressFromECS', 'PrivateLoadBalancerListener', 'PrivateLoadBalancerListenerAction', 'PrivateLoadBalancerSG', 'PrivateLoadBalancerTargetGroupAttribute', 'PrivateRouteOne', 'PrivateRouteTableOne', 'PrivateRouteTableOneAssociation', 'PrivateRouteTableTwo', 'PrivateRouteTableTwoAssociation', 'PrivateRouteTwo', 'PrivateSubnetOne', 'PrivateSubnetOneOutput', 'PrivateSubnetTwo', 'PrivateSubnetTwoOutput', 'PropertyType', 'PublicListenerOutput', 'PublicLoadBalancer', 'PublicLoadBalancerListener', 'PublicLoadBalancerListenerAction', 'PublicLoadBalancerSG', 'PublicLoadBalancerSGEgress', 'PublicLoadBalancerTargetGroupAttribute', 'PublicRoute', 'PublicRouteTable', 'PublicSubnetOne', 'PublicSubnetOneOutput', 'PublicSubnetOneRouteTableAssociation', 'PublicSubnetTwo', 'PublicSubnetTwoOutput', 'PublicSubnetTwoRouteTableAssociation', 'Ref', 'RefDict', 'RefIntrinsic', 'RefList', 'SECURITY_GROUP_ID', 'SSM_PARAMETER_STRING', 'SSM_PARAMETER_STRING_LIST', 'STRING', 'STRING_EQUALS', 'STRING_EQUALS_IGNORE_CASE', 'STRING_LIKE', 'STRING_NOT_EQUALS', 'STRING_NOT_EQUALS_IGNORE_CASE', 'STRING_NOT_LIKE', 'SUBNET_ID', 'Select', 'Split', 'Sub', 'SubnetConfigMapping', 'Tag', 'TemplateCondition', 'Transform', 'VOLUME_ID', 'VPC', 'VPCIdOutput', 'VPC_ID', 'accessanalyzer', 'acmpca', 'aiops', 'amazonmq', 'amplify', 'amplifyuibuilder', 'apigateway', 'apigatewayv2', 'appconfig', 'appflow', 'appintegrations', 'applicationautoscaling', 'applicationinsights', 'applicationsignals', 'appmesh', 'apprunner', 'appstream', 'appsync', 'apptest', 'aps', 'arcregionswitch', 'arczonalshift', 'ask', 'athena', 'auditmanager', 'autoscaling', 'autoscalingplans', 'b2bi', 'backup', 'backupgateway', 'batch', 'bcmdataexports', 'bedrock', 'bedrockagentcore', 'billing', 'billingconductor', 'budgets', 'cases', 'cassandra', 'ce', 'certificatemanager', 'chatbot', 'cleanrooms', 'cleanroomsml', 'cloud9', 'cloudformation', 'cloudfront', 'cloudtrail', 'cloudwatch', 'codeartifact', 'codebuild', 'codecommit', 'codeconnections', 'codedeploy', 'codeguruprofiler', 'codegurureviewer', 'codepipeline', 'codestar', 'codestarconnections', 'codestarnotifications', 'cognito', 'comprehend', 'config', 'connect', 'connectcampaigns', 'connectcampaignsv2', 'controltower', 'cur', 'customerprofiles', 'databrew', 'datapipeline', 'datasync', 'datazone', 'dax', 'deadline', 'detective', 'devopsagent', 'devopsguru', 'directoryservice', 'dlm', 'dms', 'docdb', 'docdbelastic', 'dsql', 'dynamodb', 'ec2', 'ecr', 'ecs', 'efs', 'eks', 'elasticache', 'elasticbeanstalk', 'elasticloadbalancing', 'elasticloadbalancingv2', 'elasticsearch', 'emr', 'emrcontainers', 'emrserverless', 'entityresolution', 'events', 'eventschemas', 'evidently', 'evs', 'finspace', 'fis', 'fms', 'forecast', 'frauddetector', 'fsx', 'gamelift', 'get_att', 'globalaccelerator', 'glue', 'grafana', 'greengrass', 'greengrassv2', 'groundstation', 'guardduty', 'healthimaging', 'healthlake', 'iam', 'identitystore', 'imagebuilder', 'inspector', 'inspectorv2', 'internetmonitor', 'invoicing', 'iot', 'iotanalytics', 'iotcoredeviceadvisor', 'iotevents', 'iotfleetwise', 'iotsitewise', 'iotthingsgraph', 'iottwinmaker', 'iotwireless', 'ivs', 'ivschat', 'kafkaconnect', 'kendra', 'kendraranking', 'kinesis', 'kinesisanalytics', 'kinesisanalyticsv2', 'kinesisfirehose', 'kinesisvideo', 'kms', 'lakeformation', 'lambda_', 'launchwizard', 'lex', 'licensemanager', 'lightsail', 'location', 'logs', 'lookoutequipment', 'lookoutvision', 'm2', 'macie', 'managedblockchain', 'mediaconnect', 'mediaconvert', 'medialive', 'mediapackage', 'mediapackagev2', 'mediastore', 'mediatailor', 'memorydb', 'mpa', 'msk', 'mwaa', 'neptune', 'neptunegraph', 'networkfirewall', 'networkmanager', 'notifications', 'notificationscontacts', 'oam', 'observabilityadmin', 'odb', 'omics', 'opensearchserverless', 'opensearchservice', 'opsworks', 'organizations', 'osis', 'panorama', 'paymentcryptography', 'pcaconnectorad', 'pcaconnectorscep', 'pcs', 'personalize', 'pinpoint', 'pinpointemail', 'pipes', 'proton', 'qbusiness', 'qldb', 'quicksight', 'ram', 'rbin', 'rds', 'redshift', 'redshiftserverless', 'ref', 'refactorspaces', 'rekognition', 'resiliencehub', 'resourceexplorer2', 'resourcegroups', 'robomaker', 'rolesanywhere', 'route53', 'route53profiles', 'route53recoverycontrol', 'route53recoveryreadiness', 'route53resolver', 'rtbfabric', 'rum', 's3', 's3express', 's3objectlambda', 's3outposts', 's3tables', 's3vectors', 'sagemaker', 'scheduler', 'sdb', 'secretsmanager', 'securityhub', 'securitylake', 'serverless', 'servicecatalog', 'servicecatalogappregistry', 'servicediscovery', 'ses', 'setup_params', 'setup_resources', 'shield', 'signer', 'simspaceweaver', 'smsvoice', 'sns', 'sqs', 'ssm', 'ssmcontacts', 'ssmguiconnect', 'ssmincidents', 'ssmquicksetup', 'sso', 'stepfunctions', 'supportapp', 'synthetics', 'systemsmanagersap', 'timestream', 'transfer', 'verifiedpermissions', 'voiceid', 'vpclattice', 'waf', 'wafregional', 'wafv2', 'wetwire_aws', 'wisdom', 'workspaces', 'workspacesinstances', 'workspacesthinclient', 'workspacesweb', 'xray']
