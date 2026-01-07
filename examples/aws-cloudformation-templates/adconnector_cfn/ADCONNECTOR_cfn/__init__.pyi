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

from .compute import ADConnectorLambdaFunction as ADConnectorLambdaFunction
from .compute import ADConnectorLambdaFunctionCapacityProviderVpcConfig as ADConnectorLambdaFunctionCapacityProviderVpcConfig
from .compute import ADConnectorLambdaFunctionContent as ADConnectorLambdaFunctionContent
from .compute import ADConnectorLambdaFunctionEnvironment as ADConnectorLambdaFunctionEnvironment
from .main import ADConnectorResource as ADConnectorResource
from .monitoring import ADConnectorLambdaLogsLogGroup as ADConnectorLambdaLogsLogGroup
from .network import ADConnectorDomainMembersSG as ADConnectorDomainMembersSG
from .network import ADConnectorDomainMembersSGAssociationParameter as ADConnectorDomainMembersSGAssociationParameter
from .network import ADConnectorDomainMembersSGEgress as ADConnectorDomainMembersSGEgress
from .network import ADConnectorDomainMembersSGEgress1 as ADConnectorDomainMembersSGEgress1
from .network import ADConnectorDomainMembersSGEgress2 as ADConnectorDomainMembersSGEgress2
from .network import ADConnectorDomainMembersSGEgress3 as ADConnectorDomainMembersSGEgress3
from .network import DHCPOptions as DHCPOptions
from .network import DHCPOptionsAssociationParameter as DHCPOptionsAssociationParameter
from .network import DHCPOptionsVPCAssociation as DHCPOptionsVPCAssociation
from .outputs import ADConnectorADConnectorDomainMembersSGOutput as ADConnectorADConnectorDomainMembersSGOutput
from .outputs import ADConnectorDirectoryIdOutput as ADConnectorDirectoryIdOutput
from .outputs import ADConnectorDirectoryNameOutput as ADConnectorDirectoryNameOutput
from .outputs import ADConnectorLinuxEC2SeamlessDomainJoinInstanceProfileOutput as ADConnectorLinuxEC2SeamlessDomainJoinInstanceProfileOutput
from .outputs import ADConnectorLinuxEC2SeamlessDomainJoinRoleOutput as ADConnectorLinuxEC2SeamlessDomainJoinRoleOutput
from .outputs import ADConnectorWindowsEC2SeamlessDomainJoinInstanceProfileOutput as ADConnectorWindowsEC2SeamlessDomainJoinInstanceProfileOutput
from .outputs import ADConnectorWindowsEC2SeamlessDomainJoinRoleOutput as ADConnectorWindowsEC2SeamlessDomainJoinRoleOutput
from .params import ADConnectorDescription as ADConnectorDescription
from .params import ADConnectorSize as ADConnectorSize
from .params import CreateADConnectorDomainMembersSG as CreateADConnectorDomainMembersSG
from .params import CreateDHCPOptionSet as CreateDHCPOptionSet
from .params import CreateLinuxEC2DomainJoinResources as CreateLinuxEC2DomainJoinResources
from .params import CreateWindowsEC2DomainJoinResources as CreateWindowsEC2DomainJoinResources
from .params import DHCPOptionSetConditionCondition as DHCPOptionSetConditionCondition
from .params import DomainDNSName as DomainDNSName
from .params import DomainDNSServers as DomainDNSServers
from .params import DomainJoinUser as DomainJoinUser
from .params import DomainJoinUserPassword as DomainJoinUserPassword
from .params import DomainMembersSGConditionCondition as DomainMembersSGConditionCondition
from .params import DomainNetBiosName as DomainNetBiosName
from .params import LambdaFunctionName as LambdaFunctionName
from .params import LambdaLogLevel as LambdaLogLevel
from .params import LambdaLogsCloudWatchKMSKey as LambdaLogsCloudWatchKMSKey
from .params import LambdaLogsCloudWatchKMSKeyConditionCondition as LambdaLogsCloudWatchKMSKeyConditionCondition
from .params import LambdaLogsLogGroupRetention as LambdaLogsLogGroupRetention
from .params import LambdaS3BucketName as LambdaS3BucketName
from .params import LambdaZipFileName as LambdaZipFileName
from .params import LinuxEC2DomainJoinResourcesConditionCondition as LinuxEC2DomainJoinResourcesConditionCondition
from .params import PrivateSubnet1ID as PrivateSubnet1ID
from .params import PrivateSubnet2ID as PrivateSubnet2ID
from .params import SSMLogsBucketName as SSMLogsBucketName
from .params import SSMLogsBucketNameConditionCondition as SSMLogsBucketNameConditionCondition
from .params import SecretsManagerDomainCredentialsSecretsKMSKey as SecretsManagerDomainCredentialsSecretsKMSKey
from .params import SecretsManagerDomainCredentialsSecretsKMSKeyConditionCondition as SecretsManagerDomainCredentialsSecretsKMSKeyConditionCondition
from .params import VPCID as VPCID
from .params import WindowsEC2DomainJoinResourcesConditionCondition as WindowsEC2DomainJoinResourcesConditionCondition
from .security import ADConnectorLambdaRole as ADConnectorLambdaRole
from .security import ADConnectorLambdaRoleAllowStatement0 as ADConnectorLambdaRoleAllowStatement0
from .security import ADConnectorLambdaRoleAllowStatement0_1 as ADConnectorLambdaRoleAllowStatement0_1
from .security import ADConnectorLambdaRoleAllowStatement0_2 as ADConnectorLambdaRoleAllowStatement0_2
from .security import ADConnectorLambdaRoleAllowStatement0_3 as ADConnectorLambdaRoleAllowStatement0_3
from .security import ADConnectorLambdaRoleAllowStatement1 as ADConnectorLambdaRoleAllowStatement1
from .security import ADConnectorLambdaRoleAllowStatement1_1 as ADConnectorLambdaRoleAllowStatement1_1
from .security import ADConnectorLambdaRoleAllowStatement2 as ADConnectorLambdaRoleAllowStatement2
from .security import ADConnectorLambdaRoleAssumeRolePolicyDocument as ADConnectorLambdaRoleAssumeRolePolicyDocument
from .security import ADConnectorLambdaRolePolicies0PolicyDocument as ADConnectorLambdaRolePolicies0PolicyDocument
from .security import ADConnectorLambdaRolePolicies1PolicyDocument as ADConnectorLambdaRolePolicies1PolicyDocument
from .security import ADConnectorLambdaRolePolicies2PolicyDocument as ADConnectorLambdaRolePolicies2PolicyDocument
from .security import ADConnectorLambdaRolePolicy as ADConnectorLambdaRolePolicy
from .security import ADConnectorLambdaRolePolicy1 as ADConnectorLambdaRolePolicy1
from .security import ADConnectorLambdaRolePolicy2 as ADConnectorLambdaRolePolicy2
from .security import ADConnectorLinuxEC2DomainJoinInstanceProfile as ADConnectorLinuxEC2DomainJoinInstanceProfile
from .security import ADConnectorLinuxEC2DomainJoinRole as ADConnectorLinuxEC2DomainJoinRole
from .security import ADConnectorLinuxEC2DomainJoinRoleAllowStatement0 as ADConnectorLinuxEC2DomainJoinRoleAllowStatement0
from .security import ADConnectorLinuxEC2DomainJoinRoleAllowStatement0_1 as ADConnectorLinuxEC2DomainJoinRoleAllowStatement0_1
from .security import ADConnectorLinuxEC2DomainJoinRoleAllowStatement0_2 as ADConnectorLinuxEC2DomainJoinRoleAllowStatement0_2
from .security import ADConnectorLinuxEC2DomainJoinRoleAssumeRolePolicyDocument as ADConnectorLinuxEC2DomainJoinRoleAssumeRolePolicyDocument
from .security import ADConnectorLinuxEC2DomainJoinRolePolicies0PolicyDocument as ADConnectorLinuxEC2DomainJoinRolePolicies0PolicyDocument
from .security import ADConnectorLinuxEC2DomainJoinRolePolicies2PolicyDocument as ADConnectorLinuxEC2DomainJoinRolePolicies2PolicyDocument
from .security import ADConnectorLinuxEC2DomainJoinRolePolicy as ADConnectorLinuxEC2DomainJoinRolePolicy
from .security import ADConnectorLinuxEC2DomainJoinRolePolicy1 as ADConnectorLinuxEC2DomainJoinRolePolicy1
from .security import ADConnectorLinuxEC2SeamlessDomainJoinSecret as ADConnectorLinuxEC2SeamlessDomainJoinSecret
from .security import ADConnectorServiceAccountSecret as ADConnectorServiceAccountSecret
from .security import ADConnectorWindowsEC2DomainJoinInstanceProfile as ADConnectorWindowsEC2DomainJoinInstanceProfile
from .security import ADConnectorWindowsEC2DomainJoinRole as ADConnectorWindowsEC2DomainJoinRole
from .security import ADConnectorWindowsEC2DomainJoinRoleAllowStatement0 as ADConnectorWindowsEC2DomainJoinRoleAllowStatement0
from .security import ADConnectorWindowsEC2DomainJoinRoleAllowStatement0_1 as ADConnectorWindowsEC2DomainJoinRoleAllowStatement0_1
from .security import ADConnectorWindowsEC2DomainJoinRoleAssumeRolePolicyDocument as ADConnectorWindowsEC2DomainJoinRoleAssumeRolePolicyDocument
from .security import ADConnectorWindowsEC2DomainJoinRolePolicies0PolicyDocument as ADConnectorWindowsEC2DomainJoinRolePolicies0PolicyDocument
from .security import ADConnectorWindowsEC2DomainJoinRolePolicy as ADConnectorWindowsEC2DomainJoinRolePolicy

__all__: list[str] = ['ADConnectorADConnectorDomainMembersSGOutput', 'ADConnectorDescription', 'ADConnectorDirectoryIdOutput', 'ADConnectorDirectoryNameOutput', 'ADConnectorDomainMembersSG', 'ADConnectorDomainMembersSGAssociationParameter', 'ADConnectorDomainMembersSGEgress', 'ADConnectorDomainMembersSGEgress1', 'ADConnectorDomainMembersSGEgress2', 'ADConnectorDomainMembersSGEgress3', 'ADConnectorLambdaFunction', 'ADConnectorLambdaFunctionCapacityProviderVpcConfig', 'ADConnectorLambdaFunctionContent', 'ADConnectorLambdaFunctionEnvironment', 'ADConnectorLambdaLogsLogGroup', 'ADConnectorLambdaRole', 'ADConnectorLambdaRoleAllowStatement0', 'ADConnectorLambdaRoleAllowStatement0_1', 'ADConnectorLambdaRoleAllowStatement0_2', 'ADConnectorLambdaRoleAllowStatement0_3', 'ADConnectorLambdaRoleAllowStatement1', 'ADConnectorLambdaRoleAllowStatement1_1', 'ADConnectorLambdaRoleAllowStatement2', 'ADConnectorLambdaRoleAssumeRolePolicyDocument', 'ADConnectorLambdaRolePolicies0PolicyDocument', 'ADConnectorLambdaRolePolicies1PolicyDocument', 'ADConnectorLambdaRolePolicies2PolicyDocument', 'ADConnectorLambdaRolePolicy', 'ADConnectorLambdaRolePolicy1', 'ADConnectorLambdaRolePolicy2', 'ADConnectorLinuxEC2DomainJoinInstanceProfile', 'ADConnectorLinuxEC2DomainJoinRole', 'ADConnectorLinuxEC2DomainJoinRoleAllowStatement0', 'ADConnectorLinuxEC2DomainJoinRoleAllowStatement0_1', 'ADConnectorLinuxEC2DomainJoinRoleAllowStatement0_2', 'ADConnectorLinuxEC2DomainJoinRoleAssumeRolePolicyDocument', 'ADConnectorLinuxEC2DomainJoinRolePolicies0PolicyDocument', 'ADConnectorLinuxEC2DomainJoinRolePolicies2PolicyDocument', 'ADConnectorLinuxEC2DomainJoinRolePolicy', 'ADConnectorLinuxEC2DomainJoinRolePolicy1', 'ADConnectorLinuxEC2SeamlessDomainJoinInstanceProfileOutput', 'ADConnectorLinuxEC2SeamlessDomainJoinRoleOutput', 'ADConnectorLinuxEC2SeamlessDomainJoinSecret', 'ADConnectorResource', 'ADConnectorServiceAccountSecret', 'ADConnectorSize', 'ADConnectorWindowsEC2DomainJoinInstanceProfile', 'ADConnectorWindowsEC2DomainJoinRole', 'ADConnectorWindowsEC2DomainJoinRoleAllowStatement0', 'ADConnectorWindowsEC2DomainJoinRoleAllowStatement0_1', 'ADConnectorWindowsEC2DomainJoinRoleAssumeRolePolicyDocument', 'ADConnectorWindowsEC2DomainJoinRolePolicies0PolicyDocument', 'ADConnectorWindowsEC2DomainJoinRolePolicy', 'ADConnectorWindowsEC2SeamlessDomainJoinInstanceProfileOutput', 'ADConnectorWindowsEC2SeamlessDomainJoinRoleOutput', 'AMI_ID', 'ARN', 'AVAILABILITY_ZONE', 'AWS_ACCOUNT_ID', 'AWS_NOTIFICATION_ARNS', 'AWS_NO_VALUE', 'AWS_PARTITION', 'AWS_REGION', 'AWS_STACK_ID', 'AWS_STACK_NAME', 'AWS_URL_SUFFIX', 'And', 'Base64', 'COMMA_DELIMITED_LIST', 'Cidr', 'CloudFormationResource', 'CloudFormationTemplate', 'Condition', 'CreateADConnectorDomainMembersSG', 'CreateDHCPOptionSet', 'CreateLinuxEC2DomainJoinResources', 'CreateWindowsEC2DomainJoinResources', 'DHCPOptionSetConditionCondition', 'DHCPOptions', 'DHCPOptionsAssociationParameter', 'DHCPOptionsVPCAssociation', 'DenyStatement', 'DomainDNSName', 'DomainDNSServers', 'DomainJoinUser', 'DomainJoinUserPassword', 'DomainMembersSGConditionCondition', 'DomainNetBiosName', 'Equals', 'FindInMap', 'GetAZs', 'GetAtt', 'HOSTED_ZONE_ID', 'INSTANCE_ID', 'If', 'ImportValue', 'Join', 'KEY_PAIR', 'LIST_AVAILABILITY_ZONE', 'LIST_NUMBER', 'LIST_SECURITY_GROUP_ID', 'LIST_SUBNET_ID', 'LambdaFunctionName', 'LambdaLogLevel', 'LambdaLogsCloudWatchKMSKey', 'LambdaLogsCloudWatchKMSKeyConditionCondition', 'LambdaLogsLogGroupRetention', 'LambdaS3BucketName', 'LambdaZipFileName', 'LinuxEC2DomainJoinResourcesConditionCondition', 'Mapping', 'NUMBER', 'Not', 'Or', 'Output', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'PrivateSubnet1ID', 'PrivateSubnet2ID', 'PropertyType', 'Ref', 'RefDict', 'RefList', 'SECURITY_GROUP_ID', 'SSMLogsBucketName', 'SSMLogsBucketNameConditionCondition', 'SSM_PARAMETER_STRING', 'SSM_PARAMETER_STRING_LIST', 'STRING', 'SUBNET_ID', 'SecretsManagerDomainCredentialsSecretsKMSKey', 'SecretsManagerDomainCredentialsSecretsKMSKeyConditionCondition', 'Select', 'Split', 'Sub', 'TemplateCondition', 'Transform', 'VOLUME_ID', 'VPCID', 'VPC_ID', 'WindowsEC2DomainJoinResourcesConditionCondition', 'accessanalyzer', 'acmpca', 'aiops', 'amazonmq', 'amplify', 'amplifyuibuilder', 'apigateway', 'apigatewayv2', 'appconfig', 'appflow', 'appintegrations', 'applicationautoscaling', 'applicationinsights', 'applicationsignals', 'appmesh', 'apprunner', 'appstream', 'appsync', 'apptest', 'aps', 'arcregionswitch', 'arczonalshift', 'ask', 'athena', 'auditmanager', 'autoscaling', 'autoscalingplans', 'b2bi', 'backup', 'backupgateway', 'batch', 'bcmdataexports', 'bedrock', 'bedrockagentcore', 'billing', 'billingconductor', 'budgets', 'cases', 'cassandra', 'ce', 'certificatemanager', 'chatbot', 'cleanrooms', 'cleanroomsml', 'cloud9', 'cloudformation', 'cloudfront', 'cloudtrail', 'cloudwatch', 'codeartifact', 'codebuild', 'codecommit', 'codeconnections', 'codedeploy', 'codeguruprofiler', 'codegurureviewer', 'codepipeline', 'codestar', 'codestarconnections', 'codestarnotifications', 'cognito', 'comprehend', 'config', 'connect', 'connectcampaigns', 'connectcampaignsv2', 'controltower', 'cur', 'customerprofiles', 'databrew', 'datapipeline', 'datasync', 'datazone', 'dax', 'deadline', 'detective', 'devopsagent', 'devopsguru', 'directoryservice', 'dlm', 'dms', 'docdb', 'docdbelastic', 'dsql', 'dynamodb', 'ec2', 'ecr', 'ecs', 'efs', 'eks', 'elasticache', 'elasticbeanstalk', 'elasticloadbalancing', 'elasticloadbalancingv2', 'elasticsearch', 'emr', 'emrcontainers', 'emrserverless', 'entityresolution', 'events', 'eventschemas', 'evidently', 'evs', 'finspace', 'fis', 'fms', 'forecast', 'frauddetector', 'fsx', 'gamelift', 'get_att', 'globalaccelerator', 'glue', 'grafana', 'greengrass', 'greengrassv2', 'groundstation', 'guardduty', 'healthimaging', 'healthlake', 'iam', 'identitystore', 'imagebuilder', 'inspector', 'inspectorv2', 'internetmonitor', 'invoicing', 'iot', 'iotanalytics', 'iotcoredeviceadvisor', 'iotevents', 'iotfleetwise', 'iotsitewise', 'iotthingsgraph', 'iottwinmaker', 'iotwireless', 'ivs', 'ivschat', 'kafkaconnect', 'kendra', 'kendraranking', 'kinesis', 'kinesisanalytics', 'kinesisanalyticsv2', 'kinesisfirehose', 'kinesisvideo', 'kms', 'lakeformation', 'lambda_', 'launchwizard', 'lex', 'licensemanager', 'lightsail', 'location', 'logs', 'lookoutequipment', 'lookoutvision', 'm2', 'macie', 'managedblockchain', 'mediaconnect', 'mediaconvert', 'medialive', 'mediapackage', 'mediapackagev2', 'mediastore', 'mediatailor', 'memorydb', 'mpa', 'msk', 'mwaa', 'neptune', 'neptunegraph', 'networkfirewall', 'networkmanager', 'notifications', 'notificationscontacts', 'oam', 'observabilityadmin', 'odb', 'omics', 'opensearchserverless', 'opensearchservice', 'opsworks', 'organizations', 'osis', 'panorama', 'paymentcryptography', 'pcaconnectorad', 'pcaconnectorscep', 'pcs', 'personalize', 'pinpoint', 'pinpointemail', 'pipes', 'proton', 'qbusiness', 'qldb', 'quicksight', 'ram', 'rbin', 'rds', 'redshift', 'redshiftserverless', 'ref', 'refactorspaces', 'rekognition', 'resiliencehub', 'resourceexplorer2', 'resourcegroups', 'robomaker', 'rolesanywhere', 'route53', 'route53profiles', 'route53recoverycontrol', 'route53recoveryreadiness', 'route53resolver', 'rtbfabric', 'rum', 's3', 's3express', 's3objectlambda', 's3outposts', 's3tables', 's3vectors', 'sagemaker', 'scheduler', 'sdb', 'secretsmanager', 'securityhub', 'securitylake', 'serverless', 'servicecatalog', 'servicecatalogappregistry', 'servicediscovery', 'ses', 'setup_params', 'setup_resources', 'shield', 'signer', 'simspaceweaver', 'smsvoice', 'sns', 'sqs', 'ssm', 'ssmcontacts', 'ssmguiconnect', 'ssmincidents', 'ssmquicksetup', 'sso', 'stepfunctions', 'supportapp', 'synthetics', 'systemsmanagersap', 'timestream', 'transfer', 'verifiedpermissions', 'voiceid', 'vpclattice', 'waf', 'wafregional', 'wafv2', 'wetwire_aws', 'wisdom', 'workspaces', 'workspacesinstances', 'workspacesthinclient', 'workspacesweb', 'xray']
