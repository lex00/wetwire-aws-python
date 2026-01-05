"""Monitoring resources: CentralEventLogQuery, CentralEventLogQueryReason, CentralEventLogPolicy."""

from . import *  # noqa: F403


class CentralEventLogQuery:
    resource: logs.QueryDefinition
    name = 'CentralCloudFormationEventLogs'
    query_string = 'fields time, account, region, `detail.resource-type`, `detail.logical-resource-id`, `detail.status-details.status` | sort @timestamp desc'
    log_group_names = [CentralEventLogName]


class CentralEventLogQueryReason:
    resource: logs.QueryDefinition
    name = 'CentralCloudFormationFailures'
    query_string = 'fields time, account, region, `detail.resource-type`, `detail.logical-resource-id`, `detail.status-details.status` as status, `detail.status-details.status-reason` as reason | sort @timestamp desc | filter status like "FAILED" | filter reason not like "canceled" | filter resource not like "AWS::CloudFormation::Stack" '
    log_group_names = [CentralEventLogName]


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
