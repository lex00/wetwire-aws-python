"""Stack resources."""

from . import *  # noqa: F403


class ASCPrivateLinkCertificateDomainValidationOption:
    resource: certificatemanager.Certificate.DomainValidationOption
    domain_name = DomainName
    hosted_zone_id = HostedZone


class ASCPrivateLinkCertificate:
    resource: certificatemanager.Certificate
    domain_name = DomainName
    validation_method = certificatemanager.ValidationMethod.DNS
    domain_validation_options = [ASCPrivateLinkCertificateDomainValidationOption]


class ASCPrivateLinkEnablePrivateDNS:
    # Unknown resource type: Custom::CustomResource
    resource: CloudFormationResource
    service_token = ASCPrivateLinkLambdaFunction.Arn
    action = 'EnablePrivateDNS'
    service_id = ASCPrivateLinkVPCES
    domain_name = DomainName
    hosted_zone_id = HostedZone
    depends_on = [ASCPrivateLinkVPCES]
