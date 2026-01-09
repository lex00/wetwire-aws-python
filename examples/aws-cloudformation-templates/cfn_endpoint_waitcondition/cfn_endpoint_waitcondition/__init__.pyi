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

from .compute import BastionInstance as BastionInstance
from .compute import BastionInstanceAssociationParameter as BastionInstanceAssociationParameter
from .compute import PrivateInstance as PrivateInstance
from .compute import PrivateInstanceAssociationParameter as PrivateInstanceAssociationParameter
from .infra import PrivateWaitHandle as PrivateWaitHandle
from .main import PrivateWaitCondition as PrivateWaitCondition
from .network import BastionSG as BastionSG
from .network import BastionSGAssociationParameter as BastionSGAssociationParameter
from .network import BastionSGEgress as BastionSGEgress
from .network import CfnEndpoint as CfnEndpoint
from .network import DefaultPublicRoute as DefaultPublicRoute
from .network import EndpointSG as EndpointSG
from .network import EndpointSGAssociationParameter as EndpointSGAssociationParameter
from .network import EndpointSGEgress as EndpointSGEgress
from .network import InternetGateway as InternetGateway
from .network import InternetGatewayAssociationParameter as InternetGatewayAssociationParameter
from .network import InternetGatewayAttachment as InternetGatewayAttachment
from .network import PrivateRouteTable1 as PrivateRouteTable1
from .network import PrivateRouteTable1AssociationParameter as PrivateRouteTable1AssociationParameter
from .network import PrivateRouteTable2 as PrivateRouteTable2
from .network import PrivateRouteTable2AssociationParameter as PrivateRouteTable2AssociationParameter
from .network import PrivateSG as PrivateSG
from .network import PrivateSGAssociationParameter as PrivateSGAssociationParameter
from .network import PrivateSGIngress as PrivateSGIngress
from .network import PrivateSubnet1 as PrivateSubnet1
from .network import PrivateSubnet1AssociationParameter as PrivateSubnet1AssociationParameter
from .network import PrivateSubnet1RouteTableAssociation as PrivateSubnet1RouteTableAssociation
from .network import PrivateSubnet2 as PrivateSubnet2
from .network import PrivateSubnet2AssociationParameter as PrivateSubnet2AssociationParameter
from .network import PrivateSubnet2RouteTableAssociation as PrivateSubnet2RouteTableAssociation
from .network import PublicRouteTable as PublicRouteTable
from .network import PublicRouteTableAssociationParameter as PublicRouteTableAssociationParameter
from .network import PublicSubnet1 as PublicSubnet1
from .network import PublicSubnet1AssociationParameter as PublicSubnet1AssociationParameter
from .network import PublicSubnet1RouteTableAssociation as PublicSubnet1RouteTableAssociation
from .network import PublicSubnet2 as PublicSubnet2
from .network import PublicSubnet2AssociationParameter as PublicSubnet2AssociationParameter
from .network import PublicSubnet2RouteTableAssociation as PublicSubnet2RouteTableAssociation
from .network import S3Endpoint as S3Endpoint
from .network import S3EndpointAllowStatement0 as S3EndpointAllowStatement0
from .network import S3EndpointPolicyDocument as S3EndpointPolicyDocument
from .network import VPC as VPC
from .network import VPCAssociationParameter as VPCAssociationParameter
from .outputs import CfnEndpointOutput as CfnEndpointOutput
from .outputs import PrivateSubnetsOutput as PrivateSubnetsOutput
from .outputs import PublicSubnetsOutput as PublicSubnetsOutput
from .outputs import S3EndpointOutput as S3EndpointOutput
from .outputs import VPCOutput as VPCOutput
from .params import EnvironmentName as EnvironmentName
from .params import KeyName as KeyName
from .params import LinuxAMI as LinuxAMI
from .params import PrivateSubnet1CIDR as PrivateSubnet1CIDR
from .params import PrivateSubnet2CIDR as PrivateSubnet2CIDR
from .params import PublicSubnet1CIDR as PublicSubnet1CIDR
from .params import PublicSubnet2CIDR as PublicSubnet2CIDR
from .params import VpcCIDR as VpcCIDR
from .security import BastionProfile as BastionProfile
from .security import PrivateProfile as PrivateProfile
from .security import RootRole as RootRole
from .security import RootRoleAllowStatement0 as RootRoleAllowStatement0
from .security import RootRoleAllowStatement0_1 as RootRoleAllowStatement0_1
from .security import RootRoleAssumeRolePolicyDocument as RootRoleAssumeRolePolicyDocument
from .security import RootRolePolicies0PolicyDocument as RootRolePolicies0PolicyDocument
from .security import RootRolePolicy as RootRolePolicy

__all__: list[str] = ['AMI_ID', 'ARN', 'AVAILABILITY_ZONE', 'AWS_ACCOUNT_ID', 'AWS_NOTIFICATION_ARNS', 'AWS_NO_VALUE', 'AWS_PARTITION', 'AWS_REGION', 'AWS_STACK_ID', 'AWS_STACK_NAME', 'AWS_URL_SUFFIX', 'And', 'Base64', 'BastionInstance', 'BastionInstanceAssociationParameter', 'BastionProfile', 'BastionSG', 'BastionSGAssociationParameter', 'BastionSGEgress', 'COMMA_DELIMITED_LIST', 'CfnEndpoint', 'CfnEndpointOutput', 'Cidr', 'CloudFormationResource', 'CloudFormationTemplate', 'Condition', 'DefaultPublicRoute', 'DenyStatement', 'EndpointSG', 'EndpointSGAssociationParameter', 'EndpointSGEgress', 'EnvironmentName', 'Equals', 'FindInMap', 'GetAZs', 'GetAtt', 'HOSTED_ZONE_ID', 'INSTANCE_ID', 'If', 'ImportValue', 'InternetGateway', 'InternetGatewayAssociationParameter', 'InternetGatewayAttachment', 'Join', 'KEY_PAIR', 'KeyName', 'LIST_AVAILABILITY_ZONE', 'LIST_NUMBER', 'LIST_SECURITY_GROUP_ID', 'LIST_SUBNET_ID', 'LinuxAMI', 'Mapping', 'NUMBER', 'Not', 'Or', 'Output', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'PrivateInstance', 'PrivateInstanceAssociationParameter', 'PrivateProfile', 'PrivateRouteTable1', 'PrivateRouteTable1AssociationParameter', 'PrivateRouteTable2', 'PrivateRouteTable2AssociationParameter', 'PrivateSG', 'PrivateSGAssociationParameter', 'PrivateSGIngress', 'PrivateSubnet1', 'PrivateSubnet1AssociationParameter', 'PrivateSubnet1CIDR', 'PrivateSubnet1RouteTableAssociation', 'PrivateSubnet2', 'PrivateSubnet2AssociationParameter', 'PrivateSubnet2CIDR', 'PrivateSubnet2RouteTableAssociation', 'PrivateSubnetsOutput', 'PrivateWaitCondition', 'PrivateWaitHandle', 'PropertyType', 'PublicRouteTable', 'PublicRouteTableAssociationParameter', 'PublicSubnet1', 'PublicSubnet1AssociationParameter', 'PublicSubnet1CIDR', 'PublicSubnet1RouteTableAssociation', 'PublicSubnet2', 'PublicSubnet2AssociationParameter', 'PublicSubnet2CIDR', 'PublicSubnet2RouteTableAssociation', 'PublicSubnetsOutput', 'Ref', 'RefDict', 'RefList', 'RootRole', 'RootRoleAllowStatement0', 'RootRoleAllowStatement0_1', 'RootRoleAssumeRolePolicyDocument', 'RootRolePolicies0PolicyDocument', 'RootRolePolicy', 'S3Endpoint', 'S3EndpointAllowStatement0', 'S3EndpointOutput', 'S3EndpointPolicyDocument', 'SECURITY_GROUP_ID', 'SSM_PARAMETER_STRING', 'SSM_PARAMETER_STRING_LIST', 'STRING', 'SUBNET_ID', 'Select', 'Split', 'Sub', 'TemplateCondition', 'Transform', 'VOLUME_ID', 'VPC', 'VPCAssociationParameter', 'VPCOutput', 'VPC_ID', 'VpcCIDR', 'accessanalyzer', 'acmpca', 'aiops', 'amazonmq', 'amplify', 'amplifyuibuilder', 'apigateway', 'apigatewayv2', 'appconfig', 'appflow', 'appintegrations', 'applicationautoscaling', 'applicationinsights', 'applicationsignals', 'appmesh', 'apprunner', 'appstream', 'appsync', 'apptest', 'aps', 'arcregionswitch', 'arczonalshift', 'ask', 'athena', 'auditmanager', 'autoscaling', 'autoscalingplans', 'b2bi', 'backup', 'backupgateway', 'batch', 'bcmdataexports', 'bedrock', 'bedrockagentcore', 'billing', 'billingconductor', 'budgets', 'cases', 'cassandra', 'ce', 'certificatemanager', 'chatbot', 'cleanrooms', 'cleanroomsml', 'cloud9', 'cloudformation', 'cloudfront', 'cloudtrail', 'cloudwatch', 'codeartifact', 'codebuild', 'codecommit', 'codeconnections', 'codedeploy', 'codeguruprofiler', 'codegurureviewer', 'codepipeline', 'codestar', 'codestarconnections', 'codestarnotifications', 'cognito', 'comprehend', 'config', 'connect', 'connectcampaigns', 'connectcampaignsv2', 'controltower', 'cur', 'customerprofiles', 'databrew', 'datapipeline', 'datasync', 'datazone', 'dax', 'deadline', 'detective', 'devopsagent', 'devopsguru', 'directoryservice', 'dlm', 'dms', 'docdb', 'docdbelastic', 'dsql', 'dynamodb', 'ec2', 'ecr', 'ecs', 'efs', 'eks', 'elasticache', 'elasticbeanstalk', 'elasticloadbalancing', 'elasticloadbalancingv2', 'elasticsearch', 'emr', 'emrcontainers', 'emrserverless', 'entityresolution', 'events', 'eventschemas', 'evidently', 'evs', 'finspace', 'fis', 'fms', 'forecast', 'frauddetector', 'fsx', 'gamelift', 'get_att', 'globalaccelerator', 'glue', 'grafana', 'greengrass', 'greengrassv2', 'groundstation', 'guardduty', 'healthimaging', 'healthlake', 'iam', 'identitystore', 'imagebuilder', 'inspector', 'inspectorv2', 'internetmonitor', 'invoicing', 'iot', 'iotanalytics', 'iotcoredeviceadvisor', 'iotevents', 'iotfleetwise', 'iotsitewise', 'iotthingsgraph', 'iottwinmaker', 'iotwireless', 'ivs', 'ivschat', 'kafkaconnect', 'kendra', 'kendraranking', 'kinesis', 'kinesisanalytics', 'kinesisanalyticsv2', 'kinesisfirehose', 'kinesisvideo', 'kms', 'lakeformation', 'lambda_', 'launchwizard', 'lex', 'licensemanager', 'lightsail', 'location', 'logs', 'lookoutequipment', 'lookoutvision', 'm2', 'macie', 'managedblockchain', 'mediaconnect', 'mediaconvert', 'medialive', 'mediapackage', 'mediapackagev2', 'mediastore', 'mediatailor', 'memorydb', 'mpa', 'msk', 'mwaa', 'neptune', 'neptunegraph', 'networkfirewall', 'networkmanager', 'notifications', 'notificationscontacts', 'oam', 'observabilityadmin', 'odb', 'omics', 'opensearchserverless', 'opensearchservice', 'opsworks', 'organizations', 'osis', 'panorama', 'paymentcryptography', 'pcaconnectorad', 'pcaconnectorscep', 'pcs', 'personalize', 'pinpoint', 'pinpointemail', 'pipes', 'proton', 'qbusiness', 'qldb', 'quicksight', 'ram', 'rbin', 'rds', 'redshift', 'redshiftserverless', 'ref', 'refactorspaces', 'rekognition', 'resiliencehub', 'resourceexplorer2', 'resourcegroups', 'robomaker', 'rolesanywhere', 'route53', 'route53profiles', 'route53recoverycontrol', 'route53recoveryreadiness', 'route53resolver', 'rtbfabric', 'rum', 's3', 's3express', 's3objectlambda', 's3outposts', 's3tables', 's3vectors', 'sagemaker', 'scheduler', 'sdb', 'secretsmanager', 'securityhub', 'securitylake', 'serverless', 'servicecatalog', 'servicecatalogappregistry', 'servicediscovery', 'ses', 'setup_params', 'setup_resources', 'shield', 'signer', 'simspaceweaver', 'smsvoice', 'sns', 'sqs', 'ssm', 'ssmcontacts', 'ssmguiconnect', 'ssmincidents', 'ssmquicksetup', 'sso', 'stepfunctions', 'supportapp', 'synthetics', 'systemsmanagersap', 'timestream', 'transfer', 'verifiedpermissions', 'voiceid', 'vpclattice', 'waf', 'wafregional', 'wafv2', 'wetwire_aws', 'wisdom', 'workspaces', 'workspacesinstances', 'workspacesthinclient', 'workspacesweb', 'xray']
