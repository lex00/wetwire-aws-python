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
    template_body = {
        'Rain::Embed': 'log-setup-target-accounts.yaml',
    }
    capabilities = ['CAPABILITY_IAM']
    stack_instances_group = [TargetAccountLoggingStackInstances]
    parameters = [TargetAccountLoggingParameter]
    permission_model = 'SERVICE_MANAGED'
    description = 'This stack set is part of a sample that demonstrates how to set up cross account logging. It configures logging resources in target accounts.'
    operation_preferences = TargetAccountLoggingOperationPreferences
    auto_deployment = TargetAccountLoggingAutoDeployment
    stack_set_name = 'log-setup'
    depends_on = [CentralEventRule, CentralEventLog, CentralEventLogPolicy]
