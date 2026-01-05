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

from .network import Distribution as Distribution
from .network import DistributionDefaultCacheBehavior as DistributionDefaultCacheBehavior
from .network import DistributionDistributionConfig as DistributionDistributionConfig
from .network import DistributionLogging as DistributionLogging
from .network import DistributionOrigin as DistributionOrigin
from .network import DistributionS3OriginConfig as DistributionS3OriginConfig
from .network import DistributionViewerCertificate as DistributionViewerCertificate
from .network import OriginAccessControl as OriginAccessControl
from .network import OriginAccessControlOriginAccessControlConfig as OriginAccessControlOriginAccessControlConfig
from .outputs import SiteURLOutput as SiteURLOutput
from .params import AppName as AppName
from .params import WebACL as WebACL
from .security import CloudFrontLogsReplicationPolicy as CloudFrontLogsReplicationPolicy
from .security import CloudFrontLogsReplicationPolicyAllowStatement0 as CloudFrontLogsReplicationPolicyAllowStatement0
from .security import CloudFrontLogsReplicationPolicyAllowStatement1 as CloudFrontLogsReplicationPolicyAllowStatement1
from .security import CloudFrontLogsReplicationPolicyAllowStatement2 as CloudFrontLogsReplicationPolicyAllowStatement2
from .security import CloudFrontLogsReplicationPolicyPolicyDocument as CloudFrontLogsReplicationPolicyPolicyDocument
from .security import CloudFrontLogsReplicationRole as CloudFrontLogsReplicationRole
from .security import CloudFrontLogsReplicationRoleAllowStatement0 as CloudFrontLogsReplicationRoleAllowStatement0
from .security import CloudFrontLogsReplicationRoleAssumeRolePolicyDocument as CloudFrontLogsReplicationRoleAssumeRolePolicyDocument
from .security import ContentReplicationPolicy as ContentReplicationPolicy
from .security import ContentReplicationPolicyAllowStatement0 as ContentReplicationPolicyAllowStatement0
from .security import ContentReplicationPolicyAllowStatement1 as ContentReplicationPolicyAllowStatement1
from .security import ContentReplicationPolicyAllowStatement2 as ContentReplicationPolicyAllowStatement2
from .security import ContentReplicationPolicyPolicyDocument as ContentReplicationPolicyPolicyDocument
from .security import ContentReplicationRole as ContentReplicationRole
from .security import ContentReplicationRoleAllowStatement0 as ContentReplicationRoleAllowStatement0
from .security import ContentReplicationRoleAssumeRolePolicyDocument as ContentReplicationRoleAssumeRolePolicyDocument
from .storage import CloudFrontLogsBucket as CloudFrontLogsBucket
from .storage import CloudFrontLogsBucketBucketEncryption as CloudFrontLogsBucketBucketEncryption
from .storage import CloudFrontLogsBucketDeleteMarkerReplication as CloudFrontLogsBucketDeleteMarkerReplication
from .storage import CloudFrontLogsBucketLoggingConfiguration as CloudFrontLogsBucketLoggingConfiguration
from .storage import CloudFrontLogsBucketPolicyPolicy as CloudFrontLogsBucketPolicyPolicy
from .storage import CloudFrontLogsBucketPolicyPolicyAllowStatement1 as CloudFrontLogsBucketPolicyPolicyAllowStatement1
from .storage import CloudFrontLogsBucketPolicyPolicyDenyStatement0 as CloudFrontLogsBucketPolicyPolicyDenyStatement0
from .storage import CloudFrontLogsBucketPolicyPolicyPolicyDocument as CloudFrontLogsBucketPolicyPolicyPolicyDocument
from .storage import CloudFrontLogsBucketPublicAccessBlockConfiguration as CloudFrontLogsBucketPublicAccessBlockConfiguration
from .storage import CloudFrontLogsBucketReplicationConfiguration as CloudFrontLogsBucketReplicationConfiguration
from .storage import CloudFrontLogsBucketReplicationDestination as CloudFrontLogsBucketReplicationDestination
from .storage import CloudFrontLogsBucketReplicationRule as CloudFrontLogsBucketReplicationRule
from .storage import CloudFrontLogsBucketServerSideEncryptionByDefault as CloudFrontLogsBucketServerSideEncryptionByDefault
from .storage import CloudFrontLogsBucketServerSideEncryptionRule as CloudFrontLogsBucketServerSideEncryptionRule
from .storage import CloudFrontLogsLogBucket as CloudFrontLogsLogBucket
from .storage import CloudFrontLogsLogBucketBucketEncryption as CloudFrontLogsLogBucketBucketEncryption
from .storage import CloudFrontLogsLogBucketDefaultRetention as CloudFrontLogsLogBucketDefaultRetention
from .storage import CloudFrontLogsLogBucketDeleteMarkerReplication as CloudFrontLogsLogBucketDeleteMarkerReplication
from .storage import CloudFrontLogsLogBucketObjectLockConfiguration as CloudFrontLogsLogBucketObjectLockConfiguration
from .storage import CloudFrontLogsLogBucketObjectLockRule as CloudFrontLogsLogBucketObjectLockRule
from .storage import CloudFrontLogsLogBucketPolicyPolicy as CloudFrontLogsLogBucketPolicyPolicy
from .storage import CloudFrontLogsLogBucketPolicyPolicyAllowStatement1 as CloudFrontLogsLogBucketPolicyPolicyAllowStatement1
from .storage import CloudFrontLogsLogBucketPolicyPolicyDenyStatement0 as CloudFrontLogsLogBucketPolicyPolicyDenyStatement0
from .storage import CloudFrontLogsLogBucketPolicyPolicyPolicyDocument as CloudFrontLogsLogBucketPolicyPolicyPolicyDocument
from .storage import CloudFrontLogsLogBucketPublicAccessBlockConfiguration as CloudFrontLogsLogBucketPublicAccessBlockConfiguration
from .storage import CloudFrontLogsLogBucketServerSideEncryptionByDefault as CloudFrontLogsLogBucketServerSideEncryptionByDefault
from .storage import CloudFrontLogsLogBucketServerSideEncryptionRule as CloudFrontLogsLogBucketServerSideEncryptionRule
from .storage import CloudFrontLogsReplicaBucket as CloudFrontLogsReplicaBucket
from .storage import CloudFrontLogsReplicaBucketBucketEncryption as CloudFrontLogsReplicaBucketBucketEncryption
from .storage import CloudFrontLogsReplicaBucketDeleteMarkerReplication as CloudFrontLogsReplicaBucketDeleteMarkerReplication
from .storage import CloudFrontLogsReplicaBucketPolicyPolicy as CloudFrontLogsReplicaBucketPolicyPolicy
from .storage import CloudFrontLogsReplicaBucketPolicyPolicyAllowStatement1 as CloudFrontLogsReplicaBucketPolicyPolicyAllowStatement1
from .storage import CloudFrontLogsReplicaBucketPolicyPolicyDenyStatement0 as CloudFrontLogsReplicaBucketPolicyPolicyDenyStatement0
from .storage import CloudFrontLogsReplicaBucketPolicyPolicyPolicyDocument as CloudFrontLogsReplicaBucketPolicyPolicyPolicyDocument
from .storage import CloudFrontLogsReplicaBucketPublicAccessBlockConfiguration as CloudFrontLogsReplicaBucketPublicAccessBlockConfiguration
from .storage import CloudFrontLogsReplicaBucketServerSideEncryptionByDefault as CloudFrontLogsReplicaBucketServerSideEncryptionByDefault
from .storage import CloudFrontLogsReplicaBucketServerSideEncryptionRule as CloudFrontLogsReplicaBucketServerSideEncryptionRule
from .storage import ContentBucket as ContentBucket
from .storage import ContentBucketBucketEncryption as ContentBucketBucketEncryption
from .storage import ContentBucketDeleteMarkerReplication as ContentBucketDeleteMarkerReplication
from .storage import ContentBucketLoggingConfiguration as ContentBucketLoggingConfiguration
from .storage import ContentBucketPolicyPolicy as ContentBucketPolicyPolicy
from .storage import ContentBucketPolicyPolicyAllowStatement1 as ContentBucketPolicyPolicyAllowStatement1
from .storage import ContentBucketPolicyPolicyDenyStatement0 as ContentBucketPolicyPolicyDenyStatement0
from .storage import ContentBucketPolicyPolicyPolicyDocument as ContentBucketPolicyPolicyPolicyDocument
from .storage import ContentBucketPublicAccessBlockConfiguration as ContentBucketPublicAccessBlockConfiguration
from .storage import ContentBucketReplicationConfiguration as ContentBucketReplicationConfiguration
from .storage import ContentBucketReplicationDestination as ContentBucketReplicationDestination
from .storage import ContentBucketReplicationRule as ContentBucketReplicationRule
from .storage import ContentBucketServerSideEncryptionByDefault as ContentBucketServerSideEncryptionByDefault
from .storage import ContentBucketServerSideEncryptionRule as ContentBucketServerSideEncryptionRule
from .storage import ContentLogBucket as ContentLogBucket
from .storage import ContentLogBucketBucketEncryption as ContentLogBucketBucketEncryption
from .storage import ContentLogBucketDefaultRetention as ContentLogBucketDefaultRetention
from .storage import ContentLogBucketDeleteMarkerReplication as ContentLogBucketDeleteMarkerReplication
from .storage import ContentLogBucketObjectLockConfiguration as ContentLogBucketObjectLockConfiguration
from .storage import ContentLogBucketObjectLockRule as ContentLogBucketObjectLockRule
from .storage import ContentLogBucketPolicyPolicy as ContentLogBucketPolicyPolicy
from .storage import ContentLogBucketPolicyPolicyAllowStatement1 as ContentLogBucketPolicyPolicyAllowStatement1
from .storage import ContentLogBucketPolicyPolicyDenyStatement0 as ContentLogBucketPolicyPolicyDenyStatement0
from .storage import ContentLogBucketPolicyPolicyPolicyDocument as ContentLogBucketPolicyPolicyPolicyDocument
from .storage import ContentLogBucketPublicAccessBlockConfiguration as ContentLogBucketPublicAccessBlockConfiguration
from .storage import ContentLogBucketServerSideEncryptionByDefault as ContentLogBucketServerSideEncryptionByDefault
from .storage import ContentLogBucketServerSideEncryptionRule as ContentLogBucketServerSideEncryptionRule
from .storage import ContentReplicaBucket as ContentReplicaBucket
from .storage import ContentReplicaBucketBucketEncryption as ContentReplicaBucketBucketEncryption
from .storage import ContentReplicaBucketDeleteMarkerReplication as ContentReplicaBucketDeleteMarkerReplication
from .storage import ContentReplicaBucketPolicyPolicy as ContentReplicaBucketPolicyPolicy
from .storage import ContentReplicaBucketPolicyPolicyAllowStatement1 as ContentReplicaBucketPolicyPolicyAllowStatement1
from .storage import ContentReplicaBucketPolicyPolicyDenyStatement0 as ContentReplicaBucketPolicyPolicyDenyStatement0
from .storage import ContentReplicaBucketPolicyPolicyPolicyDocument as ContentReplicaBucketPolicyPolicyPolicyDocument
from .storage import ContentReplicaBucketPublicAccessBlockConfiguration as ContentReplicaBucketPublicAccessBlockConfiguration
from .storage import ContentReplicaBucketServerSideEncryptionByDefault as ContentReplicaBucketServerSideEncryptionByDefault
from .storage import ContentReplicaBucketServerSideEncryptionRule as ContentReplicaBucketServerSideEncryptionRule

__all__: list[str] = ['AMI_ID', 'ARN', 'ARN_EQUALS', 'ARN_LIKE', 'ARN_NOT_EQUALS', 'ARN_NOT_LIKE', 'AVAILABILITY_ZONE', 'AWS_ACCOUNT_ID', 'AWS_NOTIFICATION_ARNS', 'AWS_NO_VALUE', 'AWS_PARTITION', 'AWS_REGION', 'AWS_STACK_ID', 'AWS_STACK_NAME', 'AWS_URL_SUFFIX', 'And', 'AppName', 'Attr', 'BOOL', 'Base64', 'COMMA_DELIMITED_LIST', 'Cidr', 'CloudFormationResource', 'CloudFormationTemplate', 'CloudFrontLogsBucket', 'CloudFrontLogsBucketBucketEncryption', 'CloudFrontLogsBucketDeleteMarkerReplication', 'CloudFrontLogsBucketLoggingConfiguration', 'CloudFrontLogsBucketPolicyPolicy', 'CloudFrontLogsBucketPolicyPolicyAllowStatement1', 'CloudFrontLogsBucketPolicyPolicyDenyStatement0', 'CloudFrontLogsBucketPolicyPolicyPolicyDocument', 'CloudFrontLogsBucketPublicAccessBlockConfiguration', 'CloudFrontLogsBucketReplicationConfiguration', 'CloudFrontLogsBucketReplicationDestination', 'CloudFrontLogsBucketReplicationRule', 'CloudFrontLogsBucketServerSideEncryptionByDefault', 'CloudFrontLogsBucketServerSideEncryptionRule', 'CloudFrontLogsLogBucket', 'CloudFrontLogsLogBucketBucketEncryption', 'CloudFrontLogsLogBucketDefaultRetention', 'CloudFrontLogsLogBucketDeleteMarkerReplication', 'CloudFrontLogsLogBucketObjectLockConfiguration', 'CloudFrontLogsLogBucketObjectLockRule', 'CloudFrontLogsLogBucketPolicyPolicy', 'CloudFrontLogsLogBucketPolicyPolicyAllowStatement1', 'CloudFrontLogsLogBucketPolicyPolicyDenyStatement0', 'CloudFrontLogsLogBucketPolicyPolicyPolicyDocument', 'CloudFrontLogsLogBucketPublicAccessBlockConfiguration', 'CloudFrontLogsLogBucketServerSideEncryptionByDefault', 'CloudFrontLogsLogBucketServerSideEncryptionRule', 'CloudFrontLogsReplicaBucket', 'CloudFrontLogsReplicaBucketBucketEncryption', 'CloudFrontLogsReplicaBucketDeleteMarkerReplication', 'CloudFrontLogsReplicaBucketPolicyPolicy', 'CloudFrontLogsReplicaBucketPolicyPolicyAllowStatement1', 'CloudFrontLogsReplicaBucketPolicyPolicyDenyStatement0', 'CloudFrontLogsReplicaBucketPolicyPolicyPolicyDocument', 'CloudFrontLogsReplicaBucketPublicAccessBlockConfiguration', 'CloudFrontLogsReplicaBucketServerSideEncryptionByDefault', 'CloudFrontLogsReplicaBucketServerSideEncryptionRule', 'CloudFrontLogsReplicationPolicy', 'CloudFrontLogsReplicationPolicyAllowStatement0', 'CloudFrontLogsReplicationPolicyAllowStatement1', 'CloudFrontLogsReplicationPolicyAllowStatement2', 'CloudFrontLogsReplicationPolicyPolicyDocument', 'CloudFrontLogsReplicationRole', 'CloudFrontLogsReplicationRoleAllowStatement0', 'CloudFrontLogsReplicationRoleAssumeRolePolicyDocument', 'Condition', 'ContentBucket', 'ContentBucketBucketEncryption', 'ContentBucketDeleteMarkerReplication', 'ContentBucketLoggingConfiguration', 'ContentBucketPolicyPolicy', 'ContentBucketPolicyPolicyAllowStatement1', 'ContentBucketPolicyPolicyDenyStatement0', 'ContentBucketPolicyPolicyPolicyDocument', 'ContentBucketPublicAccessBlockConfiguration', 'ContentBucketReplicationConfiguration', 'ContentBucketReplicationDestination', 'ContentBucketReplicationRule', 'ContentBucketServerSideEncryptionByDefault', 'ContentBucketServerSideEncryptionRule', 'ContentLogBucket', 'ContentLogBucketBucketEncryption', 'ContentLogBucketDefaultRetention', 'ContentLogBucketDeleteMarkerReplication', 'ContentLogBucketObjectLockConfiguration', 'ContentLogBucketObjectLockRule', 'ContentLogBucketPolicyPolicy', 'ContentLogBucketPolicyPolicyAllowStatement1', 'ContentLogBucketPolicyPolicyDenyStatement0', 'ContentLogBucketPolicyPolicyPolicyDocument', 'ContentLogBucketPublicAccessBlockConfiguration', 'ContentLogBucketServerSideEncryptionByDefault', 'ContentLogBucketServerSideEncryptionRule', 'ContentReplicaBucket', 'ContentReplicaBucketBucketEncryption', 'ContentReplicaBucketDeleteMarkerReplication', 'ContentReplicaBucketPolicyPolicy', 'ContentReplicaBucketPolicyPolicyAllowStatement1', 'ContentReplicaBucketPolicyPolicyDenyStatement0', 'ContentReplicaBucketPolicyPolicyPolicyDocument', 'ContentReplicaBucketPublicAccessBlockConfiguration', 'ContentReplicaBucketServerSideEncryptionByDefault', 'ContentReplicaBucketServerSideEncryptionRule', 'ContentReplicationPolicy', 'ContentReplicationPolicyAllowStatement0', 'ContentReplicationPolicyAllowStatement1', 'ContentReplicationPolicyAllowStatement2', 'ContentReplicationPolicyPolicyDocument', 'ContentReplicationRole', 'ContentReplicationRoleAllowStatement0', 'ContentReplicationRoleAssumeRolePolicyDocument', 'DATE_EQUALS', 'DATE_GREATER_THAN', 'DATE_GREATER_THAN_EQUALS', 'DATE_LESS_THAN', 'DATE_LESS_THAN_EQUALS', 'DATE_NOT_EQUALS', 'DenyStatement', 'Distribution', 'DistributionDefaultCacheBehavior', 'DistributionDistributionConfig', 'DistributionLogging', 'DistributionOrigin', 'DistributionS3OriginConfig', 'DistributionViewerCertificate', 'Equals', 'FindInMap', 'GetAZs', 'GetAtt', 'HOSTED_ZONE_ID', 'INSTANCE_ID', 'IP_ADDRESS', 'If', 'ImportValue', 'Join', 'KEY_PAIR', 'LIST_AVAILABILITY_ZONE', 'LIST_NUMBER', 'LIST_SECURITY_GROUP_ID', 'LIST_SUBNET_ID', 'Mapping', 'NOT_IP_ADDRESS', 'NULL', 'NUMBER', 'NUMERIC_EQUALS', 'NUMERIC_GREATER_THAN', 'NUMERIC_GREATER_THAN_EQUALS', 'NUMERIC_LESS_THAN', 'NUMERIC_LESS_THAN_EQUALS', 'NUMERIC_NOT_EQUALS', 'Not', 'Or', 'OriginAccessControl', 'OriginAccessControlOriginAccessControlConfig', 'Output', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'PropertyType', 'Ref', 'RefDict', 'RefIntrinsic', 'RefList', 'SECURITY_GROUP_ID', 'SSM_PARAMETER_STRING', 'SSM_PARAMETER_STRING_LIST', 'STRING', 'STRING_EQUALS', 'STRING_EQUALS_IGNORE_CASE', 'STRING_LIKE', 'STRING_NOT_EQUALS', 'STRING_NOT_EQUALS_IGNORE_CASE', 'STRING_NOT_LIKE', 'SUBNET_ID', 'Select', 'SiteURLOutput', 'Split', 'Sub', 'Tag', 'TemplateCondition', 'Transform', 'VOLUME_ID', 'VPC_ID', 'WebACL', 'accessanalyzer', 'acmpca', 'aiops', 'amazonmq', 'amplify', 'amplifyuibuilder', 'apigateway', 'apigatewayv2', 'appconfig', 'appflow', 'appintegrations', 'applicationautoscaling', 'applicationinsights', 'applicationsignals', 'appmesh', 'apprunner', 'appstream', 'appsync', 'apptest', 'aps', 'arcregionswitch', 'arczonalshift', 'ask', 'athena', 'auditmanager', 'autoscaling', 'autoscalingplans', 'b2bi', 'backup', 'backupgateway', 'batch', 'bcmdataexports', 'bedrock', 'bedrockagentcore', 'billing', 'billingconductor', 'budgets', 'cases', 'cassandra', 'ce', 'certificatemanager', 'chatbot', 'cleanrooms', 'cleanroomsml', 'cloud9', 'cloudformation', 'cloudfront', 'cloudtrail', 'cloudwatch', 'codeartifact', 'codebuild', 'codecommit', 'codeconnections', 'codedeploy', 'codeguruprofiler', 'codegurureviewer', 'codepipeline', 'codestar', 'codestarconnections', 'codestarnotifications', 'cognito', 'comprehend', 'config', 'connect', 'connectcampaigns', 'connectcampaignsv2', 'controltower', 'cur', 'customerprofiles', 'databrew', 'datapipeline', 'datasync', 'datazone', 'dax', 'deadline', 'detective', 'devopsagent', 'devopsguru', 'directoryservice', 'dlm', 'dms', 'docdb', 'docdbelastic', 'dsql', 'dynamodb', 'ec2', 'ecr', 'ecs', 'efs', 'eks', 'elasticache', 'elasticbeanstalk', 'elasticloadbalancing', 'elasticloadbalancingv2', 'elasticsearch', 'emr', 'emrcontainers', 'emrserverless', 'entityresolution', 'events', 'eventschemas', 'evidently', 'evs', 'finspace', 'fis', 'fms', 'forecast', 'frauddetector', 'fsx', 'gamelift', 'get_att', 'globalaccelerator', 'glue', 'grafana', 'greengrass', 'greengrassv2', 'groundstation', 'guardduty', 'healthimaging', 'healthlake', 'iam', 'identitystore', 'imagebuilder', 'inspector', 'inspectorv2', 'internetmonitor', 'invoicing', 'iot', 'iotanalytics', 'iotcoredeviceadvisor', 'iotevents', 'iotfleetwise', 'iotsitewise', 'iotthingsgraph', 'iottwinmaker', 'iotwireless', 'ivs', 'ivschat', 'kafkaconnect', 'kendra', 'kendraranking', 'kinesis', 'kinesisanalytics', 'kinesisanalyticsv2', 'kinesisfirehose', 'kinesisvideo', 'kms', 'lakeformation', 'lambda_', 'launchwizard', 'lex', 'licensemanager', 'lightsail', 'location', 'logs', 'lookoutequipment', 'lookoutvision', 'm2', 'macie', 'managedblockchain', 'mediaconnect', 'mediaconvert', 'medialive', 'mediapackage', 'mediapackagev2', 'mediastore', 'mediatailor', 'memorydb', 'mpa', 'msk', 'mwaa', 'neptune', 'neptunegraph', 'networkfirewall', 'networkmanager', 'notifications', 'notificationscontacts', 'oam', 'observabilityadmin', 'odb', 'omics', 'opensearchserverless', 'opensearchservice', 'opsworks', 'organizations', 'osis', 'panorama', 'paymentcryptography', 'pcaconnectorad', 'pcaconnectorscep', 'pcs', 'personalize', 'pinpoint', 'pinpointemail', 'pipes', 'proton', 'qbusiness', 'qldb', 'quicksight', 'ram', 'rbin', 'rds', 'redshift', 'redshiftserverless', 'ref', 'refactorspaces', 'rekognition', 'resiliencehub', 'resourceexplorer2', 'resourcegroups', 'robomaker', 'rolesanywhere', 'route53', 'route53profiles', 'route53recoverycontrol', 'route53recoveryreadiness', 'route53resolver', 'rtbfabric', 'rum', 's3', 's3express', 's3objectlambda', 's3outposts', 's3tables', 's3vectors', 'sagemaker', 'scheduler', 'sdb', 'secretsmanager', 'securityhub', 'securitylake', 'servicecatalog', 'servicecatalogappregistry', 'servicediscovery', 'ses', 'setup_params', 'setup_resources', 'shield', 'signer', 'simspaceweaver', 'smsvoice', 'sns', 'sqs', 'ssm', 'ssmcontacts', 'ssmguiconnect', 'ssmincidents', 'ssmquicksetup', 'sso', 'stepfunctions', 'supportapp', 'synthetics', 'systemsmanagersap', 'timestream', 'transfer', 'verifiedpermissions', 'voiceid', 'vpclattice', 'waf', 'wafregional', 'wafv2', 'wetwire_aws', 'wisdom', 'workspaces', 'workspacesinstances', 'workspacesthinclient', 'workspacesweb', 'xray']
