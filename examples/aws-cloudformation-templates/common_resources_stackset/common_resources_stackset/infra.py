"""Infra resources: StackSet."""

from . import *  # noqa: F403


class StackSetDeploymentTargets(cloudformation.StackSet.DeploymentTargets):
    organizational_unit_ids = [OUID]


class StackSetStackInstances(cloudformation.StackSet.StackInstances):
    deployment_targets = StackSetDeploymentTargets
    regions = ['us-east-1', 'us-west-2']


class StackSetParameter(cloudformation.StackSet.Parameter):
    parameter_key = 'AppName'
    parameter_value = 'stackset-logging-sample'


class StackSetOperationPreferences(cloudformation.StackSet.OperationPreferences):
    failure_tolerance_count = 0
    max_concurrent_count = 2
    region_concurrency_type = 'PARALLEL'


class StackSetAutoDeployment(cloudformation.StackSet.AutoDeployment):
    enabled = True
    retain_stacks_on_account_removal = True


class StackSet(cloudformation.StackSet):
    template_body = {
        'Rain::Embed': 'common-resources-pkg.yaml',
    }
    capabilities = ['CAPABILITY_IAM']
    stack_instances_group = [StackSetStackInstances]
    parameters = [StackSetParameter]
    permission_model = 'SERVICE_MANAGED'
    description = 'This stack set is part of a sample that demonstrates how to set up cross account logging'
    operation_preferences = StackSetOperationPreferences
    auto_deployment = StackSetAutoDeployment
    stack_set_name = 'common-resources'
