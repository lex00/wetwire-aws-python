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

from .database import LinkTable as LinkTable
from .database import LinkTableAttributeDefinition as LinkTableAttributeDefinition
from .database import LinkTableAttributeDefinition1 as LinkTableAttributeDefinition1
from .database import LinkTableKeySchema as LinkTableKeySchema
from .database import LinkTableKeySchema1 as LinkTableKeySchema1
from .database import LinkTableLocalSecondaryIndex as LinkTableLocalSecondaryIndex
from .database import LinkTableProjection as LinkTableProjection
from .main import LoggingProcessor as LoggingProcessor
from .main import LoggingProcessorEnvironment as LoggingProcessorEnvironment
from .main import LoggingStream as LoggingStream
from .main import SiteAPI as SiteAPI
from .messaging import LoggingDLQ as LoggingDLQ
from .network import CloudFrontCachePolicyAPI as CloudFrontCachePolicyAPI
from .network import CloudFrontCachePolicyAPICachePolicyConfig as CloudFrontCachePolicyAPICachePolicyConfig
from .network import CloudFrontCachePolicyAPICookiesConfig as CloudFrontCachePolicyAPICookiesConfig
from .network import CloudFrontCachePolicyAPIHeadersConfig as CloudFrontCachePolicyAPIHeadersConfig
from .network import CloudFrontCachePolicyAPIParametersInCacheKeyAndForwardedToOrigin as CloudFrontCachePolicyAPIParametersInCacheKeyAndForwardedToOrigin
from .network import CloudFrontCachePolicyAPIQueryStringsConfig as CloudFrontCachePolicyAPIQueryStringsConfig
from .network import CloudFrontCachePolicyClient as CloudFrontCachePolicyClient
from .network import CloudFrontCachePolicyClientCachePolicyConfig as CloudFrontCachePolicyClientCachePolicyConfig
from .network import CloudFrontCachePolicyClientCookiesConfig as CloudFrontCachePolicyClientCookiesConfig
from .network import CloudFrontCachePolicyClientHeadersConfig as CloudFrontCachePolicyClientHeadersConfig
from .network import CloudFrontCachePolicyClientParametersInCacheKeyAndForwardedToOrigin as CloudFrontCachePolicyClientParametersInCacheKeyAndForwardedToOrigin
from .network import CloudFrontCachePolicyClientQueryStringsConfig as CloudFrontCachePolicyClientQueryStringsConfig
from .network import CloudFrontCachePolicyDefault as CloudFrontCachePolicyDefault
from .network import CloudFrontCachePolicyDefaultCachePolicyConfig as CloudFrontCachePolicyDefaultCachePolicyConfig
from .network import CloudFrontCachePolicyDefaultCookiesConfig as CloudFrontCachePolicyDefaultCookiesConfig
from .network import CloudFrontCachePolicyDefaultHeadersConfig as CloudFrontCachePolicyDefaultHeadersConfig
from .network import CloudFrontCachePolicyDefaultParametersInCacheKeyAndForwardedToOrigin as CloudFrontCachePolicyDefaultParametersInCacheKeyAndForwardedToOrigin
from .network import CloudFrontCachePolicyDefaultQueryStringsConfig as CloudFrontCachePolicyDefaultQueryStringsConfig
from .network import CloudFrontDistro as CloudFrontDistro
from .network import CloudFrontDistroCacheBehavior as CloudFrontDistroCacheBehavior
from .network import CloudFrontDistroCacheBehavior1 as CloudFrontDistroCacheBehavior1
from .network import CloudFrontDistroCacheBehavior2 as CloudFrontDistroCacheBehavior2
from .network import CloudFrontDistroCacheBehavior3 as CloudFrontDistroCacheBehavior3
from .network import CloudFrontDistroCacheBehavior4 as CloudFrontDistroCacheBehavior4
from .network import CloudFrontDistroCacheBehavior5 as CloudFrontDistroCacheBehavior5
from .network import CloudFrontDistroCustomErrorResponse as CloudFrontDistroCustomErrorResponse
from .network import CloudFrontDistroCustomErrorResponse1 as CloudFrontDistroCustomErrorResponse1
from .network import CloudFrontDistroCustomErrorResponse2 as CloudFrontDistroCustomErrorResponse2
from .network import CloudFrontDistroDefaultCacheBehavior as CloudFrontDistroDefaultCacheBehavior
from .network import CloudFrontDistroDistributionConfig as CloudFrontDistroDistributionConfig
from .network import CloudFrontDistroLegacyCustomOrigin as CloudFrontDistroLegacyCustomOrigin
from .network import CloudFrontDistroLegacyCustomOrigin1 as CloudFrontDistroLegacyCustomOrigin1
from .network import CloudFrontDistroLogging as CloudFrontDistroLogging
from .network import CloudFrontDistroOrigin as CloudFrontDistroOrigin
from .network import CloudFrontDistroOrigin1 as CloudFrontDistroOrigin1
from .network import CloudFrontDistroViewerCertificate as CloudFrontDistroViewerCertificate
from .network import CloudFrontLogDistro as CloudFrontLogDistro
from .network import CloudFrontLogDistroEndPoint as CloudFrontLogDistroEndPoint
from .network import CloudFrontLogDistroKinesisStreamConfig as CloudFrontLogDistroKinesisStreamConfig
from .outputs import VueAppAPIRootOutput as VueAppAPIRootOutput
from .outputs import VueAppAuthDomainOutput as VueAppAuthDomainOutput
from .outputs import VueAppClientIdOutput as VueAppClientIdOutput
from .outputs import VueAppNameOutput as VueAppNameOutput
from .params import AppName as AppName
from .params import ClientAddress as ClientAddress
from .params import CustomDomain as CustomDomain
from .params import IsLocalCondition as IsLocalCondition
from .params import UseLocalClient as UseLocalClient
from .security import DDBCrudRole as DDBCrudRole
from .security import DDBCrudRoleAllowStatement0 as DDBCrudRoleAllowStatement0
from .security import DDBCrudRoleAssumeRolePolicyDocument as DDBCrudRoleAssumeRolePolicyDocument
from .security import DDBCrudRolePolicy as DDBCrudRolePolicy
from .security import DDBReadRole as DDBReadRole
from .security import DDBReadRoleAllowStatement0 as DDBReadRoleAllowStatement0
from .security import DDBReadRoleAssumeRolePolicyDocument as DDBReadRoleAssumeRolePolicyDocument
from .security import DDBReadRolePolicy as DDBReadRolePolicy
from .security import LoggingRole as LoggingRole
from .security import LoggingRoleAllowStatement0 as LoggingRoleAllowStatement0
from .security import LoggingRoleAssumeRolePolicyDocument as LoggingRoleAssumeRolePolicyDocument
from .security import LoggingRolePolicy as LoggingRolePolicy
from .security import UserPool as UserPool
from .security import UserPoolClient as UserPoolClient
from .security import UserPoolDomain as UserPoolDomain
from .security import UserPoolPasswordPolicy as UserPoolPasswordPolicy
from .security import UserPoolPolicies as UserPoolPolicies
from .security import UserPoolSchemaAttribute as UserPoolSchemaAttribute
from .storage import CloudFrontAccessLogsBucket as CloudFrontAccessLogsBucket

__all__: list[str] = ['AMI_ID', 'ARN', 'AVAILABILITY_ZONE', 'AWS_ACCOUNT_ID', 'AWS_NOTIFICATION_ARNS', 'AWS_NO_VALUE', 'AWS_PARTITION', 'AWS_REGION', 'AWS_STACK_ID', 'AWS_STACK_NAME', 'AWS_URL_SUFFIX', 'And', 'AppName', 'Base64', 'COMMA_DELIMITED_LIST', 'Cidr', 'ClientAddress', 'CloudFormationResource', 'CloudFormationTemplate', 'CloudFrontAccessLogsBucket', 'CloudFrontCachePolicyAPI', 'CloudFrontCachePolicyAPICachePolicyConfig', 'CloudFrontCachePolicyAPICookiesConfig', 'CloudFrontCachePolicyAPIHeadersConfig', 'CloudFrontCachePolicyAPIParametersInCacheKeyAndForwardedToOrigin', 'CloudFrontCachePolicyAPIQueryStringsConfig', 'CloudFrontCachePolicyClient', 'CloudFrontCachePolicyClientCachePolicyConfig', 'CloudFrontCachePolicyClientCookiesConfig', 'CloudFrontCachePolicyClientHeadersConfig', 'CloudFrontCachePolicyClientParametersInCacheKeyAndForwardedToOrigin', 'CloudFrontCachePolicyClientQueryStringsConfig', 'CloudFrontCachePolicyDefault', 'CloudFrontCachePolicyDefaultCachePolicyConfig', 'CloudFrontCachePolicyDefaultCookiesConfig', 'CloudFrontCachePolicyDefaultHeadersConfig', 'CloudFrontCachePolicyDefaultParametersInCacheKeyAndForwardedToOrigin', 'CloudFrontCachePolicyDefaultQueryStringsConfig', 'CloudFrontDistro', 'CloudFrontDistroCacheBehavior', 'CloudFrontDistroCacheBehavior1', 'CloudFrontDistroCacheBehavior2', 'CloudFrontDistroCacheBehavior3', 'CloudFrontDistroCacheBehavior4', 'CloudFrontDistroCacheBehavior5', 'CloudFrontDistroCustomErrorResponse', 'CloudFrontDistroCustomErrorResponse1', 'CloudFrontDistroCustomErrorResponse2', 'CloudFrontDistroDefaultCacheBehavior', 'CloudFrontDistroDistributionConfig', 'CloudFrontDistroLegacyCustomOrigin', 'CloudFrontDistroLegacyCustomOrigin1', 'CloudFrontDistroLogging', 'CloudFrontDistroOrigin', 'CloudFrontDistroOrigin1', 'CloudFrontDistroViewerCertificate', 'CloudFrontLogDistro', 'CloudFrontLogDistroEndPoint', 'CloudFrontLogDistroKinesisStreamConfig', 'Condition', 'CustomDomain', 'DDBCrudRole', 'DDBCrudRoleAllowStatement0', 'DDBCrudRoleAssumeRolePolicyDocument', 'DDBCrudRolePolicy', 'DDBReadRole', 'DDBReadRoleAllowStatement0', 'DDBReadRoleAssumeRolePolicyDocument', 'DDBReadRolePolicy', 'DenyStatement', 'Equals', 'FindInMap', 'GetAZs', 'GetAtt', 'HOSTED_ZONE_ID', 'INSTANCE_ID', 'If', 'ImportValue', 'IsLocalCondition', 'Join', 'KEY_PAIR', 'LIST_AVAILABILITY_ZONE', 'LIST_NUMBER', 'LIST_SECURITY_GROUP_ID', 'LIST_SUBNET_ID', 'LinkTable', 'LinkTableAttributeDefinition', 'LinkTableAttributeDefinition1', 'LinkTableKeySchema', 'LinkTableKeySchema1', 'LinkTableLocalSecondaryIndex', 'LinkTableProjection', 'LoggingDLQ', 'LoggingProcessor', 'LoggingProcessorEnvironment', 'LoggingRole', 'LoggingRoleAllowStatement0', 'LoggingRoleAssumeRolePolicyDocument', 'LoggingRolePolicy', 'LoggingStream', 'Mapping', 'NUMBER', 'Not', 'Or', 'Output', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'PropertyType', 'Ref', 'RefDict', 'RefList', 'SECURITY_GROUP_ID', 'SSM_PARAMETER_STRING', 'SSM_PARAMETER_STRING_LIST', 'STRING', 'SUBNET_ID', 'Select', 'SiteAPI', 'Split', 'Sub', 'TemplateCondition', 'Transform', 'UseLocalClient', 'UserPool', 'UserPoolClient', 'UserPoolDomain', 'UserPoolPasswordPolicy', 'UserPoolPolicies', 'UserPoolSchemaAttribute', 'VOLUME_ID', 'VPC_ID', 'VueAppAPIRootOutput', 'VueAppAuthDomainOutput', 'VueAppClientIdOutput', 'VueAppNameOutput', 'accessanalyzer', 'acmpca', 'aiops', 'amazonmq', 'amplify', 'amplifyuibuilder', 'apigateway', 'apigatewayv2', 'appconfig', 'appflow', 'appintegrations', 'applicationautoscaling', 'applicationinsights', 'applicationsignals', 'appmesh', 'apprunner', 'appstream', 'appsync', 'apptest', 'aps', 'arcregionswitch', 'arczonalshift', 'ask', 'athena', 'auditmanager', 'autoscaling', 'autoscalingplans', 'b2bi', 'backup', 'backupgateway', 'batch', 'bcmdataexports', 'bedrock', 'bedrockagentcore', 'billing', 'billingconductor', 'budgets', 'cases', 'cassandra', 'ce', 'certificatemanager', 'chatbot', 'cleanrooms', 'cleanroomsml', 'cloud9', 'cloudformation', 'cloudfront', 'cloudtrail', 'cloudwatch', 'codeartifact', 'codebuild', 'codecommit', 'codeconnections', 'codedeploy', 'codeguruprofiler', 'codegurureviewer', 'codepipeline', 'codestar', 'codestarconnections', 'codestarnotifications', 'cognito', 'comprehend', 'config', 'connect', 'connectcampaigns', 'connectcampaignsv2', 'controltower', 'cur', 'customerprofiles', 'databrew', 'datapipeline', 'datasync', 'datazone', 'dax', 'deadline', 'detective', 'devopsagent', 'devopsguru', 'directoryservice', 'dlm', 'dms', 'docdb', 'docdbelastic', 'dsql', 'dynamodb', 'ec2', 'ecr', 'ecs', 'efs', 'eks', 'elasticache', 'elasticbeanstalk', 'elasticloadbalancing', 'elasticloadbalancingv2', 'elasticsearch', 'emr', 'emrcontainers', 'emrserverless', 'entityresolution', 'events', 'eventschemas', 'evidently', 'evs', 'finspace', 'fis', 'fms', 'forecast', 'frauddetector', 'fsx', 'gamelift', 'get_att', 'globalaccelerator', 'glue', 'grafana', 'greengrass', 'greengrassv2', 'groundstation', 'guardduty', 'healthimaging', 'healthlake', 'iam', 'identitystore', 'imagebuilder', 'inspector', 'inspectorv2', 'internetmonitor', 'invoicing', 'iot', 'iotanalytics', 'iotcoredeviceadvisor', 'iotevents', 'iotfleetwise', 'iotsitewise', 'iotthingsgraph', 'iottwinmaker', 'iotwireless', 'ivs', 'ivschat', 'kafkaconnect', 'kendra', 'kendraranking', 'kinesis', 'kinesisanalytics', 'kinesisanalyticsv2', 'kinesisfirehose', 'kinesisvideo', 'kms', 'lakeformation', 'lambda_', 'launchwizard', 'lex', 'licensemanager', 'lightsail', 'location', 'logs', 'lookoutequipment', 'lookoutvision', 'm2', 'macie', 'managedblockchain', 'mediaconnect', 'mediaconvert', 'medialive', 'mediapackage', 'mediapackagev2', 'mediastore', 'mediatailor', 'memorydb', 'mpa', 'msk', 'mwaa', 'neptune', 'neptunegraph', 'networkfirewall', 'networkmanager', 'notifications', 'notificationscontacts', 'oam', 'observabilityadmin', 'odb', 'omics', 'opensearchserverless', 'opensearchservice', 'opsworks', 'organizations', 'osis', 'panorama', 'paymentcryptography', 'pcaconnectorad', 'pcaconnectorscep', 'pcs', 'personalize', 'pinpoint', 'pinpointemail', 'pipes', 'proton', 'qbusiness', 'qldb', 'quicksight', 'ram', 'rbin', 'rds', 'redshift', 'redshiftserverless', 'ref', 'refactorspaces', 'rekognition', 'resiliencehub', 'resourceexplorer2', 'resourcegroups', 'robomaker', 'rolesanywhere', 'route53', 'route53profiles', 'route53recoverycontrol', 'route53recoveryreadiness', 'route53resolver', 'rtbfabric', 'rum', 's3', 's3express', 's3objectlambda', 's3outposts', 's3tables', 's3vectors', 'sagemaker', 'scheduler', 'sdb', 'secretsmanager', 'securityhub', 'securitylake', 'serverless', 'servicecatalog', 'servicecatalogappregistry', 'servicediscovery', 'ses', 'setup_params', 'setup_resources', 'shield', 'signer', 'simspaceweaver', 'smsvoice', 'sns', 'sqs', 'ssm', 'ssmcontacts', 'ssmguiconnect', 'ssmincidents', 'ssmquicksetup', 'sso', 'stepfunctions', 'supportapp', 'synthetics', 'systemsmanagersap', 'timestream', 'transfer', 'verifiedpermissions', 'voiceid', 'vpclattice', 'waf', 'wafregional', 'wafv2', 'wetwire_aws', 'wisdom', 'workspaces', 'workspacesinstances', 'workspacesthinclient', 'workspacesweb', 'xray']
