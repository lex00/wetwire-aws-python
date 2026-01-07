"""Stack resources."""

from . import *  # noqa: F403


class ASCPrivateLinkCertificateDomainValidationOption(certificatemanager.Certificate.DomainValidationOption):
    domain_name = DomainName
    hosted_zone_id = HostedZone


class ASCPrivateLinkCertificate(certificatemanager.Certificate):
    domain_name = DomainName
    validation_method = certificatemanager.ValidationMethod.DNS
    domain_validation_options = [ASCPrivateLinkCertificateDomainValidationOption]


class ASCPrivateLinkEnablePrivateDNS(CloudFormationResource):
    # Unknown resource type: Custom::CustomResource
    service_token = ASCPrivateLinkLambdaFunction.Arn
    action = 'EnablePrivateDNS'
    service_id = ASCPrivateLinkVPCES
    domain_name = DomainName
    hosted_zone_id = HostedZone
    depends_on = [ASCPrivateLinkVPCES]
