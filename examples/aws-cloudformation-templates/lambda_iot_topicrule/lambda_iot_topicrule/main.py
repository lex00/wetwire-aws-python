"""Stack resources."""

from . import *  # noqa: F403


class IoTPolicyAllowStatement0:
    resource: PolicyStatement
    action = 'iot:Connect'
    resource_arn = [Sub('arn:${AWS::Partition}:iot:${AWS::Region}:${AWS::AccountId}:client/*')]


class IoTPolicyAllowStatement1:
    resource: PolicyStatement
    action = 'iot:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:iot:${AWS::Region}:${AWS::AccountId}:topic/${AWS::StackName}'),
        Sub('arn:${AWS::Partition}:iot:${AWS::Region}:${AWS::AccountId}:topic/topic_1'),
        Sub('arn:${AWS::Partition}:iot:${AWS::Region}:${AWS::AccountId}:topic/topic_2'),
        Sub('arn:${AWS::Partition}:iot:${AWS::Region}:${AWS::AccountId}:topic/sdk/*'),
    ]


class IoTPolicyAllowStatement2:
    resource: PolicyStatement
    action = 'iot:Subscribe'
    resource_arn = [Sub('arn:${AWS::Partition}:iot:${AWS::Region}:${AWS::AccountId}:topicfilter/*')]


class IoTPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [IoTPolicyAllowStatement0, IoTPolicyAllowStatement1, IoTPolicyAllowStatement2]


class IoTPolicy:
    resource: iot.Policy
    policy_document = IoTPolicyPolicyDocument


class IoTPolicyPrincipalAttachment:
    resource: iot.PolicyPrincipalAttachment
    policy_name = IoTPolicy
    principal = CertificateARN


class IoTTopicRuleLambdaAction:
    resource: iot.TopicRule.LambdaAction
    function_arn = MyLambda.Arn


class IoTTopicRuleAction:
    resource: iot.TopicRule.Action
    lambda_ = IoTTopicRuleLambdaAction


class IoTTopicRuleTopicRulePayload:
    resource: iot.TopicRule.TopicRulePayload
    actions = [IoTTopicRuleAction]
    aws_iot_sql_version = '2016-03-23'
    sql = " SELECT * FROM 'topic_2'"
    rule_disabled = False


class IoTTopicRule:
    resource: iot.TopicRule
    rule_name = AWS_STACK_NAME
    topic_rule_payload = IoTTopicRuleTopicRulePayload


class IoTThing:
    resource: iot.Thing
    thing_name = AWS_STACK_NAME


class OpenIoTStarPolicyAllowStatement0:
    resource: PolicyStatement
    action = 'iot:*'
    resource_arn = '*'


class OpenIoTStarPolicyPolicyDocument:
    resource: PolicyDocument
    statement = [OpenIoTStarPolicyAllowStatement0]


class OpenIoTStarPolicy:
    resource: iot.Policy
    policy_document = OpenIoTStarPolicyPolicyDocument


class IoTThingPrincipalAttachment:
    resource: iot.ThingPrincipalAttachment
    principal = CertificateARN
    thing_name = IoTThing
