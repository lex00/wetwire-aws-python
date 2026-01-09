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

from .database import NeptuneDBCluster as NeptuneDBCluster
from .database import NeptuneDBClusterParameterGroup as NeptuneDBClusterParameterGroup
from .database import NeptuneDBInstance as NeptuneDBInstance
from .database import NeptuneDBParameterGroup as NeptuneDBParameterGroup
from .database import NeptuneDBSubnetGroup as NeptuneDBSubnetGroup
from .messaging import NeptuneAlarmSubscription as NeptuneAlarmSubscription
from .messaging import NeptuneAlarmTopic as NeptuneAlarmTopic
from .monitoring import NeptunePrimaryCpuAlarm as NeptunePrimaryCpuAlarm
from .monitoring import NeptunePrimaryCpuAlarmDimension as NeptunePrimaryCpuAlarmDimension
from .monitoring import NeptunePrimaryGremlinRequestsPerSecAlarm as NeptunePrimaryGremlinRequestsPerSecAlarm
from .monitoring import NeptunePrimaryGremlinRequestsPerSecAlarmDimension as NeptunePrimaryGremlinRequestsPerSecAlarmDimension
from .monitoring import NeptunePrimaryMemoryAlarm as NeptunePrimaryMemoryAlarm
from .monitoring import NeptunePrimaryMemoryAlarmDimension as NeptunePrimaryMemoryAlarmDimension
from .monitoring import NeptunePrimarySparqlRequestsPerSecAlarm as NeptunePrimarySparqlRequestsPerSecAlarm
from .monitoring import NeptunePrimarySparqlRequestsPerSecAlarmDimension as NeptunePrimarySparqlRequestsPerSecAlarmDimension
from .network import NeptuneDBSG as NeptuneDBSG
from .network import NeptuneDBSGAssociationParameter as NeptuneDBSGAssociationParameter
from .outputs import NeptuneEndpointAddressOutput as NeptuneEndpointAddressOutput
from .outputs import NeptuneEndpointPortOutput as NeptuneEndpointPortOutput
from .outputs import NeptuneReadEndpointAddressOutput as NeptuneReadEndpointAddressOutput
from .outputs import NeptuneSnsTopicOutput as NeptuneSnsTopicOutput
from .params import AppName as AppName
from .params import BackupRetentionPeriod as BackupRetentionPeriod
from .params import CreateSnsSubscriptionCondition as CreateSnsSubscriptionCondition
from .params import CreateSnsTopicCondition as CreateSnsTopicCondition
from .params import DBClusterIdentifier as DBClusterIdentifier
from .params import DBInstanceClass as DBInstanceClass
from .params import EnableAuditLogUploadCondition as EnableAuditLogUploadCondition
from .params import Env as Env
from .params import GremlinRequestsPerSecThreshold as GremlinRequestsPerSecThreshold
from .params import HighCpuAlarmThreshold as HighCpuAlarmThreshold
from .params import IAMAuthEnabled as IAMAuthEnabled
from .params import LowMemoryAlarmThreshold as LowMemoryAlarmThreshold
from .params import MajorVersionUpgrade as MajorVersionUpgrade
from .params import MinorVersionUpgrade as MinorVersionUpgrade
from .params import NeptuneDBClusterPreferredBackupWindow as NeptuneDBClusterPreferredBackupWindow
from .params import NeptuneDBClusterPreferredMaintenanceWindow as NeptuneDBClusterPreferredMaintenanceWindow
from .params import NeptuneDBInstancePreferredMaintenanceWindow as NeptuneDBInstancePreferredMaintenanceWindow
from .params import NeptuneDBSubnetGroupName as NeptuneDBSubnetGroupName
from .params import NeptuneQueryTimeout as NeptuneQueryTimeout
from .params import NeptuneSNSTopicArn as NeptuneSNSTopicArn
from .params import Owner as Owner
from .params import Port as Port
from .params import SNSEmailSubscription as SNSEmailSubscription
from .params import SparqlRequestsPerSecThreshold as SparqlRequestsPerSecThreshold
from .params import Storage as Storage
from .params import StorageEncrypted as StorageEncrypted
from .params import Tier as Tier
from .params import UploadAuditLogs as UploadAuditLogs
from .params import User as User
from .params import VPCStack as VPCStack
from .params import Version as Version
from .security import NeptuneCloudWatchPolicy as NeptuneCloudWatchPolicy
from .security import NeptuneCloudWatchPolicyAllowStatement0 as NeptuneCloudWatchPolicyAllowStatement0
from .security import NeptuneCloudWatchPolicyAllowStatement1 as NeptuneCloudWatchPolicyAllowStatement1
from .security import NeptuneCloudWatchPolicyPolicyDocument as NeptuneCloudWatchPolicyPolicyDocument
from .security import NeptuneRole as NeptuneRole
from .security import NeptuneRoleAllowStatement0 as NeptuneRoleAllowStatement0
from .security import NeptuneRoleAssumeRolePolicyDocument as NeptuneRoleAssumeRolePolicyDocument
from .security import NeptuneS3Policy as NeptuneS3Policy
from .security import NeptuneS3PolicyAllowStatement0 as NeptuneS3PolicyAllowStatement0
from .security import NeptuneS3PolicyPolicyDocument as NeptuneS3PolicyPolicyDocument

__all__: list[str] = ['AMI_ID', 'ARN', 'AVAILABILITY_ZONE', 'AWS_ACCOUNT_ID', 'AWS_NOTIFICATION_ARNS', 'AWS_NO_VALUE', 'AWS_PARTITION', 'AWS_REGION', 'AWS_STACK_ID', 'AWS_STACK_NAME', 'AWS_URL_SUFFIX', 'And', 'AppName', 'BackupRetentionPeriod', 'Base64', 'COMMA_DELIMITED_LIST', 'Cidr', 'CloudFormationResource', 'CloudFormationTemplate', 'Condition', 'CreateSnsSubscriptionCondition', 'CreateSnsTopicCondition', 'DBClusterIdentifier', 'DBInstanceClass', 'DenyStatement', 'EnableAuditLogUploadCondition', 'Env', 'Equals', 'FindInMap', 'GetAZs', 'GetAtt', 'GremlinRequestsPerSecThreshold', 'HOSTED_ZONE_ID', 'HighCpuAlarmThreshold', 'IAMAuthEnabled', 'INSTANCE_ID', 'If', 'ImportValue', 'Join', 'KEY_PAIR', 'LIST_AVAILABILITY_ZONE', 'LIST_NUMBER', 'LIST_SECURITY_GROUP_ID', 'LIST_SUBNET_ID', 'LowMemoryAlarmThreshold', 'MajorVersionUpgrade', 'Mapping', 'MinorVersionUpgrade', 'NUMBER', 'NeptuneAlarmSubscription', 'NeptuneAlarmTopic', 'NeptuneCloudWatchPolicy', 'NeptuneCloudWatchPolicyAllowStatement0', 'NeptuneCloudWatchPolicyAllowStatement1', 'NeptuneCloudWatchPolicyPolicyDocument', 'NeptuneDBCluster', 'NeptuneDBClusterParameterGroup', 'NeptuneDBClusterPreferredBackupWindow', 'NeptuneDBClusterPreferredMaintenanceWindow', 'NeptuneDBInstance', 'NeptuneDBInstancePreferredMaintenanceWindow', 'NeptuneDBParameterGroup', 'NeptuneDBSG', 'NeptuneDBSGAssociationParameter', 'NeptuneDBSubnetGroup', 'NeptuneDBSubnetGroupName', 'NeptuneEndpointAddressOutput', 'NeptuneEndpointPortOutput', 'NeptunePrimaryCpuAlarm', 'NeptunePrimaryCpuAlarmDimension', 'NeptunePrimaryGremlinRequestsPerSecAlarm', 'NeptunePrimaryGremlinRequestsPerSecAlarmDimension', 'NeptunePrimaryMemoryAlarm', 'NeptunePrimaryMemoryAlarmDimension', 'NeptunePrimarySparqlRequestsPerSecAlarm', 'NeptunePrimarySparqlRequestsPerSecAlarmDimension', 'NeptuneQueryTimeout', 'NeptuneReadEndpointAddressOutput', 'NeptuneRole', 'NeptuneRoleAllowStatement0', 'NeptuneRoleAssumeRolePolicyDocument', 'NeptuneS3Policy', 'NeptuneS3PolicyAllowStatement0', 'NeptuneS3PolicyPolicyDocument', 'NeptuneSNSTopicArn', 'NeptuneSnsTopicOutput', 'Not', 'Or', 'Output', 'Owner', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'Port', 'PropertyType', 'Ref', 'RefDict', 'RefList', 'SECURITY_GROUP_ID', 'SNSEmailSubscription', 'SSM_PARAMETER_STRING', 'SSM_PARAMETER_STRING_LIST', 'STRING', 'SUBNET_ID', 'Select', 'SparqlRequestsPerSecThreshold', 'Split', 'Storage', 'StorageEncrypted', 'Sub', 'TemplateCondition', 'Tier', 'Transform', 'UploadAuditLogs', 'User', 'VOLUME_ID', 'VPCStack', 'VPC_ID', 'Version', 'accessanalyzer', 'acmpca', 'aiops', 'amazonmq', 'amplify', 'amplifyuibuilder', 'apigateway', 'apigatewayv2', 'appconfig', 'appflow', 'appintegrations', 'applicationautoscaling', 'applicationinsights', 'applicationsignals', 'appmesh', 'apprunner', 'appstream', 'appsync', 'apptest', 'aps', 'arcregionswitch', 'arczonalshift', 'ask', 'athena', 'auditmanager', 'autoscaling', 'autoscalingplans', 'b2bi', 'backup', 'backupgateway', 'batch', 'bcmdataexports', 'bedrock', 'bedrockagentcore', 'billing', 'billingconductor', 'budgets', 'cases', 'cassandra', 'ce', 'certificatemanager', 'chatbot', 'cleanrooms', 'cleanroomsml', 'cloud9', 'cloudformation', 'cloudfront', 'cloudtrail', 'cloudwatch', 'codeartifact', 'codebuild', 'codecommit', 'codeconnections', 'codedeploy', 'codeguruprofiler', 'codegurureviewer', 'codepipeline', 'codestar', 'codestarconnections', 'codestarnotifications', 'cognito', 'comprehend', 'config', 'connect', 'connectcampaigns', 'connectcampaignsv2', 'controltower', 'cur', 'customerprofiles', 'databrew', 'datapipeline', 'datasync', 'datazone', 'dax', 'deadline', 'detective', 'devopsagent', 'devopsguru', 'directoryservice', 'dlm', 'dms', 'docdb', 'docdbelastic', 'dsql', 'dynamodb', 'ec2', 'ecr', 'ecs', 'efs', 'eks', 'elasticache', 'elasticbeanstalk', 'elasticloadbalancing', 'elasticloadbalancingv2', 'elasticsearch', 'emr', 'emrcontainers', 'emrserverless', 'entityresolution', 'events', 'eventschemas', 'evidently', 'evs', 'finspace', 'fis', 'fms', 'forecast', 'frauddetector', 'fsx', 'gamelift', 'get_att', 'globalaccelerator', 'glue', 'grafana', 'greengrass', 'greengrassv2', 'groundstation', 'guardduty', 'healthimaging', 'healthlake', 'iam', 'identitystore', 'imagebuilder', 'inspector', 'inspectorv2', 'internetmonitor', 'invoicing', 'iot', 'iotanalytics', 'iotcoredeviceadvisor', 'iotevents', 'iotfleetwise', 'iotsitewise', 'iotthingsgraph', 'iottwinmaker', 'iotwireless', 'ivs', 'ivschat', 'kafkaconnect', 'kendra', 'kendraranking', 'kinesis', 'kinesisanalytics', 'kinesisanalyticsv2', 'kinesisfirehose', 'kinesisvideo', 'kms', 'lakeformation', 'lambda_', 'launchwizard', 'lex', 'licensemanager', 'lightsail', 'location', 'logs', 'lookoutequipment', 'lookoutvision', 'm2', 'macie', 'managedblockchain', 'mediaconnect', 'mediaconvert', 'medialive', 'mediapackage', 'mediapackagev2', 'mediastore', 'mediatailor', 'memorydb', 'mpa', 'msk', 'mwaa', 'neptune', 'neptunegraph', 'networkfirewall', 'networkmanager', 'notifications', 'notificationscontacts', 'oam', 'observabilityadmin', 'odb', 'omics', 'opensearchserverless', 'opensearchservice', 'opsworks', 'organizations', 'osis', 'panorama', 'paymentcryptography', 'pcaconnectorad', 'pcaconnectorscep', 'pcs', 'personalize', 'pinpoint', 'pinpointemail', 'pipes', 'proton', 'qbusiness', 'qldb', 'quicksight', 'ram', 'rbin', 'rds', 'redshift', 'redshiftserverless', 'ref', 'refactorspaces', 'rekognition', 'resiliencehub', 'resourceexplorer2', 'resourcegroups', 'robomaker', 'rolesanywhere', 'route53', 'route53profiles', 'route53recoverycontrol', 'route53recoveryreadiness', 'route53resolver', 'rtbfabric', 'rum', 's3', 's3express', 's3objectlambda', 's3outposts', 's3tables', 's3vectors', 'sagemaker', 'scheduler', 'sdb', 'secretsmanager', 'securityhub', 'securitylake', 'serverless', 'servicecatalog', 'servicecatalogappregistry', 'servicediscovery', 'ses', 'setup_params', 'setup_resources', 'shield', 'signer', 'simspaceweaver', 'smsvoice', 'sns', 'sqs', 'ssm', 'ssmcontacts', 'ssmguiconnect', 'ssmincidents', 'ssmquicksetup', 'sso', 'stepfunctions', 'supportapp', 'synthetics', 'systemsmanagersap', 'timestream', 'transfer', 'verifiedpermissions', 'voiceid', 'vpclattice', 'waf', 'wafregional', 'wafv2', 'wetwire_aws', 'wisdom', 'workspaces', 'workspacesinstances', 'workspacesthinclient', 'workspacesweb', 'xray']
