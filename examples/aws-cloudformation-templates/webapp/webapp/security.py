"""Security resources: SiteCloudFrontLogsReplicationRole, SiteContentReplicationRole, TestResourceHandlerRole, SiteWebACL, CognitoUserPool, CognitoDomain, JwtResourceHandlerRole, CognitoClient, TestResourceHandlerPolicy, SiteContentReplicationPolicy, SiteCloudFrontLogsReplicationPolicy."""

from . import *  # noqa: F403


class SiteCloudFrontLogsReplicationRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['s3.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class SiteCloudFrontLogsReplicationRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [SiteCloudFrontLogsReplicationRoleAllowStatement0]


class SiteCloudFrontLogsReplicationRole(iam.Role):
    assume_role_policy_document = SiteCloudFrontLogsReplicationRoleAssumeRolePolicyDocument
    path = '/'


class SiteContentReplicationRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['s3.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class SiteContentReplicationRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [SiteContentReplicationRoleAllowStatement0]


class SiteContentReplicationRole(iam.Role):
    assume_role_policy_document = SiteContentReplicationRoleAssumeRolePolicyDocument
    path = '/'


class TestResourceHandlerRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class TestResourceHandlerRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [TestResourceHandlerRoleAllowStatement0]


class TestResourceHandlerRole(iam.Role):
    assume_role_policy_document = TestResourceHandlerRoleAssumeRolePolicyDocument
    managed_policy_arns = ['arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole']


class SiteWebACLAllowAction:
    resource: wafv2.WebACL.AllowAction


class SiteWebACLDefaultAction:
    resource: wafv2.WebACL.DefaultAction
    allow = SiteWebACLAllowAction


class SiteWebACLVisibilityConfig:
    resource: wafv2.WebACL.VisibilityConfig
    sampled_requests_enabled = True
    cloud_watch_metrics_enabled = True
    metric_name = 'MetricForWebACLWithAMR'


class SiteWebACLOverrideAction:
    resource: wafv2.WebACL.OverrideAction
    none = {}


class SiteWebACLVisibilityConfig1:
    resource: wafv2.WebACL.VisibilityConfig
    sampled_requests_enabled = True
    cloud_watch_metrics_enabled = True
    metric_name = 'MetricForAMRCRS'


class SiteWebACLExcludedRule:
    resource: wafv2.WebACL.ExcludedRule
    name = 'NoUserAgent_HEADER'


class SiteWebACLManagedRuleGroupStatement:
    resource: wafv2.WebACL.ManagedRuleGroupStatement
    vendor_name = 'AWS'
    name = 'AWSManagedRulesCommonRuleSet'
    excluded_rules = [SiteWebACLExcludedRule]


class SiteWebACLStatement:
    resource: wafv2.WebACL.Statement
    managed_rule_group_statement = SiteWebACLManagedRuleGroupStatement


class SiteWebACLRule:
    resource: wafv2.WebACL.Rule
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


class CognitoUserPoolAdminCreateUserConfig:
    resource: cognito.UserPool.AdminCreateUserConfig
    allow_admin_create_user_only = True


class CognitoUserPoolSchemaAttribute:
    resource: cognito.UserPool.SchemaAttribute
    name = 'email'
    required = True


class CognitoUserPoolSchemaAttribute1:
    resource: cognito.UserPool.SchemaAttribute
    name = 'given_name'
    required = True


class CognitoUserPoolSchemaAttribute2:
    resource: cognito.UserPool.SchemaAttribute
    name = 'family_name'
    required = True


class CognitoUserPool(cognito.UserPool):
    user_pool_name = AppName
    admin_create_user_config = CognitoUserPoolAdminCreateUserConfig
    auto_verified_attributes = ['email']
    schema = [CognitoUserPoolSchemaAttribute, CognitoUserPoolSchemaAttribute1, CognitoUserPoolSchemaAttribute2]
    depends_on = [SiteDistribution]


class CognitoDomain(cognito.UserPoolDomain):
    domain = AppName
    user_pool_id = CognitoUserPool


class JwtResourceHandlerRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = ['sts:AssumeRole']


class JwtResourceHandlerRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
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


class TestResourceHandlerPolicyAllowStatement0:
    resource: PolicyStatement
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


class TestResourceHandlerPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [TestResourceHandlerPolicyAllowStatement0]


class TestResourceHandlerPolicy(iam.RolePolicy):
    policy_document = TestResourceHandlerPolicyPolicyDocument
    policy_name = 'handler-policy'
    role_name = TestResourceHandlerRole


class SiteContentReplicationPolicyAllowStatement0:
    resource: PolicyStatement
    action = [
        's3:GetReplicationConfiguration',
        's3:ListBucket',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}')


class SiteContentReplicationPolicyAllowStatement1:
    resource: PolicyStatement
    action = [
        's3:GetObjectVersionForReplication',
        's3:GetObjectVersionAcl',
        's3:GetObjectVersionTagging',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-content-${AWS::Region}-${AWS::AccountId}/*')


class SiteContentReplicationPolicyAllowStatement2:
    resource: PolicyStatement
    action = [
        's3:ReplicateObject',
        's3:ReplicateDelete',
        's3:ReplicationTags',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-content-replicas-${AWS::Region}-${AWS::AccountId}/*')


class SiteContentReplicationPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [SiteContentReplicationPolicyAllowStatement0, SiteContentReplicationPolicyAllowStatement1, SiteContentReplicationPolicyAllowStatement2]


class SiteContentReplicationPolicy(iam.RolePolicy):
    policy_document = SiteContentReplicationPolicyPolicyDocument
    policy_name = 'bucket-replication-policy'
    role_name = SiteContentReplicationRole


class SiteCloudFrontLogsReplicationPolicyAllowStatement0:
    resource: PolicyStatement
    action = [
        's3:GetReplicationConfiguration',
        's3:ListBucket',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}')


class SiteCloudFrontLogsReplicationPolicyAllowStatement1:
    resource: PolicyStatement
    action = [
        's3:GetObjectVersionForReplication',
        's3:GetObjectVersionAcl',
        's3:GetObjectVersionTagging',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-${AWS::Region}-${AWS::AccountId}/*')


class SiteCloudFrontLogsReplicationPolicyAllowStatement2:
    resource: PolicyStatement
    action = [
        's3:ReplicateObject',
        's3:ReplicateDelete',
        's3:ReplicationTags',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:s3:::${AppName}-cflogs-replicas-${AWS::Region}-${AWS::AccountId}/*')


class SiteCloudFrontLogsReplicationPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [SiteCloudFrontLogsReplicationPolicyAllowStatement0, SiteCloudFrontLogsReplicationPolicyAllowStatement1, SiteCloudFrontLogsReplicationPolicyAllowStatement2]


class SiteCloudFrontLogsReplicationPolicy(iam.RolePolicy):
    policy_document = SiteCloudFrontLogsReplicationPolicyPolicyDocument
    policy_name = 'bucket-replication-policy'
    role_name = SiteCloudFrontLogsReplicationRole
