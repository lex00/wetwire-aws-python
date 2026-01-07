"""Template outputs."""

from . import *  # noqa: F403


class ServiceCatalogCloudFormationProductNameOutput(Output):
    value = ServiceCatalogCloudFormationProduct.ProductName
    export_name = Sub('${AppName}-ServiceCatalogCloudFormationProductName')


class ServiceCatalogProvisioningArtifactIdsOutput(Output):
    value = ServiceCatalogCloudFormationProduct.ProvisioningArtifactIds
    export_name = Sub('${AppName}-ServiceCatalogCloudFormationProvisioningArtifactIds')


class ServiceCatalogProvisioningArtifactNamesOutput(Output):
    value = ServiceCatalogCloudFormationProduct.ProvisioningArtifactNames
    export_name = Sub('${AppName}-ServiceCatalogCloudFormationProvisioningArtifactNames')
