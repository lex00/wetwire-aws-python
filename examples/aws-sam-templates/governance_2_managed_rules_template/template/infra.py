"""Infra resources: S3NoPublicReadRule, ApiGWLoggingRule, S3NoPublicWriteRule."""

from . import *  # noqa: F403


class S3NoPublicReadRuleScope(config.ConfigRule.Scope):
    compliance_resource_types = ['AWS::S3::Bucket']


class S3NoPublicReadRuleSource(config.ConfigRule.Source):
    owner = 'AWS'
    source_identifier = 'S3_BUCKET_PUBLIC_READ_PROHIBITED'


class S3NoPublicReadRule(config.ConfigRule):
    description = 'S3 block public read'
    scope = S3NoPublicReadRuleScope
    source = S3NoPublicReadRuleSource


class ApiGWLoggingRuleScope(config.ConfigRule.Scope):
    compliance_resource_types = ['AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Stage']


class ApiGWLoggingRuleSource(config.ConfigRule.Source):
    owner = 'AWS'
    source_identifier = 'API_GW_EXECUTION_LOGGING_ENABLED'


class ApiGWLoggingRule(config.ConfigRule):
    description = 'Require API GW Logging'
    scope = ApiGWLoggingRuleScope
    source = ApiGWLoggingRuleSource


class S3NoPublicWriteRuleScope(config.ConfigRule.Scope):
    compliance_resource_types = ['AWS::S3::Bucket']


class S3NoPublicWriteRuleSource(config.ConfigRule.Source):
    owner = 'AWS'
    source_identifier = 'S3_BUCKET_PUBLIC_WRITE_PROHIBITED'


class S3NoPublicWriteRule(config.ConfigRule):
    description = 'S3 block public write'
    scope = S3NoPublicWriteRuleScope
    source = S3NoPublicWriteRuleSource
