"""Compute resources: EC2Instance."""

from . import *  # noqa: F403


class EC2Instance:
    resource: ec2.Instance
    instance_type = InstanceType
    iam_instance_profile = IAMRole
    key_name = KeyName
    image_id = InstanceAMI
    subnet_id = SubnetId
    user_data = Base64(Sub("""<script>
mkdir C:\Downloads\Amazon\AmazonCloudWatchAgent
powershell -Command "(New-Object Net.WebClient).DownloadFile('https://s3.amazonaws.com/amazoncloudwatch-agent/windows/amd64/latest/amazon-cloudwatch-agent.msi','C:\Downloads\Amazon\AmazonCloudWatchAgent\amazon-cloudwatch-agent.msi')"
C:\Downloads\Amazon\AmazonCloudWatchAgent\amazon-cloudwatch-agent.msi
cfn-init.exe -v --stack ${AWS::StackId} --resource EC2Instance --region ${AWS::Region} --configsets default
cfn-signal.exe -e %errorlevel% --stack ${AWS::StackId} --resource EC2Instance --region ${AWS::Region}
</script>"""))
