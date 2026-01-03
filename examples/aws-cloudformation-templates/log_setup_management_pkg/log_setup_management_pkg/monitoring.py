"""Monitoring resources: CentralEventLog, CentralEventLogPolicy, CentralEventLogQueryReason, CentralEventLogQuery."""

from . import *  # noqa: F403


class CentralEventLog:
    resource: logs.LogGroup
    log_group_class = logs.LogGroupClass.STANDARD
    log_group_name = CentralEventLogName
    kms_key_id = CentralEventLogKey.Arn
    depends_on = [CentralEventBus]


class CentralEventLogPolicy:
    resource: logs.ResourcePolicy
    policy_name = 'CentralEventLogResourcePolicy'
    policy_document = Sub("""{
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "delivery.logs.amazonaws.com",
          "events.amazonaws.com"
        ]
      },
      "Action": [
        "logs:PutLogEvents",
        "logs:CreateLogStream"
      ],
      "Resource": "${CentralEventLog.Arn}"
    }
  ]
}
""")


class CentralEventLogQueryReason:
    resource: logs.QueryDefinition
    name = 'CentralCloudFormationFailures'
    query_string = 'fields time, account, region, `detail.resource-type`, `detail.logical-resource-id`, `detail.status-details.status` as status, `detail.status-details.status-reason` as reason | sort @timestamp desc | filter status like "FAILED" | filter reason not like "canceled" | filter resource not like "AWS::CloudFormation::Stack" '
    log_group_names = [CentralEventLogName]


class CentralEventLogQuery:
    resource: logs.QueryDefinition
    name = 'CentralCloudFormationEventLogs'
    query_string = 'fields time, account, region, `detail.resource-type`, `detail.logical-resource-id`, `detail.status-details.status` | sort @timestamp desc'
    log_group_names = [CentralEventLogName]
