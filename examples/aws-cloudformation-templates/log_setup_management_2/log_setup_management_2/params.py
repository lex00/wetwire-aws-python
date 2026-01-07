"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class OUID(Parameter):
    """The Id of the Organization Unit to deploy the stack set to."""

    type = STRING
    description = 'The Id of the Organization Unit to deploy the stack set to.'
    default = 'ou-qxtx-vv0thlla'


class OrgID(Parameter):
    """The Id of the Organization to verify the cross account API call. All accounts in this org will be granted permissions to put events onto the default event bus in this account. Note that this is not the OUID, it's the org itself and should start with o-"""

    type = STRING
    description = "The Id of the Organization to verify the cross account API call. All accounts in this org will be granted permissions to put events onto the default event bus in this account. Note that this is not the OUID, it's the org itself and should start with o-"
    default = 'o-jhfo4fcm1s'


class CentralEventBusName(Parameter):
    type = STRING
    default = 'central-cloudformation'


class CentralEventLogName(Parameter):
    type = STRING
    default = 'central-cloudformation-logs'


class KmsKeyId(Parameter):
    """The ID of an AWS Key Management Service (KMS) for Amazon SQS, or a custom KMS. To use the AWS managed KMS for Amazon SQS, specify a (default) alias ARN, alias name (for example alias/aws/sqs), key ARN, or key ID"""

    type = STRING
    description = 'The ID of an AWS Key Management Service (KMS) for Amazon SQS, or a custom KMS. To use the AWS managed KMS for Amazon SQS, specify a (default) alias ARN, alias name (for example alias/aws/sqs), key ARN, or key ID'
    default = 'alias/aws/sqs'


class StackSetRegions(Parameter):
    """AWS Regions where stack instances should be deployed in target accounts"""

    type = COMMA_DELIMITED_LIST
    description = 'AWS Regions where stack instances should be deployed in target accounts'
    default = 'us-east-1,eu-west-1'
