"""Template outputs."""

from . import *  # noqa: F403


class NeptuneEndpointAddressOutput:
    """Neptune DB endpoint address"""

    resource: Output
    value = NeptuneDBCluster.Endpoint
    description = 'Neptune DB endpoint address'
    export_name = Sub('${Env}-${AppName}-neptune-endpoint-address')


class NeptuneReadEndpointAddressOutput:
    """Neptune DB read-only endpoint address"""

    resource: Output
    value = NeptuneDBCluster.ReadEndpoint
    description = 'Neptune DB read-only endpoint address'
    export_name = Sub('${Env}-${AppName}-neptune-read-endpoint-address')


class NeptuneSnsTopicOutput:
    """Neptune SNS Topic for alarms"""

    resource: Output
    value = If("CreateSnsTopic", NeptuneAlarmTopic, NeptuneSNSTopicArn)
    description = 'Neptune SNS Topic for alarms'
    export_name = Sub('${Env}-${AppName}-neptune-sns-topic')


class NeptuneEndpointPortOutput:
    """Endpoint port"""

    resource: Output
    value = NeptuneDBCluster.Port
    description = 'Endpoint port'
    export_name = Sub('${Env}-${AppName}-neptune-endpoint-port')
