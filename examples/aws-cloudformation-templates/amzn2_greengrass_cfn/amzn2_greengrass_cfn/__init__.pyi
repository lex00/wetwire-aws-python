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

from .compute import CreateThingFunction as CreateThingFunction
from .compute import CreateThingFunctionCode as CreateThingFunctionCode
from .compute import GGSampleFunction as GGSampleFunction
from .compute import GGSampleFunctionCode as GGSampleFunctionCode
from .compute import GGSampleFunctionVersion as GGSampleFunctionVersion
from .compute import GroupDeploymentResetFunction as GroupDeploymentResetFunction
from .compute import GroupDeploymentResetFunctionCode as GroupDeploymentResetFunctionCode
from .compute import GroupDeploymentResetFunctionEnvironment as GroupDeploymentResetFunctionEnvironment
from .compute import InstanceAZFunction as InstanceAZFunction
from .compute import InstanceAZFunctionCode as InstanceAZFunctionCode
from .main import FunctionDefinition as FunctionDefinition
from .main import FunctionDefinitionDefaultConfig as FunctionDefinitionDefaultConfig
from .main import FunctionDefinitionEnvironment as FunctionDefinitionEnvironment
from .main import FunctionDefinitionExecution as FunctionDefinitionExecution
from .main import FunctionDefinitionExecution1 as FunctionDefinitionExecution1
from .main import FunctionDefinitionFunction as FunctionDefinitionFunction
from .main import FunctionDefinitionFunctionConfiguration as FunctionDefinitionFunctionConfiguration
from .main import FunctionDefinitionFunctionDefinitionVersion as FunctionDefinitionFunctionDefinitionVersion
from .main import FunctionDefinitionRunAs as FunctionDefinitionRunAs
from .main import GreengrassCoreDefinition as GreengrassCoreDefinition
from .main import GreengrassCoreDefinitionVersion as GreengrassCoreDefinitionVersion
from .main import GreengrassCoreDefinitionVersionCore as GreengrassCoreDefinitionVersionCore
from .main import GreengrassGroup as GreengrassGroup
from .main import GreengrassGroupGroupVersion as GreengrassGroupGroupVersion
from .main import GreengrassInstance as GreengrassInstance
from .main import GreengrassInstanceAssociationParameter as GreengrassInstanceAssociationParameter
from .main import GroupDeploymentReset as GroupDeploymentReset
from .main import InstanceAZ as InstanceAZ
from .main import IoTThing as IoTThing
from .main import RouteTableAssociationAPublic as RouteTableAssociationAPublic
from .main import SubnetAPublic as SubnetAPublic
from .main import SubscriptionDefinition as SubscriptionDefinition
from .main import SubscriptionDefinitionSubscription as SubscriptionDefinitionSubscription
from .main import SubscriptionDefinitionSubscription1 as SubscriptionDefinitionSubscription1
from .main import SubscriptionDefinitionSubscription2 as SubscriptionDefinitionSubscription2
from .main import SubscriptionDefinitionSubscriptionDefinitionVersion as SubscriptionDefinitionSubscriptionDefinitionVersion
from .network import InstanceSecurityGroup as InstanceSecurityGroup
from .network import InstanceSecurityGroupEgress as InstanceSecurityGroupEgress
from .network import InternetGateway as InternetGateway
from .network import RouteTablePublic as RouteTablePublic
from .network import RouteTablePublicInternetRoute as RouteTablePublicInternetRoute
from .network import VPC as VPC
from .network import VPCGatewayAttachment as VPCGatewayAttachment
from .outputs import EC2IPAddressOutput as EC2IPAddressOutput
from .params import CoreName as CoreName
from .params import InstanceType as InstanceType
from .params import LatestAmiId as LatestAmiId
from .params import SecurityAccessCIDR as SecurityAccessCIDR
from .params import myKeyPair as myKeyPair
from .security import GreengrassResourceRole as GreengrassResourceRole
from .security import GreengrassResourceRoleAllowStatement0 as GreengrassResourceRoleAllowStatement0
from .security import GreengrassResourceRoleAllowStatement0_1 as GreengrassResourceRoleAllowStatement0_1
from .security import GreengrassResourceRoleAllowStatement1 as GreengrassResourceRoleAllowStatement1
from .security import GreengrassResourceRoleAssumeRolePolicyDocument as GreengrassResourceRoleAssumeRolePolicyDocument
from .security import GreengrassResourceRolePolicies0PolicyDocument as GreengrassResourceRolePolicies0PolicyDocument
from .security import GreengrassResourceRolePolicy as GreengrassResourceRolePolicy
from .security import LambdaExecutionRole as LambdaExecutionRole
from .security import LambdaExecutionRoleAllowStatement0 as LambdaExecutionRoleAllowStatement0
from .security import LambdaExecutionRoleAllowStatement0_1 as LambdaExecutionRoleAllowStatement0_1
from .security import LambdaExecutionRoleAllowStatement1 as LambdaExecutionRoleAllowStatement1
from .security import LambdaExecutionRoleAllowStatement2 as LambdaExecutionRoleAllowStatement2
from .security import LambdaExecutionRoleAllowStatement3 as LambdaExecutionRoleAllowStatement3
from .security import LambdaExecutionRoleAllowStatement4 as LambdaExecutionRoleAllowStatement4
from .security import LambdaExecutionRoleAssumeRolePolicyDocument as LambdaExecutionRoleAssumeRolePolicyDocument
from .security import LambdaExecutionRolePolicies0PolicyDocument as LambdaExecutionRolePolicies0PolicyDocument
from .security import LambdaExecutionRolePolicy as LambdaExecutionRolePolicy

__all__: list[str] = ['AMI_ID', 'ARN', 'ARN_EQUALS', 'ARN_LIKE', 'ARN_NOT_EQUALS', 'ARN_NOT_LIKE', 'AVAILABILITY_ZONE', 'AWS_ACCOUNT_ID', 'AWS_NOTIFICATION_ARNS', 'AWS_NO_VALUE', 'AWS_PARTITION', 'AWS_REGION', 'AWS_STACK_ID', 'AWS_STACK_NAME', 'AWS_URL_SUFFIX', 'And', 'Attr', 'BOOL', 'Base64', 'COMMA_DELIMITED_LIST', 'Cidr', 'CloudFormationResource', 'CloudFormationTemplate', 'Condition', 'CoreName', 'CreateThingFunction', 'CreateThingFunctionCode', 'DATE_EQUALS', 'DATE_GREATER_THAN', 'DATE_GREATER_THAN_EQUALS', 'DATE_LESS_THAN', 'DATE_LESS_THAN_EQUALS', 'DATE_NOT_EQUALS', 'DenyStatement', 'EC2IPAddressOutput', 'Equals', 'FindInMap', 'FunctionDefinition', 'FunctionDefinitionDefaultConfig', 'FunctionDefinitionEnvironment', 'FunctionDefinitionExecution', 'FunctionDefinitionExecution1', 'FunctionDefinitionFunction', 'FunctionDefinitionFunctionConfiguration', 'FunctionDefinitionFunctionDefinitionVersion', 'FunctionDefinitionRunAs', 'GGSampleFunction', 'GGSampleFunctionCode', 'GGSampleFunctionVersion', 'GetAZs', 'GetAtt', 'GreengrassCoreDefinition', 'GreengrassCoreDefinitionVersion', 'GreengrassCoreDefinitionVersionCore', 'GreengrassGroup', 'GreengrassGroupGroupVersion', 'GreengrassInstance', 'GreengrassInstanceAssociationParameter', 'GreengrassResourceRole', 'GreengrassResourceRoleAllowStatement0', 'GreengrassResourceRoleAllowStatement0_1', 'GreengrassResourceRoleAllowStatement1', 'GreengrassResourceRoleAssumeRolePolicyDocument', 'GreengrassResourceRolePolicies0PolicyDocument', 'GreengrassResourceRolePolicy', 'GroupDeploymentReset', 'GroupDeploymentResetFunction', 'GroupDeploymentResetFunctionCode', 'GroupDeploymentResetFunctionEnvironment', 'HOSTED_ZONE_ID', 'INSTANCE_ID', 'IP_ADDRESS', 'If', 'ImportValue', 'InstanceAZ', 'InstanceAZFunction', 'InstanceAZFunctionCode', 'InstanceSecurityGroup', 'InstanceSecurityGroupEgress', 'InstanceType', 'InternetGateway', 'IoTThing', 'Join', 'KEY_PAIR', 'LIST_AVAILABILITY_ZONE', 'LIST_NUMBER', 'LIST_SECURITY_GROUP_ID', 'LIST_SUBNET_ID', 'LambdaExecutionRole', 'LambdaExecutionRoleAllowStatement0', 'LambdaExecutionRoleAllowStatement0_1', 'LambdaExecutionRoleAllowStatement1', 'LambdaExecutionRoleAllowStatement2', 'LambdaExecutionRoleAllowStatement3', 'LambdaExecutionRoleAllowStatement4', 'LambdaExecutionRoleAssumeRolePolicyDocument', 'LambdaExecutionRolePolicies0PolicyDocument', 'LambdaExecutionRolePolicy', 'LatestAmiId', 'Mapping', 'NOT_IP_ADDRESS', 'NULL', 'NUMBER', 'NUMERIC_EQUALS', 'NUMERIC_GREATER_THAN', 'NUMERIC_GREATER_THAN_EQUALS', 'NUMERIC_LESS_THAN', 'NUMERIC_LESS_THAN_EQUALS', 'NUMERIC_NOT_EQUALS', 'Not', 'Or', 'Output', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'PropertyType', 'Ref', 'RefDict', 'RefIntrinsic', 'RefList', 'RouteTableAssociationAPublic', 'RouteTablePublic', 'RouteTablePublicInternetRoute', 'SECURITY_GROUP_ID', 'SSM_PARAMETER_STRING', 'SSM_PARAMETER_STRING_LIST', 'STRING', 'STRING_EQUALS', 'STRING_EQUALS_IGNORE_CASE', 'STRING_LIKE', 'STRING_NOT_EQUALS', 'STRING_NOT_EQUALS_IGNORE_CASE', 'STRING_NOT_LIKE', 'SUBNET_ID', 'SecurityAccessCIDR', 'Select', 'Split', 'Sub', 'SubnetAPublic', 'SubscriptionDefinition', 'SubscriptionDefinitionSubscription', 'SubscriptionDefinitionSubscription1', 'SubscriptionDefinitionSubscription2', 'SubscriptionDefinitionSubscriptionDefinitionVersion', 'Tag', 'TemplateCondition', 'Transform', 'VOLUME_ID', 'VPC', 'VPCGatewayAttachment', 'VPC_ID', 'accessanalyzer', 'acmpca', 'aiops', 'amazonmq', 'amplify', 'amplifyuibuilder', 'apigateway', 'apigatewayv2', 'appconfig', 'appflow', 'appintegrations', 'applicationautoscaling', 'applicationinsights', 'applicationsignals', 'appmesh', 'apprunner', 'appstream', 'appsync', 'apptest', 'aps', 'arcregionswitch', 'arczonalshift', 'ask', 'athena', 'auditmanager', 'autoscaling', 'autoscalingplans', 'b2bi', 'backup', 'backupgateway', 'batch', 'bcmdataexports', 'bedrock', 'bedrockagentcore', 'billing', 'billingconductor', 'budgets', 'cases', 'cassandra', 'ce', 'certificatemanager', 'chatbot', 'cleanrooms', 'cleanroomsml', 'cloud9', 'cloudformation', 'cloudfront', 'cloudtrail', 'cloudwatch', 'codeartifact', 'codebuild', 'codecommit', 'codeconnections', 'codedeploy', 'codeguruprofiler', 'codegurureviewer', 'codepipeline', 'codestar', 'codestarconnections', 'codestarnotifications', 'cognito', 'comprehend', 'config', 'connect', 'connectcampaigns', 'connectcampaignsv2', 'controltower', 'cur', 'customerprofiles', 'databrew', 'datapipeline', 'datasync', 'datazone', 'dax', 'deadline', 'detective', 'devopsagent', 'devopsguru', 'directoryservice', 'dlm', 'dms', 'docdb', 'docdbelastic', 'dsql', 'dynamodb', 'ec2', 'ecr', 'ecs', 'efs', 'eks', 'elasticache', 'elasticbeanstalk', 'elasticloadbalancing', 'elasticloadbalancingv2', 'elasticsearch', 'emr', 'emrcontainers', 'emrserverless', 'entityresolution', 'events', 'eventschemas', 'evidently', 'evs', 'finspace', 'fis', 'fms', 'forecast', 'frauddetector', 'fsx', 'gamelift', 'get_att', 'globalaccelerator', 'glue', 'grafana', 'greengrass', 'greengrassv2', 'groundstation', 'guardduty', 'healthimaging', 'healthlake', 'iam', 'identitystore', 'imagebuilder', 'inspector', 'inspectorv2', 'internetmonitor', 'invoicing', 'iot', 'iotanalytics', 'iotcoredeviceadvisor', 'iotevents', 'iotfleetwise', 'iotsitewise', 'iotthingsgraph', 'iottwinmaker', 'iotwireless', 'ivs', 'ivschat', 'kafkaconnect', 'kendra', 'kendraranking', 'kinesis', 'kinesisanalytics', 'kinesisanalyticsv2', 'kinesisfirehose', 'kinesisvideo', 'kms', 'lakeformation', 'lambda_', 'launchwizard', 'lex', 'licensemanager', 'lightsail', 'location', 'logs', 'lookoutequipment', 'lookoutvision', 'm2', 'macie', 'managedblockchain', 'mediaconnect', 'mediaconvert', 'medialive', 'mediapackage', 'mediapackagev2', 'mediastore', 'mediatailor', 'memorydb', 'mpa', 'msk', 'mwaa', 'myKeyPair', 'neptune', 'neptunegraph', 'networkfirewall', 'networkmanager', 'notifications', 'notificationscontacts', 'oam', 'observabilityadmin', 'odb', 'omics', 'opensearchserverless', 'opensearchservice', 'opsworks', 'organizations', 'osis', 'panorama', 'paymentcryptography', 'pcaconnectorad', 'pcaconnectorscep', 'pcs', 'personalize', 'pinpoint', 'pinpointemail', 'pipes', 'proton', 'qbusiness', 'qldb', 'quicksight', 'ram', 'rbin', 'rds', 'redshift', 'redshiftserverless', 'ref', 'refactorspaces', 'rekognition', 'resiliencehub', 'resourceexplorer2', 'resourcegroups', 'robomaker', 'rolesanywhere', 'route53', 'route53profiles', 'route53recoverycontrol', 'route53recoveryreadiness', 'route53resolver', 'rtbfabric', 'rum', 's3', 's3express', 's3objectlambda', 's3outposts', 's3tables', 's3vectors', 'sagemaker', 'scheduler', 'sdb', 'secretsmanager', 'securityhub', 'securitylake', 'serverless', 'servicecatalog', 'servicecatalogappregistry', 'servicediscovery', 'ses', 'setup_params', 'setup_resources', 'shield', 'signer', 'simspaceweaver', 'smsvoice', 'sns', 'sqs', 'ssm', 'ssmcontacts', 'ssmguiconnect', 'ssmincidents', 'ssmquicksetup', 'sso', 'stepfunctions', 'supportapp', 'synthetics', 'systemsmanagersap', 'timestream', 'transfer', 'verifiedpermissions', 'voiceid', 'vpclattice', 'waf', 'wafregional', 'wafv2', 'wetwire_aws', 'wisdom', 'workspaces', 'workspacesinstances', 'workspacesthinclient', 'workspacesweb', 'xray']
