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
    # Loader
    setup_resources,
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

from .compute import ControlPlane as ControlPlane
from .compute import ControlPlaneResourcesVpcConfig as ControlPlaneResourcesVpcConfig
from .compute import LaunchTemplate as LaunchTemplate
from .compute import LaunchTemplateBlockDeviceMapping as LaunchTemplateBlockDeviceMapping
from .compute import LaunchTemplateEbs as LaunchTemplateEbs
from .compute import LaunchTemplateLaunchTemplateData as LaunchTemplateLaunchTemplateData
from .compute import LaunchTemplateMetadataOptions as LaunchTemplateMetadataOptions
from .compute import LaunchTemplateTagSpecification as LaunchTemplateTagSpecification
from .compute import LaunchTemplateTagSpecification1 as LaunchTemplateTagSpecification1
from .compute import LaunchTemplateTagSpecification2 as LaunchTemplateTagSpecification2
from .compute import ManagedNodeGroup as ManagedNodeGroup
from .compute import ManagedNodeGroupScalingConfig as ManagedNodeGroupScalingConfig
from .compute import ManagedNodeGroupSsoIdentity as ManagedNodeGroupSsoIdentity
from .network import AttachGateway as AttachGateway
from .network import ControlPlaneSecurityGroup as ControlPlaneSecurityGroup
from .network import ControlPlaneSecurityGroupIngress as ControlPlaneSecurityGroupIngress
from .network import EIP1 as EIP1
from .network import EIP2 as EIP2
from .network import EIP3 as EIP3
from .network import InternetGateway as InternetGateway
from .network import InternetGatewayAssociationParameter as InternetGatewayAssociationParameter
from .network import NATGateway1 as NATGateway1
from .network import NATGateway1AssociationParameter as NATGateway1AssociationParameter
from .network import NATGateway2 as NATGateway2
from .network import NATGateway2AssociationParameter as NATGateway2AssociationParameter
from .network import NATGateway3 as NATGateway3
from .network import NATGateway3AssociationParameter as NATGateway3AssociationParameter
from .network import PrivateRoute1 as PrivateRoute1
from .network import PrivateRoute2 as PrivateRoute2
from .network import PrivateRoute3 as PrivateRoute3
from .network import PrivateRouteTable1 as PrivateRouteTable1
from .network import PrivateRouteTable1AssociationParameter as PrivateRouteTable1AssociationParameter
from .network import PrivateRouteTable2 as PrivateRouteTable2
from .network import PrivateRouteTable2AssociationParameter as PrivateRouteTable2AssociationParameter
from .network import PrivateRouteTable3 as PrivateRouteTable3
from .network import PrivateRouteTable3AssociationParameter as PrivateRouteTable3AssociationParameter
from .network import PrivateRouteTableAssociation1 as PrivateRouteTableAssociation1
from .network import PrivateRouteTableAssociation2 as PrivateRouteTableAssociation2
from .network import PrivateRouteTableAssociation3 as PrivateRouteTableAssociation3
from .network import PrivateSubnet1 as PrivateSubnet1
from .network import PrivateSubnet1AssociationParameter as PrivateSubnet1AssociationParameter
from .network import PrivateSubnet2 as PrivateSubnet2
from .network import PrivateSubnet2AssociationParameter as PrivateSubnet2AssociationParameter
from .network import PrivateSubnet3 as PrivateSubnet3
from .network import PrivateSubnet3AssociationParameter as PrivateSubnet3AssociationParameter
from .network import PublicRouteTable as PublicRouteTable
from .network import PublicRouteTableAssociation1 as PublicRouteTableAssociation1
from .network import PublicRouteTableAssociation2 as PublicRouteTableAssociation2
from .network import PublicRouteTableAssociation3 as PublicRouteTableAssociation3
from .network import PublicRouteTableAssociationParameter as PublicRouteTableAssociationParameter
from .network import PublicSubnet1 as PublicSubnet1
from .network import PublicSubnet1AssociationParameter as PublicSubnet1AssociationParameter
from .network import PublicSubnet1AssociationParameter1 as PublicSubnet1AssociationParameter1
from .network import PublicSubnet2 as PublicSubnet2
from .network import PublicSubnet2AssociationParameter as PublicSubnet2AssociationParameter
from .network import PublicSubnet2AssociationParameter1 as PublicSubnet2AssociationParameter1
from .network import PublicSubnet3 as PublicSubnet3
from .network import PublicSubnet3AssociationParameter as PublicSubnet3AssociationParameter
from .network import PublicSubnet3AssociationParameter1 as PublicSubnet3AssociationParameter1
from .network import RouteInternetGateway as RouteInternetGateway
from .network import VPC as VPC
from .network import VPCAssociationParameter as VPCAssociationParameter
from .params import EKSClusterVersion as EKSClusterVersion
from .params import NodeGroupInstanceTypes as NodeGroupInstanceTypes
from .params import PrivateCidrBlock1 as PrivateCidrBlock1
from .params import PrivateCidrBlock2 as PrivateCidrBlock2
from .params import PrivateCidrBlock3 as PrivateCidrBlock3
from .params import PublicCidrBlock1 as PublicCidrBlock1
from .params import PublicCidrBlock2 as PublicCidrBlock2
from .params import PublicCidrBlock3 as PublicCidrBlock3
from .params import ServicePrincipalPartitionMapMapping as ServicePrincipalPartitionMapMapping
from .params import VPCCidrBlock as VPCCidrBlock
from .security import EKSClusterRole as EKSClusterRole
from .security import EKSClusterRoleAllowStatement0 as EKSClusterRoleAllowStatement0
from .security import EKSClusterRoleAssumeRolePolicyDocument as EKSClusterRoleAssumeRolePolicyDocument
from .security import NodeInstanceRole as NodeInstanceRole
from .security import NodeInstanceRoleAllowStatement0 as NodeInstanceRoleAllowStatement0
from .security import NodeInstanceRoleAssumeRolePolicyDocument as NodeInstanceRoleAssumeRolePolicyDocument

__all__: list[str] = ['AMI_ID', 'ARN', 'ARN_EQUALS', 'ARN_LIKE', 'ARN_NOT_EQUALS', 'ARN_NOT_LIKE', 'AVAILABILITY_ZONE', 'AWS_ACCOUNT_ID', 'AWS_NOTIFICATION_ARNS', 'AWS_NO_VALUE', 'AWS_PARTITION', 'AWS_REGION', 'AWS_STACK_ID', 'AWS_STACK_NAME', 'AWS_URL_SUFFIX', 'And', 'AttachGateway', 'Attr', 'BOOL', 'Base64', 'COMMA_DELIMITED_LIST', 'Cidr', 'CloudFormationResource', 'CloudFormationTemplate', 'Condition', 'ControlPlane', 'ControlPlaneResourcesVpcConfig', 'ControlPlaneSecurityGroup', 'ControlPlaneSecurityGroupIngress', 'DATE_EQUALS', 'DATE_GREATER_THAN', 'DATE_GREATER_THAN_EQUALS', 'DATE_LESS_THAN', 'DATE_LESS_THAN_EQUALS', 'DATE_NOT_EQUALS', 'DenyStatement', 'EIP1', 'EIP2', 'EIP3', 'EKSClusterRole', 'EKSClusterRoleAllowStatement0', 'EKSClusterRoleAssumeRolePolicyDocument', 'EKSClusterVersion', 'Equals', 'FindInMap', 'GetAZs', 'GetAtt', 'HOSTED_ZONE_ID', 'INSTANCE_ID', 'IP_ADDRESS', 'If', 'ImportValue', 'InternetGateway', 'InternetGatewayAssociationParameter', 'Join', 'KEY_PAIR', 'LIST_AVAILABILITY_ZONE', 'LIST_NUMBER', 'LIST_SECURITY_GROUP_ID', 'LIST_SUBNET_ID', 'LaunchTemplate', 'LaunchTemplateBlockDeviceMapping', 'LaunchTemplateEbs', 'LaunchTemplateLaunchTemplateData', 'LaunchTemplateMetadataOptions', 'LaunchTemplateTagSpecification', 'LaunchTemplateTagSpecification1', 'LaunchTemplateTagSpecification2', 'ManagedNodeGroup', 'ManagedNodeGroupScalingConfig', 'ManagedNodeGroupSsoIdentity', 'Mapping', 'NATGateway1', 'NATGateway1AssociationParameter', 'NATGateway2', 'NATGateway2AssociationParameter', 'NATGateway3', 'NATGateway3AssociationParameter', 'NOT_IP_ADDRESS', 'NULL', 'NUMBER', 'NUMERIC_EQUALS', 'NUMERIC_GREATER_THAN', 'NUMERIC_GREATER_THAN_EQUALS', 'NUMERIC_LESS_THAN', 'NUMERIC_LESS_THAN_EQUALS', 'NUMERIC_NOT_EQUALS', 'NodeGroupInstanceTypes', 'NodeInstanceRole', 'NodeInstanceRoleAllowStatement0', 'NodeInstanceRoleAssumeRolePolicyDocument', 'Not', 'Or', 'Output', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'PrivateCidrBlock1', 'PrivateCidrBlock2', 'PrivateCidrBlock3', 'PrivateRoute1', 'PrivateRoute2', 'PrivateRoute3', 'PrivateRouteTable1', 'PrivateRouteTable1AssociationParameter', 'PrivateRouteTable2', 'PrivateRouteTable2AssociationParameter', 'PrivateRouteTable3', 'PrivateRouteTable3AssociationParameter', 'PrivateRouteTableAssociation1', 'PrivateRouteTableAssociation2', 'PrivateRouteTableAssociation3', 'PrivateSubnet1', 'PrivateSubnet1AssociationParameter', 'PrivateSubnet2', 'PrivateSubnet2AssociationParameter', 'PrivateSubnet3', 'PrivateSubnet3AssociationParameter', 'PropertyType', 'PublicCidrBlock1', 'PublicCidrBlock2', 'PublicCidrBlock3', 'PublicRouteTable', 'PublicRouteTableAssociation1', 'PublicRouteTableAssociation2', 'PublicRouteTableAssociation3', 'PublicRouteTableAssociationParameter', 'PublicSubnet1', 'PublicSubnet1AssociationParameter', 'PublicSubnet1AssociationParameter1', 'PublicSubnet2', 'PublicSubnet2AssociationParameter', 'PublicSubnet2AssociationParameter1', 'PublicSubnet3', 'PublicSubnet3AssociationParameter', 'PublicSubnet3AssociationParameter1', 'Ref', 'RefDict', 'RefIntrinsic', 'RefList', 'RouteInternetGateway', 'SECURITY_GROUP_ID', 'SSM_PARAMETER_STRING', 'SSM_PARAMETER_STRING_LIST', 'STRING', 'STRING_EQUALS', 'STRING_EQUALS_IGNORE_CASE', 'STRING_LIKE', 'STRING_NOT_EQUALS', 'STRING_NOT_EQUALS_IGNORE_CASE', 'STRING_NOT_LIKE', 'SUBNET_ID', 'Select', 'ServicePrincipalPartitionMapMapping', 'Split', 'Sub', 'Tag', 'TemplateCondition', 'Transform', 'VOLUME_ID', 'VPC', 'VPCAssociationParameter', 'VPCCidrBlock', 'VPC_ID', 'accessanalyzer', 'acmpca', 'aiops', 'amazonmq', 'amplify', 'amplifyuibuilder', 'apigateway', 'apigatewayv2', 'appconfig', 'appflow', 'appintegrations', 'applicationautoscaling', 'applicationinsights', 'applicationsignals', 'appmesh', 'apprunner', 'appstream', 'appsync', 'apptest', 'aps', 'arcregionswitch', 'arczonalshift', 'ask', 'athena', 'auditmanager', 'autoscaling', 'autoscalingplans', 'b2bi', 'backup', 'backupgateway', 'batch', 'bcmdataexports', 'bedrock', 'bedrockagentcore', 'billing', 'billingconductor', 'budgets', 'cases', 'cassandra', 'ce', 'certificatemanager', 'chatbot', 'cleanrooms', 'cleanroomsml', 'cloud9', 'cloudformation', 'cloudfront', 'cloudtrail', 'cloudwatch', 'codeartifact', 'codebuild', 'codecommit', 'codeconnections', 'codedeploy', 'codeguruprofiler', 'codegurureviewer', 'codepipeline', 'codestar', 'codestarconnections', 'codestarnotifications', 'cognito', 'comprehend', 'config', 'connect', 'connectcampaigns', 'connectcampaignsv2', 'controltower', 'cur', 'customerprofiles', 'databrew', 'datapipeline', 'datasync', 'datazone', 'dax', 'deadline', 'detective', 'devopsagent', 'devopsguru', 'directoryservice', 'dlm', 'dms', 'docdb', 'docdbelastic', 'dsql', 'dynamodb', 'ec2', 'ecr', 'ecs', 'efs', 'eks', 'elasticache', 'elasticbeanstalk', 'elasticloadbalancing', 'elasticloadbalancingv2', 'elasticsearch', 'emr', 'emrcontainers', 'emrserverless', 'entityresolution', 'events', 'eventschemas', 'evidently', 'evs', 'finspace', 'fis', 'fms', 'forecast', 'frauddetector', 'fsx', 'gamelift', 'get_att', 'globalaccelerator', 'glue', 'grafana', 'greengrass', 'greengrassv2', 'groundstation', 'guardduty', 'healthimaging', 'healthlake', 'iam', 'identitystore', 'imagebuilder', 'inspector', 'inspectorv2', 'internetmonitor', 'invoicing', 'iot', 'iotanalytics', 'iotcoredeviceadvisor', 'iotevents', 'iotfleetwise', 'iotsitewise', 'iotthingsgraph', 'iottwinmaker', 'iotwireless', 'ivs', 'ivschat', 'kafkaconnect', 'kendra', 'kendraranking', 'kinesis', 'kinesisanalytics', 'kinesisanalyticsv2', 'kinesisfirehose', 'kinesisvideo', 'kms', 'lakeformation', 'lambda_', 'launchwizard', 'lex', 'licensemanager', 'lightsail', 'location', 'logs', 'lookoutequipment', 'lookoutvision', 'm2', 'macie', 'managedblockchain', 'mediaconnect', 'mediaconvert', 'medialive', 'mediapackage', 'mediapackagev2', 'mediastore', 'mediatailor', 'memorydb', 'mpa', 'msk', 'mwaa', 'neptune', 'neptunegraph', 'networkfirewall', 'networkmanager', 'notifications', 'notificationscontacts', 'oam', 'observabilityadmin', 'odb', 'omics', 'opensearchserverless', 'opensearchservice', 'opsworks', 'organizations', 'osis', 'panorama', 'paymentcryptography', 'pcaconnectorad', 'pcaconnectorscep', 'pcs', 'personalize', 'pinpoint', 'pinpointemail', 'pipes', 'proton', 'qbusiness', 'qldb', 'quicksight', 'ram', 'rbin', 'rds', 'redshift', 'redshiftserverless', 'ref', 'refactorspaces', 'rekognition', 'resiliencehub', 'resourceexplorer2', 'resourcegroups', 'robomaker', 'rolesanywhere', 'route53', 'route53profiles', 'route53recoverycontrol', 'route53recoveryreadiness', 'route53resolver', 'rtbfabric', 'rum', 's3', 's3express', 's3objectlambda', 's3outposts', 's3tables', 's3vectors', 'sagemaker', 'scheduler', 'sdb', 'secretsmanager', 'securityhub', 'securitylake', 'serverless', 'servicecatalog', 'servicecatalogappregistry', 'servicediscovery', 'ses', 'setup_params', 'setup_resources', 'shield', 'signer', 'simspaceweaver', 'smsvoice', 'sns', 'sqs', 'ssm', 'ssmcontacts', 'ssmguiconnect', 'ssmincidents', 'ssmquicksetup', 'sso', 'stepfunctions', 'supportapp', 'synthetics', 'systemsmanagersap', 'timestream', 'transfer', 'verifiedpermissions', 'voiceid', 'vpclattice', 'waf', 'wafregional', 'wafv2', 'wetwire_aws', 'wisdom', 'workspaces', 'workspacesinstances', 'workspacesthinclient', 'workspacesweb', 'xray']
