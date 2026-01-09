"""Security resources: MyWAFACL, MyWAFAssociation."""

from . import *  # noqa: F403


class MyWAFACLDefaultAction(wafv2.WebACL.DefaultAction):
    allow = {}


class MyWAFACLVisibilityConfig(wafv2.WebACL.VisibilityConfig):
    cloud_watch_metrics_enabled = True
    metric_name = 'AppRules'
    sampled_requests_enabled = True


class MyWAFACLRuleAction(wafv2.RuleGroup.RuleAction):
    block = {}


class MyWAFACLRateBasedStatement(wafv2.RuleGroup.RateBasedStatement):
    aggregate_key_type = 'IP'
    limit = 100


class MyWAFACLStatement(wafv2.RuleGroup.Statement):
    rate_based_statement = MyWAFACLRateBasedStatement


class MyWAFACLVisibilityConfig1(wafv2.RuleGroup.VisibilityConfig):
    cloud_watch_metrics_enabled = True
    metric_name = 'RateLimiter'
    sampled_requests_enabled = True


class MyWAFACLRule(wafv2.RuleGroup.Rule):
    action = MyWAFACLRuleAction
    name = 'RateLimit'
    priority = 0
    statement = MyWAFACLStatement
    visibility_config = MyWAFACLVisibilityConfig1


class MyWAFACL(wafv2.WebACL):
    default_action = MyWAFACLDefaultAction
    description = 'Application WAF'
    scope = 'REGIONAL'
    visibility_config = MyWAFACLVisibilityConfig
    rules = [MyWAFACLRule]


class MyWAFAssociation(wafv2.WebACLAssociation):
    resource_arn = Sub('arn:aws:apigateway:${AWS::Region}::/restapis/${ApiId}/stages/${ApiStage}', {
    'ApiId': MyApi,
    'ApiStage': MyApiProdStage  # noqa: WAW019 - SAM implicit resource,
})
    web_acl_arn = MyWAFACL.Arn
