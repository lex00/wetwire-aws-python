"""Messaging resources: ECSScheduledTask."""

from . import *  # noqa: F403


class ECSScheduledTaskEcsParameters:
    resource: events.Rule.EcsParameters
    task_count = SchedulerTasksCount
    task_definition_arn = TaskDefinition


class ECSScheduledTaskTarget:
    resource: events.Rule.Target
    arn = ECSCluster.Arn
    id = 'Target1'
    role_arn = ECSEventRole.Arn
    ecs_parameters = ECSScheduledTaskEcsParameters


class ECSScheduledTask:
    resource: events.Rule
    description = 'Creating a Schedule with CloudFormation as an example'
    schedule_expression = If("CronRate", CronSchedule, RateSchedule)
    state = events.RuleState.ENABLED
    targets = [ECSScheduledTaskTarget]
    depends_on = [ECSEventRole]
