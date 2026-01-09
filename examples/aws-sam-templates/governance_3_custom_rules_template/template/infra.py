"""Infra resources: ApiGWTracingRule, LambdaTracingRule."""

from . import *  # noqa: F403


class ApiGWTracingRuleScope(config.ConfigRule.Scope):
    compliance_resource_types = ['AWS::ApiGateway::Stage']


class ApiGWTracingRuleSourceDetail(config.ConfigRule.SourceDetail):
    event_source = 'aws.config'
    message_type = 'ConfigurationItemChangeNotification'


class ApiGWTracingRuleSourceDetail1(config.ConfigRule.SourceDetail):
    event_source = 'aws.config'
    message_type = 'OversizedConfigurationItemChangeNotification'


class ApiGWTracingRuleSource(config.ConfigRule.Source):
    owner = 'CUSTOM_LAMBDA'
    source_identifier = GenericRuleLambda.Arn
    source_details = [ApiGWTracingRuleSourceDetail, ApiGWTracingRuleSourceDetail1]


class ApiGWTracingRule(config.ConfigRule):
    description = 'Require API GW enabled tracing'
    input_parameters = {
        'resourceTypesArray': ['AWS::ApiGateway::Stage'],
        'keyPath': 'tracingEnabled',
        'acceptedValues': [True],
    }
    scope = ApiGWTracingRuleScope
    source = ApiGWTracingRuleSource
    depends_on = [GeneralLambdaAccessPermission]


class LambdaTracingRuleScope(config.ConfigRule.Scope):
    compliance_resource_types = ['AWS::Lambda::Function']


class LambdaTracingRuleSourceDetail(config.ConfigRule.SourceDetail):
    event_source = 'aws.config'
    message_type = 'ConfigurationItemChangeNotification'


class LambdaTracingRuleSourceDetail1(config.ConfigRule.SourceDetail):
    event_source = 'aws.config'
    message_type = 'OversizedConfigurationItemChangeNotification'


class LambdaTracingRuleSource(config.ConfigRule.Source):
    owner = 'CUSTOM_LAMBDA'
    source_identifier = GenericRuleLambda.Arn
    source_details = [LambdaTracingRuleSourceDetail, LambdaTracingRuleSourceDetail1]


class LambdaTracingRule(config.ConfigRule):
    description = 'Require X-Ray Active tracing on Lambda'
    input_parameters = {
        'resourceTypesArray': ['AWS::Lambda::Function'],
        'keyPath': 'tracingConfig.mode',
        'acceptedValues': ['Active'],
    }
    scope = LambdaTracingRuleScope
    source = LambdaTracingRuleSource
    depends_on = [GeneralLambdaAccessPermission]
