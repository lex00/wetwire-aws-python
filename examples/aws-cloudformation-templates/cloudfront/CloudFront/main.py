"""Stack resources."""

from . import *  # noqa: F403


class EC2InstanceEbs(ec2.Instance.Ebs):
    volume_size = BootVolSize
    volume_type = BootVolType


class EC2InstanceBlockDeviceMapping(ec2.Instance.BlockDeviceMapping):
    device_name = '/dev/sda1'
    ebs = EC2InstanceEbs


class EC2InstanceAssociationParameter(ec2.Instance.AssociationParameter):
    key = 'Name'
    value = [Sub('${AppName}-${Environment}-ec2-instance')]


class EC2InstanceAssociationParameter1(ec2.Instance.AssociationParameter):
    key = 'Environment'
    value = [Environment]


class EC2Instance(ec2.Instance):
    image_id = EC2ImageId
    instance_type = EC2InstanceType
    subnet_id = PublicSubnetId1
    block_device_mappings = [EC2InstanceBlockDeviceMapping]
    security_group_ids = [EC2InstanceSG, ALBExternalAccessSG]
    key_name = KeyPairName
    tags = [EC2InstanceAssociationParameter, EC2InstanceAssociationParameter1]


class OriginALBTGTargetGroupAttribute(elasticloadbalancingv2.TargetGroup.TargetGroupAttribute):
    key = 'deregistration_delay.timeout_seconds'
    value = ALBTargetGroupAttributeDeregistration


class OriginALBTGTargetDescription(elasticloadbalancingv2.TargetGroup.TargetDescription):
    id = EC2Instance
    port = OriginALBTGPort


class OriginALBTGTargetGroupAttribute1(elasticloadbalancingv2.TargetGroup.TargetGroupAttribute):
    key = 'Name'
    value = Sub('${AppName}-${Environment}-alb-tg')


class OriginALBTGTargetGroupAttribute2(elasticloadbalancingv2.TargetGroup.TargetGroupAttribute):
    key = 'Environment'
    value = Environment


class OriginALBTG(elasticloadbalancingv2.TargetGroup):
    name = Sub('${AppName}-${Environment}-alb-tg')
    health_check_protocol = HealthCheckProtocol
    health_check_path = HealthCheckPath
    health_check_port = OriginALBTGPort
    health_check_interval_seconds = ALBTargetGroupHealthCheckIntervalSeconds
    health_check_timeout_seconds = ALBTargetGroupHealthCheckTimeoutSeconds
    healthy_threshold_count = ALBTargetGroupHealthyThresholdCount
    unhealthy_threshold_count = ALBTargetGroupUnhealthyThresholdCount
    target_group_attributes = [OriginALBTGTargetGroupAttribute]
    target_type = elasticloadbalancingv2.TargetTypeEnum.INSTANCE
    targets = [OriginALBTGTargetDescription]
    port = OriginALBTGPort
    protocol = elasticloadbalancingv2.ProtocolEnum.HTTP
    vpc_id = VpcId
    tags = [OriginALBTGTargetGroupAttribute1, OriginALBTGTargetGroupAttribute2]
    depends_on = [OriginALB]


class OriginALBHttpsListenerAction(elasticloadbalancingv2.ListenerRule.Action):
    target_group_arn = OriginALBTG
    type_ = 'forward'


class OriginALBHttpsListenerCertificate(elasticloadbalancingv2.ListenerCertificate.Certificate):
    certificate_arn = Sub('arn:${AWS::Partition}:acm:${AWS::Region}:${AWS::AccountId}:certificate/${ACMCertificateIdentifier}')


class OriginALBHttpsListener(elasticloadbalancingv2.Listener):
    default_actions = [OriginALBHttpsListenerAction]
    load_balancer_arn = OriginALB
    port = 443
    protocol = elasticloadbalancingv2.ProtocolEnum.HTTPS
    certificates = [OriginALBHttpsListenerCertificate]
    ssl_policy = 'ELBSecurityPolicy-FS-2018-06'
    depends_on = [OriginALBTG]


class OriginALBHttpsListenerRuleAction(elasticloadbalancingv2.ListenerRule.Action):
    type_ = 'forward'
    target_group_arn = OriginALBTG


class OriginALBHttpsListenerRuleRuleCondition(elasticloadbalancingv2.ListenerRule.RuleCondition):
    field_ = 'path-pattern'
    values = ['/*']


class OriginALBHttpsListenerRule(elasticloadbalancingv2.ListenerRule):
    actions = [OriginALBHttpsListenerRuleAction]
    conditions = [OriginALBHttpsListenerRuleRuleCondition]
    listener_arn = OriginALBHttpsListener
    priority = 1
    depends_on = [OriginALBHttpsListener]
