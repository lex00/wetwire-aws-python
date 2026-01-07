"""Stack resources."""

from . import *  # noqa: F403


class ASCPrivateLinkCertificate(certificatemanager.Certificate):
    resource: certificatemanager.Certificate
    domain_name = DomainName
    validation_method = certificatemanager.ValidationMethod.DNS


class ASCPrivateLinkEnablePrivateDNS(CloudFormationResource):
    # Unknown resource type: Custom::CustomResource
    resource: CloudFormationResource
    service_token = ASCPrivateLinkLambdaFunction.Arn
    action = 'EnablePrivateDNS'
    service_id = ASCPrivateLinkVPCES
    domain_name = DomainName
    depends_on = [ASCPrivateLinkVPCES]
