"""Template outputs."""

from . import *  # noqa: F403


class AutoScalingGroupOutput(Output):
    """AutoScaling Group Name"""

    value = AutoScalingGroup
    description = 'AutoScaling Group Name'
    export_name = Sub('${AWS::StackName}-AutoScalingGroup')


class StackNameOutput(Output):
    """Stack Name"""

    value = AWS_STACK_NAME
    description = 'Stack Name'


class URLOutput(Output):
    """The URL of the website"""

    value = Join('', [
    'http://',
    ElasticLoadBalancer.DNSName,
])
    description = 'The URL of the website'
