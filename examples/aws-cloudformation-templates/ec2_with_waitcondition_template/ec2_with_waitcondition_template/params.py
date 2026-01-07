"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class KeyName(Parameter):
    """Name of an existing EC2 KeyPair to enable SSH access to the instance"""

    type = KEY_PAIR
    description = 'Name of an existing EC2 KeyPair to enable SSH access to the instance'
    default = 'slinger_testing'
    constraint_description = 'must be the name of an existing EC2 KeyPair.'


class InstanceName(Parameter):
    """Name of EC2 instance"""

    type = STRING
    description = 'Name of EC2 instance'
    constraint_description = 'must be a valid EC2 instance string name.'


class InstanceType(Parameter):
    """Basic EC2 instance type"""

    type = STRING
    description = 'Basic EC2 instance type'
    default = 'c4.2xlarge'
    allowed_values = [
    't1.micro',
    't2.nano',
    't2.micro',
    't2.small',
    't2.medium',
    't2.large',
    'm1.small',
    'm1.medium',
    'm1.large',
    'm1.xlarge',
    'm2.xlarge',
    'm2.2xlarge',
    'm2.4xlarge',
    'm3.medium',
    'm3.large',
    'm3.xlarge',
    'm3.2xlarge',
    'm4.large',
    'm4.xlarge',
    'm4.2xlarge',
    'm4.4xlarge',
    'm4.10xlarge',
    'c1.medium',
    'c1.xlarge',
    'c3.large',
    'c3.xlarge',
    'c3.2xlarge',
    'c3.4xlarge',
    'c3.8xlarge',
    'c4.large',
    'c4.xlarge',
    'c4.2xlarge',
    'c4.4xlarge',
    'c4.8xlarge',
    'g2.2xlarge',
    'g2.8xlarge',
    'r3.large',
    'r3.xlarge',
    'r3.2xlarge',
    'r3.4xlarge',
    'r3.8xlarge',
    'i2.xlarge',
    'i2.2xlarge',
    'i2.4xlarge',
    'i2.8xlarge',
    'd2.xlarge',
    'd2.2xlarge',
    'd2.4xlarge',
    'd2.8xlarge',
    'hs1.8xlarge',
    'cr1.8xlarge',
    'cc2.8xlarge',
]
    constraint_description = 'must be a valid EC2 instance type.'


class ImageId(Parameter):
    """Basic instance ami"""

    type = AMI_ID
    description = 'Basic instance ami'


class VpcId(Parameter):
    """VpcId of your existing Virtual Private Cloud (VPC)"""

    type = STRING
    description = 'VpcId of your existing Virtual Private Cloud (VPC)'


class SubnetId(Parameter):
    """SubnetId of an existing subnet in your Virtual Private Cloud (VPC)"""

    type = STRING
    description = 'SubnetId of an existing subnet in your Virtual Private Cloud (VPC)'


class SSHLocation(Parameter):
    """ The IP address range that can be used to SSH to the EC2 instances"""

    type = STRING
    description = ' The IP address range that can be used to SSH to the EC2 instances'
    default = '0.0.0.0/0'
    allowed_pattern = '(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})/(\\d{1,2})'
    min_length = 9
    max_length = 18
    constraint_description = 'must be a valid IP CIDR range of the form x.x.x.x/x.'


class BudgetCode(Parameter):
    """ Budget code to save money"""

    type = STRING
    description = ' Budget code to save money'
    default = 'A019517'
    constraint_description = 'must be a valid budget code.'


class LaunchPlatform(Parameter):
    """ Mark current platform"""

    type = STRING
    description = ' Mark current platform'
    default = 'bitstorm_dev'
    constraint_description = 'must be a valid platform like bitstorm_qc bitstorm_dev bitstorm_staggin bitstorm_live.'


class LaunchUser(Parameter):
    """ Mark current tester"""

    type = STRING
    description = ' Mark current tester'
    default = 'null'
    constraint_description = 'must be a valid and existing tester.'


class TestID(Parameter):
    """ Mark current testcase"""

    type = STRING
    description = ' Mark current testcase'
    constraint_description = 'must be a valid and existing testcase id.'


class TestTarget(Parameter):
    """ Mark current test target"""

    type = STRING
    description = ' Mark current test target'
    constraint_description = 'must be a valid and existing test target name.'


class AgentID(Parameter):
    """ Mark current agent"""

    type = STRING
    description = ' Mark current agent'


class IsMaster(Parameter):
    """Mark master agent"""

    type = STRING
    description = 'Mark master agent'
    default = 'False'


class MasterID(Parameter):
    """Mark master ID"""

    type = STRING
    description = 'Mark master ID'
    default = 'null'
