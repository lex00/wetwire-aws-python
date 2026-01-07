"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class StackName(Parameter):
    """The name of the parent cluster stack that you created. Necessary to locate and reference resources created by that stack."""

    type = STRING
    description = 'The name of the parent cluster stack that you created. Necessary to locate and reference resources created by that stack.'
    default = 'production'


class ServiceName(Parameter):
    """A name for the service"""

    type = STRING
    description = 'A name for the service'
    default = 'nginx'


class ImageUrl(Parameter):
    """The url of a docker image that contains the application process that will handle the traffic for this service"""

    type = STRING
    description = 'The url of a docker image that contains the application process that will handle the traffic for this service'
    default = 'nginx'


class ContainerPort(Parameter):
    """What port number the application inside the docker container is binding to"""

    type = NUMBER
    description = 'What port number the application inside the docker container is binding to'
    default = 80


class ContainerCpu(Parameter):
    """How much CPU to give the container. 1024 is 1 CPU"""

    type = NUMBER
    description = 'How much CPU to give the container. 1024 is 1 CPU'
    default = 256


class ContainerMemory(Parameter):
    """How much memory in megabytes to give the container"""

    type = NUMBER
    description = 'How much memory in megabytes to give the container'
    default = 512


class Path(Parameter):
    """A path on the public load balancer that this service should be connected to. Use * to send all load balancer traffic to this service."""

    type = STRING
    description = 'A path on the public load balancer that this service should be connected to. Use * to send all load balancer traffic to this service.'
    default = '*'


class Priority(Parameter):
    """The priority for the routing rule added to the load balancer. This only applies if your have multiple services which have been assigned to different paths on the load balancer."""

    type = NUMBER
    description = 'The priority for the routing rule added to the load balancer. This only applies if your have multiple services which have been assigned to different paths on the load balancer.'
    default = 1


class DesiredCount(Parameter):
    """How many copies of the service task to run"""

    type = NUMBER
    description = 'How many copies of the service task to run'
    default = 2


class Role(Parameter):
    """(Optional) An IAM role to give the service's containers if the code within needs to access other AWS resources like S3 buckets, DynamoDB tables, etc"""

    type = STRING
    description = "(Optional) An IAM role to give the service's containers if the code within needs to access other AWS resources like S3 buckets, DynamoDB tables, etc"
    default = ''


class HasCustomRoleCondition(TemplateCondition):
    logical_id = 'HasCustomRole'
    expression = Not(Equals(Role, ''))
