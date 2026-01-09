"""Security resources: JwtResourceHandlerRole, SiteContentReplicationRole, SiteWebACL, SiteCloudFrontLogsReplicationRole, TestResourceHandlerRole, TestResourceHandlerPolicy, SiteCloudFrontLogsReplicationPolicy, SiteContentReplicationPolicy."""

from . import *  # noqa: F403


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
