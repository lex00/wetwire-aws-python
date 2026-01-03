"""Security resources: ADConnectorServiceAccountSecret, ADConnectorLambdaRole, ADConnectorLinuxEC2SeamlessDomainJoinSecret, ADConnectorLinuxEC2DomainJoinRole, ADConnectorLinuxEC2DomainJoinInstanceProfile, ADConnectorWindowsEC2DomainJoinRole, ADConnectorWindowsEC2DomainJoinInstanceProfile."""

from . import *  # noqa: F403


class ADConnectorServiceAccountSecret:
    resource: secretsmanager.Secret
    name = Sub('ADConnector-ServiceAccount-${DomainNetBiosName}-Domain')
    description = Sub('ADConnector Service Account for ${DomainNetBiosName} Domain')
    secret_string = Sub('{ "username" : "${DomainJoinUser}", "password" : "${DomainJoinUserPassword}" }')
    kms_key_id = If("SecretsManagerDomainCredentialsSecretsKMSKeyCondition", SecretsManagerDomainCredentialsSecretsKMSKey, AWS_NO_VALUE)
    deletion_policy = 'Retain'


class ADConnectorLambdaRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['lambda.amazonaws.com'],
    }
    action = 'sts:AssumeRole'


class ADConnectorLambdaRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ADConnectorLambdaRoleAllowStatement0]


class ADConnectorLambdaRoleAllowStatement0_1:
    resource: PolicyStatement
    sid = 'CreateLogGroup'
    action = 'logs:CreateLogGroup'
    resource_arn = Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:${ADConnectorLambdaLogsLogGroup}')


class ADConnectorLambdaRoleAllowStatement1:
    resource: PolicyStatement
    sid = 'CreateLogStreamAndEvents'
    action = [
        'logs:CreateLogStream',
        'logs:PutLogEvents',
    ]
    resource_arn = Sub('arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:${ADConnectorLambdaLogsLogGroup}:log-stream:*')


class ADConnectorLambdaRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [ADConnectorLambdaRoleAllowStatement0_1, ADConnectorLambdaRoleAllowStatement1]


class ADConnectorLambdaRolePolicy:
    resource: iam.Role.Policy
    policy_name = 'CloudWatchLogGroup'
    policy_document = ADConnectorLambdaRolePolicies0PolicyDocument


class ADConnectorLambdaRoleAllowStatement0_2:
    resource: PolicyStatement
    sid = 'Directory'
    action = [
        'ds:ConnectDirectory',
        'ds:DeleteDirectory',
    ]
    resource_arn = '*'


class ADConnectorLambdaRoleAllowStatement1_1:
    resource: PolicyStatement
    sid = 'CreateAdConnectorEc2Resources'
    action = [
        'ec2:DescribeSubnets',
        'ec2:DescribeVpcs',
        'ec2:CreateSecurityGroup',
        'ec2:CreateNetworkInterface',
        'ec2:DescribeNetworkInterfaces',
        'ec2:AuthorizeSecurityGroupIngress',
        'ec2:AuthorizeSecurityGroupEgress',
        'ec2:CreateTags',
    ]
    resource_arn = '*'
    condition = {
        BOOL: {
            'aws:ViaAWSService': True,
        },
    }


class ADConnectorLambdaRoleAllowStatement2:
    resource: PolicyStatement
    sid = 'DeleteAdConnectorEc2Resources'
    action = [
        'ec2:DeleteSecurityGroup',
        'ec2:DescribeNetworkInterfaces',
        'ec2:DeleteNetworkInterface',
        'ec2:RevokeSecurityGroupIngress',
        'ec2:RevokeSecurityGroupEgress',
        'ec2:DeleteTags',
    ]
    resource_arn = '*'
    condition = {
        BOOL: {
            'aws:ViaAWSService': True,
        },
    }


class ADConnectorLambdaRolePolicies1PolicyDocument:
    resource: PolicyDocument
    statement = [ADConnectorLambdaRoleAllowStatement0_2, ADConnectorLambdaRoleAllowStatement1_1, ADConnectorLambdaRoleAllowStatement2]


class ADConnectorLambdaRolePolicy1:
    resource: iam.Role.Policy
    policy_name = 'ADConnector'
    policy_document = ADConnectorLambdaRolePolicies1PolicyDocument


class ADConnectorLambdaRoleAllowStatement0_3:
    resource: PolicyStatement
    sid = 'GetSecret'
    action = 'secretsmanager:GetSecretValue'
    resource_arn = ADConnectorServiceAccountSecret


class ADConnectorLambdaRolePolicies2PolicyDocument:
    resource: PolicyDocument
    statement = [ADConnectorLambdaRoleAllowStatement0_3]


class ADConnectorLambdaRolePolicy2:
    resource: iam.Role.Policy
    policy_name = 'ADConnectorServiceAccountSecret'
    policy_document = ADConnectorLambdaRolePolicies2PolicyDocument


class ADConnectorLambdaRole:
    resource: iam.Role
    role_name = Sub('${LambdaFunctionName}-LambdaRole')
    description = 'Rights to Setup AD Connector'
    assume_role_policy_document = ADConnectorLambdaRoleAssumeRolePolicyDocument
    path = '/'
    tags = [{
        'Key': 'StackName',
        'Value': AWS_STACK_NAME,
    }]
    policies = [ADConnectorLambdaRolePolicy, ADConnectorLambdaRolePolicy1, ADConnectorLambdaRolePolicy2, If("SecretsManagerDomainCredentialsSecretsKMSKeyCondition", {
    'PolicyName': 'KMSKeyForSecret',
    'PolicyDocument': {
        'Version': '2012-10-17',
        'Statement': [{
            'Effect': 'Allow',
            'Action': 'kms:Decrypt',
            'Resource': SecretsManagerDomainCredentialsSecretsKMSKey,
        }],
    },
}, AWS_NO_VALUE)]


class ADConnectorLinuxEC2SeamlessDomainJoinSecret:
    resource: secretsmanager.Secret
    name = Sub('aws/directory-services/${ADConnectorResource}/seamless-domain-join')
    description = Sub('AD Credentials for Seamless Domain Join Windows/Linux EC2 instances to ${DomainNetBiosName} Domain via AD Connector')
    secret_string = Sub('{ "awsSeamlessDomainUsername" : "${DomainJoinUser}", "awsSeamlessDomainPassword" : "${DomainJoinUserPassword}" }')
    kms_key_id = If("SecretsManagerDomainCredentialsSecretsKMSKeyCondition", SecretsManagerDomainCredentialsSecretsKMSKey, AWS_NO_VALUE)
    condition = 'LinuxEC2DomainJoinResourcesCondition'
    deletion_policy = 'Retain'


class ADConnectorLinuxEC2DomainJoinRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = 'sts:AssumeRole'


class ADConnectorLinuxEC2DomainJoinRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ADConnectorLinuxEC2DomainJoinRoleAllowStatement0]


class ADConnectorLinuxEC2DomainJoinRoleAllowStatement0_1:
    resource: PolicyStatement
    action = 's3:GetObject'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::aws-ssm-${AWS::Region}/*'),
        Sub('arn:${AWS::Partition}:s3:::aws-windows-downloads-${AWS::Region}/*'),
        Sub('arn:${AWS::Partition}:s3:::amazon-ssm-${AWS::Region}/*'),
        Sub('arn:${AWS::Partition}:s3:::amazon-ssm-packages-${AWS::Region}/*'),
        Sub('arn:${AWS::Partition}:s3:::${AWS::Region}-birdwatcher-prod/*'),
        Sub('arn:${AWS::Partition}:s3:::patch-baseline-snapshot-${AWS::Region}/*'),
        Sub('arn:${AWS::Partition}:s3:::aws-ssm-distributor-file-${AWS::Region}/*'),
        Sub('arn:${AWS::Partition}:s3:::aws-ssm-document-attachments-${AWS::Region}/*'),
    ]


class ADConnectorLinuxEC2DomainJoinRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [ADConnectorLinuxEC2DomainJoinRoleAllowStatement0_1]


class ADConnectorLinuxEC2DomainJoinRolePolicy:
    resource: iam.Role.Policy
    policy_name = 'SSMAgent'
    policy_document = ADConnectorLinuxEC2DomainJoinRolePolicies0PolicyDocument


class ADConnectorLinuxEC2DomainJoinRoleAllowStatement0_2:
    resource: PolicyStatement
    action = [
        'secretsmanager:GetSecretValue',
        'secretsmanager:DescribeSecret',
    ]
    resource_arn = ADConnectorLinuxEC2SeamlessDomainJoinSecret


class ADConnectorLinuxEC2DomainJoinRolePolicies2PolicyDocument:
    resource: PolicyDocument
    statement = [ADConnectorLinuxEC2DomainJoinRoleAllowStatement0_2]


class ADConnectorLinuxEC2DomainJoinRolePolicy1:
    resource: iam.Role.Policy
    policy_name = 'ADConnectorLinuxEC2SeamlessDomainJoinSecret'
    policy_document = ADConnectorLinuxEC2DomainJoinRolePolicies2PolicyDocument


class ADConnectorLinuxEC2DomainJoinRole:
    resource: iam.Role
    role_name = Sub('${DomainNetBiosName}-LinuxEC2DomainJoinRole-ADConnector')
    description = Sub('IAM Role to Seamlessly Join Linux EC2 Instances to ${DomainNetBiosName} Domain via AD Connector')
    assume_role_policy_document = ADConnectorLinuxEC2DomainJoinRoleAssumeRolePolicyDocument
    managed_policy_arns = [Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonSSMManagedInstanceCore'), Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonSSMDirectoryServiceAccess')]
    path = '/'
    tags = [{
        'Key': 'StackName',
        'Value': AWS_STACK_NAME,
    }]
    policies = [ADConnectorLinuxEC2DomainJoinRolePolicy, If("SSMLogsBucketNameCondition", {
    'PolicyName': 'SsmLogs',
    'PolicyDocument': {
        'Version': '2012-10-17',
        'Statement': [{
            'Effect': 'Allow',
            'Action': [
                's3:GetObject',
                's3:PutObject',
                's3:PutObjectAcl',
                's3:GetEncryptionConfiguration',
            ],
            'Resource': [
                Sub('arn:${AWS::Partition}:s3:::${SSMLogsBucketName}'),
                Sub('arn:${AWS::Partition}:s3:::${SSMLogsBucketName}/*'),
            ],
        }],
    },
}, AWS_NO_VALUE), ADConnectorLinuxEC2DomainJoinRolePolicy1, If("SecretsManagerDomainCredentialsSecretsKMSKeyCondition", {
    'PolicyName': 'KMSKeyForSecret',
    'PolicyDocument': {
        'Version': '2012-10-17',
        'Statement': [{
            'Effect': 'Allow',
            'Action': 'kms:Decrypt',
            'Resource': SecretsManagerDomainCredentialsSecretsKMSKey,
        }],
    },
}, AWS_NO_VALUE)]
    condition = 'LinuxEC2DomainJoinResourcesCondition'


class ADConnectorLinuxEC2DomainJoinInstanceProfile:
    resource: iam.InstanceProfile
    instance_profile_name = ADConnectorLinuxEC2DomainJoinRole
    path = '/'
    roles = [ADConnectorLinuxEC2DomainJoinRole]
    condition = 'LinuxEC2DomainJoinResourcesCondition'


class ADConnectorWindowsEC2DomainJoinRoleAllowStatement0:
    resource: PolicyStatement
    principal = {
        'Service': ['ec2.amazonaws.com'],
    }
    action = 'sts:AssumeRole'


class ADConnectorWindowsEC2DomainJoinRoleAssumeRolePolicyDocument:
    resource: PolicyDocument
    statement = [ADConnectorWindowsEC2DomainJoinRoleAllowStatement0]


class ADConnectorWindowsEC2DomainJoinRoleAllowStatement0_1:
    resource: PolicyStatement
    action = 's3:GetObject'
    resource_arn = [
        Sub('arn:${AWS::Partition}:s3:::aws-ssm-${AWS::Region}/*'),
        Sub('arn:${AWS::Partition}:s3:::aws-windows-downloads-${AWS::Region}/*'),
        Sub('arn:${AWS::Partition}:s3:::amazon-ssm-${AWS::Region}/*'),
        Sub('arn:${AWS::Partition}:s3:::amazon-ssm-packages-${AWS::Region}/*'),
        Sub('arn:${AWS::Partition}:s3:::${AWS::Region}-birdwatcher-prod/*'),
        Sub('arn:${AWS::Partition}:s3:::patch-baseline-snapshot-${AWS::Region}/*'),
        Sub('arn:${AWS::Partition}:s3:::aws-ssm-distributor-file-${AWS::Region}/*'),
        Sub('arn:${AWS::Partition}:s3:::aws-ssm-document-attachments-${AWS::Region}/*'),
    ]


class ADConnectorWindowsEC2DomainJoinRolePolicies0PolicyDocument:
    resource: PolicyDocument
    statement = [ADConnectorWindowsEC2DomainJoinRoleAllowStatement0_1]


class ADConnectorWindowsEC2DomainJoinRolePolicy:
    resource: iam.Role.Policy
    policy_name = 'SSMAgent'
    policy_document = ADConnectorWindowsEC2DomainJoinRolePolicies0PolicyDocument


class ADConnectorWindowsEC2DomainJoinRole:
    resource: iam.Role
    role_name = Sub('${DomainNetBiosName}-ADConnector-WindowsEC2DomainJoinRole')
    description = Sub('IAM Role to Seamlessly Join Windows EC2 Instances to ${DomainDNSName} Domain via AD Connector')
    assume_role_policy_document = ADConnectorWindowsEC2DomainJoinRoleAssumeRolePolicyDocument
    managed_policy_arns = [Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonSSMManagedInstanceCore'), Sub('arn:${AWS::Partition}:iam::aws:policy/AmazonSSMDirectoryServiceAccess')]
    path = '/'
    tags = [{
        'Key': 'StackName',
        'Value': AWS_STACK_NAME,
    }]
    policies = [ADConnectorWindowsEC2DomainJoinRolePolicy, If("SSMLogsBucketNameCondition", {
    'PolicyName': 'SsmLogs',
    'PolicyDocument': {
        'Version': '2012-10-17',
        'Statement': [{
            'Effect': 'Allow',
            'Action': [
                's3:GetObject',
                's3:PutObject',
                's3:PutObjectAcl',
                's3:GetEncryptionConfiguration',
            ],
            'Resource': [
                Sub('arn:${AWS::Partition}:s3:::${SSMLogsBucketName}'),
                Sub('arn:${AWS::Partition}:s3:::${SSMLogsBucketName}/*'),
            ],
        }],
    },
}, AWS_NO_VALUE)]
    condition = 'WindowsEC2DomainJoinResourcesCondition'


class ADConnectorWindowsEC2DomainJoinInstanceProfile:
    resource: iam.InstanceProfile
    instance_profile_name = ADConnectorWindowsEC2DomainJoinRole
    path = '/'
    roles = [ADConnectorWindowsEC2DomainJoinRole]
    condition = 'WindowsEC2DomainJoinResourcesCondition'
