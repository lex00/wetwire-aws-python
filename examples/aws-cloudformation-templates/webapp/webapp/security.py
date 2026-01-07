"""Security resources: SiteContentReplicationRole, SiteWebACL, SiteCloudFrontLogsReplicationRole, CognitoUserPool, JwtResourceHandlerRole, CognitoClient, TestResourceHandlerRole, TestResourceHandlerPolicy, CognitoDomain, SiteCloudFrontLogsReplicationPolicy, SiteContentReplicationPolicy."""

from . import *  # noqa: F403


class SiteContentReplicationRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['s3.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class SiteContentReplicationRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [SiteContentReplicationRoleAllowStatement0]


class SiteContentReplicationRole(iam.Role):
    assume_role_policy_document = SiteContentReplicationRoleAssumeRolePolicyDocument
    path = '/'


class SiteWebACLDefaultAction(wafv2.WebACL.DefaultAction):
    allow = {}


class SiteWebACLVisibilityConfig(wafv2.WebACL.VisibilityConfig):
    sampled_requests_enabled = True
    cloud_watch_metrics_enabled = True
    metric_name = 'MetricForWebACLWithAMR'


class SiteWebACLOverrideAction(wafv2.WebACL.OverrideAction):
    none = {}


class SiteWebACLVisibilityConfig1(wafv2.WebACL.VisibilityConfig):
    sampled_requests_enabled = True
    cloud_watch_metrics_enabled = True
    metric_name = 'MetricForAMRCRS'


class SiteWebACLExcludedRule(wafv2.WebACL.ExcludedRule):
    name = 'NoUserAgent_HEADER'


class SiteWebACLManagedRuleGroupStatement(wafv2.WebACL.ManagedRuleGroupStatement):
    vendor_name = 'AWS'
    name = 'AWSManagedRulesCommonRuleSet'
    excluded_rules = [SiteWebACLExcludedRule]


class SiteWebACLStatement(wafv2.WebACL.Statement):
    managed_rule_group_statement = SiteWebACLManagedRuleGroupStatement


class SiteWebACLRule(wafv2.WebACL.Rule):
    name = 'AWS-AWSManagedRulesCommonRuleSet'
    priority = 0
    override_action = SiteWebACLOverrideAction
    visibility_config = SiteWebACLVisibilityConfig1
    statement = SiteWebACLStatement


class SiteWebACL(wafv2.WebACL):
    name = Sub('${AppName}-WebACLWithAMR')
    scope = 'CLOUDFRONT'
    description = 'Web ACL with AWS Managed Rules'
    default_action = SiteWebACLDefaultAction
    visibility_config = SiteWebACLVisibilityConfig
    tags = [{
        'Key': 'Name',
        'Value': AppName,
    }]
    rules = [SiteWebACLRule]


class SiteCloudFrontLogsReplicationRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['s3.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class SiteCloudFrontLogsReplicationRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [SiteCloudFrontLogsReplicationRoleAllowStatement0]


class SiteCloudFrontLogsReplicationRole(iam.Role):
    assume_role_policy_document = SiteCloudFrontLogsReplicationRoleAssumeRolePolicyDocument
    path = '/'


class CognitoUserPoolAdminCreateUserConfig(cognito.UserPool.AdminCreateUserConfig):
    allow_admin_create_user_only = True


class CognitoUserPoolSchemaAttribute(cognito.UserPool.SchemaAttribute):
    name = 'email'
    required = True


class CognitoUserPoolSchemaAttribute1(cognito.UserPool.SchemaAttribute):
    name = 'given_name'
    required = True


class CognitoUserPoolSchemaAttribute2(cognito.UserPool.SchemaAttribute):
    name = 'family_name'
    required = True


class CognitoUserPool(cognito.UserPool):
    user_pool_name = AppName
    admin_create_user_config = CognitoUserPoolAdminCreateUserConfig
    auto_verified_attributes = ['email']
    schema = [CognitoUserPoolSchemaAttribute, CognitoUserPoolSchemaAttribute1, CognitoUserPoolSchemaAttribute2]
    depends_on = [SiteDistribution]


class JwtResourceHandlerRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class JwtResourceHandlerRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [JwtResourceHandlerRoleAllowStatement0]


class JwtResourceHandlerRole(iam.Role):
    assume_role_policy_document = JwtResourceHandlerRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole']


class CognitoClient(cognito.UserPoolClient):
    client_name = AppName
    generate_secret = False
    user_pool_id = CognitoUserPool
    callback_ur_ls = [Sub('https://${SiteDistribution.DomainName}/index.html')]
    allowed_o_auth_flows = ['code']
    allowed_o_auth_flows_user_pool_client = True
    allowed_o_auth_scopes = ['phone', 'email', 'openid']
    supported_identity_providers = ['COGNITO']


class TestResourceHandlerRoleAllowStatement0(PolicyStatement):
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class TestResourceHandlerRoleAssumeRolePolicyDocument(PolicyDocument):
    statement = [TestResourceHandlerRoleAllowStatement0]


class TestResourceHandlerRole(iam.Role):
    assume_role_policy_document = TestResourceHandlerRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole']


class TestResourceHandlerPolicyAllowStatement0(PolicyStatement):
    action = [
        'dynamodb:BatchGetItem',
        'dynamodb:GetItem',
        'dynamodb:Query',
        'dynamodb:Scan',
        'dynamodb:BatchWriteItem',
        'dynamodb:PutItem',
        'dynamodb:UpdateItem',
    ]
    resource_arn = [TestTable.Arn]


class TestResourceHandlerPolicyPolicyDocument(PolicyDocument):
    statement = [TestResourceHandlerPolicyAllowStatement0]


class TestResourceHandlerPolicy(iam.RolePolicy):
    policy_document = TestResourceHandlerPolicyPolicyDocument
    policy_name = 'handler-policy'
    role_name = TestResourceHandlerRole


class CognitoDomain(cognito.UserPoolDomain):
    domain = AppName
    user_pool_id = CognitoUserPool


class SiteCloudFrontLogsReplicationPolicyAllowStatement0(PolicyStatement):
    action = [
        's3:GetReplicationConfiguration',
        's3:ListBucket',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}')


class SiteCloudFrontLogsReplicationPolicyAllowStatement1(PolicyStatement):
    action = [
        's3:GetObjectVersionForReplication',
        's3:GetObjectVersionAcl',
        's3:GetObjectVersionTagging',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}/*')


class SiteCloudFrontLogsReplicationPolicyAllowStatement2(PolicyStatement):
    action = [
        's3:ReplicateObject',
        's3:ReplicateDelete',
        's3:ReplicationTags',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}/*')


class SiteCloudFrontLogsReplicationPolicyPolicyDocument(PolicyDocument):
    statement = [SiteCloudFrontLogsReplicationPolicyAllowStatement0, SiteCloudFrontLogsReplicationPolicyAllowStatement1, SiteCloudFrontLogsReplicationPolicyAllowStatement2]


class SiteCloudFrontLogsReplicationPolicy(iam.RolePolicy):
    policy_document = SiteCloudFrontLogsReplicationPolicyPolicyDocument
    policy_name = 'bucket-replication-policy'
    role_name = SiteCloudFrontLogsReplicationRole


class SiteContentReplicationPolicyAllowStatement0(PolicyStatement):
    action = [
        's3:GetReplicationConfiguration',
        's3:ListBucket',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}')


class SiteContentReplicationPolicyAllowStatement1(PolicyStatement):
    action = [
        's3:GetObjectVersionForReplication',
        's3:GetObjectVersionAcl',
        's3:GetObjectVersionTagging',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}/*')


class SiteContentReplicationPolicyAllowStatement2(PolicyStatement):
    action = [
        's3:ReplicateObject',
        's3:ReplicateDelete',
        's3:ReplicationTags',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-content-replicas-${AWS::Region}-${AWS::AccountId}/*')


class SiteContentReplicationPolicyPolicyDocument(PolicyDocument):
    statement = [SiteContentReplicationPolicyAllowStatement0, SiteContentReplicationPolicyAllowStatement1, SiteContentReplicationPolicyAllowStatement2]


class SiteContentReplicationPolicy(iam.RolePolicy):
    policy_document = SiteContentReplicationPolicyPolicyDocument
    policy_name = 'bucket-replication-policy'
    role_name = SiteContentReplicationRole
