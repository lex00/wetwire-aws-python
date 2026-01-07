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

from .compute import Server as Server
from .compute import ServerAssociationParameter as ServerAssociationParameter
from .compute import ServerBlockDeviceMapping as ServerBlockDeviceMapping
from .compute import ServerEbs as ServerEbs
from .main import CloudFrontDistribution as CloudFrontDistribution
from .main import CloudFrontDistributionCacheBehavior as CloudFrontDistributionCacheBehavior
from .main import CloudFrontDistributionCustomOriginConfig as CloudFrontDistributionCustomOriginConfig
from .main import CloudFrontDistributionDefaultCacheBehavior as CloudFrontDistributionDefaultCacheBehavior
from .main import CloudFrontDistributionDistributionConfig as CloudFrontDistributionDistributionConfig
from .main import CloudFrontDistributionOrigin as CloudFrontDistributionOrigin
from .network import CloudFrontCachePolicy as CloudFrontCachePolicy
from .network import CloudFrontCachePolicyCachePolicyConfig as CloudFrontCachePolicyCachePolicyConfig
from .network import CloudFrontCachePolicyCookiesConfig as CloudFrontCachePolicyCookiesConfig
from .network import CloudFrontCachePolicyHeadersConfig as CloudFrontCachePolicyHeadersConfig
from .network import CloudFrontCachePolicyParametersInCacheKeyAndForwardedToOrigin as CloudFrontCachePolicyParametersInCacheKeyAndForwardedToOrigin
from .network import CloudFrontCachePolicyQueryStringsConfig as CloudFrontCachePolicyQueryStringsConfig
from .network import InstanceSecurityGroup as InstanceSecurityGroup
from .network import InstanceSecurityGroupAssociationParameter as InstanceSecurityGroupAssociationParameter
from .network import InstanceSecurityGroupEgress as InstanceSecurityGroupEgress
from .network import InstanceSecurityGroupIngress as InstanceSecurityGroupIngress
from .network import NetworkInternetGateway as NetworkInternetGateway
from .network import NetworkInternetGatewayAssociationParameter as NetworkInternetGatewayAssociationParameter
from .network import NetworkPrivateSubnet1DefaultRoute as NetworkPrivateSubnet1DefaultRoute
from .network import NetworkPrivateSubnet1RouteTable as NetworkPrivateSubnet1RouteTable
from .network import NetworkPrivateSubnet1RouteTableAssociation as NetworkPrivateSubnet1RouteTableAssociation
from .network import NetworkPrivateSubnet1RouteTableAssociationParameter as NetworkPrivateSubnet1RouteTableAssociationParameter
from .network import NetworkPrivateSubnet1Subnet as NetworkPrivateSubnet1Subnet
from .network import NetworkPrivateSubnet1SubnetAssociationParameter as NetworkPrivateSubnet1SubnetAssociationParameter
from .network import NetworkPrivateSubnet2DefaultRoute as NetworkPrivateSubnet2DefaultRoute
from .network import NetworkPrivateSubnet2RouteTable as NetworkPrivateSubnet2RouteTable
from .network import NetworkPrivateSubnet2RouteTableAssociation as NetworkPrivateSubnet2RouteTableAssociation
from .network import NetworkPrivateSubnet2RouteTableAssociationParameter as NetworkPrivateSubnet2RouteTableAssociationParameter
from .network import NetworkPrivateSubnet2Subnet as NetworkPrivateSubnet2Subnet
from .network import NetworkPrivateSubnet2SubnetAssociationParameter as NetworkPrivateSubnet2SubnetAssociationParameter
from .network import NetworkPublicSubnet1 as NetworkPublicSubnet1
from .network import NetworkPublicSubnet1AssociationParameter as NetworkPublicSubnet1AssociationParameter
from .network import NetworkPublicSubnet1DefaultRoute as NetworkPublicSubnet1DefaultRoute
from .network import NetworkPublicSubnet1EIP as NetworkPublicSubnet1EIP
from .network import NetworkPublicSubnet1EIPAssociationParameter as NetworkPublicSubnet1EIPAssociationParameter
from .network import NetworkPublicSubnet1NATGateway as NetworkPublicSubnet1NATGateway
from .network import NetworkPublicSubnet1NATGatewayAssociationParameter as NetworkPublicSubnet1NATGatewayAssociationParameter
from .network import NetworkPublicSubnet1RouteTable as NetworkPublicSubnet1RouteTable
from .network import NetworkPublicSubnet1RouteTableAssociation as NetworkPublicSubnet1RouteTableAssociation
from .network import NetworkPublicSubnet1RouteTableAssociationParameter as NetworkPublicSubnet1RouteTableAssociationParameter
from .network import NetworkPublicSubnet2 as NetworkPublicSubnet2
from .network import NetworkPublicSubnet2AssociationParameter as NetworkPublicSubnet2AssociationParameter
from .network import NetworkPublicSubnet2DefaultRoute as NetworkPublicSubnet2DefaultRoute
from .network import NetworkPublicSubnet2EIP as NetworkPublicSubnet2EIP
from .network import NetworkPublicSubnet2EIPAssociationParameter as NetworkPublicSubnet2EIPAssociationParameter
from .network import NetworkPublicSubnet2NATGateway as NetworkPublicSubnet2NATGateway
from .network import NetworkPublicSubnet2NATGatewayAssociationParameter as NetworkPublicSubnet2NATGatewayAssociationParameter
from .network import NetworkPublicSubnet2RouteTable as NetworkPublicSubnet2RouteTable
from .network import NetworkPublicSubnet2RouteTableAssociation as NetworkPublicSubnet2RouteTableAssociation
from .network import NetworkPublicSubnet2RouteTableAssociationParameter as NetworkPublicSubnet2RouteTableAssociationParameter
from .network import NetworkVPC as NetworkVPC
from .network import NetworkVPCAssociationParameter as NetworkVPCAssociationParameter
from .network import NetworkVPCGW as NetworkVPCGW
from .outputs import URLOutput as URLOutput
from .params import InstanceType as InstanceType
from .params import LatestAMI as LatestAMI
from .params import PrefixesMapping as PrefixesMapping
from .security import InstanceProfile as InstanceProfile
from .security import InstanceRole as InstanceRole
from .security import InstanceRoleAllowStatement0 as InstanceRoleAllowStatement0
from .security import InstanceRoleAssumeRolePolicyDocument as InstanceRoleAssumeRolePolicyDocument
from .security import InstanceRolePolicy as InstanceRolePolicy
from .security import InstanceRolePolicyAllowStatement0 as InstanceRolePolicyAllowStatement0
from .security import InstanceRolePolicyPolicyDocument as InstanceRolePolicyPolicyDocument

__all__: list[str] = ['AMI_ID', 'ARN', 'AVAILABILITY_ZONE', 'AWS_ACCOUNT_ID', 'AWS_NOTIFICATION_ARNS', 'AWS_NO_VALUE', 'AWS_PARTITION', 'AWS_REGION', 'AWS_STACK_ID', 'AWS_STACK_NAME', 'AWS_URL_SUFFIX', 'And', 'Base64', 'COMMA_DELIMITED_LIST', 'Cidr', 'CloudFormationResource', 'CloudFormationTemplate', 'CloudFrontCachePolicy', 'CloudFrontCachePolicyCachePolicyConfig', 'CloudFrontCachePolicyCookiesConfig', 'CloudFrontCachePolicyHeadersConfig', 'CloudFrontCachePolicyParametersInCacheKeyAndForwardedToOrigin', 'CloudFrontCachePolicyQueryStringsConfig', 'CloudFrontDistribution', 'CloudFrontDistributionCacheBehavior', 'CloudFrontDistributionCustomOriginConfig', 'CloudFrontDistributionDefaultCacheBehavior', 'CloudFrontDistributionDistributionConfig', 'CloudFrontDistributionOrigin', 'Condition', 'DenyStatement', 'Equals', 'FindInMap', 'GetAZs', 'GetAtt', 'HOSTED_ZONE_ID', 'INSTANCE_ID', 'If', 'ImportValue', 'InstanceProfile', 'InstanceRole', 'InstanceRoleAllowStatement0', 'InstanceRoleAssumeRolePolicyDocument', 'InstanceRolePolicy', 'InstanceRolePolicyAllowStatement0', 'InstanceRolePolicyPolicyDocument', 'InstanceSecurityGroup', 'InstanceSecurityGroupAssociationParameter', 'InstanceSecurityGroupEgress', 'InstanceSecurityGroupIngress', 'InstanceType', 'Join', 'KEY_PAIR', 'LIST_AVAILABILITY_ZONE', 'LIST_NUMBER', 'LIST_SECURITY_GROUP_ID', 'LIST_SUBNET_ID', 'LatestAMI', 'Mapping', 'NUMBER', 'NetworkInternetGateway', 'NetworkInternetGatewayAssociationParameter', 'NetworkPrivateSubnet1DefaultRoute', 'NetworkPrivateSubnet1RouteTable', 'NetworkPrivateSubnet1RouteTableAssociation', 'NetworkPrivateSubnet1RouteTableAssociationParameter', 'NetworkPrivateSubnet1Subnet', 'NetworkPrivateSubnet1SubnetAssociationParameter', 'NetworkPrivateSubnet2DefaultRoute', 'NetworkPrivateSubnet2RouteTable', 'NetworkPrivateSubnet2RouteTableAssociation', 'NetworkPrivateSubnet2RouteTableAssociationParameter', 'NetworkPrivateSubnet2Subnet', 'NetworkPrivateSubnet2SubnetAssociationParameter', 'NetworkPublicSubnet1', 'NetworkPublicSubnet1AssociationParameter', 'NetworkPublicSubnet1DefaultRoute', 'NetworkPublicSubnet1EIP', 'NetworkPublicSubnet1EIPAssociationParameter', 'NetworkPublicSubnet1NATGateway', 'NetworkPublicSubnet1NATGatewayAssociationParameter', 'NetworkPublicSubnet1RouteTable', 'NetworkPublicSubnet1RouteTableAssociation', 'NetworkPublicSubnet1RouteTableAssociationParameter', 'NetworkPublicSubnet2', 'NetworkPublicSubnet2AssociationParameter', 'NetworkPublicSubnet2DefaultRoute', 'NetworkPublicSubnet2EIP', 'NetworkPublicSubnet2EIPAssociationParameter', 'NetworkPublicSubnet2NATGateway', 'NetworkPublicSubnet2NATGatewayAssociationParameter', 'NetworkPublicSubnet2RouteTable', 'NetworkPublicSubnet2RouteTableAssociation', 'NetworkPublicSubnet2RouteTableAssociationParameter', 'NetworkVPC', 'NetworkVPCAssociationParameter', 'NetworkVPCGW', 'Not', 'Or', 'Output', 'Parameter', 'PolicyDocument', 'PolicyStatement', 'PrefixesMapping', 'PropertyType', 'Ref', 'RefDict', 'RefList', 'SECURITY_GROUP_ID', 'SSM_PARAMETER_STRING', 'SSM_PARAMETER_STRING_LIST', 'STRING', 'SUBNET_ID', 'Select', 'Server', 'ServerAssociationParameter', 'ServerBlockDeviceMapping', 'ServerEbs', 'Split', 'Sub', 'TemplateCondition', 'Transform', 'URLOutput', 'VOLUME_ID', 'VPC_ID', 'accessanalyzer', 'acmpca', 'aiops', 'amazonmq', 'amplify', 'amplifyuibuilder', 'apigateway', 'apigatewayv2', 'appconfig', 'appflow', 'appintegrations', 'applicationautoscaling', 'applicationinsights', 'applicationsignals', 'appmesh', 'apprunner', 'appstream', 'appsync', 'apptest', 'aps', 'arcregionswitch', 'arczonalshift', 'ask', 'athena', 'auditmanager', 'autoscaling', 'autoscalingplans', 'b2bi', 'backup', 'backupgateway', 'batch', 'bcmdataexports', 'bedrock', 'bedrockagentcore', 'billing', 'billingconductor', 'budgets', 'cases', 'cassandra', 'ce', 'certificatemanager', 'chatbot', 'cleanrooms', 'cleanroomsml', 'cloud9', 'cloudformation', 'cloudfront', 'cloudtrail', 'cloudwatch', 'codeartifact', 'codebuild', 'codecommit', 'codeconnections', 'codedeploy', 'codeguruprofiler', 'codegurureviewer', 'codepipeline', 'codestar', 'codestarconnections', 'codestarnotifications', 'cognito', 'comprehend', 'config', 'connect', 'connectcampaigns', 'connectcampaignsv2', 'controltower', 'cur', 'customerprofiles', 'databrew', 'datapipeline', 'datasync', 'datazone', 'dax', 'deadline', 'detective', 'devopsagent', 'devopsguru', 'directoryservice', 'dlm', 'dms', 'docdb', 'docdbelastic', 'dsql', 'dynamodb', 'ec2', 'ecr', 'ecs', 'efs', 'eks', 'elasticache', 'elasticbeanstalk', 'elasticloadbalancing', 'elasticloadbalancingv2', 'elasticsearch', 'emr', 'emrcontainers', 'emrserverless', 'entityresolution', 'events', 'eventschemas', 'evidently', 'evs', 'finspace', 'fis', 'fms', 'forecast', 'frauddetector', 'fsx', 'gamelift', 'get_att', 'globalaccelerator', 'glue', 'grafana', 'greengrass', 'greengrassv2', 'groundstation', 'guardduty', 'healthimaging', 'healthlake', 'iam', 'identitystore', 'imagebuilder', 'inspector', 'inspectorv2', 'internetmonitor', 'invoicing', 'iot', 'iotanalytics', 'iotcoredeviceadvisor', 'iotevents', 'iotfleetwise', 'iotsitewise', 'iotthingsgraph', 'iottwinmaker', 'iotwireless', 'ivs', 'ivschat', 'kafkaconnect', 'kendra', 'kendraranking', 'kinesis', 'kinesisanalytics', 'kinesisanalyticsv2', 'kinesisfirehose', 'kinesisvideo', 'kms', 'lakeformation', 'lambda_', 'launchwizard', 'lex', 'licensemanager', 'lightsail', 'location', 'logs', 'lookoutequipment', 'lookoutvision', 'm2', 'macie', 'managedblockchain', 'mediaconnect', 'mediaconvert', 'medialive', 'mediapackage', 'mediapackagev2', 'mediastore', 'mediatailor', 'memorydb', 'mpa', 'msk', 'mwaa', 'neptune', 'neptunegraph', 'networkfirewall', 'networkmanager', 'notifications', 'notificationscontacts', 'oam', 'observabilityadmin', 'odb', 'omics', 'opensearchserverless', 'opensearchservice', 'opsworks', 'organizations', 'osis', 'panorama', 'paymentcryptography', 'pcaconnectorad', 'pcaconnectorscep', 'pcs', 'personalize', 'pinpoint', 'pinpointemail', 'pipes', 'proton', 'qbusiness', 'qldb', 'quicksight', 'ram', 'rbin', 'rds', 'redshift', 'redshiftserverless', 'ref', 'refactorspaces', 'rekognition', 'resiliencehub', 'resourceexplorer2', 'resourcegroups', 'robomaker', 'rolesanywhere', 'route53', 'route53profiles', 'route53recoverycontrol', 'route53recoveryreadiness', 'route53resolver', 'rtbfabric', 'rum', 's3', 's3express', 's3objectlambda', 's3outposts', 's3tables', 's3vectors', 'sagemaker', 'scheduler', 'sdb', 'secretsmanager', 'securityhub', 'securitylake', 'serverless', 'servicecatalog', 'servicecatalogappregistry', 'servicediscovery', 'ses', 'setup_params', 'setup_resources', 'shield', 'signer', 'simspaceweaver', 'smsvoice', 'sns', 'sqs', 'ssm', 'ssmcontacts', 'ssmguiconnect', 'ssmincidents', 'ssmquicksetup', 'sso', 'stepfunctions', 'supportapp', 'synthetics', 'systemsmanagersap', 'timestream', 'transfer', 'verifiedpermissions', 'voiceid', 'vpclattice', 'waf', 'wafregional', 'wafv2', 'wetwire_aws', 'wisdom', 'workspaces', 'workspacesinstances', 'workspacesthinclient', 'workspacesweb', 'xray']
