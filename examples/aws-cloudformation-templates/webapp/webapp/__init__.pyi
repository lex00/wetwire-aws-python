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

from .compute import JwtResourceHandler as JwtResourceHandler
from .compute import JwtResourceHandlerContent as JwtResourceHandlerContent
from .compute import JwtResourceHandlerEnvironment as JwtResourceHandlerEnvironment
from .compute import JwtResourcePermission as JwtResourcePermission
from .compute import JwtResourceRootPermission as JwtResourceRootPermission
from .compute import TestResourceHandler as TestResourceHandler
from .compute import TestResourceHandlerContent as TestResourceHandlerContent
from .compute import TestResourceHandlerEnvironment as TestResourceHandlerEnvironment
from .compute import TestResourcePermission as TestResourcePermission
from .compute import TestResourceRootPermission as TestResourceRootPermission
from .database import TestTable as TestTable
from .database import TestTableAttributeDefinition as TestTableAttributeDefinition
from .database import TestTableKeySchema as TestTableKeySchema
from .main import JwtResourceGet as JwtResourceGet
from .main import JwtResourceGetIntegration as JwtResourceGetIntegration
from .main import JwtResourceOptions as JwtResourceOptions
from .main import JwtResourceOptionsIntegration as JwtResourceOptionsIntegration
from .main import JwtResourceResource as JwtResourceResource
from .main import RestApi as RestApi
from .main import RestApiAuthorizer as RestApiAuthorizer
from .main import RestApiDeployment as RestApiDeployment
from .main import RestApiStage as RestApiStage
from .main import SiteDistribution as SiteDistribution
from .main import SiteDistributionDefaultCacheBehavior as SiteDistributionDefaultCacheBehavior
from .main import SiteDistributionDistributionConfig as SiteDistributionDistributionConfig
from .main import SiteDistributionLogging as SiteDistributionLogging
from .main import SiteDistributionOrigin as SiteDistributionOrigin
from .main import SiteDistributionS3OriginConfig as SiteDistributionS3OriginConfig
from .main import SiteDistributionViewerCertificate as SiteDistributionViewerCertificate
from .main import TestResourceGet as TestResourceGet
from .main import TestResourceGetIntegration as TestResourceGetIntegration
from .main import TestResourceOptions as TestResourceOptions
from .main import TestResourceOptionsIntegration as TestResourceOptionsIntegration
from .main import TestResourceResource as TestResourceResource
from .network import SiteOriginAccessControl as SiteOriginAccessControl
from .network import SiteOriginAccessControlOriginAccessControlConfig as SiteOriginAccessControlOriginAccessControlConfig
from .outputs import AppClientIdOutput as AppClientIdOutput
from .outputs import AppNameOutput as AppNameOutput
from .outputs import CognitoDomainPrefixOutput as CognitoDomainPrefixOutput
from .outputs import RedirectURIOutput as RedirectURIOutput
from .outputs import RestApiInvokeURLOutput as RestApiInvokeURLOutput
from .outputs import SiteURLOutput as SiteURLOutput
from .params import AppName as AppName
from .params import LambdaCodeS3Bucket as LambdaCodeS3Bucket
from .params import LambdaCodeS3Key as LambdaCodeS3Key
from .security import CognitoClient as CognitoClient
from .security import CognitoDomain as CognitoDomain
from .security import CognitoUserPool as CognitoUserPool
from .security import CognitoUserPoolAdminCreateUserConfig as CognitoUserPoolAdminCreateUserConfig
from .security import CognitoUserPoolSchemaAttribute as CognitoUserPoolSchemaAttribute
from .security import CognitoUserPoolSchemaAttribute1 as CognitoUserPoolSchemaAttribute1
from .security import CognitoUserPoolSchemaAttribute2 as CognitoUserPoolSchemaAttribute2
from .security import JwtResourceHandlerRole as JwtResourceHandlerRole
from .security import JwtResourceHandlerRoleAllowStatement0 as JwtResourceHandlerRoleAllowStatement0
from .security import JwtResourceHandlerRoleAssumeRolePolicyDocument as JwtResourceHandlerRoleAssumeRolePolicyDocument
from .security import SiteCloudFrontLogsReplicationPolicy as SiteCloudFrontLogsReplicationPolicy
from .security import SiteCloudFrontLogsReplicationPolicyAllowStatement0 as SiteCloudFrontLogsReplicationPolicyAllowStatement0
from .security import SiteCloudFrontLogsReplicationPolicyAllowStatement1 as SiteCloudFrontLogsReplicationPolicyAllowStatement1
from .security import SiteCloudFrontLogsReplicationPolicyAllowStatement2 as SiteCloudFrontLogsReplicationPolicyAllowStatement2
from .security import SiteCloudFrontLogsReplicationPolicyPolicyDocument as SiteCloudFrontLogsReplicationPolicyPolicyDocument
from .security import SiteCloudFrontLogsReplicationRole as SiteCloudFrontLogsReplicationRole
from .security import SiteCloudFrontLogsReplicationRoleAllowStatement0 as SiteCloudFrontLogsReplicationRoleAllowStatement0
from .security import SiteCloudFrontLogsReplicationRoleAssumeRolePolicyDocument as SiteCloudFrontLogsReplicationRoleAssumeRolePolicyDocument
from .security import SiteContentReplicationPolicy as SiteContentReplicationPolicy
from .security import SiteContentReplicationPolicyAllowStatement0 as SiteContentReplicationPolicyAllowStatement0
from .security import SiteContentReplicationPolicyAllowStatement1 as SiteContentReplicationPolicyAllowStatement1
from .security import SiteContentReplicationPolicyAllowStatement2 as SiteContentReplicationPolicyAllowStatement2
from .security import SiteContentReplicationPolicyPolicyDocument as SiteContentReplicationPolicyPolicyDocument
from .security import SiteContentReplicationRole as SiteContentReplicationRole
from .security import SiteContentReplicationRoleAllowStatement0 as SiteContentReplicationRoleAllowStatement0
from .security import SiteContentReplicationRoleAssumeRolePolicyDocument as SiteContentReplicationRoleAssumeRolePolicyDocument
from .security import SiteWebACL as SiteWebACL
from .security import SiteWebACLAllowAction as SiteWebACLAllowAction
from .security import SiteWebACLDefaultAction as SiteWebACLDefaultAction
from .security import SiteWebACLExcludedRule as SiteWebACLExcludedRule
from .security import SiteWebACLManagedRuleGroupStatement as SiteWebACLManagedRuleGroupStatement
from .security import SiteWebACLOverrideAction as SiteWebACLOverrideAction
from .security import SiteWebACLRule as SiteWebACLRule
from .security import SiteWebACLStatement as SiteWebACLStatement
from .security import SiteWebACLVisibilityConfig as SiteWebACLVisibilityConfig
from .security import SiteWebACLVisibilityConfig1 as SiteWebACLVisibilityConfig1
from .security import TestResourceHandlerPolicy as TestResourceHandlerPolicy
from .security import TestResourceHandlerPolicyAllowStatement0 as TestResourceHandlerPolicyAllowStatement0
from .security import TestResourceHandlerPolicyPolicyDocument as TestResourceHandlerPolicyPolicyDocument
from .security import TestResourceHandlerRole as TestResourceHandlerRole
from .security import TestResourceHandlerRoleAllowStatement0 as TestResourceHandlerRoleAllowStatement0
from .security import TestResourceHandlerRoleAssumeRolePolicyDocument as TestResourceHandlerRoleAssumeRolePolicyDocument
from .storage import SiteCloudFrontLogsBucket as SiteCloudFrontLogsBucket
from .storage import SiteCloudFrontLogsBucketAccessPolicy as SiteCloudFrontLogsBucketAccessPolicy
from .storage import SiteCloudFrontLogsBucketAccessPolicyAllowStatement1 as SiteCloudFrontLogsBucketAccessPolicyAllowStatement1
from .storage import SiteCloudFrontLogsBucketAccessPolicyDenyStatement0 as SiteCloudFrontLogsBucketAccessPolicyDenyStatement0
from .storage import SiteCloudFrontLogsBucketAccessPolicyPolicyDocument as SiteCloudFrontLogsBucketAccessPolicyPolicyDocument
from .storage import SiteCloudFrontLogsBucketBucketEncryption as SiteCloudFrontLogsBucketBucketEncryption
from .storage import SiteCloudFrontLogsBucketDeleteMarkerReplication as SiteCloudFrontLogsBucketDeleteMarkerReplication
from .storage import SiteCloudFrontLogsBucketLoggingConfiguration as SiteCloudFrontLogsBucketLoggingConfiguration
from .storage import SiteCloudFrontLogsBucketOwnershipControls as SiteCloudFrontLogsBucketOwnershipControls
from .storage import SiteCloudFrontLogsBucketOwnershipControlsRule as SiteCloudFrontLogsBucketOwnershipControlsRule
from .storage import SiteCloudFrontLogsBucketPublicAccessBlockConfiguration as SiteCloudFrontLogsBucketPublicAccessBlockConfiguration
from .storage import SiteCloudFrontLogsBucketReplicationConfiguration as SiteCloudFrontLogsBucketReplicationConfiguration
from .storage import SiteCloudFrontLogsBucketReplicationDestination as SiteCloudFrontLogsBucketReplicationDestination
from .storage import SiteCloudFrontLogsBucketReplicationRule as SiteCloudFrontLogsBucketReplicationRule
from .storage import SiteCloudFrontLogsBucketServerSideEncryptionByDefault as SiteCloudFrontLogsBucketServerSideEncryptionByDefault
from .storage import SiteCloudFrontLogsBucketServerSideEncryptionRule as SiteCloudFrontLogsBucketServerSideEncryptionRule
from .storage import SiteCloudFrontLogsLogBucket as SiteCloudFrontLogsLogBucket
from .storage import SiteCloudFrontLogsLogBucketAccessPolicy as SiteCloudFrontLogsLogBucketAccessPolicy
from .storage import SiteCloudFrontLogsLogBucketAccessPolicyAllowStatement1 as SiteCloudFrontLogsLogBucketAccessPolicyAllowStatement1
from .storage import SiteCloudFrontLogsLogBucketAccessPolicyDenyStatement0 as SiteCloudFrontLogsLogBucketAccessPolicyDenyStatement0
from .storage import SiteCloudFrontLogsLogBucketAccessPolicyPolicyDocument as SiteCloudFrontLogsLogBucketAccessPolicyPolicyDocument
from .storage import SiteCloudFrontLogsLogBucketBucketEncryption as SiteCloudFrontLogsLogBucketBucketEncryption
from .storage import SiteCloudFrontLogsLogBucketDefaultRetention as SiteCloudFrontLogsLogBucketDefaultRetention
from .storage import SiteCloudFrontLogsLogBucketDeleteMarkerReplication as SiteCloudFrontLogsLogBucketDeleteMarkerReplication
from .storage import SiteCloudFrontLogsLogBucketObjectLockConfiguration as SiteCloudFrontLogsLogBucketObjectLockConfiguration
from .storage import SiteCloudFrontLogsLogBucketObjectLockRule as SiteCloudFrontLogsLogBucketObjectLockRule
from .storage import SiteCloudFrontLogsLogBucketPublicAccessBlockConfiguration as SiteCloudFrontLogsLogBucketPublicAccessBlockConfiguration
from .storage import SiteCloudFrontLogsLogBucketServerSideEncryptionByDefault as SiteCloudFrontLogsLogBucketServerSideEncryptionByDefault
from .storage import SiteCloudFrontLogsLogBucketServerSideEncryptionRule as SiteCloudFrontLogsLogBucketServerSideEncryptionRule
from .storage import SiteCloudFrontLogsReplicaBucket as SiteCloudFrontLogsReplicaBucket
from .storage import SiteCloudFrontLogsReplicaBucketAccessPolicy as SiteCloudFrontLogsReplicaBucketAccessPolicy
from .storage import SiteCloudFrontLogsReplicaBucketAccessPolicyAllowStatement1 as SiteCloudFrontLogsReplicaBucketAccessPolicyAllowStatement1
from .storage import SiteCloudFrontLogsReplicaBucketAccessPolicyDenyStatement0 as SiteCloudFrontLogsReplicaBucketAccessPolicyDenyStatement0
from .storage import SiteCloudFrontLogsReplicaBucketAccessPolicyPolicyDocument as SiteCloudFrontLogsReplicaBucketAccessPolicyPolicyDocument
from .storage import SiteCloudFrontLogsReplicaBucketBucketEncryption as SiteCloudFrontLogsReplicaBucketBucketEncryption
from .storage import SiteCloudFrontLogsReplicaBucketDeleteMarkerReplication as SiteCloudFrontLogsReplicaBucketDeleteMarkerReplication
from .storage import SiteCloudFrontLogsReplicaBucketPublicAccessBlockConfiguration as SiteCloudFrontLogsReplicaBucketPublicAccessBlockConfiguration
from .storage import SiteCloudFrontLogsReplicaBucketServerSideEncryptionByDefault as SiteCloudFrontLogsReplicaBucketServerSideEncryptionByDefault
from .storage import SiteCloudFrontLogsReplicaBucketServerSideEncryptionRule as SiteCloudFrontLogsReplicaBucketServerSideEncryptionRule
from .storage import SiteContentBucket as SiteContentBucket
from .storage import SiteContentBucketAccessPolicy as SiteContentBucketAccessPolicy
from .storage import SiteContentBucketAccessPolicyAllowStatement0 as SiteContentBucketAccessPolicyAllowStatement0
from .storage import SiteContentBucketAccessPolicyAllowStatement2 as SiteContentBucketAccessPolicyAllowStatement2
from .storage import SiteContentBucketAccessPolicyDenyStatement1 as SiteContentBucketAccessPolicyDenyStatement1
from .storage import SiteContentBucketAccessPolicyPolicyDocument as SiteContentBucketAccessPolicyPolicyDocument
from .storage import SiteContentBucketBucketEncryption as SiteContentBucketBucketEncryption
from .storage import SiteContentBucketDeleteMarkerReplication as SiteContentBucketDeleteMarkerReplication
from .storage import SiteContentBucketLoggingConfiguration as SiteContentBucketLoggingConfiguration
from .storage import SiteContentBucketPublicAccessBlockConfiguration as SiteContentBucketPublicAccessBlockConfiguration
from .storage import SiteContentBucketReplicationConfiguration as SiteContentBucketReplicationConfiguration
from .storage import SiteContentBucketReplicationDestination as SiteContentBucketReplicationDestination
from .storage import SiteContentBucketReplicationRule as SiteContentBucketReplicationRule
from .storage import SiteContentBucketServerSideEncryptionByDefault as SiteContentBucketServerSideEncryptionByDefault
from .storage import SiteContentBucketServerSideEncryptionRule as SiteContentBucketServerSideEncryptionRule
from .storage import SiteContentLogBucket as SiteContentLogBucket
from .storage import SiteContentLogBucketAccessPolicy as SiteContentLogBucketAccessPolicy
from .storage import SiteContentLogBucketAccessPolicyAllowStatement1 as SiteContentLogBucketAccessPolicyAllowStatement1
from .storage import SiteContentLogBucketAccessPolicyDenyStatement0 as SiteContentLogBucketAccessPolicyDenyStatement0
from .storage import SiteContentLogBucketAccessPolicyPolicyDocument as SiteContentLogBucketAccessPolicyPolicyDocument
from .storage import SiteContentLogBucketBucketEncryption as SiteContentLogBucketBucketEncryption
from .storage import SiteContentLogBucketDefaultRetention as SiteContentLogBucketDefaultRetention
from .storage import SiteContentLogBucketDeleteMarkerReplication as SiteContentLogBucketDeleteMarkerReplication
from .storage import SiteContentLogBucketObjectLockConfiguration as SiteContentLogBucketObjectLockConfiguration
from .storage import SiteContentLogBucketObjectLockRule as SiteContentLogBucketObjectLockRule
from .storage import SiteContentLogBucketPublicAccessBlockConfiguration as SiteContentLogBucketPublicAccessBlockConfiguration
from .storage import SiteContentLogBucketServerSideEncryptionByDefault as SiteContentLogBucketServerSideEncryptionByDefault
from .storage import SiteContentLogBucketServerSideEncryptionRule as SiteContentLogBucketServerSideEncryptionRule
from .storage import SiteContentReplicaBucket as SiteContentReplicaBucket
from .storage import SiteContentReplicaBucketAccessPolicy as SiteContentReplicaBucketAccessPolicy
from .storage import SiteContentReplicaBucketAccessPolicyAllowStatement1 as SiteContentReplicaBucketAccessPolicyAllowStatement1
from .storage import SiteContentReplicaBucketAccessPolicyDenyStatement0 as SiteContentReplicaBucketAccessPolicyDenyStatement0
from .storage import SiteContentReplicaBucketAccessPolicyPolicyDocument as SiteContentReplicaBucketAccessPolicyPolicyDocument
from .storage import SiteContentReplicaBucketBucketEncryption as SiteContentReplicaBucketBucketEncryption
from .storage import SiteContentReplicaBucketDeleteMarkerReplication as SiteContentReplicaBucketDeleteMarkerReplication
from .storage import SiteContentReplicaBucketPublicAccessBlockConfiguration as SiteContentReplicaBucketPublicAccessBlockConfiguration
from .storage import SiteContentReplicaBucketServerSideEncryptionByDefault as SiteContentReplicaBucketServerSideEncryptionByDefault
from .storage import SiteContentReplicaBucketServerSideEncryptionRule as SiteContentReplicaBucketServerSideEncryptionRule

__all__: list[str] = ['AMI_ID', 'ARN', 'ARN_EQUALS', 'ARN_LIKE', 'ARN_NOT_EQUALS', 'ARN_NOT_LIKE', 'AVAILABILITY_ZONE', 'AWS_ACCOUNT_ID', 'AWS_NOTIFICATION_ARNS', 'AWS_NO_VALUE', 'AWS_PARTITION', 'AWS_REGION', 'AWS_STACK_ID', 'AWS_STACK_NAME', 'AWS_URL_SUFFIX', 'And', 'AppClientIdOutput', 'AppName', 'AppNameOutput', 'Attr', 'BOOL', 'Base64', 'COMMA_DELIMITED_LIST', 'Cidr', 'CloudFormationResource', 'CloudFormationTemplate', 'CognitoClient', 'CognitoDomain', 'CognitoDomainPrefixOutput', 'CognitoUserPool', 'CognitoUserPoolAdminCreateUserConfig', 'CognitoUserPoolSchemaAttribute', 'CognitoUserPoolSchemaAttribute1', 'CognitoUserPoolSchemaAttribute2', 'Condition', 'DATE_EQUALS', 'DATE_GREATER_THAN', 'DATE_GREATER_THAN_EQUALS', 'DATE_LESS_THAN', 'DATE_LESS_THAN_EQUALS', 'DATE_NOT_EQUALS', 'DenyStatement', 'Equals', 'FindInMap', 'GetAZs', 'GetAtt', 'HOSTED_ZONE_ID', 'INSTANCE_ID', 'IP_ADDRESS', 'If', 'ImportValue', 'Join', 'JwtResourceGet', 'JwtResourceGetIntegration', 'JwtResourceHandler', 'JwtResourceHandlerContent', 'JwtResourceHandlerEnvironment', 'JwtResourceHandlerRole', 'JwtResourceHandlerRoleAllowStatement0', 'JwtResourceHandlerRoleAssumeRolePolicyDocument', 'JwtResourceOptions', 'JwtResourceOptionsIntegration', 'JwtResourcePermission', 'JwtResourceResource', 'JwtResourceRootPermission', 'KEY_PAIR', 'LIST_AVAILABILITY_ZONE', 'LIST_NUMBER', 'LIST_SECURITY_GROUP_ID', 'LIST_SUBNET_ID', 'LambdaCodeS3Bucket', 'LambdaCodeS3Key', 'Mapping', 'NOT_IP_ADDRESS', 'NULL', 'NUMBER', 'NUMERIC_EQUALS', 'NUMERIC_GREATER_THAN', 'NUMERIC_GREATER_THAN_EQUALS', 'NUMERIC_LESS_THAN', 'NUMERIC_LESS_THAN_EQUALS', 'NUMERIC_NOT_EQUALS', 'Not', 'Or', 'Output', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'PropertyType', 'RedirectURIOutput', 'Ref', 'RefDict', 'RefIntrinsic', 'RefList', 'RestApi', 'RestApiAuthorizer', 'RestApiDeployment', 'RestApiInvokeURLOutput', 'RestApiStage', 'SECURITY_GROUP_ID', 'SSM_PARAMETER_STRING', 'SSM_PARAMETER_STRING_LIST', 'STRING', 'STRING_EQUALS', 'STRING_EQUALS_IGNORE_CASE', 'STRING_LIKE', 'STRING_NOT_EQUALS', 'STRING_NOT_EQUALS_IGNORE_CASE', 'STRING_NOT_LIKE', 'SUBNET_ID', 'Select', 'SiteCloudFrontLogsBucket', 'SiteCloudFrontLogsBucketAccessPolicy', 'SiteCloudFrontLogsBucketAccessPolicyAllowStatement1', 'SiteCloudFrontLogsBucketAccessPolicyDenyStatement0', 'SiteCloudFrontLogsBucketAccessPolicyPolicyDocument', 'SiteCloudFrontLogsBucketBucketEncryption', 'SiteCloudFrontLogsBucketDeleteMarkerReplication', 'SiteCloudFrontLogsBucketLoggingConfiguration', 'SiteCloudFrontLogsBucketOwnershipControls', 'SiteCloudFrontLogsBucketOwnershipControlsRule', 'SiteCloudFrontLogsBucketPublicAccessBlockConfiguration', 'SiteCloudFrontLogsBucketReplicationConfiguration', 'SiteCloudFrontLogsBucketReplicationDestination', 'SiteCloudFrontLogsBucketReplicationRule', 'SiteCloudFrontLogsBucketServerSideEncryptionByDefault', 'SiteCloudFrontLogsBucketServerSideEncryptionRule', 'SiteCloudFrontLogsLogBucket', 'SiteCloudFrontLogsLogBucketAccessPolicy', 'SiteCloudFrontLogsLogBucketAccessPolicyAllowStatement1', 'SiteCloudFrontLogsLogBucketAccessPolicyDenyStatement0', 'SiteCloudFrontLogsLogBucketAccessPolicyPolicyDocument', 'SiteCloudFrontLogsLogBucketBucketEncryption', 'SiteCloudFrontLogsLogBucketDefaultRetention', 'SiteCloudFrontLogsLogBucketDeleteMarkerReplication', 'SiteCloudFrontLogsLogBucketObjectLockConfiguration', 'SiteCloudFrontLogsLogBucketObjectLockRule', 'SiteCloudFrontLogsLogBucketPublicAccessBlockConfiguration', 'SiteCloudFrontLogsLogBucketServerSideEncryptionByDefault', 'SiteCloudFrontLogsLogBucketServerSideEncryptionRule', 'SiteCloudFrontLogsReplicaBucket', 'SiteCloudFrontLogsReplicaBucketAccessPolicy', 'SiteCloudFrontLogsReplicaBucketAccessPolicyAllowStatement1', 'SiteCloudFrontLogsReplicaBucketAccessPolicyDenyStatement0', 'SiteCloudFrontLogsReplicaBucketAccessPolicyPolicyDocument', 'SiteCloudFrontLogsReplicaBucketBucketEncryption', 'SiteCloudFrontLogsReplicaBucketDeleteMarkerReplication', 'SiteCloudFrontLogsReplicaBucketPublicAccessBlockConfiguration', 'SiteCloudFrontLogsReplicaBucketServerSideEncryptionByDefault', 'SiteCloudFrontLogsReplicaBucketServerSideEncryptionRule', 'SiteCloudFrontLogsReplicationPolicy', 'SiteCloudFrontLogsReplicationPolicyAllowStatement0', 'SiteCloudFrontLogsReplicationPolicyAllowStatement1', 'SiteCloudFrontLogsReplicationPolicyAllowStatement2', 'SiteCloudFrontLogsReplicationPolicyPolicyDocument', 'SiteCloudFrontLogsReplicationRole', 'SiteCloudFrontLogsReplicationRoleAllowStatement0', 'SiteCloudFrontLogsReplicationRoleAssumeRolePolicyDocument', 'SiteContentBucket', 'SiteContentBucketAccessPolicy', 'SiteContentBucketAccessPolicyAllowStatement0', 'SiteContentBucketAccessPolicyAllowStatement2', 'SiteContentBucketAccessPolicyDenyStatement1', 'SiteContentBucketAccessPolicyPolicyDocument', 'SiteContentBucketBucketEncryption', 'SiteContentBucketDeleteMarkerReplication', 'SiteContentBucketLoggingConfiguration', 'SiteContentBucketPublicAccessBlockConfiguration', 'SiteContentBucketReplicationConfiguration', 'SiteContentBucketReplicationDestination', 'SiteContentBucketReplicationRule', 'SiteContentBucketServerSideEncryptionByDefault', 'SiteContentBucketServerSideEncryptionRule', 'SiteContentLogBucket', 'SiteContentLogBucketAccessPolicy', 'SiteContentLogBucketAccessPolicyAllowStatement1', 'SiteContentLogBucketAccessPolicyDenyStatement0', 'SiteContentLogBucketAccessPolicyPolicyDocument', 'SiteContentLogBucketBucketEncryption', 'SiteContentLogBucketDefaultRetention', 'SiteContentLogBucketDeleteMarkerReplication', 'SiteContentLogBucketObjectLockConfiguration', 'SiteContentLogBucketObjectLockRule', 'SiteContentLogBucketPublicAccessBlockConfiguration', 'SiteContentLogBucketServerSideEncryptionByDefault', 'SiteContentLogBucketServerSideEncryptionRule', 'SiteContentReplicaBucket', 'SiteContentReplicaBucketAccessPolicy', 'SiteContentReplicaBucketAccessPolicyAllowStatement1', 'SiteContentReplicaBucketAccessPolicyDenyStatement0', 'SiteContentReplicaBucketAccessPolicyPolicyDocument', 'SiteContentReplicaBucketBucketEncryption', 'SiteContentReplicaBucketDeleteMarkerReplication', 'SiteContentReplicaBucketPublicAccessBlockConfiguration', 'SiteContentReplicaBucketServerSideEncryptionByDefault', 'SiteContentReplicaBucketServerSideEncryptionRule', 'SiteContentReplicationPolicy', 'SiteContentReplicationPolicyAllowStatement0', 'SiteContentReplicationPolicyAllowStatement1', 'SiteContentReplicationPolicyAllowStatement2', 'SiteContentReplicationPolicyPolicyDocument', 'SiteContentReplicationRole', 'SiteContentReplicationRoleAllowStatement0', 'SiteContentReplicationRoleAssumeRolePolicyDocument', 'SiteDistribution', 'SiteDistributionDefaultCacheBehavior', 'SiteDistributionDistributionConfig', 'SiteDistributionLogging', 'SiteDistributionOrigin', 'SiteDistributionS3OriginConfig', 'SiteDistributionViewerCertificate', 'SiteOriginAccessControl', 'SiteOriginAccessControlOriginAccessControlConfig', 'SiteURLOutput', 'SiteWebACL', 'SiteWebACLAllowAction', 'SiteWebACLDefaultAction', 'SiteWebACLExcludedRule', 'SiteWebACLManagedRuleGroupStatement', 'SiteWebACLOverrideAction', 'SiteWebACLRule', 'SiteWebACLStatement', 'SiteWebACLVisibilityConfig', 'SiteWebACLVisibilityConfig1', 'Split', 'Sub', 'Tag', 'TemplateCondition', 'TestResourceGet', 'TestResourceGetIntegration', 'TestResourceHandler', 'TestResourceHandlerContent', 'TestResourceHandlerEnvironment', 'TestResourceHandlerPolicy', 'TestResourceHandlerPolicyAllowStatement0', 'TestResourceHandlerPolicyPolicyDocument', 'TestResourceHandlerRole', 'TestResourceHandlerRoleAllowStatement0', 'TestResourceHandlerRoleAssumeRolePolicyDocument', 'TestResourceOptions', 'TestResourceOptionsIntegration', 'TestResourcePermission', 'TestResourceResource', 'TestResourceRootPermission', 'TestTable', 'TestTableAttributeDefinition', 'TestTableKeySchema', 'Transform', 'VOLUME_ID', 'VPC_ID', 'accessanalyzer', 'acmpca', 'aiops', 'amazonmq', 'amplify', 'amplifyuibuilder', 'apigateway', 'apigatewayv2', 'appconfig', 'appflow', 'appintegrations', 'applicationautoscaling', 'applicationinsights', 'applicationsignals', 'appmesh', 'apprunner', 'appstream', 'appsync', 'apptest', 'aps', 'arcregionswitch', 'arczonalshift', 'ask', 'athena', 'auditmanager', 'autoscaling', 'autoscalingplans', 'b2bi', 'backup', 'backupgateway', 'batch', 'bcmdataexports', 'bedrock', 'bedrockagentcore', 'billing', 'billingconductor', 'budgets', 'cases', 'cassandra', 'ce', 'certificatemanager', 'chatbot', 'cleanrooms', 'cleanroomsml', 'cloud9', 'cloudformation', 'cloudfront', 'cloudtrail', 'cloudwatch', 'codeartifact', 'codebuild', 'codecommit', 'codeconnections', 'codedeploy', 'codeguruprofiler', 'codegurureviewer', 'codepipeline', 'codestar', 'codestarconnections', 'codestarnotifications', 'cognito', 'comprehend', 'config', 'connect', 'connectcampaigns', 'connectcampaignsv2', 'controltower', 'cur', 'customerprofiles', 'databrew', 'datapipeline', 'datasync', 'datazone', 'dax', 'deadline', 'detective', 'devopsagent', 'devopsguru', 'directoryservice', 'dlm', 'dms', 'docdb', 'docdbelastic', 'dsql', 'dynamodb', 'ec2', 'ecr', 'ecs', 'efs', 'eks', 'elasticache', 'elasticbeanstalk', 'elasticloadbalancing', 'elasticloadbalancingv2', 'elasticsearch', 'emr', 'emrcontainers', 'emrserverless', 'entityresolution', 'events', 'eventschemas', 'evidently', 'evs', 'finspace', 'fis', 'fms', 'forecast', 'frauddetector', 'fsx', 'gamelift', 'get_att', 'globalaccelerator', 'glue', 'grafana', 'greengrass', 'greengrassv2', 'groundstation', 'guardduty', 'healthimaging', 'healthlake', 'iam', 'identitystore', 'imagebuilder', 'inspector', 'inspectorv2', 'internetmonitor', 'invoicing', 'iot', 'iotanalytics', 'iotcoredeviceadvisor', 'iotevents', 'iotfleetwise', 'iotsitewise', 'iotthingsgraph', 'iottwinmaker', 'iotwireless', 'ivs', 'ivschat', 'kafkaconnect', 'kendra', 'kendraranking', 'kinesis', 'kinesisanalytics', 'kinesisanalyticsv2', 'kinesisfirehose', 'kinesisvideo', 'kms', 'lakeformation', 'lambda_', 'launchwizard', 'lex', 'licensemanager', 'lightsail', 'location', 'logs', 'lookoutequipment', 'lookoutvision', 'm2', 'macie', 'managedblockchain', 'mediaconnect', 'mediaconvert', 'medialive', 'mediapackage', 'mediapackagev2', 'mediastore', 'mediatailor', 'memorydb', 'mpa', 'msk', 'mwaa', 'neptune', 'neptunegraph', 'networkfirewall', 'networkmanager', 'notifications', 'notificationscontacts', 'oam', 'observabilityadmin', 'odb', 'omics', 'opensearchserverless', 'opensearchservice', 'opsworks', 'organizations', 'osis', 'panorama', 'paymentcryptography', 'pcaconnectorad', 'pcaconnectorscep', 'pcs', 'personalize', 'pinpoint', 'pinpointemail', 'pipes', 'proton', 'qbusiness', 'qldb', 'quicksight', 'ram', 'rbin', 'rds', 'redshift', 'redshiftserverless', 'ref', 'refactorspaces', 'rekognition', 'resiliencehub', 'resourceexplorer2', 'resourcegroups', 'robomaker', 'rolesanywhere', 'route53', 'route53profiles', 'route53recoverycontrol', 'route53recoveryreadiness', 'route53resolver', 'rtbfabric', 'rum', 's3', 's3express', 's3objectlambda', 's3outposts', 's3tables', 's3vectors', 'sagemaker', 'scheduler', 'sdb', 'secretsmanager', 'securityhub', 'securitylake', 'servicecatalog', 'servicecatalogappregistry', 'servicediscovery', 'ses', 'setup_params', 'setup_resources', 'shield', 'signer', 'simspaceweaver', 'smsvoice', 'sns', 'sqs', 'ssm', 'ssmcontacts', 'ssmguiconnect', 'ssmincidents', 'ssmquicksetup', 'sso', 'stepfunctions', 'supportapp', 'synthetics', 'systemsmanagersap', 'timestream', 'transfer', 'verifiedpermissions', 'voiceid', 'vpclattice', 'waf', 'wafregional', 'wafv2', 'wetwire_aws', 'wisdom', 'workspaces', 'workspacesinstances', 'workspacesthinclient', 'workspacesweb', 'xray']
