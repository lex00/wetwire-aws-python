"""Template outputs."""

from . import *  # noqa: F403


class ConfigRuleForVolumeTagsArnOutput(Output):
    value = ConfigRuleForVolumeTags.Arn


class ConfigRuleForVolumeTagsConfigRuleIdOutput(Output):
    value = ConfigRuleForVolumeTags.ConfigRuleId


class ConfigRuleForVolumeAutoEnableIOComplianceTypeOutput(Output):
    value = ConfigRuleForVolumeAutoEnableIO.Compliance.Type
