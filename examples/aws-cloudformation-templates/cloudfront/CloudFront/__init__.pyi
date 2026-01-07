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

from .compute import LambdaEdgeFunction as LambdaEdgeFunction
from .compute import LambdaEdgeFunctionCode as LambdaEdgeFunctionCode
from .compute import LambdaEdgeVersion as LambdaEdgeVersion
from .main import EC2Instance as EC2Instance
from .main import EC2InstanceAssociationParameter as EC2InstanceAssociationParameter
from .main import EC2InstanceAssociationParameter1 as EC2InstanceAssociationParameter1
from .main import EC2InstanceBlockDeviceMapping as EC2InstanceBlockDeviceMapping
from .main import EC2InstanceEbs as EC2InstanceEbs
from .main import OriginALBHttpsListener as OriginALBHttpsListener
from .main import OriginALBHttpsListenerAction as OriginALBHttpsListenerAction
from .main import OriginALBHttpsListenerCertificate as OriginALBHttpsListenerCertificate
from .main import OriginALBHttpsListenerRule as OriginALBHttpsListenerRule
from .main import OriginALBHttpsListenerRuleAction as OriginALBHttpsListenerRuleAction
from .main import OriginALBHttpsListenerRuleRuleCondition as OriginALBHttpsListenerRuleRuleCondition
from .main import OriginALBTG as OriginALBTG
from .main import OriginALBTGTargetDescription as OriginALBTGTargetDescription
from .main import OriginALBTGTargetGroupAttribute as OriginALBTGTargetGroupAttribute
from .main import OriginALBTGTargetGroupAttribute1 as OriginALBTGTargetGroupAttribute1
from .main import OriginALBTGTargetGroupAttribute2 as OriginALBTGTargetGroupAttribute2
from .network import ALBExternalAccessSG as ALBExternalAccessSG
from .network import ALBExternalAccessSGAssociationParameter as ALBExternalAccessSGAssociationParameter
from .network import ALBExternalAccessSGAssociationParameter1 as ALBExternalAccessSGAssociationParameter1
from .network import CloudFrontDistribution as CloudFrontDistribution
from .network import CloudFrontDistributionCookies as CloudFrontDistributionCookies
from .network import CloudFrontDistributionCustomOriginConfig as CloudFrontDistributionCustomOriginConfig
from .network import CloudFrontDistributionDefaultCacheBehavior as CloudFrontDistributionDefaultCacheBehavior
from .network import CloudFrontDistributionDistributionConfig as CloudFrontDistributionDistributionConfig
from .network import CloudFrontDistributionForwardedValues as CloudFrontDistributionForwardedValues
from .network import CloudFrontDistributionLambdaFunctionAssociation as CloudFrontDistributionLambdaFunctionAssociation
from .network import CloudFrontDistributionLogging as CloudFrontDistributionLogging
from .network import CloudFrontDistributionOrigin as CloudFrontDistributionOrigin
from .network import CloudFrontDistributionViewerCertificate as CloudFrontDistributionViewerCertificate
from .network import EC2InstanceSG as EC2InstanceSG
from .network import EC2InstanceSGAssociationParameter as EC2InstanceSGAssociationParameter
from .network import EC2InstanceSGAssociationParameter1 as EC2InstanceSGAssociationParameter1
from .network import HTTPSTcpIn as HTTPSTcpIn
from .network import HTTPTcpIn as HTTPTcpIn
from .network import OriginALB as OriginALB
from .network import OriginALBTargetGroupAttribute as OriginALBTargetGroupAttribute
from .network import OriginALBTargetGroupAttribute1 as OriginALBTargetGroupAttribute1
from .network import OriginALBTargetGroupAttribute2 as OriginALBTargetGroupAttribute2
from .network import OriginALBTargetGroupAttribute3 as OriginALBTargetGroupAttribute3
from .network import OriginALBTargetGroupAttribute4 as OriginALBTargetGroupAttribute4
from .network import Tcp8080In as Tcp8080In
from .network import Tcp8080Out as Tcp8080Out
from .outputs import ALBExternalAccessSGIDOutput as ALBExternalAccessSGIDOutput
from .outputs import AdministratorAccessIAMRoleOutput as AdministratorAccessIAMRoleOutput
from .outputs import AlternateDomainNamesOutput as AlternateDomainNamesOutput
from .outputs import CloudFrontEndpointOutput as CloudFrontEndpointOutput
from .outputs import EC2InstanceDNSOutput as EC2InstanceDNSOutput
from .outputs import EC2InstanceIDOutput as EC2InstanceIDOutput
from .outputs import EC2InstanceIPOutput as EC2InstanceIPOutput
from .outputs import EC2InstanceSGIDOutput as EC2InstanceSGIDOutput
from .outputs import LambdaEdgeFunctionARNOutput as LambdaEdgeFunctionARNOutput
from .outputs import LambdaEdgeFunctionOutput as LambdaEdgeFunctionOutput
from .outputs import LambdaEdgeVersionOutput as LambdaEdgeVersionOutput
from .outputs import LoggingBucketKMSKeyOutput as LoggingBucketKMSKeyOutput
from .outputs import LoggingBucketOutput as LoggingBucketOutput
from .outputs import OriginALBOutput as OriginALBOutput
from .params import ACMCertificateIdentifier as ACMCertificateIdentifier
from .params import ALBAttributeDeletionProtection as ALBAttributeDeletionProtection
from .params import ALBAttributeIdleTimeOut as ALBAttributeIdleTimeOut
from .params import ALBAttributeRoutingHttp2 as ALBAttributeRoutingHttp2
from .params import ALBScheme as ALBScheme
from .params import ALBTargetGroupAttributeDeregistration as ALBTargetGroupAttributeDeregistration
from .params import ALBTargetGroupHealthCheckIntervalSeconds as ALBTargetGroupHealthCheckIntervalSeconds
from .params import ALBTargetGroupHealthCheckTimeoutSeconds as ALBTargetGroupHealthCheckTimeoutSeconds
from .params import ALBTargetGroupHealthyThresholdCount as ALBTargetGroupHealthyThresholdCount
from .params import ALBTargetGroupUnhealthyThresholdCount as ALBTargetGroupUnhealthyThresholdCount
from .params import ALBType as ALBType
from .params import AlternateDomainNames as AlternateDomainNames
from .params import AppName as AppName
from .params import BootVolSize as BootVolSize
from .params import BootVolType as BootVolType
from .params import Compress as Compress
from .params import DefaultTTL as DefaultTTL
from .params import EC2ImageId as EC2ImageId
from .params import EC2InstanceType as EC2InstanceType
from .params import Environment as Environment
from .params import ForwardCookies as ForwardCookies
from .params import HealthCheckPath as HealthCheckPath
from .params import HealthCheckProtocol as HealthCheckProtocol
from .params import IPV6Enabled as IPV6Enabled
from .params import KeyPairName as KeyPairName
from .params import LambdaEventType as LambdaEventType
from .params import LoggingBucketVersioning as LoggingBucketVersioning
from .params import MaxTTL as MaxTTL
from .params import MinTTL as MinTTL
from .params import MinimumProtocolVersion as MinimumProtocolVersion
from .params import OriginALBTGPort as OriginALBTGPort
from .params import OriginKeepaliveTimeout as OriginKeepaliveTimeout
from .params import OriginProtocolPolicy as OriginProtocolPolicy
from .params import OriginReadTimeout as OriginReadTimeout
from .params import PriceClass as PriceClass
from .params import PublicSubnetId1 as PublicSubnetId1
from .params import PublicSubnetId2 as PublicSubnetId2
from .params import QueryString as QueryString
from .params import SslSupportMethod as SslSupportMethod
from .params import ViewerProtocolPolicy as ViewerProtocolPolicy
from .params import VpcId as VpcId
from .security import AdministratorAccessIAMRole as AdministratorAccessIAMRole
from .security import AdministratorAccessIAMRoleAllowStatement0 as AdministratorAccessIAMRoleAllowStatement0
from .security import AdministratorAccessIAMRoleAssumeRolePolicyDocument as AdministratorAccessIAMRoleAssumeRolePolicyDocument
from .security import LambdaEdgeIAMRole as LambdaEdgeIAMRole
from .security import LambdaEdgeIAMRoleAllowStatement0 as LambdaEdgeIAMRoleAllowStatement0
from .security import LambdaEdgeIAMRoleAllowStatement0_1 as LambdaEdgeIAMRoleAllowStatement0_1
from .security import LambdaEdgeIAMRoleAssumeRolePolicyDocument as LambdaEdgeIAMRoleAssumeRolePolicyDocument
from .security import LambdaEdgeIAMRolePolicies0PolicyDocument as LambdaEdgeIAMRolePolicies0PolicyDocument
from .security import LambdaEdgeIAMRolePolicy as LambdaEdgeIAMRolePolicy
from .security import LoggingBucketKMSKey as LoggingBucketKMSKey
from .security import LoggingBucketKMSKeyAlias as LoggingBucketKMSKeyAlias
from .security import LoggingBucketKMSKeyAllowStatement0 as LoggingBucketKMSKeyAllowStatement0
from .security import LoggingBucketKMSKeyAllowStatement1 as LoggingBucketKMSKeyAllowStatement1
from .security import LoggingBucketKMSKeyKeyPolicy as LoggingBucketKMSKeyKeyPolicy
from .storage import LoggingBucket as LoggingBucket
from .storage import LoggingBucketBucketEncryption as LoggingBucketBucketEncryption
from .storage import LoggingBucketDeleteMarkerReplication as LoggingBucketDeleteMarkerReplication
from .storage import LoggingBucketOwnershipControls as LoggingBucketOwnershipControls
from .storage import LoggingBucketOwnershipControlsRule as LoggingBucketOwnershipControlsRule
from .storage import LoggingBucketPolicy as LoggingBucketPolicy
from .storage import LoggingBucketPolicyAllowStatement0 as LoggingBucketPolicyAllowStatement0
from .storage import LoggingBucketPolicyDenyStatement1 as LoggingBucketPolicyDenyStatement1
from .storage import LoggingBucketPolicyPolicyDocument as LoggingBucketPolicyPolicyDocument
from .storage import LoggingBucketPublicAccessBlockConfiguration as LoggingBucketPublicAccessBlockConfiguration
from .storage import LoggingBucketServerSideEncryptionByDefault as LoggingBucketServerSideEncryptionByDefault
from .storage import LoggingBucketServerSideEncryptionRule as LoggingBucketServerSideEncryptionRule

__all__: list[str] = ['ACMCertificateIdentifier', 'ALBAttributeDeletionProtection', 'ALBAttributeIdleTimeOut', 'ALBAttributeRoutingHttp2', 'ALBExternalAccessSG', 'ALBExternalAccessSGAssociationParameter', 'ALBExternalAccessSGAssociationParameter1', 'ALBExternalAccessSGIDOutput', 'ALBScheme', 'ALBTargetGroupAttributeDeregistration', 'ALBTargetGroupHealthCheckIntervalSeconds', 'ALBTargetGroupHealthCheckTimeoutSeconds', 'ALBTargetGroupHealthyThresholdCount', 'ALBTargetGroupUnhealthyThresholdCount', 'ALBType', 'AMI_ID', 'ARN', 'AVAILABILITY_ZONE', 'AWS_ACCOUNT_ID', 'AWS_NOTIFICATION_ARNS', 'AWS_NO_VALUE', 'AWS_PARTITION', 'AWS_REGION', 'AWS_STACK_ID', 'AWS_STACK_NAME', 'AWS_URL_SUFFIX', 'AdministratorAccessIAMRole', 'AdministratorAccessIAMRoleAllowStatement0', 'AdministratorAccessIAMRoleAssumeRolePolicyDocument', 'AdministratorAccessIAMRoleOutput', 'AlternateDomainNames', 'AlternateDomainNamesOutput', 'And', 'AppName', 'Base64', 'BootVolSize', 'BootVolType', 'COMMA_DELIMITED_LIST', 'Cidr', 'CloudFormationResource', 'CloudFormationTemplate', 'CloudFrontDistribution', 'CloudFrontDistributionCookies', 'CloudFrontDistributionCustomOriginConfig', 'CloudFrontDistributionDefaultCacheBehavior', 'CloudFrontDistributionDistributionConfig', 'CloudFrontDistributionForwardedValues', 'CloudFrontDistributionLambdaFunctionAssociation', 'CloudFrontDistributionLogging', 'CloudFrontDistributionOrigin', 'CloudFrontDistributionViewerCertificate', 'CloudFrontEndpointOutput', 'Compress', 'Condition', 'DefaultTTL', 'DenyStatement', 'EC2ImageId', 'EC2Instance', 'EC2InstanceAssociationParameter', 'EC2InstanceAssociationParameter1', 'EC2InstanceBlockDeviceMapping', 'EC2InstanceDNSOutput', 'EC2InstanceEbs', 'EC2InstanceIDOutput', 'EC2InstanceIPOutput', 'EC2InstanceSG', 'EC2InstanceSGAssociationParameter', 'EC2InstanceSGAssociationParameter1', 'EC2InstanceSGIDOutput', 'EC2InstanceType', 'Environment', 'Equals', 'FindInMap', 'ForwardCookies', 'GetAZs', 'GetAtt', 'HOSTED_ZONE_ID', 'HTTPSTcpIn', 'HTTPTcpIn', 'HealthCheckPath', 'HealthCheckProtocol', 'INSTANCE_ID', 'IPV6Enabled', 'If', 'ImportValue', 'Join', 'KEY_PAIR', 'KeyPairName', 'LIST_AVAILABILITY_ZONE', 'LIST_NUMBER', 'LIST_SECURITY_GROUP_ID', 'LIST_SUBNET_ID', 'LambdaEdgeFunction', 'LambdaEdgeFunctionARNOutput', 'LambdaEdgeFunctionCode', 'LambdaEdgeFunctionOutput', 'LambdaEdgeIAMRole', 'LambdaEdgeIAMRoleAllowStatement0', 'LambdaEdgeIAMRoleAllowStatement0_1', 'LambdaEdgeIAMRoleAssumeRolePolicyDocument', 'LambdaEdgeIAMRolePolicies0PolicyDocument', 'LambdaEdgeIAMRolePolicy', 'LambdaEdgeVersion', 'LambdaEdgeVersionOutput', 'LambdaEventType', 'LoggingBucket', 'LoggingBucketBucketEncryption', 'LoggingBucketDeleteMarkerReplication', 'LoggingBucketKMSKey', 'LoggingBucketKMSKeyAlias', 'LoggingBucketKMSKeyAllowStatement0', 'LoggingBucketKMSKeyAllowStatement1', 'LoggingBucketKMSKeyKeyPolicy', 'LoggingBucketKMSKeyOutput', 'LoggingBucketOutput', 'LoggingBucketOwnershipControls', 'LoggingBucketOwnershipControlsRule', 'LoggingBucketPolicy', 'LoggingBucketPolicyAllowStatement0', 'LoggingBucketPolicyDenyStatement1', 'LoggingBucketPolicyPolicyDocument', 'LoggingBucketPublicAccessBlockConfiguration', 'LoggingBucketServerSideEncryptionByDefault', 'LoggingBucketServerSideEncryptionRule', 'LoggingBucketVersioning', 'Mapping', 'MaxTTL', 'MinTTL', 'MinimumProtocolVersion', 'NUMBER', 'Not', 'Or', 'OriginALB', 'OriginALBHttpsListener', 'OriginALBHttpsListenerAction', 'OriginALBHttpsListenerCertificate', 'OriginALBHttpsListenerRule', 'OriginALBHttpsListenerRuleAction', 'OriginALBHttpsListenerRuleRuleCondition', 'OriginALBOutput', 'OriginALBTG', 'OriginALBTGPort', 'OriginALBTGTargetDescription', 'OriginALBTGTargetGroupAttribute', 'OriginALBTGTargetGroupAttribute1', 'OriginALBTGTargetGroupAttribute2', 'OriginALBTargetGroupAttribute', 'OriginALBTargetGroupAttribute1', 'OriginALBTargetGroupAttribute2', 'OriginALBTargetGroupAttribute3', 'OriginALBTargetGroupAttribute4', 'OriginKeepaliveTimeout', 'OriginProtocolPolicy', 'OriginReadTimeout', 'Output', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'PriceClass', 'PropertyType', 'PublicSubnetId1', 'PublicSubnetId2', 'QueryString', 'Ref', 'RefDict', 'RefList', 'SECURITY_GROUP_ID', 'SSM_PARAMETER_STRING', 'SSM_PARAMETER_STRING_LIST', 'STRING', 'SUBNET_ID', 'Select', 'Split', 'SslSupportMethod', 'Sub', 'Tcp8080In', 'Tcp8080Out', 'TemplateCondition', 'Transform', 'VOLUME_ID', 'VPC_ID', 'ViewerProtocolPolicy', 'VpcId', 'accessanalyzer', 'acmpca', 'aiops', 'amazonmq', 'amplify', 'amplifyuibuilder', 'apigateway', 'apigatewayv2', 'appconfig', 'appflow', 'appintegrations', 'applicationautoscaling', 'applicationinsights', 'applicationsignals', 'appmesh', 'apprunner', 'appstream', 'appsync', 'apptest', 'aps', 'arcregionswitch', 'arczonalshift', 'ask', 'athena', 'auditmanager', 'autoscaling', 'autoscalingplans', 'b2bi', 'backup', 'backupgateway', 'batch', 'bcmdataexports', 'bedrock', 'bedrockagentcore', 'billing', 'billingconductor', 'budgets', 'cases', 'cassandra', 'ce', 'certificatemanager', 'chatbot', 'cleanrooms', 'cleanroomsml', 'cloud9', 'cloudformation', 'cloudfront', 'cloudtrail', 'cloudwatch', 'codeartifact', 'codebuild', 'codecommit', 'codeconnections', 'codedeploy', 'codeguruprofiler', 'codegurureviewer', 'codepipeline', 'codestar', 'codestarconnections', 'codestarnotifications', 'cognito', 'comprehend', 'config', 'connect', 'connectcampaigns', 'connectcampaignsv2', 'controltower', 'cur', 'customerprofiles', 'databrew', 'datapipeline', 'datasync', 'datazone', 'dax', 'deadline', 'detective', 'devopsagent', 'devopsguru', 'directoryservice', 'dlm', 'dms', 'docdb', 'docdbelastic', 'dsql', 'dynamodb', 'ec2', 'ecr', 'ecs', 'efs', 'eks', 'elasticache', 'elasticbeanstalk', 'elasticloadbalancing', 'elasticloadbalancingv2', 'elasticsearch', 'emr', 'emrcontainers', 'emrserverless', 'entityresolution', 'events', 'eventschemas', 'evidently', 'evs', 'finspace', 'fis', 'fms', 'forecast', 'frauddetector', 'fsx', 'gamelift', 'get_att', 'globalaccelerator', 'glue', 'grafana', 'greengrass', 'greengrassv2', 'groundstation', 'guardduty', 'healthimaging', 'healthlake', 'iam', 'identitystore', 'imagebuilder', 'inspector', 'inspectorv2', 'internetmonitor', 'invoicing', 'iot', 'iotanalytics', 'iotcoredeviceadvisor', 'iotevents', 'iotfleetwise', 'iotsitewise', 'iotthingsgraph', 'iottwinmaker', 'iotwireless', 'ivs', 'ivschat', 'kafkaconnect', 'kendra', 'kendraranking', 'kinesis', 'kinesisanalytics', 'kinesisanalyticsv2', 'kinesisfirehose', 'kinesisvideo', 'kms', 'lakeformation', 'lambda_', 'launchwizard', 'lex', 'licensemanager', 'lightsail', 'location', 'logs', 'lookoutequipment', 'lookoutvision', 'm2', 'macie', 'managedblockchain', 'mediaconnect', 'mediaconvert', 'medialive', 'mediapackage', 'mediapackagev2', 'mediastore', 'mediatailor', 'memorydb', 'mpa', 'msk', 'mwaa', 'neptune', 'neptunegraph', 'networkfirewall', 'networkmanager', 'notifications', 'notificationscontacts', 'oam', 'observabilityadmin', 'odb', 'omics', 'opensearchserverless', 'opensearchservice', 'opsworks', 'organizations', 'osis', 'panorama', 'paymentcryptography', 'pcaconnectorad', 'pcaconnectorscep', 'pcs', 'personalize', 'pinpoint', 'pinpointemail', 'pipes', 'proton', 'qbusiness', 'qldb', 'quicksight', 'ram', 'rbin', 'rds', 'redshift', 'redshiftserverless', 'ref', 'refactorspaces', 'rekognition', 'resiliencehub', 'resourceexplorer2', 'resourcegroups', 'robomaker', 'rolesanywhere', 'route53', 'route53profiles', 'route53recoverycontrol', 'route53recoveryreadiness', 'route53resolver', 'rtbfabric', 'rum', 's3', 's3express', 's3objectlambda', 's3outposts', 's3tables', 's3vectors', 'sagemaker', 'scheduler', 'sdb', 'secretsmanager', 'securityhub', 'securitylake', 'servicecatalog', 'servicecatalogappregistry', 'servicediscovery', 'ses', 'setup_params', 'setup_resources', 'shield', 'signer', 'simspaceweaver', 'smsvoice', 'sns', 'sqs', 'ssm', 'ssmcontacts', 'ssmguiconnect', 'ssmincidents', 'ssmquicksetup', 'sso', 'stepfunctions', 'supportapp', 'synthetics', 'systemsmanagersap', 'timestream', 'transfer', 'verifiedpermissions', 'voiceid', 'vpclattice', 'waf', 'wafregional', 'wafv2', 'wetwire_aws', 'wisdom', 'workspaces', 'workspacesinstances', 'workspacesthinclient', 'workspacesweb', 'xray']
