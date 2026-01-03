"""Template outputs."""

from . import *  # noqa: F403


class ServiceCatalogCloudFormationProductNameOutput:
    resource: Output
    value = ServiceCatalogCloudFormationProduct.ProductName
    export_name = Sub('${AppName}-ServiceCatalogCloudFormationProductName')


class ServiceCatalogProvisioningArtifactIdsOutput:
    resource: Output
    value = ServiceCatalogCloudFormationProduct.ProvisioningArtifactIds
    export_name = Sub('${AppName}-ServiceCatalogCloudFormationProvisioningArtifactIds')


class ServiceCatalogProvisioningArtifactNamesOutput:
    resource: Output
    value = ServiceCatalogCloudFormationProduct.ProvisioningArtifactNames
    export_name = Sub('${AppName}-ServiceCatalogCloudFormationProvisioningArtifactNames')
