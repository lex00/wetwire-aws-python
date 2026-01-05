"""Infra resources: TargetAccountLogging."""

from . import *  # noqa: F403


class TargetAccountLoggingDeploymentTargets:
    resource: cloudformation.StackSet.DeploymentTargets
    organizational_unit_ids = [OUID]


class TargetAccountLoggingStackInstances:
    resource: cloudformation.StackSet.StackInstances
    deployment_targets = TargetAccountLoggingDeploymentTargets
    regions = ['us-east-1', 'us-west-2']


class TargetAccountLoggingParameter:
    resource: cloudformation.StackSet.Parameter
    parameter_key = 'CentralEventBusArn'
    parameter_value = CentralEventBus.Arn


class TargetAccountLoggingOperationPreferences:
    resource: cloudformation.StackSet.OperationPreferences
    failure_tolerance_count = 0
    max_concurrent_count = 2
    region_concurrency_type = 'PARALLEL'


class TargetAccountLoggingAutoDeployment:
    resource: cloudformation.StackSet.AutoDeployment
    enabled = True
    retain_stacks_on_account_removal = True


class TargetAccountLogging(cloudformation.StackSet):
    template_body = """AWSTemplateFormatVersion: '2010-09-09'

Description: EventBridge Rule to send CloudFormation events to a central EventBus

Parameters:

  CentralEventBusArn:
    Type: String

Resources:

  CloudFormationEventRule:
    Type: AWS::Events::Rule
    Metadata:
      Comment: Send all cloudformation events to the central event bus
    Properties:
      Name: CloudFormationEventRule
      EventBusName: !Sub arn:aws:events:${AWS::Region}:${AWS::AccountId}:event-bus/default
      EventPattern:
        source:
          - aws.cloudformation
      State: ENABLED
      Targets:
        - Arn: !Ref CentralEventBusArn 
          RoleArn: !GetAtt EventBridgeRole.Arn
          Id: CentralEventBus
          DeadLetterConfig:
            Arn: !GetAtt DeadLetterQueue.Arn

  DeadLetterQueue:
    Type: AWS::SQS::Queue
    Properties:
      QueueName: CloudFormation-Logs-DLQ

  DeadLetterQueuePolicy:
    Type: AWS::SQS::QueuePolicy
    Properties:
      PolicyDocument:
        Version: "2012-10-17"
        Id: AllowEventBridgeToWriteLogs
        Statement:
          - Sid: AllowEventBridgeToWriteLogs
            Effect: Allow
            Principal:
              Service: events.amazonaws.com
            Action: sqs:SendMessage
            Resource: !GetAtt DeadLetterQueue.Arn
            Condition:
              ArnLike:
                aws:SourceArn: !Sub "arn:aws:events:${AWS::Region}:${AWS::AccountId}:rule/CloudFormationEventRule"
      Queues:
        - !Ref DeadLetterQueue

  EventBridgeRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: events.amazonaws.com
            Action: 'sts:AssumeRole'

  EventBridgeRolePolicy:
    Type: AWS::IAM::RolePolicy
    Metadata: 
      Comment: Allow CloudFormation events to be written to the default event bus in the target account
    Properties:
      PolicyName: EventBridgeRolePolicy
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Action: 'events:PutEvents'
            Resource: !Ref CentralEventBusArn 
      RoleName: !Ref EventBridgeRole"""
    capabilities = ['CAPABILITY_IAM']
    stack_instances_group = [TargetAccountLoggingStackInstances]
    parameters = [TargetAccountLoggingParameter]
    permission_model = 'SERVICE_MANAGED'
    description = 'This stack set is part of a sample that demonstrates how to set up cross account logging. It configures logging resources in target accounts.'
    operation_preferences = TargetAccountLoggingOperationPreferences
    auto_deployment = TargetAccountLoggingAutoDeployment
    stack_set_name = 'log-setup'
    depends_on = [CentralEventRule, CentralEventLog, CentralEventLogPolicy]
