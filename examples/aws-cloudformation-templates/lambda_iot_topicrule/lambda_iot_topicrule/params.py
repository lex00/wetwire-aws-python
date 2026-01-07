"""Parameters, Mappings, and Conditions."""

from . import *  # noqa: F403


class CertificateARN(Parameter):
    """The Amazon Resource Name (ARN) of an existing AWS IoT certificate aws iot create-keys-and-certificate --set-as-active --certificate-pem-outfile certificate.pem.crt --private-key-outfile private.pem.key"""

    type = STRING
    description = 'The Amazon Resource Name (ARN) of an existing AWS IoT certificate aws iot create-keys-and-certificate --set-as-active --certificate-pem-outfile certificate.pem.crt --private-key-outfile private.pem.key'
