"""Compute resources: VolumeAutoEnableIOComplianceCheck, ConfigPermissionToCallLambda, Ec2Volume."""

from . import *  # noqa: F403


class VolumeAutoEnableIOComplianceCheckCode:
    resource: lambda_.Function.Code
    zip_file = """var aws  = require('aws-sdk');
var config = new aws.ConfigService();
var ec2 = new aws.EC2();
exports.handler = function(event, context) {
    var compliance = evaluateCompliance(event, function(compliance, event) {
        var configurationItem = JSON.parse(event.invokingEvent).configurationItem;
        var putEvaluationsRequest = {
            Evaluations: [{
                ComplianceResourceType: configurationItem.resourceType,
                ComplianceResourceId: configurationItem.resourceId,
                ComplianceType: compliance,
                OrderingTimestamp: configurationItem.configurationItemCaptureTime
            }],
            ResultToken: event.resultToken
        };
        config.putEvaluations(putEvaluationsRequest, function(err, data) {
            if (err) context.fail(err);
            else context.succeed(data);
        });
    });
};
function evaluateCompliance(event, doReturn) {
    var configurationItem = JSON.parse(event.invokingEvent).configurationItem;
    var status = configurationItem.configurationItemStatus;
    if (configurationItem.resourceType !== 'AWS::EC2::Volume' || event.eventLeftScope || (status !== 'OK' && status !== 'ResourceDiscovered'))
        doReturn('NOT_APPLICABLE', event);
    else ec2.describeVolumeAttribute({VolumeId: configurationItem.resourceId, Attribute: 'autoEnableIO'}, function(err, data) {
        if (err) context.fail(err);
        else if (data.AutoEnableIO.Value) doReturn('COMPLIANT', event);
        else doReturn('NON_COMPLIANT', event);
    });
}
"""


class VolumeAutoEnableIOComplianceCheck(lambda_.Function):
    code = VolumeAutoEnableIOComplianceCheckCode
    handler = 'index.handler'
    runtime = lambda_.Runtime.NODEJS20_X
    timeout = '30'
    role = LambdaExecutionRole.Arn


class ConfigPermissionToCallLambda(lambda_.Permission):
    function_name = VolumeAutoEnableIOComplianceCheck.Arn
    action = 'lambda:InvokeFunction'
    principal = 'config.amazonaws.com'


class Ec2VolumeAssociationParameter:
    resource: ec2.Instance.AssociationParameter
    key = Ec2VolumeTagKey
    value = 'Ec2VolumeTagValue'


class Ec2Volume(ec2.Volume):
    auto_enable_io = Ec2VolumeAutoEnableIO
    size = '5'
    availability_zone = Select(0, GetAZs())
    tags = [Ec2VolumeAssociationParameter]
