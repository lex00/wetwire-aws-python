"""Template outputs."""

from . import *  # noqa: F403


class ConfigRuleForVolumeTagsArnOutput:
    resource: Output
    value = ConfigRuleForVolumeTags.Arn


class ConfigRuleForVolumeTagsConfigRuleIdOutput:
    resource: Output
    value = ConfigRuleForVolumeTags.ConfigRuleId


class ConfigRuleForVolumeAutoEnableIOComplianceTypeOutput:
    resource: Output
    value = GetAtt("ConfigRuleForVolumeAutoEnableIO", "Compliance.Type")
