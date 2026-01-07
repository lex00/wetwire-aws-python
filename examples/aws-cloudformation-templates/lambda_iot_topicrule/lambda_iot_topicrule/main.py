"""Stack resources."""

from . import *  # noqa: F403


class IoTTopicRuleLambdaAction(iot.TopicRule.LambdaAction):
    function_arn = MyLambda.Arn


class IoTTopicRuleAction(iot.TopicRule.Action):
    lambda_ = IoTTopicRuleLambdaAction


class IoTTopicRuleTopicRulePayload(iot.TopicRule.TopicRulePayload):
    actions = [IoTTopicRuleAction]
    aws_iot_sql_version = '2016-03-23'
    sql = " SELECT * FROM 'topic_2'"
    rule_disabled = False


class IoTTopicRule(iot.TopicRule):
    resource: iot.TopicRule
    rule_name = AWS_STACK_NAME
    topic_rule_payload = IoTTopicRuleTopicRulePayload


class IoTThing(iot.Thing):
    resource: iot.Thing
    thing_name = AWS_STACK_NAME


class IoTThingPrincipalAttachment(iot.ThingPrincipalAttachment):
    resource: iot.ThingPrincipalAttachment
    principal = CertificateARN
    thing_name = IoTThing


class OpenIoTStarPolicyAllowStatement0(PolicyStatement):
    action = 'iot:*'
    resource_arn = '*'


class OpenIoTStarPolicyPolicyDocument(PolicyDocument):
    statement = [OpenIoTStarPolicyAllowStatement0]


class OpenIoTStarPolicy(iot.Policy):
    resource: iot.Policy
    policy_document = OpenIoTStarPolicyPolicyDocument


class IoTPolicyAllowStatement0(PolicyStatement):
    action = 'iot:Connect'
    resource_arn = [Sub('arn:${AWS::Partition}:iot:${AWS::Region}:${AWS::AccountId}:client/*')]


class IoTPolicyAllowStatement1(PolicyStatement):
    action = 'iot:*'
    resource_arn = [
        Sub('arn:${AWS::Partition}:iot:${AWS::Region}:${AWS::AccountId}:topic/${AWS::StackName}'),
        Sub('arn:${AWS::Partition}:iot:${AWS::Region}:${AWS::AccountId}:topic/topic_1'),
        Sub('arn:${AWS::Partition}:iot:${AWS::Region}:${AWS::AccountId}:topic/topic_2'),
        Sub('arn:${AWS::Partition}:iot:${AWS::Region}:${AWS::AccountId}:topic/sdk/*'),
    ]


class IoTPolicyAllowStatement2(PolicyStatement):
    action = 'iot:Subscribe'
    resource_arn = [Sub('arn:${AWS::Partition}:iot:${AWS::Region}:${AWS::AccountId}:topicfilter/*')]


class IoTPolicyPolicyDocument(PolicyDocument):
    statement = [IoTPolicyAllowStatement0, IoTPolicyAllowStatement1, IoTPolicyAllowStatement2]


class IoTPolicy(iot.Policy):
    resource: iot.Policy
    policy_document = IoTPolicyPolicyDocument


class IoTPolicyPrincipalAttachment(iot.PolicyPrincipalAttachment):
    resource: iot.PolicyPrincipalAttachment
    policy_name = IoTPolicy
    principal = CertificateARN
