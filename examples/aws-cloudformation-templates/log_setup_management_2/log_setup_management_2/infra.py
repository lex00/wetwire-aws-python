"""Infra resources: TargetAccountLogging."""

from . import *  # noqa: F403


class TargetAccountLoggingDeploymentTargets(cloudformation.StackSet.DeploymentTargets):
    organizational_unit_ids = [OUID]


class TargetAccountLoggingStackInstances(cloudformation.StackSet.StackInstances):
    deployment_targets = TargetAccountLoggingDeploymentTargets
    regions = StackSetRegions


class TargetAccountLoggingParameter(cloudformation.StackSet.Parameter):
    parameter_key = 'CentralEventBusArn'
    parameter_value = CentralEventBus.Arn


class TargetAccountLoggingParameter1(cloudformation.StackSet.Parameter):
    parameter_key = 'KmsKeyId'
    parameter_value = KmsKeyId


class TargetAccountLoggingOperationPreferences(cloudformation.StackSet.OperationPreferences):
    failure_tolerance_count = 0
    max_concurrent_count = 2
    region_concurrency_type = 'PARALLEL'


class TargetAccountLoggingAutoDeployment(cloudformation.StackSet.AutoDeployment):
    enabled = True
    retain_stacks_on_account_removal = True


class TargetAccountLogging(cloudformation.StackSet):
    resource: cloudformation.StackSet
    template_body = """AWSTemplateFormatVersion: "2010-09-09"

Description: EventBridge Rule to send CloudFormation events to a central EventBus

Parameters:
  CentralEventBusArn:
    Type: String
  KmsKeyId:
    Type: String
    Description: 'The ID of an AWS Key Management Service (KMS) for Amazon SQS, or a custom KMS. To use the AWS managed KMS for Amazon SQS, specify a (default) alias ARN, alias name (for example alias/aws/sqs), key ARN, or key ID'
    Default: alias/aws/sqs

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
      KmsMasterKeyId: !Ref KmsKeyId

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
                aws:SourceArn: !Sub arn:aws:events:${AWS::Region}:${AWS::AccountId}:rule/CloudFormationEventRule
      Queues:
        - !Ref DeadLetterQueue

  EventBridgeRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal:
              Service: events.amazonaws.com
            Action: sts:AssumeRole

  EventBridgeRolePolicy:
    Type: AWS::IAM::RolePolicy
    Metadata:
      Comment: Allow CloudFormation events to be written to the default event bus in the target account
    Properties:
      PolicyName: EventBridgeRolePolicy
      PolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Action: events:PutEvents
            Resource: !Ref CentralEventBusArn
      RoleName: !Ref EventBridgeRole
"""
    capabilities = ['CAPABILITY_IAM']
    stack_instances_group = [TargetAccountLoggingStackInstances]
    parameters = [TargetAccountLoggingParameter, TargetAccountLoggingParameter1]
    permission_model = 'SERVICE_MANAGED'
    description = 'This stack set is part of a sample that demonstrates how to set up cross account logging. It configures logging resources in target accounts.'
    operation_preferences = TargetAccountLoggingOperationPreferences
    auto_deployment = TargetAccountLoggingAutoDeployment
    stack_set_name = 'log-setup'
    depends_on = [CentralEventRule, CentralEventLog, CentralEventLogPolicy]
