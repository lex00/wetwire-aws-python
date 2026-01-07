"""Messaging resources: ECSScheduledTask."""

from . import *  # noqa: F403


class ECSScheduledTaskEcsParameters(events.Rule.EcsParameters):
    task_count = SchedulerTasksCount
    task_definition_arn = TaskDefinition


class ECSScheduledTaskTarget(events.Rule.Target):
    arn = ECSCluster.Arn
    id = 'Target1'
    role_arn = ECSEventRole.Arn
    ecs_parameters = ECSScheduledTaskEcsParameters


class ECSScheduledTask(events.Rule):
    resource: events.Rule
    description = 'Creating a Schedule with CloudFormation as an example'
    schedule_expression = If("CronRate", CronSchedule, RateSchedule)
    state = events.RuleState.ENABLED
    targets = [ECSScheduledTaskTarget]
    depends_on = [ECSEventRole]
