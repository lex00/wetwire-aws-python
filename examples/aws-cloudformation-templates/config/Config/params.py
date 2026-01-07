"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class DeliveryChannelExists(Parameter):
    """Do you have an exisiting AWS Config delivery channel?"""

    type = STRING
    description = 'Do you have an exisiting AWS Config delivery channel?'
    default = 'false'
    allowed_values = [
    'false',
    'true',
]


class Ec2VolumeAutoEnableIO(Parameter):
    type = STRING
    default = 'false'
    allowed_values = [
    'false',
    'true',
]


class Ec2VolumeTagKey(Parameter):
    type = STRING
    default = 'CostCenter'


class CreateDeliveryChannelCondition(TemplateCondition):
    logical_id = 'CreateDeliveryChannel'
    expression = Equals(DeliveryChannelExists, 'false')
