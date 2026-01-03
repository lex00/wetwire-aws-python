"""Template outputs."""

from . import *  # noqa: F403


class AutoScalingGroupOutput:
    """AutoScaling Group Name"""

    resource: Output
    value = AutoScalingGroup
    description = 'AutoScaling Group Name'
    export_name = Sub('${AWS::StackName}-AutoScalingGroup')


class StackNameOutput:
    """Stack Name"""

    resource: Output
    value = AWS_STACK_NAME
    description = 'Stack Name'


class URLOutput:
    """The URL of the website"""

    resource: Output
    value = Join('', [
    'http://',
    ElasticLoadBalancer.DNSName,
])
    description = 'The URL of the website'
