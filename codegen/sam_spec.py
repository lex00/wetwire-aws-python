"""
SAM (Serverless Application Model) resource specifications.

This module provides static definitions for AWS SAM resource types,
which are not included in the official CloudFormation spec.

Reference: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/
"""

from __future__ import annotations

# SAM-specific enum values
SAM_ENUMS: dict[str, list[str]] = {
    "Runtime": [
        # Python runtimes
        "python3.9",
        "python3.10",
        "python3.11",
        "python3.12",
        "python3.13",
        # Node.js runtimes
        "nodejs18.x",
        "nodejs20.x",
        "nodejs22.x",
        # Java runtimes
        "java11",
        "java17",
        "java21",
        # .NET runtimes
        "dotnet6",
        "dotnet8",
        # Go runtime
        "go1.x",
        # Ruby runtimes
        "ruby3.2",
        "ruby3.3",
        # Provided runtimes (custom)
        "provided",
        "provided.al2",
        "provided.al2023",
    ],
    "Architecture": [
        "x86_64",
        "arm64",
    ],
    "PackageType": [
        "Zip",
        "Image",
    ],
    "AuthType": [
        "NONE",
        "AWS_IAM",
        "COGNITO_USER_POOLS",
    ],
    "HttpApiAuthType": [
        "NONE",
        "AWS_IAM",
        "JWT",
    ],
}


# SAM Resource Type definitions
# Format mirrors CloudFormation spec structure for compatibility with parse.py
SAM_RESOURCES: dict[str, dict] = {
    "AWS::Serverless::Function": {
        "Documentation": "https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html",
        "Properties": {
            "FunctionName": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "A name for the function.",
            },
            "Handler": {
                "PrimitiveType": "String",
                "Required": False,  # Not required for Image package type
                "Documentation": "Function within your code that is called to begin execution.",
            },
            "Runtime": {
                "PrimitiveType": "String",
                "Required": False,  # Not required for Image package type
                "Documentation": "The runtime environment for the Lambda function.",
            },
            "CodeUri": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "S3 URI, local file path, or FunctionCode object of the function code.",
            },
            "ImageUri": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "URI of a container image in ECR for Image package type.",
            },
            "Description": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "A description of the function.",
            },
            "MemorySize": {
                "PrimitiveType": "Integer",
                "Required": False,
                "Documentation": "The amount of memory available to the function during execution.",
            },
            "Timeout": {
                "PrimitiveType": "Integer",
                "Required": False,
                "Documentation": "Function execution time in seconds before Lambda terminates it.",
            },
            "Role": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "ARN of an IAM role to use for this function.",
            },
            "Policies": {
                "Type": "List",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "Policies to attach to the function's execution role.",
            },
            "Environment": {
                "Type": "Environment",
                "Required": False,
                "Documentation": "Environment variables for the function.",
            },
            "Events": {
                "Type": "Map",
                "ItemType": "EventSource",
                "Required": False,
                "Documentation": "Event sources that trigger the function.",
            },
            "Tags": {
                "Type": "Map",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "Tags to apply to the function.",
            },
            "Tracing": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "X-Ray tracing mode (Active or PassThrough).",
            },
            "Layers": {
                "Type": "List",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "List of LayerVersion ARNs to add to the function.",
            },
            "Architectures": {
                "Type": "List",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "The instruction set architecture (x86_64 or arm64).",
            },
            "PackageType": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Lambda deployment package type (Zip or Image).",
            },
            "VpcConfig": {
                "Type": "VpcConfig",
                "Required": False,
                "Documentation": "VPC configuration for the function.",
            },
            "DeadLetterQueue": {
                "Type": "DeadLetterQueue",
                "Required": False,
                "Documentation": "Dead letter queue configuration.",
            },
            "ReservedConcurrentExecutions": {
                "PrimitiveType": "Integer",
                "Required": False,
                "Documentation": "Maximum concurrent executions for the function.",
            },
            "ProvisionedConcurrencyConfig": {
                "Type": "ProvisionedConcurrencyConfig",
                "Required": False,
                "Documentation": "Provisioned concurrency configuration.",
            },
            "AssumeRolePolicyDocument": {
                "PrimitiveType": "Json",
                "Required": False,
                "Documentation": "Custom assume role policy document for the role.",
            },
            "AutoPublishAlias": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Alias name for automatic publishing.",
            },
            "EphemeralStorage": {
                "Type": "EphemeralStorage",
                "Required": False,
                "Documentation": "Size of the /tmp directory in MB.",
            },
            "FunctionUrlConfig": {
                "Type": "FunctionUrlConfig",
                "Required": False,
                "Documentation": "Function URL configuration.",
            },
            "SnapStart": {
                "Type": "SnapStart",
                "Required": False,
                "Documentation": "SnapStart configuration for the function.",
            },
            "LoggingConfig": {
                "Type": "LoggingConfig",
                "Required": False,
                "Documentation": "Logging configuration for the function.",
            },
        },
        "Attributes": {
            "Arn": {"PrimitiveType": "String"},
        },
    },
    "AWS::Serverless::Api": {
        "Documentation": "https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-api.html",
        "Properties": {
            "Name": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "A name for the API Gateway RestApi resource.",
            },
            "StageName": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "The name of the stage.",
            },
            "DefinitionUri": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "S3 URI or local path to an OpenAPI document.",
            },
            "DefinitionBody": {
                "PrimitiveType": "Json",
                "Required": False,
                "Documentation": "OpenAPI specification as inline JSON.",
            },
            "Description": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Description of the API.",
            },
            "Auth": {
                "Type": "ApiAuth",
                "Required": False,
                "Documentation": "Auth configuration for the API.",
            },
            "Cors": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "CORS configuration. Can be string or CorsConfiguration.",
            },
            "EndpointConfiguration": {
                "Type": "EndpointConfiguration",
                "Required": False,
                "Documentation": "Endpoint type configuration.",
            },
            "Tags": {
                "Type": "Map",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "Tags to apply to the API.",
            },
            "TracingEnabled": {
                "PrimitiveType": "Boolean",
                "Required": False,
                "Documentation": "Enable X-Ray tracing.",
            },
            "CacheClusterEnabled": {
                "PrimitiveType": "Boolean",
                "Required": False,
                "Documentation": "Enable API caching.",
            },
            "CacheClusterSize": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Cache cluster size.",
            },
            "Variables": {
                "Type": "Map",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "Stage variables.",
            },
            "BinaryMediaTypes": {
                "Type": "List",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "List of binary media types.",
            },
            "MethodSettings": {
                "Type": "List",
                "ItemType": "MethodSetting",
                "Required": False,
                "Documentation": "Method settings for the API stage.",
            },
            "OpenApiVersion": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "OpenAPI version (e.g., '3.0.1').",
            },
            "GatewayResponses": {
                "Type": "Map",
                "ItemType": "GatewayResponse",
                "Required": False,
                "Documentation": "Gateway response configurations.",
            },
            "AccessLogSetting": {
                "Type": "AccessLogSetting",
                "Required": False,
                "Documentation": "Access log settings for the stage.",
            },
            "CanarySetting": {
                "Type": "CanarySetting",
                "Required": False,
                "Documentation": "Canary deployment settings.",
            },
            "Domain": {
                "Type": "DomainConfiguration",
                "Required": False,
                "Documentation": "Custom domain configuration.",
            },
        },
        "Attributes": {
            "RootResourceId": {"PrimitiveType": "String"},
        },
    },
    "AWS::Serverless::HttpApi": {
        "Documentation": "https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-httpapi.html",
        "Properties": {
            "StageName": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "The name of the API stage.",
            },
            "DefinitionUri": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "S3 URI or local path to an OpenAPI document.",
            },
            "DefinitionBody": {
                "PrimitiveType": "Json",
                "Required": False,
                "Documentation": "OpenAPI specification as inline JSON.",
            },
            "Description": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Description of the HTTP API.",
            },
            "Auth": {
                "Type": "HttpApiAuth",
                "Required": False,
                "Documentation": "Auth configuration for the HTTP API.",
            },
            "CorsConfiguration": {
                "Type": "CorsConfiguration",
                "Required": False,
                "Documentation": "CORS configuration.",
            },
            "Tags": {
                "Type": "Map",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "Tags to apply to the HTTP API.",
            },
            "DefaultRouteSettings": {
                "Type": "RouteSettings",
                "Required": False,
                "Documentation": "Default route settings.",
            },
            "RouteSettings": {
                "Type": "Map",
                "ItemType": "RouteSettings",
                "Required": False,
                "Documentation": "Route-specific settings.",
            },
            "StageVariables": {
                "Type": "Map",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "Stage variables.",
            },
            "FailOnWarnings": {
                "PrimitiveType": "Boolean",
                "Required": False,
                "Documentation": "Fail deployment on warnings.",
            },
            "AccessLogSettings": {
                "Type": "AccessLogSettings",
                "Required": False,
                "Documentation": "Access logging settings.",
            },
            "Domain": {
                "Type": "HttpApiDomainConfiguration",
                "Required": False,
                "Documentation": "Custom domain configuration.",
            },
            "DisableExecuteApiEndpoint": {
                "PrimitiveType": "Boolean",
                "Required": False,
                "Documentation": "Disable the default endpoint.",
            },
        },
        "Attributes": {
            "ApiEndpoint": {"PrimitiveType": "String"},
        },
    },
    "AWS::Serverless::SimpleTable": {
        "Documentation": "https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-simpletable.html",
        "Properties": {
            "TableName": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Name of the DynamoDB table.",
            },
            "PrimaryKey": {
                "Type": "PrimaryKey",
                "Required": False,
                "Documentation": "Primary key configuration.",
            },
            "ProvisionedThroughput": {
                "Type": "ProvisionedThroughput",
                "Required": False,
                "Documentation": "Provisioned throughput settings.",
            },
            "Tags": {
                "Type": "Map",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "Tags to apply to the table.",
            },
            "SSESpecification": {
                "Type": "SSESpecification",
                "Required": False,
                "Documentation": "Server-side encryption specification.",
            },
        },
        "Attributes": {
            "Arn": {"PrimitiveType": "String"},
        },
    },
    "AWS::Serverless::LayerVersion": {
        "Documentation": "https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-layerversion.html",
        "Properties": {
            "LayerName": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Name of the layer.",
            },
            "Description": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Description of the layer.",
            },
            "ContentUri": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "S3 URI or local path to the layer content.",
            },
            "CompatibleRuntimes": {
                "Type": "List",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "List of compatible runtimes.",
            },
            "CompatibleArchitectures": {
                "Type": "List",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "List of compatible architectures.",
            },
            "LicenseInfo": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "License information for the layer.",
            },
            "RetentionPolicy": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Retention policy (Retain or Delete).",
            },
        },
        "Attributes": {
            "Arn": {"PrimitiveType": "String"},
            "LayerVersionArn": {"PrimitiveType": "String"},
        },
    },
    "AWS::Serverless::StateMachine": {
        "Documentation": "https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-statemachine.html",
        "Properties": {
            "Name": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Name of the state machine.",
            },
            "Definition": {
                "PrimitiveType": "Json",
                "Required": False,
                "Documentation": "State machine definition as JSON.",
            },
            "DefinitionUri": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "S3 URI or local path to definition file.",
            },
            "DefinitionSubstitutions": {
                "Type": "Map",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "Substitutions for the definition.",
            },
            "Role": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "IAM role ARN for the state machine.",
            },
            "Policies": {
                "Type": "List",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "Policies to attach to the execution role.",
            },
            "Events": {
                "Type": "Map",
                "ItemType": "StateMachineEvent",
                "Required": False,
                "Documentation": "Event sources that trigger the state machine.",
            },
            "Tags": {
                "Type": "Map",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "Tags to apply to the state machine.",
            },
            "Type": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "State machine type (STANDARD or EXPRESS).",
            },
            "Tracing": {
                "Type": "TracingConfiguration",
                "Required": False,
                "Documentation": "X-Ray tracing configuration.",
            },
            "Logging": {
                "Type": "LoggingConfiguration",
                "Required": False,
                "Documentation": "CloudWatch Logs configuration.",
            },
        },
        "Attributes": {
            "Arn": {"PrimitiveType": "String"},
            "Name": {"PrimitiveType": "String"},
        },
    },
    "AWS::Serverless::Application": {
        "Documentation": "https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-application.html",
        "Properties": {
            "Location": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "SAR application ID or S3 URI.",
            },
            "Parameters": {
                "Type": "Map",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "Application parameters.",
            },
            "Tags": {
                "Type": "Map",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "Tags to apply to the application.",
            },
            "NotificationArns": {
                "Type": "List",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "SNS topic ARNs for stack notifications.",
            },
            "TimeoutInMinutes": {
                "PrimitiveType": "Integer",
                "Required": False,
                "Documentation": "Timeout for stack creation in minutes.",
            },
        },
        "Attributes": {
            "Outputs": {"PrimitiveType": "Json"},
        },
    },
    "AWS::Serverless::Connector": {
        "Documentation": "https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-connector.html",
        "Properties": {
            "Source": {
                "Type": "ConnectorSource",
                "Required": True,
                "Documentation": "The source resource.",
            },
            "Destination": {
                "Type": "ConnectorDestination",
                "Required": True,
                "Documentation": "The destination resource.",
            },
            "Permissions": {
                "Type": "List",
                "PrimitiveItemType": "String",
                "Required": True,
                "Documentation": "Permissions to grant (Read, Write).",
            },
        },
        "Attributes": {},
    },
    "AWS::Serverless::GraphQLApi": {
        "Documentation": "https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-graphqlapi.html",
        "Properties": {
            "Name": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Name of the GraphQL API.",
            },
            "SchemaUri": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "S3 URI or local path to the GraphQL schema.",
            },
            "SchemaInline": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Inline GraphQL schema definition.",
            },
            "Auth": {
                "Type": "GraphQLAuth",
                "Required": True,
                "Documentation": "Authentication configuration.",
            },
            "Functions": {
                "Type": "Map",
                "ItemType": "GraphQLFunction",
                "Required": False,
                "Documentation": "AppSync function configurations.",
            },
            "Resolvers": {
                "Type": "Map",
                "ItemType": "GraphQLResolver",
                "Required": False,
                "Documentation": "GraphQL resolver configurations.",
            },
            "DataSources": {
                "Type": "Map",
                "ItemType": "GraphQLDataSource",
                "Required": False,
                "Documentation": "Data source configurations.",
            },
            "Tags": {
                "Type": "Map",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "Tags to apply to the GraphQL API.",
            },
            "XrayEnabled": {
                "PrimitiveType": "Boolean",
                "Required": False,
                "Documentation": "Enable X-Ray tracing.",
            },
            "Logging": {
                "Type": "GraphQLLogging",
                "Required": False,
                "Documentation": "CloudWatch Logs configuration.",
            },
            "Cache": {
                "Type": "GraphQLCache",
                "Required": False,
                "Documentation": "API caching configuration.",
            },
            "DomainName": {
                "Type": "GraphQLDomainName",
                "Required": False,
                "Documentation": "Custom domain name configuration.",
            },
        },
        "Attributes": {
            "ApiId": {"PrimitiveType": "String"},
            "Arn": {"PrimitiveType": "String"},
            "GraphQLDns": {"PrimitiveType": "String"},
            "GraphQLUrl": {"PrimitiveType": "String"},
            "RealtimeDns": {"PrimitiveType": "String"},
            "RealtimeUrl": {"PrimitiveType": "String"},
        },
    },
}


# SAM Property Types (nested structures)
SAM_PROPERTY_TYPES: dict[str, dict] = {
    # Function event types
    "AWS::Serverless::Function.ApiEvent": {
        "Documentation": "API Gateway event source for a function.",
        "Properties": {
            "Path": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "The URI path for the API endpoint.",
            },
            "Method": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "The HTTP method (GET, POST, etc.).",
            },
            "RestApiId": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Reference to an AWS::Serverless::Api resource.",
            },
            "Auth": {
                "Type": "ApiEventAuth",
                "Required": False,
                "Documentation": "Auth configuration for this endpoint.",
            },
        },
    },
    "AWS::Serverless::Function.S3Event": {
        "Documentation": "S3 event source for a function.",
        "Properties": {
            "Bucket": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "S3 bucket ARN or reference.",
            },
            "Events": {
                "Type": "List",
                "PrimitiveItemType": "String",
                "Required": True,
                "Documentation": "S3 event types to trigger on.",
            },
            "Filter": {
                "Type": "S3NotificationFilter",
                "Required": False,
                "Documentation": "Filter rules for S3 events.",
            },
        },
    },
    "AWS::Serverless::Function.SQSEvent": {
        "Documentation": "SQS event source for a function.",
        "Properties": {
            "Queue": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "SQS queue ARN or reference.",
            },
            "BatchSize": {
                "PrimitiveType": "Integer",
                "Required": False,
                "Documentation": "Maximum number of messages per batch.",
            },
            "Enabled": {
                "PrimitiveType": "Boolean",
                "Required": False,
                "Documentation": "Whether the event source is enabled.",
            },
            "MaximumBatchingWindowInSeconds": {
                "PrimitiveType": "Integer",
                "Required": False,
                "Documentation": "Maximum batching window in seconds.",
            },
        },
    },
    "AWS::Serverless::Function.SNSEvent": {
        "Documentation": "SNS event source for a function.",
        "Properties": {
            "Topic": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "SNS topic ARN.",
            },
            "FilterPolicy": {
                "PrimitiveType": "Json",
                "Required": False,
                "Documentation": "SNS filter policy.",
            },
            "Region": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "AWS region for cross-region subscriptions.",
            },
        },
    },
    "AWS::Serverless::Function.KinesisEvent": {
        "Documentation": "Kinesis event source for a function.",
        "Properties": {
            "Stream": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "Kinesis stream ARN.",
            },
            "StartingPosition": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "Starting position (TRIM_HORIZON, LATEST, AT_TIMESTAMP).",
            },
            "BatchSize": {
                "PrimitiveType": "Integer",
                "Required": False,
                "Documentation": "Maximum number of records per batch.",
            },
            "Enabled": {
                "PrimitiveType": "Boolean",
                "Required": False,
                "Documentation": "Whether the event source is enabled.",
            },
        },
    },
    "AWS::Serverless::Function.DynamoDBEvent": {
        "Documentation": "DynamoDB Streams event source for a function.",
        "Properties": {
            "Stream": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "DynamoDB stream ARN.",
            },
            "StartingPosition": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "Starting position (TRIM_HORIZON, LATEST).",
            },
            "BatchSize": {
                "PrimitiveType": "Integer",
                "Required": False,
                "Documentation": "Maximum number of records per batch.",
            },
            "Enabled": {
                "PrimitiveType": "Boolean",
                "Required": False,
                "Documentation": "Whether the event source is enabled.",
            },
        },
    },
    "AWS::Serverless::Function.ScheduleEvent": {
        "Documentation": "CloudWatch Events schedule for a function.",
        "Properties": {
            "Schedule": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "Schedule expression (rate or cron).",
            },
            "Name": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Name for the rule.",
            },
            "Description": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Description of the rule.",
            },
            "Input": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "JSON input to pass to the function.",
            },
            "Enabled": {
                "PrimitiveType": "Boolean",
                "Required": False,
                "Documentation": "Whether the rule is enabled.",
            },
        },
    },
    "AWS::Serverless::Function.CloudWatchEvent": {
        "Documentation": "CloudWatch Events/EventBridge event source.",
        "Properties": {
            "Pattern": {
                "PrimitiveType": "Json",
                "Required": True,
                "Documentation": "Event pattern to match.",
            },
            "EventBusName": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Name of the event bus.",
            },
            "Input": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "JSON input to pass to the function.",
            },
        },
    },
    "AWS::Serverless::Function.HttpApiEvent": {
        "Documentation": "HTTP API event source for a function.",
        "Properties": {
            "Path": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "The URI path for the HTTP API endpoint.",
            },
            "Method": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "The HTTP method (GET, POST, etc.).",
            },
            "ApiId": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Reference to an AWS::Serverless::HttpApi resource.",
            },
            "Auth": {
                "Type": "HttpApiEventAuth",
                "Required": False,
                "Documentation": "Auth configuration for this endpoint.",
            },
            "PayloadFormatVersion": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Payload format version (1.0 or 2.0).",
            },
        },
    },
    "AWS::Serverless::Function.CognitoEvent": {
        "Documentation": "Cognito User Pool trigger event.",
        "Properties": {
            "UserPool": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "Cognito User Pool ARN or reference.",
            },
            "Trigger": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "The trigger type (PreSignUp, PostConfirmation, etc.).",
            },
        },
    },
    "AWS::Serverless::Function.EventBridgeRuleEvent": {
        "Documentation": "EventBridge rule event source.",
        "Properties": {
            "Pattern": {
                "PrimitiveType": "Json",
                "Required": True,
                "Documentation": "Event pattern to match.",
            },
            "EventBusName": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Name of the event bus.",
            },
            "Input": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "JSON input to pass to the function.",
            },
            "InputPath": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "JSON path to use as input.",
            },
            "DeadLetterConfig": {
                "Type": "DeadLetterConfig",
                "Required": False,
                "Documentation": "Dead letter queue configuration.",
            },
            "RetryPolicy": {
                "Type": "RetryPolicy",
                "Required": False,
                "Documentation": "Retry policy configuration.",
            },
        },
    },
    # Function property types
    "AWS::Serverless::Function.Environment": {
        "Documentation": "Environment variable configuration.",
        "Properties": {
            "Variables": {
                "Type": "Map",
                "PrimitiveItemType": "String",
                "Required": True,
                "Documentation": "Environment variables as key-value pairs.",
            },
        },
    },
    "AWS::Serverless::Function.VpcConfig": {
        "Documentation": "VPC configuration for the function.",
        "Properties": {
            "SecurityGroupIds": {
                "Type": "List",
                "PrimitiveItemType": "String",
                "Required": True,
                "Documentation": "List of security group IDs.",
            },
            "SubnetIds": {
                "Type": "List",
                "PrimitiveItemType": "String",
                "Required": True,
                "Documentation": "List of subnet IDs.",
            },
        },
    },
    "AWS::Serverless::Function.DeadLetterQueue": {
        "Documentation": "Dead letter queue configuration.",
        "Properties": {
            "Type": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "Type of DLQ (SQS or SNS).",
            },
            "TargetArn": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "ARN of the DLQ.",
            },
        },
    },
    "AWS::Serverless::Function.ProvisionedConcurrencyConfig": {
        "Documentation": "Provisioned concurrency configuration.",
        "Properties": {
            "ProvisionedConcurrentExecutions": {
                "PrimitiveType": "Integer",
                "Required": True,
                "Documentation": "Number of provisioned concurrent executions.",
            },
        },
    },
    "AWS::Serverless::Function.EphemeralStorage": {
        "Documentation": "Ephemeral storage configuration.",
        "Properties": {
            "Size": {
                "PrimitiveType": "Integer",
                "Required": True,
                "Documentation": "Size of /tmp directory in MB (512-10240).",
            },
        },
    },
    "AWS::Serverless::Function.FunctionUrlConfig": {
        "Documentation": "Function URL configuration.",
        "Properties": {
            "AuthType": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "Auth type (AWS_IAM or NONE).",
            },
            "Cors": {
                "Type": "FunctionUrlCors",
                "Required": False,
                "Documentation": "CORS configuration.",
            },
            "InvokeMode": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Invoke mode (BUFFERED or RESPONSE_STREAM).",
            },
        },
    },
    "AWS::Serverless::Function.SnapStart": {
        "Documentation": "SnapStart configuration.",
        "Properties": {
            "ApplyOn": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "When to apply SnapStart (PublishedVersions or None).",
            },
        },
    },
    "AWS::Serverless::Function.LoggingConfig": {
        "Documentation": "Logging configuration.",
        "Properties": {
            "LogFormat": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Log format (Text or JSON).",
            },
            "ApplicationLogLevel": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Application log level.",
            },
            "SystemLogLevel": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "System log level.",
            },
            "LogGroup": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "CloudWatch log group name.",
            },
        },
    },
    # Api property types
    "AWS::Serverless::Api.ApiAuth": {
        "Documentation": "API auth configuration.",
        "Properties": {
            "DefaultAuthorizer": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Default authorizer for all endpoints.",
            },
            "Authorizers": {
                "Type": "Map",
                "ItemType": "ApiAuthorizer",
                "Required": False,
                "Documentation": "Authorizer definitions.",
            },
            "ApiKeyRequired": {
                "PrimitiveType": "Boolean",
                "Required": False,
                "Documentation": "Whether API key is required.",
            },
        },
    },
    "AWS::Serverless::Api.EndpointConfiguration": {
        "Documentation": "Endpoint configuration.",
        "Properties": {
            "Type": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "Endpoint type (REGIONAL, EDGE, PRIVATE).",
            },
            "VpcEndpointIds": {
                "Type": "List",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "VPC endpoint IDs for PRIVATE endpoints.",
            },
        },
    },
    # SimpleTable property types
    "AWS::Serverless::SimpleTable.PrimaryKey": {
        "Documentation": "Primary key configuration.",
        "Properties": {
            "Name": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "Name of the primary key attribute.",
            },
            "Type": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "Type of the primary key (String, Number, Binary).",
            },
        },
    },
    "AWS::Serverless::SimpleTable.ProvisionedThroughput": {
        "Documentation": "Provisioned throughput settings.",
        "Properties": {
            "ReadCapacityUnits": {
                "PrimitiveType": "Integer",
                "Required": True,
                "Documentation": "Read capacity units.",
            },
            "WriteCapacityUnits": {
                "PrimitiveType": "Integer",
                "Required": True,
                "Documentation": "Write capacity units.",
            },
        },
    },
    "AWS::Serverless::SimpleTable.SSESpecification": {
        "Documentation": "Server-side encryption specification.",
        "Properties": {
            "SSEEnabled": {
                "PrimitiveType": "Boolean",
                "Required": False,
                "Documentation": "Whether server-side encryption is enabled.",
            },
        },
    },
    # Connector property types
    "AWS::Serverless::Connector.ConnectorSource": {
        "Documentation": "Connector source resource.",
        "Properties": {
            "Id": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "Logical ID of the source resource.",
            },
            "Type": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Resource type of the source.",
            },
            "Arn": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "ARN of the source resource.",
            },
            "RoleName": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Role name for the source.",
            },
        },
    },
    "AWS::Serverless::Connector.ConnectorDestination": {
        "Documentation": "Connector destination resource.",
        "Properties": {
            "Id": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Logical ID of the destination resource.",
            },
            "Type": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Resource type of the destination.",
            },
            "Arn": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "ARN of the destination resource.",
            },
        },
    },
    # StateMachine property types
    "AWS::Serverless::StateMachine.TracingConfiguration": {
        "Documentation": "X-Ray tracing configuration.",
        "Properties": {
            "Enabled": {
                "PrimitiveType": "Boolean",
                "Required": False,
                "Documentation": "Whether tracing is enabled.",
            },
        },
    },
    "AWS::Serverless::StateMachine.LoggingConfiguration": {
        "Documentation": "CloudWatch Logs configuration.",
        "Properties": {
            "Level": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Logging level (ALL, ERROR, FATAL, OFF).",
            },
            "IncludeExecutionData": {
                "PrimitiveType": "Boolean",
                "Required": False,
                "Documentation": "Whether to include execution data in logs.",
            },
            "Destinations": {
                "Type": "List",
                "ItemType": "LogDestination",
                "Required": False,
                "Documentation": "Log destinations.",
            },
        },
    },
    # HttpApi property types
    "AWS::Serverless::HttpApi.HttpApiAuth": {
        "Documentation": "HTTP API auth configuration.",
        "Properties": {
            "DefaultAuthorizer": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Default authorizer for all routes.",
            },
            "Authorizers": {
                "Type": "Map",
                "ItemType": "HttpApiAuthorizer",
                "Required": False,
                "Documentation": "Authorizer definitions.",
            },
        },
    },
    "AWS::Serverless::HttpApi.CorsConfiguration": {
        "Documentation": "CORS configuration for HTTP API.",
        "Properties": {
            "AllowOrigins": {
                "Type": "List",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "Allowed origins.",
            },
            "AllowMethods": {
                "Type": "List",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "Allowed HTTP methods.",
            },
            "AllowHeaders": {
                "Type": "List",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "Allowed headers.",
            },
            "ExposeHeaders": {
                "Type": "List",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "Headers to expose.",
            },
            "MaxAge": {
                "PrimitiveType": "Integer",
                "Required": False,
                "Documentation": "Max age for preflight cache.",
            },
            "AllowCredentials": {
                "PrimitiveType": "Boolean",
                "Required": False,
                "Documentation": "Whether credentials are allowed.",
            },
        },
    },
    "AWS::Serverless::HttpApi.RouteSettings": {
        "Documentation": "Route settings for HTTP API.",
        "Properties": {
            "ThrottlingBurstLimit": {
                "PrimitiveType": "Integer",
                "Required": False,
                "Documentation": "Throttling burst limit.",
            },
            "ThrottlingRateLimit": {
                "PrimitiveType": "Double",
                "Required": False,
                "Documentation": "Throttling rate limit.",
            },
        },
    },
    # GraphQLApi property types
    "AWS::Serverless::GraphQLApi.GraphQLAuth": {
        "Documentation": "GraphQL API auth configuration.",
        "Properties": {
            "Type": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "Auth type (API_KEY, AWS_IAM, COGNITO_USER_POOLS, OPENID_CONNECT).",
            },
            "UserPool": {
                "Type": "CognitoUserPoolConfig",
                "Required": False,
                "Documentation": "Cognito User Pool configuration.",
            },
            "OpenIdConnect": {
                "Type": "OpenIdConnectConfig",
                "Required": False,
                "Documentation": "OpenID Connect configuration.",
            },
            "LambdaAuthorizer": {
                "Type": "LambdaAuthorizerConfig",
                "Required": False,
                "Documentation": "Lambda authorizer configuration.",
            },
            "Additional": {
                "Type": "List",
                "ItemType": "AdditionalAuth",
                "Required": False,
                "Documentation": "Additional auth providers.",
            },
        },
    },
    # Additional nested property types referenced by other types
    "AWS::Serverless::Api.ApiAuthorizer": {
        "Documentation": "API Gateway authorizer configuration.",
        "Properties": {
            "AuthorizationScopes": {
                "Type": "List",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "List of authorization scopes.",
            },
            "Identity": {
                "PrimitiveType": "Json",
                "Required": False,
                "Documentation": "Identity source configuration.",
            },
            "FunctionArn": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Lambda authorizer function ARN.",
            },
            "FunctionPayloadType": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Payload type (TOKEN or REQUEST).",
            },
            "UserPoolArn": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Cognito User Pool ARN.",
            },
        },
    },
    "AWS::Serverless::Function.ApiEventAuth": {
        "Documentation": "Auth configuration for API event.",
        "Properties": {
            "Authorizer": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Authorizer name.",
            },
            "AuthorizationScopes": {
                "Type": "List",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "Authorization scopes.",
            },
            "ApiKeyRequired": {
                "PrimitiveType": "Boolean",
                "Required": False,
                "Documentation": "Whether API key is required.",
            },
            "ResourcePolicy": {
                "PrimitiveType": "Json",
                "Required": False,
                "Documentation": "Resource policy for the endpoint.",
            },
        },
    },
    "AWS::Serverless::Function.DeadLetterConfig": {
        "Documentation": "Dead letter queue configuration.",
        "Properties": {
            "Arn": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "ARN of the SQS queue or SNS topic.",
            },
            "Type": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Type of destination (SQS or SNS).",
            },
            "QueueLogicalId": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Logical ID of an SQS queue in the same template.",
            },
        },
    },
    "AWS::Serverless::Function.RetryPolicy": {
        "Documentation": "Retry policy for event source.",
        "Properties": {
            "MaximumEventAgeInSeconds": {
                "PrimitiveType": "Integer",
                "Required": False,
                "Documentation": "Maximum age of event in seconds.",
            },
            "MaximumRetryAttempts": {
                "PrimitiveType": "Integer",
                "Required": False,
                "Documentation": "Maximum retry attempts.",
            },
        },
    },
    "AWS::Serverless::Function.FunctionUrlCors": {
        "Documentation": "CORS configuration for function URL.",
        "Properties": {
            "AllowCredentials": {
                "PrimitiveType": "Boolean",
                "Required": False,
                "Documentation": "Whether credentials are allowed.",
            },
            "AllowHeaders": {
                "Type": "List",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "Allowed headers.",
            },
            "AllowMethods": {
                "Type": "List",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "Allowed methods.",
            },
            "AllowOrigins": {
                "Type": "List",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "Allowed origins.",
            },
            "ExposeHeaders": {
                "Type": "List",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "Exposed headers.",
            },
            "MaxAge": {
                "PrimitiveType": "Integer",
                "Required": False,
                "Documentation": "Max age for preflight cache.",
            },
        },
    },
    "AWS::Serverless::Function.HttpApiEventAuth": {
        "Documentation": "Auth configuration for HTTP API event.",
        "Properties": {
            "Authorizer": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Authorizer name.",
            },
            "AuthorizationScopes": {
                "Type": "List",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "Authorization scopes.",
            },
        },
    },
    "AWS::Serverless::Function.S3NotificationFilter": {
        "Documentation": "S3 notification filter configuration.",
        "Properties": {
            "S3Key": {
                "PrimitiveType": "Json",
                "Required": False,
                "Documentation": "S3 key filter rules.",
            },
        },
    },
    "AWS::Serverless::GraphQLApi.AdditionalAuth": {
        "Documentation": "Additional auth provider configuration.",
        "Properties": {
            "Type": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "Auth type.",
            },
            "UserPool": {
                "Type": "CognitoUserPoolConfig",
                "Required": False,
                "Documentation": "Cognito User Pool configuration.",
            },
            "OpenIdConnect": {
                "Type": "OpenIdConnectConfig",
                "Required": False,
                "Documentation": "OpenID Connect configuration.",
            },
            "LambdaAuthorizer": {
                "Type": "LambdaAuthorizerConfig",
                "Required": False,
                "Documentation": "Lambda authorizer configuration.",
            },
        },
    },
    "AWS::Serverless::GraphQLApi.LambdaAuthorizerConfig": {
        "Documentation": "Lambda authorizer configuration for GraphQL API.",
        "Properties": {
            "AuthorizerUri": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "Lambda function URI.",
            },
            "AuthorizerResultTtlInSeconds": {
                "PrimitiveType": "Integer",
                "Required": False,
                "Documentation": "TTL for cached authorizer results.",
            },
            "IdentityValidationExpression": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Regex for identity validation.",
            },
        },
    },
    "AWS::Serverless::GraphQLApi.OpenIdConnectConfig": {
        "Documentation": "OpenID Connect configuration.",
        "Properties": {
            "Issuer": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "OIDC issuer URL.",
            },
            "AuthTTL": {
                "PrimitiveType": "Integer",
                "Required": False,
                "Documentation": "Auth token TTL.",
            },
            "ClientId": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "OIDC client ID.",
            },
            "IatTTL": {
                "PrimitiveType": "Integer",
                "Required": False,
                "Documentation": "Issued-at token TTL.",
            },
        },
    },
    "AWS::Serverless::GraphQLApi.CognitoUserPoolConfig": {
        "Documentation": "Cognito User Pool configuration.",
        "Properties": {
            "UserPoolId": {
                "PrimitiveType": "String",
                "Required": True,
                "Documentation": "Cognito User Pool ID.",
            },
            "AwsRegion": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "AWS region for the User Pool.",
            },
            "AppIdClientRegex": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Regex for allowed app client IDs.",
            },
            "DefaultAction": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Default action (ALLOW or DENY).",
            },
        },
    },
    "AWS::Serverless::HttpApi.HttpApiAuthorizer": {
        "Documentation": "HTTP API authorizer configuration.",
        "Properties": {
            "AuthorizationScopes": {
                "Type": "List",
                "PrimitiveItemType": "String",
                "Required": False,
                "Documentation": "Authorization scopes.",
            },
            "IdentitySource": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Identity source expression.",
            },
            "JwtConfiguration": {
                "PrimitiveType": "Json",
                "Required": False,
                "Documentation": "JWT configuration.",
            },
            "FunctionArn": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Lambda authorizer function ARN.",
            },
            "FunctionInvokeRole": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "IAM role for invoking the authorizer.",
            },
            "AuthorizerPayloadFormatVersion": {
                "PrimitiveType": "String",
                "Required": False,
                "Documentation": "Payload format version (1.0 or 2.0).",
            },
            "EnableSimpleResponses": {
                "PrimitiveType": "Boolean",
                "Required": False,
                "Documentation": "Enable simple responses.",
            },
        },
    },
    "AWS::Serverless::StateMachine.LogDestination": {
        "Documentation": "Log destination for state machine.",
        "Properties": {
            "CloudWatchLogsLogGroup": {
                "PrimitiveType": "Json",
                "Required": False,
                "Documentation": "CloudWatch Logs log group configuration.",
            },
        },
    },
}


def get_sam_resources() -> dict[str, dict]:
    """Get SAM resource definitions.

    Returns a copy of SAM_RESOURCES to prevent mutation.
    """
    return SAM_RESOURCES.copy()


def get_sam_property_types() -> dict[str, dict]:
    """Get SAM property type definitions.

    Returns a copy of SAM_PROPERTY_TYPES to prevent mutation.
    """
    return SAM_PROPERTY_TYPES.copy()


def get_sam_enums() -> dict[str, list[str]]:
    """Get SAM enum definitions.

    Returns a copy of SAM_ENUMS to prevent mutation.
    """
    return SAM_ENUMS.copy()
