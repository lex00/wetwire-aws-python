"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class DBName(Parameter):
    """The database name"""

    type = STRING
    description = 'The database name'
    default = 'MyDatabase'
    allowed_pattern = '[a-zA-Z][a-zA-Z0-9]*'
    min_length = 1
    max_length = 64
    constraint_description = 'must begin with a letter and contain only alphanumeric characters.'


class DBUser(Parameter):
    """The database admin account username"""

    type = STRING
    description = 'The database admin account username'
    allowed_pattern = '[a-zA-Z][a-zA-Z0-9]*'
    min_length = 1
    max_length = 16
    constraint_description = 'must begin with a letter and contain only alphanumeric characters.'
    no_echo = True


class DBAllocatedStorage(Parameter):
    """The size of the database (Gb)"""

    type = NUMBER
    description = 'The size of the database (Gb)'
    default = '5'
    min_value = 5
    max_value = 1024
    constraint_description = 'must be between 5 and 1024Gb.'


class DBInstanceClass(Parameter):
    """The database instance type"""

    type = STRING
    description = 'The database instance type'
    default = 'db.t3.medium'
    constraint_description = 'must select a valid database instance type.'


class EC2SecurityGroup(Parameter):
    """The EC2 security group that contains instances that need access to the database"""

    type = STRING
    description = 'The EC2 security group that contains instances that need access to the database'
    default = 'default'
    allowed_pattern = '[a-zA-Z0-9\\-]+'
    constraint_description = 'must be a valid security group name.'


class MultiAZ(Parameter):
    """Multi-AZ master database"""

    type = STRING
    description = 'Multi-AZ master database'
    default = 'false'
    allowed_values = [
    'true',
    'false',
]
    constraint_description = 'must be true or false.'


class EnableReadReplica(Parameter):
    """Enable the ReadReplica"""

    type = STRING
    description = 'Enable the ReadReplica'
    default = 'true'
    allowed_values = [
    'true',
    'false',
]
    constraint_description = 'must be true or false.'


class IsEC2VPCCondition(TemplateCondition):
    logical_id = 'IsEC2VPC'
    expression = Or(conditions=[Equals(AWS_REGION, 'eu-central-1'), Equals(AWS_REGION, 'cn-north-1')])


class EnableReadReplicaCondition(TemplateCondition):
    logical_id = 'EnableReadReplica'
    expression = Equals(EnableReadReplica, 'true')
