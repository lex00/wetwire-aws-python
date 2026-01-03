"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class OUID:
    resource: Parameter
    type = STRING
    default = 'ou-qxtx-vv0thlla'


class KmsKeyId:
    """The ID of an AWS Key Management Service (KMS) for Amazon SQS, or a custom KMS. To use the AWS managed KMS for Amazon SQS, specify a (default) alias ARN, alias name (for example alias/aws/sqs), key ARN, or key ID"""

    resource: Parameter
    type = STRING
    description = 'The ID of an AWS Key Management Service (KMS) for Amazon SQS, or a custom KMS. To use the AWS managed KMS for Amazon SQS, specify a (default) alias ARN, alias name (for example alias/aws/sqs), key ARN, or key ID'
    default = 'alias/aws/sqs'


class StackSetRegions:
    """AWS Regions where stack instances should be deployed in target accounts"""

    resource: Parameter
    type = COMMA_DELIMITED_LIST
    description = 'AWS Regions where stack instances should be deployed in target accounts'
    default = 'us-east-1,eu-west-1'
