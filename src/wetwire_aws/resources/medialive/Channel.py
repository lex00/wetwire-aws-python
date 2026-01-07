"""PropertyTypes for AWS::MediaLive::Channel."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AacSettings(PropertyType):
    bitrate: DslValue[float] | None = None
    coding_mode: DslValue[str] | None = None
    input_type: DslValue[str] | None = None
    profile: DslValue[str] | None = None
    rate_control_mode: DslValue[str] | None = None
    raw_format: DslValue[str] | None = None
    sample_rate: DslValue[float] | None = None
    spec: DslValue[str] | None = None
    vbr_quality: DslValue[str] | None = None


@dataclass
class Ac3Settings(PropertyType):
    attenuation_control: DslValue[str] | None = None
    bitrate: DslValue[float] | None = None
    bitstream_mode: DslValue[str] | None = None
    coding_mode: DslValue[str] | None = None
    dialnorm: DslValue[int] | None = None
    drc_profile: DslValue[str] | None = None
    lfe_filter: DslValue[str] | None = None
    metadata_control: DslValue[str] | None = None


@dataclass
class AdditionalDestinations(PropertyType):
    destination: DslValue[OutputLocationRef] | None = None


@dataclass
class AncillarySourceSettings(PropertyType):
    source_ancillary_channel_number: DslValue[int] | None = None


@dataclass
class AnywhereSettings(PropertyType):
    channel_placement_group_id: DslValue[str] | None = None
    cluster_id: DslValue[str] | None = None


@dataclass
class ArchiveCdnSettings(PropertyType):
    archive_s3_settings: DslValue[ArchiveS3Settings] | None = None


@dataclass
class ArchiveContainerSettings(PropertyType):
    m2ts_settings: DslValue[M2tsSettings] | None = None
    raw_settings: DslValue[RawSettings] | None = None


@dataclass
class ArchiveGroupSettings(PropertyType):
    archive_cdn_settings: DslValue[ArchiveCdnSettings] | None = None
    destination: DslValue[OutputLocationRef] | None = None
    rollover_interval: DslValue[int] | None = None


@dataclass
class ArchiveOutputSettings(PropertyType):
    container_settings: DslValue[ArchiveContainerSettings] | None = None
    extension: DslValue[str] | None = None
    name_modifier: DslValue[str] | None = None


@dataclass
class ArchiveS3Settings(PropertyType):
    canned_acl: DslValue[str] | None = None


@dataclass
class AribDestinationSettings(PropertyType):
    pass


@dataclass
class AribSourceSettings(PropertyType):
    pass


@dataclass
class AudioChannelMapping(PropertyType):
    input_channel_levels: list[DslValue[InputChannelLevel]] = field(
        default_factory=list
    )
    output_channel: DslValue[int] | None = None


@dataclass
class AudioCodecSettings(PropertyType):
    aac_settings: DslValue[AacSettings] | None = None
    ac3_settings: DslValue[Ac3Settings] | None = None
    eac3_atmos_settings: DslValue[Eac3AtmosSettings] | None = None
    eac3_settings: DslValue[Eac3Settings] | None = None
    mp2_settings: DslValue[Mp2Settings] | None = None
    pass_through_settings: DslValue[PassThroughSettings] | None = None
    wav_settings: DslValue[WavSettings] | None = None


@dataclass
class AudioDescription(PropertyType):
    audio_dash_roles: list[DslValue[str]] = field(default_factory=list)
    audio_normalization_settings: DslValue[AudioNormalizationSettings] | None = None
    audio_selector_name: DslValue[str] | None = None
    audio_type: DslValue[str] | None = None
    audio_type_control: DslValue[str] | None = None
    audio_watermarking_settings: DslValue[AudioWatermarkSettings] | None = None
    codec_settings: DslValue[AudioCodecSettings] | None = None
    dvb_dash_accessibility: DslValue[str] | None = None
    language_code: DslValue[str] | None = None
    language_code_control: DslValue[str] | None = None
    name: DslValue[str] | None = None
    remix_settings: DslValue[RemixSettings] | None = None
    stream_name: DslValue[str] | None = None


@dataclass
class AudioDolbyEDecode(PropertyType):
    program_selection: DslValue[str] | None = None


@dataclass
class AudioHlsRenditionSelection(PropertyType):
    group_id: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class AudioLanguageSelection(PropertyType):
    language_code: DslValue[str] | None = None
    language_selection_policy: DslValue[str] | None = None


@dataclass
class AudioNormalizationSettings(PropertyType):
    algorithm: DslValue[str] | None = None
    algorithm_control: DslValue[str] | None = None
    target_lkfs: DslValue[float] | None = None


@dataclass
class AudioOnlyHlsSettings(PropertyType):
    audio_group_id: DslValue[str] | None = None
    audio_only_image: DslValue[InputLocation] | None = None
    audio_track_type: DslValue[str] | None = None
    segment_type: DslValue[str] | None = None


@dataclass
class AudioPidSelection(PropertyType):
    pid: DslValue[int] | None = None


@dataclass
class AudioSelector(PropertyType):
    name: DslValue[str] | None = None
    selector_settings: DslValue[AudioSelectorSettings] | None = None


@dataclass
class AudioSelectorSettings(PropertyType):
    audio_hls_rendition_selection: DslValue[AudioHlsRenditionSelection] | None = None
    audio_language_selection: DslValue[AudioLanguageSelection] | None = None
    audio_pid_selection: DslValue[AudioPidSelection] | None = None
    audio_track_selection: DslValue[AudioTrackSelection] | None = None


@dataclass
class AudioSilenceFailoverSettings(PropertyType):
    audio_selector_name: DslValue[str] | None = None
    audio_silence_threshold_msec: DslValue[int] | None = None


@dataclass
class AudioTrack(PropertyType):
    track: DslValue[int] | None = None


@dataclass
class AudioTrackSelection(PropertyType):
    dolby_e_decode: DslValue[AudioDolbyEDecode] | None = None
    tracks: list[DslValue[AudioTrack]] = field(default_factory=list)


@dataclass
class AudioWatermarkSettings(PropertyType):
    nielsen_watermarks_settings: DslValue[NielsenWatermarksSettings] | None = None


@dataclass
class AutomaticInputFailoverSettings(PropertyType):
    error_clear_time_msec: DslValue[int] | None = None
    failover_conditions: list[DslValue[FailoverCondition]] = field(default_factory=list)
    input_preference: DslValue[str] | None = None
    secondary_input_id: DslValue[str] | None = None


@dataclass
class Av1ColorSpaceSettings(PropertyType):
    color_space_passthrough_settings: DslValue[ColorSpacePassthroughSettings] | None = (
        None
    )
    hdr10_settings: DslValue[Hdr10Settings] | None = None
    rec601_settings: DslValue[Rec601Settings] | None = None
    rec709_settings: DslValue[Rec709Settings] | None = None


@dataclass
class Av1Settings(PropertyType):
    afd_signaling: DslValue[str] | None = None
    bitrate: DslValue[int] | None = None
    buf_size: DslValue[int] | None = None
    color_space_settings: DslValue[Av1ColorSpaceSettings] | None = None
    fixed_afd: DslValue[str] | None = None
    framerate_denominator: DslValue[int] | None = None
    framerate_numerator: DslValue[int] | None = None
    gop_size: DslValue[float] | None = None
    gop_size_units: DslValue[str] | None = None
    level: DslValue[str] | None = None
    look_ahead_rate_control: DslValue[str] | None = None
    max_bitrate: DslValue[int] | None = None
    min_bitrate: DslValue[int] | None = None
    min_i_interval: DslValue[int] | None = None
    par_denominator: DslValue[int] | None = None
    par_numerator: DslValue[int] | None = None
    qvbr_quality_level: DslValue[int] | None = None
    rate_control_mode: DslValue[str] | None = None
    scene_change_detect: DslValue[str] | None = None
    spatial_aq: DslValue[str] | None = None
    temporal_aq: DslValue[str] | None = None
    timecode_burnin_settings: DslValue[TimecodeBurninSettings] | None = None


@dataclass
class AvailBlanking(PropertyType):
    avail_blanking_image: DslValue[InputLocation] | None = None
    state: DslValue[str] | None = None


@dataclass
class AvailConfiguration(PropertyType):
    avail_settings: DslValue[AvailSettings] | None = None
    scte35_segmentation_scope: DslValue[str] | None = None


@dataclass
class AvailSettings(PropertyType):
    esam: DslValue[Esam] | None = None
    scte35_splice_insert: DslValue[Scte35SpliceInsert] | None = None
    scte35_time_signal_apos: DslValue[Scte35TimeSignalApos] | None = None


@dataclass
class BandwidthReductionFilterSettings(PropertyType):
    post_filter_sharpening: DslValue[str] | None = None
    strength: DslValue[str] | None = None


@dataclass
class BlackoutSlate(PropertyType):
    blackout_slate_image: DslValue[InputLocation] | None = None
    network_end_blackout: DslValue[str] | None = None
    network_end_blackout_image: DslValue[InputLocation] | None = None
    network_id: DslValue[str] | None = None
    state: DslValue[str] | None = None


@dataclass
class BurnInDestinationSettings(PropertyType):
    alignment: DslValue[str] | None = None
    background_color: DslValue[str] | None = None
    background_opacity: DslValue[int] | None = None
    font: DslValue[InputLocation] | None = None
    font_color: DslValue[str] | None = None
    font_opacity: DslValue[int] | None = None
    font_resolution: DslValue[int] | None = None
    font_size: DslValue[str] | None = None
    outline_color: DslValue[str] | None = None
    outline_size: DslValue[int] | None = None
    shadow_color: DslValue[str] | None = None
    shadow_opacity: DslValue[int] | None = None
    shadow_x_offset: DslValue[int] | None = None
    shadow_y_offset: DslValue[int] | None = None
    subtitle_rows: DslValue[str] | None = None
    teletext_grid_control: DslValue[str] | None = None
    x_position: DslValue[int] | None = None
    y_position: DslValue[int] | None = None


@dataclass
class CaptionDescription(PropertyType):
    accessibility: DslValue[str] | None = None
    caption_dash_roles: list[DslValue[str]] = field(default_factory=list)
    caption_selector_name: DslValue[str] | None = None
    destination_settings: DslValue[CaptionDestinationSettings] | None = None
    dvb_dash_accessibility: DslValue[str] | None = None
    language_code: DslValue[str] | None = None
    language_description: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class CaptionDestinationSettings(PropertyType):
    arib_destination_settings: DslValue[AribDestinationSettings] | None = None
    burn_in_destination_settings: DslValue[BurnInDestinationSettings] | None = None
    dvb_sub_destination_settings: DslValue[DvbSubDestinationSettings] | None = None
    ebu_tt_d_destination_settings: DslValue[EbuTtDDestinationSettings] | None = None
    embedded_destination_settings: DslValue[EmbeddedDestinationSettings] | None = None
    embedded_plus_scte20_destination_settings: (
        DslValue[EmbeddedPlusScte20DestinationSettings] | None
    ) = None
    rtmp_caption_info_destination_settings: (
        DslValue[RtmpCaptionInfoDestinationSettings] | None
    ) = None
    scte20_plus_embedded_destination_settings: (
        DslValue[Scte20PlusEmbeddedDestinationSettings] | None
    ) = None
    scte27_destination_settings: DslValue[Scte27DestinationSettings] | None = None
    smpte_tt_destination_settings: DslValue[SmpteTtDestinationSettings] | None = None
    teletext_destination_settings: DslValue[TeletextDestinationSettings] | None = None
    ttml_destination_settings: DslValue[TtmlDestinationSettings] | None = None
    webvtt_destination_settings: DslValue[WebvttDestinationSettings] | None = None


@dataclass
class CaptionLanguageMapping(PropertyType):
    caption_channel: DslValue[int] | None = None
    language_code: DslValue[str] | None = None
    language_description: DslValue[str] | None = None


@dataclass
class CaptionRectangle(PropertyType):
    height: DslValue[float] | None = None
    left_offset: DslValue[float] | None = None
    top_offset: DslValue[float] | None = None
    width: DslValue[float] | None = None


@dataclass
class CaptionSelector(PropertyType):
    language_code: DslValue[str] | None = None
    name: DslValue[str] | None = None
    selector_settings: DslValue[CaptionSelectorSettings] | None = None


@dataclass
class CaptionSelectorSettings(PropertyType):
    ancillary_source_settings: DslValue[AncillarySourceSettings] | None = None
    arib_source_settings: DslValue[AribSourceSettings] | None = None
    dvb_sub_source_settings: DslValue[DvbSubSourceSettings] | None = None
    embedded_source_settings: DslValue[EmbeddedSourceSettings] | None = None
    scte20_source_settings: DslValue[Scte20SourceSettings] | None = None
    scte27_source_settings: DslValue[Scte27SourceSettings] | None = None
    teletext_source_settings: DslValue[TeletextSourceSettings] | None = None


@dataclass
class CdiInputSpecification(PropertyType):
    resolution: DslValue[str] | None = None


@dataclass
class ChannelEngineVersionRequest(PropertyType):
    version: DslValue[str] | None = None


@dataclass
class CmafIngestCaptionLanguageMapping(PropertyType):
    caption_channel: DslValue[int] | None = None
    language_code: DslValue[str] | None = None


@dataclass
class CmafIngestGroupSettings(PropertyType):
    additional_destinations: list[DslValue[AdditionalDestinations]] = field(
        default_factory=list
    )
    caption_language_mappings: list[DslValue[CmafIngestCaptionLanguageMapping]] = field(
        default_factory=list
    )
    destination: DslValue[OutputLocationRef] | None = None
    id3_behavior: DslValue[str] | None = None
    id3_name_modifier: DslValue[str] | None = None
    klv_behavior: DslValue[str] | None = None
    klv_name_modifier: DslValue[str] | None = None
    nielsen_id3_behavior: DslValue[str] | None = None
    nielsen_id3_name_modifier: DslValue[str] | None = None
    scte35_name_modifier: DslValue[str] | None = None
    scte35_type: DslValue[str] | None = None
    segment_length: DslValue[int] | None = None
    segment_length_units: DslValue[str] | None = None
    send_delay_ms: DslValue[int] | None = None
    timed_metadata_id3_frame: DslValue[str] | None = None
    timed_metadata_id3_period: DslValue[int] | None = None
    timed_metadata_passthrough: DslValue[str] | None = None


@dataclass
class CmafIngestOutputSettings(PropertyType):
    name_modifier: DslValue[str] | None = None


@dataclass
class ColorCorrection(PropertyType):
    input_color_space: DslValue[str] | None = None
    output_color_space: DslValue[str] | None = None
    uri: DslValue[str] | None = None


@dataclass
class ColorCorrectionSettings(PropertyType):
    global_color_corrections: list[DslValue[ColorCorrection]] = field(
        default_factory=list
    )


@dataclass
class ColorSpacePassthroughSettings(PropertyType):
    pass


@dataclass
class DolbyVision81Settings(PropertyType):
    pass


@dataclass
class DvbNitSettings(PropertyType):
    network_id: DslValue[int] | None = None
    network_name: DslValue[str] | None = None
    rep_interval: DslValue[int] | None = None


@dataclass
class DvbSdtSettings(PropertyType):
    output_sdt: DslValue[str] | None = None
    rep_interval: DslValue[int] | None = None
    service_name: DslValue[str] | None = None
    service_provider_name: DslValue[str] | None = None


@dataclass
class DvbSubDestinationSettings(PropertyType):
    alignment: DslValue[str] | None = None
    background_color: DslValue[str] | None = None
    background_opacity: DslValue[int] | None = None
    font: DslValue[InputLocation] | None = None
    font_color: DslValue[str] | None = None
    font_opacity: DslValue[int] | None = None
    font_resolution: DslValue[int] | None = None
    font_size: DslValue[str] | None = None
    outline_color: DslValue[str] | None = None
    outline_size: DslValue[int] | None = None
    shadow_color: DslValue[str] | None = None
    shadow_opacity: DslValue[int] | None = None
    shadow_x_offset: DslValue[int] | None = None
    shadow_y_offset: DslValue[int] | None = None
    subtitle_rows: DslValue[str] | None = None
    teletext_grid_control: DslValue[str] | None = None
    x_position: DslValue[int] | None = None
    y_position: DslValue[int] | None = None


@dataclass
class DvbSubSourceSettings(PropertyType):
    ocr_language: DslValue[str] | None = None
    pid: DslValue[int] | None = None


@dataclass
class DvbTdtSettings(PropertyType):
    rep_interval: DslValue[int] | None = None


@dataclass
class Eac3AtmosSettings(PropertyType):
    bitrate: DslValue[float] | None = None
    coding_mode: DslValue[str] | None = None
    dialnorm: DslValue[int] | None = None
    drc_line: DslValue[str] | None = None
    drc_rf: DslValue[str] | None = None
    height_trim: DslValue[float] | None = None
    surround_trim: DslValue[float] | None = None


@dataclass
class Eac3Settings(PropertyType):
    attenuation_control: DslValue[str] | None = None
    bitrate: DslValue[float] | None = None
    bitstream_mode: DslValue[str] | None = None
    coding_mode: DslValue[str] | None = None
    dc_filter: DslValue[str] | None = None
    dialnorm: DslValue[int] | None = None
    drc_line: DslValue[str] | None = None
    drc_rf: DslValue[str] | None = None
    lfe_control: DslValue[str] | None = None
    lfe_filter: DslValue[str] | None = None
    lo_ro_center_mix_level: DslValue[float] | None = None
    lo_ro_surround_mix_level: DslValue[float] | None = None
    lt_rt_center_mix_level: DslValue[float] | None = None
    lt_rt_surround_mix_level: DslValue[float] | None = None
    metadata_control: DslValue[str] | None = None
    passthrough_control: DslValue[str] | None = None
    phase_control: DslValue[str] | None = None
    stereo_downmix: DslValue[str] | None = None
    surround_ex_mode: DslValue[str] | None = None
    surround_mode: DslValue[str] | None = None


@dataclass
class EbuTtDDestinationSettings(PropertyType):
    copyright_holder: DslValue[str] | None = None
    default_font_size: DslValue[int] | None = None
    default_line_height: DslValue[int] | None = None
    fill_line_gap: DslValue[str] | None = None
    font_family: DslValue[str] | None = None
    style_control: DslValue[str] | None = None


@dataclass
class EmbeddedDestinationSettings(PropertyType):
    pass


@dataclass
class EmbeddedPlusScte20DestinationSettings(PropertyType):
    pass


@dataclass
class EmbeddedSourceSettings(PropertyType):
    convert608_to708: DslValue[str] | None = None
    scte20_detection: DslValue[str] | None = None
    source608_channel_number: DslValue[int] | None = None
    source608_track_number: DslValue[int] | None = None


@dataclass
class EncoderSettings(PropertyType):
    audio_descriptions: list[DslValue[AudioDescription]] = field(default_factory=list)
    avail_blanking: DslValue[AvailBlanking] | None = None
    avail_configuration: DslValue[AvailConfiguration] | None = None
    blackout_slate: DslValue[BlackoutSlate] | None = None
    caption_descriptions: list[DslValue[CaptionDescription]] = field(
        default_factory=list
    )
    color_correction_settings: DslValue[ColorCorrectionSettings] | None = None
    feature_activations: DslValue[FeatureActivations] | None = None
    global_configuration: DslValue[GlobalConfiguration] | None = None
    motion_graphics_configuration: DslValue[MotionGraphicsConfiguration] | None = None
    nielsen_configuration: DslValue[NielsenConfiguration] | None = None
    output_groups: list[DslValue[OutputGroup]] = field(default_factory=list)
    thumbnail_configuration: DslValue[ThumbnailConfiguration] | None = None
    timecode_config: DslValue[TimecodeConfig] | None = None
    video_descriptions: list[DslValue[VideoDescription]] = field(default_factory=list)


@dataclass
class EpochLockingSettings(PropertyType):
    custom_epoch: DslValue[str] | None = None
    jam_sync_time: DslValue[str] | None = None


@dataclass
class Esam(PropertyType):
    acquisition_point_id: DslValue[str] | None = None
    ad_avail_offset: DslValue[int] | None = None
    password_param: DslValue[str] | None = None
    pois_endpoint: DslValue[str] | None = None
    username: DslValue[str] | None = None
    zone_identity: DslValue[str] | None = None


@dataclass
class FailoverCondition(PropertyType):
    failover_condition_settings: DslValue[FailoverConditionSettings] | None = None


@dataclass
class FailoverConditionSettings(PropertyType):
    audio_silence_settings: DslValue[AudioSilenceFailoverSettings] | None = None
    input_loss_settings: DslValue[InputLossFailoverSettings] | None = None
    video_black_settings: DslValue[VideoBlackFailoverSettings] | None = None


@dataclass
class FeatureActivations(PropertyType):
    input_prepare_schedule_actions: DslValue[str] | None = None
    output_static_image_overlay_schedule_actions: DslValue[str] | None = None


@dataclass
class FecOutputSettings(PropertyType):
    column_depth: DslValue[int] | None = None
    include_fec: DslValue[str] | None = None
    row_length: DslValue[int] | None = None


@dataclass
class Fmp4HlsSettings(PropertyType):
    audio_rendition_sets: DslValue[str] | None = None
    nielsen_id3_behavior: DslValue[str] | None = None
    timed_metadata_behavior: DslValue[str] | None = None


@dataclass
class FrameCaptureCdnSettings(PropertyType):
    frame_capture_s3_settings: DslValue[FrameCaptureS3Settings] | None = None


@dataclass
class FrameCaptureGroupSettings(PropertyType):
    destination: DslValue[OutputLocationRef] | None = None
    frame_capture_cdn_settings: DslValue[FrameCaptureCdnSettings] | None = None


@dataclass
class FrameCaptureHlsSettings(PropertyType):
    pass


@dataclass
class FrameCaptureOutputSettings(PropertyType):
    name_modifier: DslValue[str] | None = None


@dataclass
class FrameCaptureS3Settings(PropertyType):
    canned_acl: DslValue[str] | None = None


@dataclass
class FrameCaptureSettings(PropertyType):
    capture_interval: DslValue[int] | None = None
    capture_interval_units: DslValue[str] | None = None
    timecode_burnin_settings: DslValue[TimecodeBurninSettings] | None = None


@dataclass
class GlobalConfiguration(PropertyType):
    initial_audio_gain: DslValue[int] | None = None
    input_end_action: DslValue[str] | None = None
    input_loss_behavior: DslValue[InputLossBehavior] | None = None
    output_locking_mode: DslValue[str] | None = None
    output_locking_settings: DslValue[OutputLockingSettings] | None = None
    output_timing_source: DslValue[str] | None = None
    support_low_framerate_inputs: DslValue[str] | None = None


@dataclass
class H264ColorSpaceSettings(PropertyType):
    color_space_passthrough_settings: DslValue[ColorSpacePassthroughSettings] | None = (
        None
    )
    rec601_settings: DslValue[Rec601Settings] | None = None
    rec709_settings: DslValue[Rec709Settings] | None = None


@dataclass
class H264FilterSettings(PropertyType):
    bandwidth_reduction_filter_settings: (
        DslValue[BandwidthReductionFilterSettings] | None
    ) = None
    temporal_filter_settings: DslValue[TemporalFilterSettings] | None = None


@dataclass
class H264Settings(PropertyType):
    adaptive_quantization: DslValue[str] | None = None
    afd_signaling: DslValue[str] | None = None
    bitrate: DslValue[int] | None = None
    buf_fill_pct: DslValue[int] | None = None
    buf_size: DslValue[int] | None = None
    color_metadata: DslValue[str] | None = None
    color_space_settings: DslValue[H264ColorSpaceSettings] | None = None
    entropy_encoding: DslValue[str] | None = None
    filter_settings: DslValue[H264FilterSettings] | None = None
    fixed_afd: DslValue[str] | None = None
    flicker_aq: DslValue[str] | None = None
    force_field_pictures: DslValue[str] | None = None
    framerate_control: DslValue[str] | None = None
    framerate_denominator: DslValue[int] | None = None
    framerate_numerator: DslValue[int] | None = None
    gop_b_reference: DslValue[str] | None = None
    gop_closed_cadence: DslValue[int] | None = None
    gop_num_b_frames: DslValue[int] | None = None
    gop_size: DslValue[float] | None = None
    gop_size_units: DslValue[str] | None = None
    level: DslValue[str] | None = None
    look_ahead_rate_control: DslValue[str] | None = None
    max_bitrate: DslValue[int] | None = None
    min_bitrate: DslValue[int] | None = None
    min_i_interval: DslValue[int] | None = None
    min_qp: DslValue[int] | None = None
    num_ref_frames: DslValue[int] | None = None
    par_control: DslValue[str] | None = None
    par_denominator: DslValue[int] | None = None
    par_numerator: DslValue[int] | None = None
    profile: DslValue[str] | None = None
    quality_level: DslValue[str] | None = None
    qvbr_quality_level: DslValue[int] | None = None
    rate_control_mode: DslValue[str] | None = None
    scan_type: DslValue[str] | None = None
    scene_change_detect: DslValue[str] | None = None
    slices: DslValue[int] | None = None
    softness: DslValue[int] | None = None
    spatial_aq: DslValue[str] | None = None
    subgop_length: DslValue[str] | None = None
    syntax: DslValue[str] | None = None
    temporal_aq: DslValue[str] | None = None
    timecode_burnin_settings: DslValue[TimecodeBurninSettings] | None = None
    timecode_insertion: DslValue[str] | None = None


@dataclass
class H265ColorSpaceSettings(PropertyType):
    color_space_passthrough_settings: DslValue[ColorSpacePassthroughSettings] | None = (
        None
    )
    dolby_vision81_settings: DslValue[DolbyVision81Settings] | None = None
    hdr10_settings: DslValue[Hdr10Settings] | None = None
    hlg2020_settings: DslValue[Hlg2020Settings] | None = None
    rec601_settings: DslValue[Rec601Settings] | None = None
    rec709_settings: DslValue[Rec709Settings] | None = None


@dataclass
class H265FilterSettings(PropertyType):
    bandwidth_reduction_filter_settings: (
        DslValue[BandwidthReductionFilterSettings] | None
    ) = None
    temporal_filter_settings: DslValue[TemporalFilterSettings] | None = None


@dataclass
class H265Settings(PropertyType):
    adaptive_quantization: DslValue[str] | None = None
    afd_signaling: DslValue[str] | None = None
    alternative_transfer_function: DslValue[str] | None = None
    bitrate: DslValue[int] | None = None
    buf_size: DslValue[int] | None = None
    color_metadata: DslValue[str] | None = None
    color_space_settings: DslValue[H265ColorSpaceSettings] | None = None
    deblocking: DslValue[str] | None = None
    filter_settings: DslValue[H265FilterSettings] | None = None
    fixed_afd: DslValue[str] | None = None
    flicker_aq: DslValue[str] | None = None
    framerate_denominator: DslValue[int] | None = None
    framerate_numerator: DslValue[int] | None = None
    gop_b_reference: DslValue[str] | None = None
    gop_closed_cadence: DslValue[int] | None = None
    gop_num_b_frames: DslValue[int] | None = None
    gop_size: DslValue[float] | None = None
    gop_size_units: DslValue[str] | None = None
    level: DslValue[str] | None = None
    look_ahead_rate_control: DslValue[str] | None = None
    max_bitrate: DslValue[int] | None = None
    min_bitrate: DslValue[int] | None = None
    min_i_interval: DslValue[int] | None = None
    min_qp: DslValue[int] | None = None
    mv_over_picture_boundaries: DslValue[str] | None = None
    mv_temporal_predictor: DslValue[str] | None = None
    par_denominator: DslValue[int] | None = None
    par_numerator: DslValue[int] | None = None
    profile: DslValue[str] | None = None
    qvbr_quality_level: DslValue[int] | None = None
    rate_control_mode: DslValue[str] | None = None
    scan_type: DslValue[str] | None = None
    scene_change_detect: DslValue[str] | None = None
    slices: DslValue[int] | None = None
    subgop_length: DslValue[str] | None = None
    tier: DslValue[str] | None = None
    tile_height: DslValue[int] | None = None
    tile_padding: DslValue[str] | None = None
    tile_width: DslValue[int] | None = None
    timecode_burnin_settings: DslValue[TimecodeBurninSettings] | None = None
    timecode_insertion: DslValue[str] | None = None
    treeblock_size: DslValue[str] | None = None


@dataclass
class Hdr10Settings(PropertyType):
    max_cll: DslValue[int] | None = None
    max_fall: DslValue[int] | None = None


@dataclass
class Hlg2020Settings(PropertyType):
    pass


@dataclass
class HlsAkamaiSettings(PropertyType):
    connection_retry_interval: DslValue[int] | None = None
    filecache_duration: DslValue[int] | None = None
    http_transfer_mode: DslValue[str] | None = None
    num_retries: DslValue[int] | None = None
    restart_delay: DslValue[int] | None = None
    salt: DslValue[str] | None = None
    token: DslValue[str] | None = None


@dataclass
class HlsBasicPutSettings(PropertyType):
    connection_retry_interval: DslValue[int] | None = None
    filecache_duration: DslValue[int] | None = None
    num_retries: DslValue[int] | None = None
    restart_delay: DslValue[int] | None = None


@dataclass
class HlsCdnSettings(PropertyType):
    hls_akamai_settings: DslValue[HlsAkamaiSettings] | None = None
    hls_basic_put_settings: DslValue[HlsBasicPutSettings] | None = None
    hls_media_store_settings: DslValue[HlsMediaStoreSettings] | None = None
    hls_s3_settings: DslValue[HlsS3Settings] | None = None
    hls_webdav_settings: DslValue[HlsWebdavSettings] | None = None


@dataclass
class HlsGroupSettings(PropertyType):
    ad_markers: list[DslValue[str]] = field(default_factory=list)
    base_url_content: DslValue[str] | None = None
    base_url_content1: DslValue[str] | None = None
    base_url_manifest: DslValue[str] | None = None
    base_url_manifest1: DslValue[str] | None = None
    caption_language_mappings: list[DslValue[CaptionLanguageMapping]] = field(
        default_factory=list
    )
    caption_language_setting: DslValue[str] | None = None
    client_cache: DslValue[str] | None = None
    codec_specification: DslValue[str] | None = None
    constant_iv: DslValue[str] | None = None
    destination: DslValue[OutputLocationRef] | None = None
    directory_structure: DslValue[str] | None = None
    discontinuity_tags: DslValue[str] | None = None
    encryption_type: DslValue[str] | None = None
    hls_cdn_settings: DslValue[HlsCdnSettings] | None = None
    hls_id3_segment_tagging: DslValue[str] | None = None
    i_frame_only_playlists: DslValue[str] | None = None
    incomplete_segment_behavior: DslValue[str] | None = None
    index_n_segments: DslValue[int] | None = None
    input_loss_action: DslValue[str] | None = None
    iv_in_manifest: DslValue[str] | None = None
    iv_source: DslValue[str] | None = None
    keep_segments: DslValue[int] | None = None
    key_format: DslValue[str] | None = None
    key_format_versions: DslValue[str] | None = None
    key_provider_settings: DslValue[KeyProviderSettings] | None = None
    manifest_compression: DslValue[str] | None = None
    manifest_duration_format: DslValue[str] | None = None
    min_segment_length: DslValue[int] | None = None
    mode: DslValue[str] | None = None
    output_selection: DslValue[str] | None = None
    program_date_time: DslValue[str] | None = None
    program_date_time_clock: DslValue[str] | None = None
    program_date_time_period: DslValue[int] | None = None
    redundant_manifest: DslValue[str] | None = None
    segment_length: DslValue[int] | None = None
    segmentation_mode: DslValue[str] | None = None
    segments_per_subdirectory: DslValue[int] | None = None
    stream_inf_resolution: DslValue[str] | None = None
    timed_metadata_id3_frame: DslValue[str] | None = None
    timed_metadata_id3_period: DslValue[int] | None = None
    timestamp_delta_milliseconds: DslValue[int] | None = None
    ts_file_mode: DslValue[str] | None = None


@dataclass
class HlsInputSettings(PropertyType):
    bandwidth: DslValue[int] | None = None
    buffer_segments: DslValue[int] | None = None
    retries: DslValue[int] | None = None
    retry_interval: DslValue[int] | None = None
    scte35_source: DslValue[str] | None = None


@dataclass
class HlsMediaStoreSettings(PropertyType):
    connection_retry_interval: DslValue[int] | None = None
    filecache_duration: DslValue[int] | None = None
    media_store_storage_class: DslValue[str] | None = None
    num_retries: DslValue[int] | None = None
    restart_delay: DslValue[int] | None = None


@dataclass
class HlsOutputSettings(PropertyType):
    h265_packaging_type: DslValue[str] | None = None
    hls_settings: DslValue[HlsSettings] | None = None
    name_modifier: DslValue[str] | None = None
    segment_modifier: DslValue[str] | None = None


@dataclass
class HlsS3Settings(PropertyType):
    canned_acl: DslValue[str] | None = None


@dataclass
class HlsSettings(PropertyType):
    audio_only_hls_settings: DslValue[AudioOnlyHlsSettings] | None = None
    fmp4_hls_settings: DslValue[Fmp4HlsSettings] | None = None
    frame_capture_hls_settings: DslValue[FrameCaptureHlsSettings] | None = None
    standard_hls_settings: DslValue[StandardHlsSettings] | None = None


@dataclass
class HlsWebdavSettings(PropertyType):
    connection_retry_interval: DslValue[int] | None = None
    filecache_duration: DslValue[int] | None = None
    http_transfer_mode: DslValue[str] | None = None
    num_retries: DslValue[int] | None = None
    restart_delay: DslValue[int] | None = None


@dataclass
class HtmlMotionGraphicsSettings(PropertyType):
    pass


@dataclass
class InputAttachment(PropertyType):
    automatic_input_failover_settings: (
        DslValue[AutomaticInputFailoverSettings] | None
    ) = None
    input_attachment_name: DslValue[str] | None = None
    input_id: DslValue[str] | None = None
    input_settings: DslValue[InputSettings] | None = None
    logical_interface_names: list[DslValue[str]] = field(default_factory=list)


@dataclass
class InputChannelLevel(PropertyType):
    gain: DslValue[int] | None = None
    input_channel: DslValue[int] | None = None


@dataclass
class InputLocation(PropertyType):
    password_param: DslValue[str] | None = None
    uri: DslValue[str] | None = None
    username: DslValue[str] | None = None


@dataclass
class InputLossBehavior(PropertyType):
    black_frame_msec: DslValue[int] | None = None
    input_loss_image_color: DslValue[str] | None = None
    input_loss_image_slate: DslValue[InputLocation] | None = None
    input_loss_image_type: DslValue[str] | None = None
    repeat_frame_msec: DslValue[int] | None = None


@dataclass
class InputLossFailoverSettings(PropertyType):
    input_loss_threshold_msec: DslValue[int] | None = None


@dataclass
class InputSettings(PropertyType):
    audio_selectors: list[DslValue[AudioSelector]] = field(default_factory=list)
    caption_selectors: list[DslValue[CaptionSelector]] = field(default_factory=list)
    deblock_filter: DslValue[str] | None = None
    denoise_filter: DslValue[str] | None = None
    filter_strength: DslValue[int] | None = None
    input_filter: DslValue[str] | None = None
    network_input_settings: DslValue[NetworkInputSettings] | None = None
    scte35_pid: DslValue[int] | None = None
    smpte2038_data_preference: DslValue[str] | None = None
    source_end_behavior: DslValue[str] | None = None
    video_selector: DslValue[VideoSelector] | None = None


@dataclass
class InputSpecification(PropertyType):
    codec: DslValue[str] | None = None
    maximum_bitrate: DslValue[str] | None = None
    resolution: DslValue[str] | None = None


@dataclass
class KeyProviderSettings(PropertyType):
    static_key_settings: DslValue[StaticKeySettings] | None = None


@dataclass
class M2tsSettings(PropertyType):
    absent_input_audio_behavior: DslValue[str] | None = None
    arib: DslValue[str] | None = None
    arib_captions_pid: DslValue[str] | None = None
    arib_captions_pid_control: DslValue[str] | None = None
    audio_buffer_model: DslValue[str] | None = None
    audio_frames_per_pes: DslValue[int] | None = None
    audio_pids: DslValue[str] | None = None
    audio_stream_type: DslValue[str] | None = None
    bitrate: DslValue[int] | None = None
    buffer_model: DslValue[str] | None = None
    cc_descriptor: DslValue[str] | None = None
    dvb_nit_settings: DslValue[DvbNitSettings] | None = None
    dvb_sdt_settings: DslValue[DvbSdtSettings] | None = None
    dvb_sub_pids: DslValue[str] | None = None
    dvb_tdt_settings: DslValue[DvbTdtSettings] | None = None
    dvb_teletext_pid: DslValue[str] | None = None
    ebif: DslValue[str] | None = None
    ebp_audio_interval: DslValue[str] | None = None
    ebp_lookahead_ms: DslValue[int] | None = None
    ebp_placement: DslValue[str] | None = None
    ecm_pid: DslValue[str] | None = None
    es_rate_in_pes: DslValue[str] | None = None
    etv_platform_pid: DslValue[str] | None = None
    etv_signal_pid: DslValue[str] | None = None
    fragment_time: DslValue[float] | None = None
    klv: DslValue[str] | None = None
    klv_data_pids: DslValue[str] | None = None
    nielsen_id3_behavior: DslValue[str] | None = None
    null_packet_bitrate: DslValue[float] | None = None
    pat_interval: DslValue[int] | None = None
    pcr_control: DslValue[str] | None = None
    pcr_period: DslValue[int] | None = None
    pcr_pid: DslValue[str] | None = None
    pmt_interval: DslValue[int] | None = None
    pmt_pid: DslValue[str] | None = None
    program_num: DslValue[int] | None = None
    rate_mode: DslValue[str] | None = None
    scte27_pids: DslValue[str] | None = None
    scte35_control: DslValue[str] | None = None
    scte35_pid: DslValue[str] | None = None
    scte35_preroll_pullup_milliseconds: DslValue[float] | None = None
    segmentation_markers: DslValue[str] | None = None
    segmentation_style: DslValue[str] | None = None
    segmentation_time: DslValue[float] | None = None
    timed_metadata_behavior: DslValue[str] | None = None
    timed_metadata_pid: DslValue[str] | None = None
    transport_stream_id: DslValue[int] | None = None
    video_pid: DslValue[str] | None = None


@dataclass
class M3u8Settings(PropertyType):
    audio_frames_per_pes: DslValue[int] | None = None
    audio_pids: DslValue[str] | None = None
    ecm_pid: DslValue[str] | None = None
    klv_behavior: DslValue[str] | None = None
    klv_data_pids: DslValue[str] | None = None
    nielsen_id3_behavior: DslValue[str] | None = None
    pat_interval: DslValue[int] | None = None
    pcr_control: DslValue[str] | None = None
    pcr_period: DslValue[int] | None = None
    pcr_pid: DslValue[str] | None = None
    pmt_interval: DslValue[int] | None = None
    pmt_pid: DslValue[str] | None = None
    program_num: DslValue[int] | None = None
    scte35_behavior: DslValue[str] | None = None
    scte35_pid: DslValue[str] | None = None
    timed_metadata_behavior: DslValue[str] | None = None
    timed_metadata_pid: DslValue[str] | None = None
    transport_stream_id: DslValue[int] | None = None
    video_pid: DslValue[str] | None = None


@dataclass
class MaintenanceCreateSettings(PropertyType):
    maintenance_day: DslValue[str] | None = None
    maintenance_start_time: DslValue[str] | None = None


@dataclass
class MaintenanceUpdateSettings(PropertyType):
    maintenance_day: DslValue[str] | None = None
    maintenance_scheduled_date: DslValue[str] | None = None
    maintenance_start_time: DslValue[str] | None = None


@dataclass
class MediaPackageGroupSettings(PropertyType):
    destination: DslValue[OutputLocationRef] | None = None
    mediapackage_v2_group_settings: DslValue[MediaPackageV2GroupSettings] | None = None


@dataclass
class MediaPackageOutputDestinationSettings(PropertyType):
    channel_group: DslValue[str] | None = None
    channel_id: DslValue[str] | None = None
    channel_name: DslValue[str] | None = None


@dataclass
class MediaPackageOutputSettings(PropertyType):
    media_package_v2_destination_settings: (
        DslValue[MediaPackageV2DestinationSettings] | None
    ) = None


@dataclass
class MediaPackageV2DestinationSettings(PropertyType):
    audio_group_id: DslValue[str] | None = None
    audio_rendition_sets: DslValue[str] | None = None
    hls_auto_select: DslValue[str] | None = None
    hls_default: DslValue[str] | None = None


@dataclass
class MediaPackageV2GroupSettings(PropertyType):
    caption_language_mappings: list[DslValue[CaptionLanguageMapping]] = field(
        default_factory=list
    )
    id3_behavior: DslValue[str] | None = None
    klv_behavior: DslValue[str] | None = None
    nielsen_id3_behavior: DslValue[str] | None = None
    scte35_type: DslValue[str] | None = None
    segment_length: DslValue[int] | None = None
    segment_length_units: DslValue[str] | None = None
    timed_metadata_id3_frame: DslValue[str] | None = None
    timed_metadata_id3_period: DslValue[int] | None = None
    timed_metadata_passthrough: DslValue[str] | None = None


@dataclass
class MotionGraphicsConfiguration(PropertyType):
    motion_graphics_insertion: DslValue[str] | None = None
    motion_graphics_settings: DslValue[MotionGraphicsSettings] | None = None


@dataclass
class MotionGraphicsSettings(PropertyType):
    html_motion_graphics_settings: DslValue[HtmlMotionGraphicsSettings] | None = None


@dataclass
class Mp2Settings(PropertyType):
    bitrate: DslValue[float] | None = None
    coding_mode: DslValue[str] | None = None
    sample_rate: DslValue[float] | None = None


@dataclass
class Mpeg2FilterSettings(PropertyType):
    temporal_filter_settings: DslValue[TemporalFilterSettings] | None = None


@dataclass
class Mpeg2Settings(PropertyType):
    adaptive_quantization: DslValue[str] | None = None
    afd_signaling: DslValue[str] | None = None
    color_metadata: DslValue[str] | None = None
    color_space: DslValue[str] | None = None
    display_aspect_ratio: DslValue[str] | None = None
    filter_settings: DslValue[Mpeg2FilterSettings] | None = None
    fixed_afd: DslValue[str] | None = None
    framerate_denominator: DslValue[int] | None = None
    framerate_numerator: DslValue[int] | None = None
    gop_closed_cadence: DslValue[int] | None = None
    gop_num_b_frames: DslValue[int] | None = None
    gop_size: DslValue[float] | None = None
    gop_size_units: DslValue[str] | None = None
    scan_type: DslValue[str] | None = None
    subgop_length: DslValue[str] | None = None
    timecode_burnin_settings: DslValue[TimecodeBurninSettings] | None = None
    timecode_insertion: DslValue[str] | None = None


@dataclass
class MsSmoothGroupSettings(PropertyType):
    acquisition_point_id: DslValue[str] | None = None
    audio_only_timecode_control: DslValue[str] | None = None
    certificate_mode: DslValue[str] | None = None
    connection_retry_interval: DslValue[int] | None = None
    destination: DslValue[OutputLocationRef] | None = None
    event_id: DslValue[str] | None = None
    event_id_mode: DslValue[str] | None = None
    event_stop_behavior: DslValue[str] | None = None
    filecache_duration: DslValue[int] | None = None
    fragment_length: DslValue[int] | None = None
    input_loss_action: DslValue[str] | None = None
    num_retries: DslValue[int] | None = None
    restart_delay: DslValue[int] | None = None
    segmentation_mode: DslValue[str] | None = None
    send_delay_ms: DslValue[int] | None = None
    sparse_track_type: DslValue[str] | None = None
    stream_manifest_behavior: DslValue[str] | None = None
    timestamp_offset: DslValue[str] | None = None
    timestamp_offset_mode: DslValue[str] | None = None


@dataclass
class MsSmoothOutputSettings(PropertyType):
    h265_packaging_type: DslValue[str] | None = None
    name_modifier: DslValue[str] | None = None


@dataclass
class MulticastInputSettings(PropertyType):
    source_ip_address: DslValue[str] | None = None


@dataclass
class MultiplexContainerSettings(PropertyType):
    multiplex_m2ts_settings: DslValue[MultiplexM2tsSettings] | None = None


@dataclass
class MultiplexGroupSettings(PropertyType):
    pass


@dataclass
class MultiplexM2tsSettings(PropertyType):
    absent_input_audio_behavior: DslValue[str] | None = None
    arib: DslValue[str] | None = None
    audio_buffer_model: DslValue[str] | None = None
    audio_frames_per_pes: DslValue[int] | None = None
    audio_stream_type: DslValue[str] | None = None
    cc_descriptor: DslValue[str] | None = None
    ebif: DslValue[str] | None = None
    es_rate_in_pes: DslValue[str] | None = None
    klv: DslValue[str] | None = None
    nielsen_id3_behavior: DslValue[str] | None = None
    pcr_control: DslValue[str] | None = None
    pcr_period: DslValue[int] | None = None
    scte35_control: DslValue[str] | None = None
    scte35_preroll_pullup_milliseconds: DslValue[float] | None = None


@dataclass
class MultiplexOutputSettings(PropertyType):
    container_settings: DslValue[MultiplexContainerSettings] | None = None
    destination: DslValue[OutputLocationRef] | None = None


@dataclass
class MultiplexProgramChannelDestinationSettings(PropertyType):
    multiplex_id: DslValue[str] | None = None
    program_name: DslValue[str] | None = None


@dataclass
class NetworkInputSettings(PropertyType):
    hls_input_settings: DslValue[HlsInputSettings] | None = None
    multicast_input_settings: DslValue[MulticastInputSettings] | None = None
    server_validation: DslValue[str] | None = None


@dataclass
class NielsenCBET(PropertyType):
    cbet_check_digit_string: DslValue[str] | None = None
    cbet_stepaside: DslValue[str] | None = None
    csid: DslValue[str] | None = None


@dataclass
class NielsenConfiguration(PropertyType):
    distributor_id: DslValue[str] | None = None
    nielsen_pcm_to_id3_tagging: DslValue[str] | None = None


@dataclass
class NielsenNaesIiNw(PropertyType):
    check_digit_string: DslValue[str] | None = None
    sid: DslValue[float] | None = None
    timezone: DslValue[str] | None = None


@dataclass
class NielsenWatermarksSettings(PropertyType):
    nielsen_cbet_settings: DslValue[NielsenCBET] | None = None
    nielsen_distribution_type: DslValue[str] | None = None
    nielsen_naes_ii_nw_settings: DslValue[NielsenNaesIiNw] | None = None


@dataclass
class Output(PropertyType):
    audio_description_names: list[DslValue[str]] = field(default_factory=list)
    caption_description_names: list[DslValue[str]] = field(default_factory=list)
    output_name: DslValue[str] | None = None
    output_settings: DslValue[OutputSettings] | None = None
    video_description_name: DslValue[str] | None = None


@dataclass
class OutputDestination(PropertyType):
    id: DslValue[str] | None = None
    logical_interface_names: list[DslValue[str]] = field(default_factory=list)
    media_package_settings: list[DslValue[MediaPackageOutputDestinationSettings]] = (
        field(default_factory=list)
    )
    multiplex_settings: DslValue[MultiplexProgramChannelDestinationSettings] | None = (
        None
    )
    settings: list[DslValue[OutputDestinationSettings]] = field(default_factory=list)
    srt_settings: list[DslValue[SrtOutputDestinationSettings]] = field(
        default_factory=list
    )


@dataclass
class OutputDestinationSettings(PropertyType):
    password_param: DslValue[str] | None = None
    stream_name: DslValue[str] | None = None
    url: DslValue[str] | None = None
    username: DslValue[str] | None = None


@dataclass
class OutputGroup(PropertyType):
    name: DslValue[str] | None = None
    output_group_settings: DslValue[OutputGroupSettings] | None = None
    outputs: list[DslValue[Output]] = field(default_factory=list)


@dataclass
class OutputGroupSettings(PropertyType):
    archive_group_settings: DslValue[ArchiveGroupSettings] | None = None
    cmaf_ingest_group_settings: DslValue[CmafIngestGroupSettings] | None = None
    frame_capture_group_settings: DslValue[FrameCaptureGroupSettings] | None = None
    hls_group_settings: DslValue[HlsGroupSettings] | None = None
    media_package_group_settings: DslValue[MediaPackageGroupSettings] | None = None
    ms_smooth_group_settings: DslValue[MsSmoothGroupSettings] | None = None
    multiplex_group_settings: DslValue[MultiplexGroupSettings] | None = None
    rtmp_group_settings: DslValue[RtmpGroupSettings] | None = None
    srt_group_settings: DslValue[SrtGroupSettings] | None = None
    udp_group_settings: DslValue[UdpGroupSettings] | None = None


@dataclass
class OutputLocationRef(PropertyType):
    destination_ref_id: DslValue[str] | None = None


@dataclass
class OutputLockingSettings(PropertyType):
    epoch_locking_settings: DslValue[EpochLockingSettings] | None = None
    pipeline_locking_settings: DslValue[PipelineLockingSettings] | None = None


@dataclass
class OutputSettings(PropertyType):
    archive_output_settings: DslValue[ArchiveOutputSettings] | None = None
    cmaf_ingest_output_settings: DslValue[CmafIngestOutputSettings] | None = None
    frame_capture_output_settings: DslValue[FrameCaptureOutputSettings] | None = None
    hls_output_settings: DslValue[HlsOutputSettings] | None = None
    media_package_output_settings: DslValue[MediaPackageOutputSettings] | None = None
    ms_smooth_output_settings: DslValue[MsSmoothOutputSettings] | None = None
    multiplex_output_settings: DslValue[MultiplexOutputSettings] | None = None
    rtmp_output_settings: DslValue[RtmpOutputSettings] | None = None
    srt_output_settings: DslValue[SrtOutputSettings] | None = None
    udp_output_settings: DslValue[UdpOutputSettings] | None = None


@dataclass
class PassThroughSettings(PropertyType):
    pass


@dataclass
class PipelineLockingSettings(PropertyType):
    pass


@dataclass
class RawSettings(PropertyType):
    pass


@dataclass
class Rec601Settings(PropertyType):
    pass


@dataclass
class Rec709Settings(PropertyType):
    pass


@dataclass
class RemixSettings(PropertyType):
    channel_mappings: list[DslValue[AudioChannelMapping]] = field(default_factory=list)
    channels_in: DslValue[int] | None = None
    channels_out: DslValue[int] | None = None


@dataclass
class RtmpCaptionInfoDestinationSettings(PropertyType):
    pass


@dataclass
class RtmpGroupSettings(PropertyType):
    ad_markers: list[DslValue[str]] = field(default_factory=list)
    authentication_scheme: DslValue[str] | None = None
    cache_full_behavior: DslValue[str] | None = None
    cache_length: DslValue[int] | None = None
    caption_data: DslValue[str] | None = None
    include_filler_nal_units: DslValue[str] | None = None
    input_loss_action: DslValue[str] | None = None
    restart_delay: DslValue[int] | None = None


@dataclass
class RtmpOutputSettings(PropertyType):
    certificate_mode: DslValue[str] | None = None
    connection_retry_interval: DslValue[int] | None = None
    destination: DslValue[OutputLocationRef] | None = None
    num_retries: DslValue[int] | None = None


@dataclass
class Scte20PlusEmbeddedDestinationSettings(PropertyType):
    pass


@dataclass
class Scte20SourceSettings(PropertyType):
    convert608_to708: DslValue[str] | None = None
    source608_channel_number: DslValue[int] | None = None


@dataclass
class Scte27DestinationSettings(PropertyType):
    pass


@dataclass
class Scte27SourceSettings(PropertyType):
    ocr_language: DslValue[str] | None = None
    pid: DslValue[int] | None = None


@dataclass
class Scte35SpliceInsert(PropertyType):
    ad_avail_offset: DslValue[int] | None = None
    no_regional_blackout_flag: DslValue[str] | None = None
    web_delivery_allowed_flag: DslValue[str] | None = None


@dataclass
class Scte35TimeSignalApos(PropertyType):
    ad_avail_offset: DslValue[int] | None = None
    no_regional_blackout_flag: DslValue[str] | None = None
    web_delivery_allowed_flag: DslValue[str] | None = None


@dataclass
class SmpteTtDestinationSettings(PropertyType):
    pass


@dataclass
class SrtGroupSettings(PropertyType):
    input_loss_action: DslValue[str] | None = None


@dataclass
class SrtOutputDestinationSettings(PropertyType):
    encryption_passphrase_secret_arn: DslValue[str] | None = None
    stream_id: DslValue[str] | None = None
    url: DslValue[str] | None = None


@dataclass
class SrtOutputSettings(PropertyType):
    buffer_msec: DslValue[int] | None = None
    container_settings: DslValue[UdpContainerSettings] | None = None
    destination: DslValue[OutputLocationRef] | None = None
    encryption_type: DslValue[str] | None = None
    latency: DslValue[int] | None = None


@dataclass
class StandardHlsSettings(PropertyType):
    audio_rendition_sets: DslValue[str] | None = None
    m3u8_settings: DslValue[M3u8Settings] | None = None


@dataclass
class StaticKeySettings(PropertyType):
    key_provider_server: DslValue[InputLocation] | None = None
    static_key_value: DslValue[str] | None = None


@dataclass
class TeletextDestinationSettings(PropertyType):
    pass


@dataclass
class TeletextSourceSettings(PropertyType):
    output_rectangle: DslValue[CaptionRectangle] | None = None
    page_number: DslValue[str] | None = None


@dataclass
class TemporalFilterSettings(PropertyType):
    post_filter_sharpening: DslValue[str] | None = None
    strength: DslValue[str] | None = None


@dataclass
class ThumbnailConfiguration(PropertyType):
    state: DslValue[str] | None = None


@dataclass
class TimecodeBurninSettings(PropertyType):
    font_size: DslValue[str] | None = None
    position: DslValue[str] | None = None
    prefix: DslValue[str] | None = None


@dataclass
class TimecodeConfig(PropertyType):
    source: DslValue[str] | None = None
    sync_threshold: DslValue[int] | None = None


@dataclass
class TtmlDestinationSettings(PropertyType):
    style_control: DslValue[str] | None = None


@dataclass
class UdpContainerSettings(PropertyType):
    m2ts_settings: DslValue[M2tsSettings] | None = None


@dataclass
class UdpGroupSettings(PropertyType):
    input_loss_action: DslValue[str] | None = None
    timed_metadata_id3_frame: DslValue[str] | None = None
    timed_metadata_id3_period: DslValue[int] | None = None


@dataclass
class UdpOutputSettings(PropertyType):
    buffer_msec: DslValue[int] | None = None
    container_settings: DslValue[UdpContainerSettings] | None = None
    destination: DslValue[OutputLocationRef] | None = None
    fec_output_settings: DslValue[FecOutputSettings] | None = None


@dataclass
class VideoBlackFailoverSettings(PropertyType):
    black_detect_threshold: DslValue[float] | None = None
    video_black_threshold_msec: DslValue[int] | None = None


@dataclass
class VideoCodecSettings(PropertyType):
    av1_settings: DslValue[Av1Settings] | None = None
    frame_capture_settings: DslValue[FrameCaptureSettings] | None = None
    h264_settings: DslValue[H264Settings] | None = None
    h265_settings: DslValue[H265Settings] | None = None
    mpeg2_settings: DslValue[Mpeg2Settings] | None = None


@dataclass
class VideoDescription(PropertyType):
    codec_settings: DslValue[VideoCodecSettings] | None = None
    height: DslValue[int] | None = None
    name: DslValue[str] | None = None
    respond_to_afd: DslValue[str] | None = None
    scaling_behavior: DslValue[str] | None = None
    sharpness: DslValue[int] | None = None
    width: DslValue[int] | None = None


@dataclass
class VideoSelector(PropertyType):
    color_space: DslValue[str] | None = None
    color_space_settings: DslValue[VideoSelectorColorSpaceSettings] | None = None
    color_space_usage: DslValue[str] | None = None
    selector_settings: DslValue[VideoSelectorSettings] | None = None


@dataclass
class VideoSelectorColorSpaceSettings(PropertyType):
    hdr10_settings: DslValue[Hdr10Settings] | None = None


@dataclass
class VideoSelectorPid(PropertyType):
    pid: DslValue[int] | None = None


@dataclass
class VideoSelectorProgramId(PropertyType):
    program_id: DslValue[int] | None = None


@dataclass
class VideoSelectorSettings(PropertyType):
    video_selector_pid: DslValue[VideoSelectorPid] | None = None
    video_selector_program_id: DslValue[VideoSelectorProgramId] | None = None


@dataclass
class VpcOutputSettings(PropertyType):
    public_address_allocation_ids: list[DslValue[str]] = field(default_factory=list)
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnet_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class WavSettings(PropertyType):
    bit_depth: DslValue[float] | None = None
    coding_mode: DslValue[str] | None = None
    sample_rate: DslValue[float] | None = None


@dataclass
class WebvttDestinationSettings(PropertyType):
    style_control: DslValue[str] | None = None
