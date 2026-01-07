"""Template outputs."""

from . import *  # noqa: F403


class NeptuneEndpointAddressOutput(Output):
    """Neptune DB endpoint address"""

    value = NeptuneDBCluster.Endpoint
    description = 'Neptune DB endpoint address'
    export_name = Sub('${Env}-${AppName}-neptune-endpoint-address')


class NeptuneReadEndpointAddressOutput(Output):
    """Neptune DB read-only endpoint address"""

    value = NeptuneDBCluster.ReadEndpoint
    description = 'Neptune DB read-only endpoint address'
    export_name = Sub('${Env}-${AppName}-neptune-read-endpoint-address')


class NeptuneSnsTopicOutput(Output):
    """Neptune SNS Topic for alarms"""

    value = If("CreateSnsTopic", NeptuneAlarmTopic, NeptuneSNSTopicArn)
    description = 'Neptune SNS Topic for alarms'
    export_name = Sub('${Env}-${AppName}-neptune-sns-topic')


class NeptuneEndpointPortOutput(Output):
    """Endpoint port"""

    value = NeptuneDBCluster.Port
    description = 'Endpoint port'
    export_name = Sub('${Env}-${AppName}-neptune-endpoint-port')
