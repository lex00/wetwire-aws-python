"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class NumberOfRouteTables(Parameter):
    """Number of Route Table IDs to update. This must match your items in the comma-separated list of RouteTableIds parameter."""

    type = STRING
    description = 'Number of Route Table IDs to update. This must match your items in the comma-separated list of RouteTableIds parameter.'
    allowed_values = [
    1,
    2,
    3,
    4,
    5,
    6,
]


class NumberOfSecurityGroups(Parameter):
    """Number of Security Group IDs. This must match your selections in the list of SecurityGroupIds parameter."""

    type = STRING
    description = 'Number of Security Group IDs. This must match your selections in the list of SecurityGroupIds parameter.'
    allowed_values = [
    1,
    2,
    3,
    4,
    5,
    6,
]


class PeerName(Parameter):
    """Name of the VPC Peer"""

    type = STRING
    description = 'Name of the VPC Peer'
    max_length = 255


class PeerOwnerId(Parameter):
    """AWS account ID of the owner of the accepter VPC"""

    type = STRING
    description = 'AWS account ID of the owner of the accepter VPC'
    allowed_pattern = '^\\d{12}$'
    constraint_description = 'Must be 12 digits.'


class PeerRoleARN(Parameter):
    """ARN of the VPC peer role for the peering connection in another AWS account. Required when you are peering a VPC in a different AWS account."""

    type = STRING
    description = 'ARN of the VPC peer role for the peering connection in another AWS account. Required when you are peering a VPC in a different AWS account.'
    allowed_pattern = '^arn:(aws[a-zA-Z-]*)?:iam::\\d{12}:role\\/([\\w+=,.@-]*\\/)*[\\w+=,.@-]+'


class PeerVPCCIDR(Parameter):
    """CIDR of the VPC Peer"""

    type = STRING
    description = 'CIDR of the VPC Peer'
    allowed_pattern = '^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\/(1[6-9]|2[0-8]))$'
    constraint_description = 'CIDR block parameter must be in the form x.x.x.x/16-28'


class PeerVPCID(Parameter):
    """ID of the VPC with which you are creating the VPC peering connection"""

    type = STRING
    description = 'ID of the VPC with which you are creating the VPC peering connection'
    allowed_pattern = '^vpc-[0-9a-f]{17}$'
    constraint_description = 'Must have a prefix of "vpc-". Followed by 17 characters (numbers, letters "a-f")'


class RouteTableIds(Parameter):
    """Route Table IDs that will be updated to allow communications via the VPC peering connection. Note, the logical order is preserved."""

    type = STRING
    description = 'Route Table IDs that will be updated to allow communications via the VPC peering connection. Note, the logical order is preserved.'
    allowed_pattern = '^(rtb-[0-9a-f]{17})$|^((rtb-[0-9a-f]{17}(,|, ))*rtb-[0-9a-f]{17})$'
    constraint_description = 'Must have a prefix of "rtb-". Followed by 17 characters (numbers, letters "a-f"). Additional route tables can be provided, separated by a "comma".'


class SecurityGroupIds(Parameter):
    """Security Group IDs that will be updated to allow communications via the VPC peering connection. Note, the logical order is preserved."""

    type = LIST_SECURITY_GROUP_ID
    description = 'Security Group IDs that will be updated to allow communications via the VPC peering connection. Note, the logical order is preserved.'


class TemplatesS3BucketName(Parameter):
    """Templates S3 bucket name for the CloudFormation templates. S3 bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-)."""

    type = STRING
    description = 'Templates S3 bucket name for the CloudFormation templates. S3 bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).'
    allowed_pattern = '^(?=^.{3,63}$)(?!.*[.-]{2})(?!.*[--]{2})(?!^(?:(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\\.(?!$)|$)){4}$)(^(([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])\\.)*([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])$)'
    constraint_description = 'Templates S3 bucket name can include numbers, lowercase letters, uppercase letters, and hyphens (-). It cannot start or end with a hyphen (-).'


class TemplatesS3BucketRegion(Parameter):
    """AWS Region where the S3 bucket (TemplatesS3BucketName) is hosted."""

    type = STRING
    description = 'AWS Region where the S3 bucket (TemplatesS3BucketName) is hosted.'


class TemplatesS3KeyPrefix(Parameter):
    """S3 key prefix for the AWS CloudFormation templates. Key prefix can include numbers, lowercase letters, uppercase letters, hyphens (-), and forward slash (/)."""

    type = STRING
    description = 'S3 key prefix for the AWS CloudFormation templates. Key prefix can include numbers, lowercase letters, uppercase letters, hyphens (-), and forward slash (/).'
    allowed_pattern = '^[0-9a-zA-Z-/]*$'
    constraint_description = 'Templates key prefix can include numbers, lowercase letters, uppercase letters, hyphens (-), and forward slash (/).'


class VPCID(Parameter):
    """ID of the VPC"""

    type = VPC_ID
    description = 'ID of the VPC'
