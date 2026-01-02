"""PropertyTypes for AWS::MediaLive::Channel."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AacSettings(PropertyType):
    bitrate: float | None = None
    coding_mode: str | None = None
    input_type: str | None = None
    profile: str | None = None
    rate_control_mode: str | None = None
    raw_format: str | None = None
    sample_rate: float | None = None
    spec: str | None = None
    vbr_quality: str | None = None


@dataclass
class Ac3Settings(PropertyType):
    attenuation_control: str | None = None
    bitrate: float | None = None
    bitstream_mode: str | None = None
    coding_mode: str | None = None
    dialnorm: int | None = None
    drc_profile: str | None = None
    lfe_filter: str | None = None
    metadata_control: str | None = None


@dataclass
class AdditionalDestinations(PropertyType):
    destination: OutputLocationRef | None = None


@dataclass
class AncillarySourceSettings(PropertyType):
    source_ancillary_channel_number: int | None = None


@dataclass
class AnywhereSettings(PropertyType):
    channel_placement_group_id: str | None = None
    cluster_id: str | None = None


@dataclass
class ArchiveCdnSettings(PropertyType):
    archive_s3_settings: ArchiveS3Settings | None = None


@dataclass
class ArchiveContainerSettings(PropertyType):
    m2ts_settings: M2tsSettings | None = None
    raw_settings: RawSettings | None = None


@dataclass
class ArchiveGroupSettings(PropertyType):
    archive_cdn_settings: ArchiveCdnSettings | None = None
    destination: OutputLocationRef | None = None
    rollover_interval: int | None = None


@dataclass
class ArchiveOutputSettings(PropertyType):
    container_settings: ArchiveContainerSettings | None = None
    extension: str | None = None
    name_modifier: str | None = None


@dataclass
class ArchiveS3Settings(PropertyType):
    canned_acl: str | None = None


@dataclass
class AribDestinationSettings(PropertyType):
    pass


@dataclass
class AribSourceSettings(PropertyType):
    pass


@dataclass
class AudioChannelMapping(PropertyType):
    input_channel_levels: list[InputChannelLevel] = field(default_factory=list)
    output_channel: int | None = None


@dataclass
class AudioCodecSettings(PropertyType):
    aac_settings: AacSettings | None = None
    ac3_settings: Ac3Settings | None = None
    eac3_atmos_settings: Eac3AtmosSettings | None = None
    eac3_settings: Eac3Settings | None = None
    mp2_settings: Mp2Settings | None = None
    pass_through_settings: PassThroughSettings | None = None
    wav_settings: WavSettings | None = None


@dataclass
class AudioDescription(PropertyType):
    audio_dash_roles: list[String] = field(default_factory=list)
    audio_normalization_settings: AudioNormalizationSettings | None = None
    audio_selector_name: str | None = None
    audio_type: str | None = None
    audio_type_control: str | None = None
    audio_watermarking_settings: AudioWatermarkSettings | None = None
    codec_settings: AudioCodecSettings | None = None
    dvb_dash_accessibility: str | None = None
    language_code: str | None = None
    language_code_control: str | None = None
    name: str | None = None
    remix_settings: RemixSettings | None = None
    stream_name: str | None = None


@dataclass
class AudioDolbyEDecode(PropertyType):
    program_selection: str | None = None


@dataclass
class AudioHlsRenditionSelection(PropertyType):
    group_id: str | None = None
    name: str | None = None


@dataclass
class AudioLanguageSelection(PropertyType):
    language_code: str | None = None
    language_selection_policy: str | None = None


@dataclass
class AudioNormalizationSettings(PropertyType):
    algorithm: str | None = None
    algorithm_control: str | None = None
    target_lkfs: float | None = None


@dataclass
class AudioOnlyHlsSettings(PropertyType):
    audio_group_id: str | None = None
    audio_only_image: InputLocation | None = None
    audio_track_type: str | None = None
    segment_type: str | None = None


@dataclass
class AudioPidSelection(PropertyType):
    pid: int | None = None


@dataclass
class AudioSelector(PropertyType):
    name: str | None = None
    selector_settings: AudioSelectorSettings | None = None


@dataclass
class AudioSelectorSettings(PropertyType):
    audio_hls_rendition_selection: AudioHlsRenditionSelection | None = None
    audio_language_selection: AudioLanguageSelection | None = None
    audio_pid_selection: AudioPidSelection | None = None
    audio_track_selection: AudioTrackSelection | None = None


@dataclass
class AudioSilenceFailoverSettings(PropertyType):
    audio_selector_name: str | None = None
    audio_silence_threshold_msec: int | None = None


@dataclass
class AudioTrack(PropertyType):
    track: int | None = None


@dataclass
class AudioTrackSelection(PropertyType):
    dolby_e_decode: AudioDolbyEDecode | None = None
    tracks: list[AudioTrack] = field(default_factory=list)


@dataclass
class AudioWatermarkSettings(PropertyType):
    nielsen_watermarks_settings: NielsenWatermarksSettings | None = None


@dataclass
class AutomaticInputFailoverSettings(PropertyType):
    error_clear_time_msec: int | None = None
    failover_conditions: list[FailoverCondition] = field(default_factory=list)
    input_preference: str | None = None
    secondary_input_id: str | None = None


@dataclass
class Av1ColorSpaceSettings(PropertyType):
    color_space_passthrough_settings: ColorSpacePassthroughSettings | None = None
    hdr10_settings: Hdr10Settings | None = None
    rec601_settings: Rec601Settings | None = None
    rec709_settings: Rec709Settings | None = None


@dataclass
class Av1Settings(PropertyType):
    afd_signaling: str | None = None
    bitrate: int | None = None
    buf_size: int | None = None
    color_space_settings: Av1ColorSpaceSettings | None = None
    fixed_afd: str | None = None
    framerate_denominator: int | None = None
    framerate_numerator: int | None = None
    gop_size: float | None = None
    gop_size_units: str | None = None
    level: str | None = None
    look_ahead_rate_control: str | None = None
    max_bitrate: int | None = None
    min_bitrate: int | None = None
    min_i_interval: int | None = None
    par_denominator: int | None = None
    par_numerator: int | None = None
    qvbr_quality_level: int | None = None
    rate_control_mode: str | None = None
    scene_change_detect: str | None = None
    spatial_aq: str | None = None
    temporal_aq: str | None = None
    timecode_burnin_settings: TimecodeBurninSettings | None = None


@dataclass
class AvailBlanking(PropertyType):
    avail_blanking_image: InputLocation | None = None
    state: str | None = None


@dataclass
class AvailConfiguration(PropertyType):
    avail_settings: AvailSettings | None = None
    scte35_segmentation_scope: str | None = None


@dataclass
class AvailSettings(PropertyType):
    esam: Esam | None = None
    scte35_splice_insert: Scte35SpliceInsert | None = None
    scte35_time_signal_apos: Scte35TimeSignalApos | None = None


@dataclass
class BandwidthReductionFilterSettings(PropertyType):
    post_filter_sharpening: str | None = None
    strength: str | None = None


@dataclass
class BlackoutSlate(PropertyType):
    blackout_slate_image: InputLocation | None = None
    network_end_blackout: str | None = None
    network_end_blackout_image: InputLocation | None = None
    network_id: str | None = None
    state: str | None = None


@dataclass
class BurnInDestinationSettings(PropertyType):
    alignment: str | None = None
    background_color: str | None = None
    background_opacity: int | None = None
    font: InputLocation | None = None
    font_color: str | None = None
    font_opacity: int | None = None
    font_resolution: int | None = None
    font_size: str | None = None
    outline_color: str | None = None
    outline_size: int | None = None
    shadow_color: str | None = None
    shadow_opacity: int | None = None
    shadow_x_offset: int | None = None
    shadow_y_offset: int | None = None
    subtitle_rows: str | None = None
    teletext_grid_control: str | None = None
    x_position: int | None = None
    y_position: int | None = None


@dataclass
class CaptionDescription(PropertyType):
    accessibility: str | None = None
    caption_dash_roles: list[String] = field(default_factory=list)
    caption_selector_name: str | None = None
    destination_settings: CaptionDestinationSettings | None = None
    dvb_dash_accessibility: str | None = None
    language_code: str | None = None
    language_description: str | None = None
    name: str | None = None


@dataclass
class CaptionDestinationSettings(PropertyType):
    arib_destination_settings: AribDestinationSettings | None = None
    burn_in_destination_settings: BurnInDestinationSettings | None = None
    dvb_sub_destination_settings: DvbSubDestinationSettings | None = None
    ebu_tt_d_destination_settings: EbuTtDDestinationSettings | None = None
    embedded_destination_settings: EmbeddedDestinationSettings | None = None
    embedded_plus_scte20_destination_settings: (
        EmbeddedPlusScte20DestinationSettings | None
    ) = None
    rtmp_caption_info_destination_settings: (
        RtmpCaptionInfoDestinationSettings | None
    ) = None
    scte20_plus_embedded_destination_settings: (
        Scte20PlusEmbeddedDestinationSettings | None
    ) = None
    scte27_destination_settings: Scte27DestinationSettings | None = None
    smpte_tt_destination_settings: SmpteTtDestinationSettings | None = None
    teletext_destination_settings: TeletextDestinationSettings | None = None
    ttml_destination_settings: TtmlDestinationSettings | None = None
    webvtt_destination_settings: WebvttDestinationSettings | None = None


@dataclass
class CaptionLanguageMapping(PropertyType):
    caption_channel: int | None = None
    language_code: str | None = None
    language_description: str | None = None


@dataclass
class CaptionRectangle(PropertyType):
    height: float | None = None
    left_offset: float | None = None
    top_offset: float | None = None
    width: float | None = None


@dataclass
class CaptionSelector(PropertyType):
    language_code: str | None = None
    name: str | None = None
    selector_settings: CaptionSelectorSettings | None = None


@dataclass
class CaptionSelectorSettings(PropertyType):
    ancillary_source_settings: AncillarySourceSettings | None = None
    arib_source_settings: AribSourceSettings | None = None
    dvb_sub_source_settings: DvbSubSourceSettings | None = None
    embedded_source_settings: EmbeddedSourceSettings | None = None
    scte20_source_settings: Scte20SourceSettings | None = None
    scte27_source_settings: Scte27SourceSettings | None = None
    teletext_source_settings: TeletextSourceSettings | None = None


@dataclass
class CdiInputSpecification(PropertyType):
    resolution: str | None = None


@dataclass
class ChannelEngineVersionRequest(PropertyType):
    version: str | None = None


@dataclass
class CmafIngestCaptionLanguageMapping(PropertyType):
    caption_channel: int | None = None
    language_code: str | None = None


@dataclass
class CmafIngestGroupSettings(PropertyType):
    additional_destinations: list[AdditionalDestinations] = field(default_factory=list)
    caption_language_mappings: list[CmafIngestCaptionLanguageMapping] = field(
        default_factory=list
    )
    destination: OutputLocationRef | None = None
    id3_behavior: str | None = None
    id3_name_modifier: str | None = None
    klv_behavior: str | None = None
    klv_name_modifier: str | None = None
    nielsen_id3_behavior: str | None = None
    nielsen_id3_name_modifier: str | None = None
    scte35_name_modifier: str | None = None
    scte35_type: str | None = None
    segment_length: int | None = None
    segment_length_units: str | None = None
    send_delay_ms: int | None = None
    timed_metadata_id3_frame: str | None = None
    timed_metadata_id3_period: int | None = None
    timed_metadata_passthrough: str | None = None


@dataclass
class CmafIngestOutputSettings(PropertyType):
    name_modifier: str | None = None


@dataclass
class ColorCorrection(PropertyType):
    input_color_space: str | None = None
    output_color_space: str | None = None
    uri: str | None = None


@dataclass
class ColorCorrectionSettings(PropertyType):
    global_color_corrections: list[ColorCorrection] = field(default_factory=list)


@dataclass
class ColorSpacePassthroughSettings(PropertyType):
    pass


@dataclass
class DolbyVision81Settings(PropertyType):
    pass


@dataclass
class DvbNitSettings(PropertyType):
    network_id: int | None = None
    network_name: str | None = None
    rep_interval: int | None = None


@dataclass
class DvbSdtSettings(PropertyType):
    output_sdt: str | None = None
    rep_interval: int | None = None
    service_name: str | None = None
    service_provider_name: str | None = None


@dataclass
class DvbSubDestinationSettings(PropertyType):
    alignment: str | None = None
    background_color: str | None = None
    background_opacity: int | None = None
    font: InputLocation | None = None
    font_color: str | None = None
    font_opacity: int | None = None
    font_resolution: int | None = None
    font_size: str | None = None
    outline_color: str | None = None
    outline_size: int | None = None
    shadow_color: str | None = None
    shadow_opacity: int | None = None
    shadow_x_offset: int | None = None
    shadow_y_offset: int | None = None
    subtitle_rows: str | None = None
    teletext_grid_control: str | None = None
    x_position: int | None = None
    y_position: int | None = None


@dataclass
class DvbSubSourceSettings(PropertyType):
    ocr_language: str | None = None
    pid: int | None = None


@dataclass
class DvbTdtSettings(PropertyType):
    rep_interval: int | None = None


@dataclass
class Eac3AtmosSettings(PropertyType):
    bitrate: float | None = None
    coding_mode: str | None = None
    dialnorm: int | None = None
    drc_line: str | None = None
    drc_rf: str | None = None
    height_trim: float | None = None
    surround_trim: float | None = None


@dataclass
class Eac3Settings(PropertyType):
    attenuation_control: str | None = None
    bitrate: float | None = None
    bitstream_mode: str | None = None
    coding_mode: str | None = None
    dc_filter: str | None = None
    dialnorm: int | None = None
    drc_line: str | None = None
    drc_rf: str | None = None
    lfe_control: str | None = None
    lfe_filter: str | None = None
    lo_ro_center_mix_level: float | None = None
    lo_ro_surround_mix_level: float | None = None
    lt_rt_center_mix_level: float | None = None
    lt_rt_surround_mix_level: float | None = None
    metadata_control: str | None = None
    passthrough_control: str | None = None
    phase_control: str | None = None
    stereo_downmix: str | None = None
    surround_ex_mode: str | None = None
    surround_mode: str | None = None


@dataclass
class EbuTtDDestinationSettings(PropertyType):
    copyright_holder: str | None = None
    default_font_size: int | None = None
    default_line_height: int | None = None
    fill_line_gap: str | None = None
    font_family: str | None = None
    style_control: str | None = None


@dataclass
class EmbeddedDestinationSettings(PropertyType):
    pass


@dataclass
class EmbeddedPlusScte20DestinationSettings(PropertyType):
    pass


@dataclass
class EmbeddedSourceSettings(PropertyType):
    convert608_to708: str | None = None
    scte20_detection: str | None = None
    source608_channel_number: int | None = None
    source608_track_number: int | None = None


@dataclass
class EncoderSettings(PropertyType):
    audio_descriptions: list[AudioDescription] = field(default_factory=list)
    avail_blanking: AvailBlanking | None = None
    avail_configuration: AvailConfiguration | None = None
    blackout_slate: BlackoutSlate | None = None
    caption_descriptions: list[CaptionDescription] = field(default_factory=list)
    color_correction_settings: ColorCorrectionSettings | None = None
    feature_activations: FeatureActivations | None = None
    global_configuration: GlobalConfiguration | None = None
    motion_graphics_configuration: MotionGraphicsConfiguration | None = None
    nielsen_configuration: NielsenConfiguration | None = None
    output_groups: list[OutputGroup] = field(default_factory=list)
    thumbnail_configuration: ThumbnailConfiguration | None = None
    timecode_config: TimecodeConfig | None = None
    video_descriptions: list[VideoDescription] = field(default_factory=list)


@dataclass
class EpochLockingSettings(PropertyType):
    custom_epoch: str | None = None
    jam_sync_time: str | None = None


@dataclass
class Esam(PropertyType):
    acquisition_point_id: str | None = None
    ad_avail_offset: int | None = None
    password_param: str | None = None
    pois_endpoint: str | None = None
    username: str | None = None
    zone_identity: str | None = None


@dataclass
class FailoverCondition(PropertyType):
    failover_condition_settings: FailoverConditionSettings | None = None


@dataclass
class FailoverConditionSettings(PropertyType):
    audio_silence_settings: AudioSilenceFailoverSettings | None = None
    input_loss_settings: InputLossFailoverSettings | None = None
    video_black_settings: VideoBlackFailoverSettings | None = None


@dataclass
class FeatureActivations(PropertyType):
    input_prepare_schedule_actions: str | None = None
    output_static_image_overlay_schedule_actions: str | None = None


@dataclass
class FecOutputSettings(PropertyType):
    column_depth: int | None = None
    include_fec: str | None = None
    row_length: int | None = None


@dataclass
class Fmp4HlsSettings(PropertyType):
    audio_rendition_sets: str | None = None
    nielsen_id3_behavior: str | None = None
    timed_metadata_behavior: str | None = None


@dataclass
class FrameCaptureCdnSettings(PropertyType):
    frame_capture_s3_settings: FrameCaptureS3Settings | None = None


@dataclass
class FrameCaptureGroupSettings(PropertyType):
    destination: OutputLocationRef | None = None
    frame_capture_cdn_settings: FrameCaptureCdnSettings | None = None


@dataclass
class FrameCaptureHlsSettings(PropertyType):
    pass


@dataclass
class FrameCaptureOutputSettings(PropertyType):
    name_modifier: str | None = None


@dataclass
class FrameCaptureS3Settings(PropertyType):
    canned_acl: str | None = None


@dataclass
class FrameCaptureSettings(PropertyType):
    capture_interval: int | None = None
    capture_interval_units: str | None = None
    timecode_burnin_settings: TimecodeBurninSettings | None = None


@dataclass
class GlobalConfiguration(PropertyType):
    initial_audio_gain: int | None = None
    input_end_action: str | None = None
    input_loss_behavior: InputLossBehavior | None = None
    output_locking_mode: str | None = None
    output_locking_settings: OutputLockingSettings | None = None
    output_timing_source: str | None = None
    support_low_framerate_inputs: str | None = None


@dataclass
class H264ColorSpaceSettings(PropertyType):
    color_space_passthrough_settings: ColorSpacePassthroughSettings | None = None
    rec601_settings: Rec601Settings | None = None
    rec709_settings: Rec709Settings | None = None


@dataclass
class H264FilterSettings(PropertyType):
    bandwidth_reduction_filter_settings: BandwidthReductionFilterSettings | None = None
    temporal_filter_settings: TemporalFilterSettings | None = None


@dataclass
class H264Settings(PropertyType):
    adaptive_quantization: str | None = None
    afd_signaling: str | None = None
    bitrate: int | None = None
    buf_fill_pct: int | None = None
    buf_size: int | None = None
    color_metadata: str | None = None
    color_space_settings: H264ColorSpaceSettings | None = None
    entropy_encoding: str | None = None
    filter_settings: H264FilterSettings | None = None
    fixed_afd: str | None = None
    flicker_aq: str | None = None
    force_field_pictures: str | None = None
    framerate_control: str | None = None
    framerate_denominator: int | None = None
    framerate_numerator: int | None = None
    gop_b_reference: str | None = None
    gop_closed_cadence: int | None = None
    gop_num_b_frames: int | None = None
    gop_size: float | None = None
    gop_size_units: str | None = None
    level: str | None = None
    look_ahead_rate_control: str | None = None
    max_bitrate: int | None = None
    min_bitrate: int | None = None
    min_i_interval: int | None = None
    min_qp: int | None = None
    num_ref_frames: int | None = None
    par_control: str | None = None
    par_denominator: int | None = None
    par_numerator: int | None = None
    profile: str | None = None
    quality_level: str | None = None
    qvbr_quality_level: int | None = None
    rate_control_mode: str | None = None
    scan_type: str | None = None
    scene_change_detect: str | None = None
    slices: int | None = None
    softness: int | None = None
    spatial_aq: str | None = None
    subgop_length: str | None = None
    syntax: str | None = None
    temporal_aq: str | None = None
    timecode_burnin_settings: TimecodeBurninSettings | None = None
    timecode_insertion: str | None = None


@dataclass
class H265ColorSpaceSettings(PropertyType):
    color_space_passthrough_settings: ColorSpacePassthroughSettings | None = None
    dolby_vision81_settings: DolbyVision81Settings | None = None
    hdr10_settings: Hdr10Settings | None = None
    hlg2020_settings: Hlg2020Settings | None = None
    rec601_settings: Rec601Settings | None = None
    rec709_settings: Rec709Settings | None = None


@dataclass
class H265FilterSettings(PropertyType):
    bandwidth_reduction_filter_settings: BandwidthReductionFilterSettings | None = None
    temporal_filter_settings: TemporalFilterSettings | None = None


@dataclass
class H265Settings(PropertyType):
    adaptive_quantization: str | None = None
    afd_signaling: str | None = None
    alternative_transfer_function: str | None = None
    bitrate: int | None = None
    buf_size: int | None = None
    color_metadata: str | None = None
    color_space_settings: H265ColorSpaceSettings | None = None
    deblocking: str | None = None
    filter_settings: H265FilterSettings | None = None
    fixed_afd: str | None = None
    flicker_aq: str | None = None
    framerate_denominator: int | None = None
    framerate_numerator: int | None = None
    gop_b_reference: str | None = None
    gop_closed_cadence: int | None = None
    gop_num_b_frames: int | None = None
    gop_size: float | None = None
    gop_size_units: str | None = None
    level: str | None = None
    look_ahead_rate_control: str | None = None
    max_bitrate: int | None = None
    min_bitrate: int | None = None
    min_i_interval: int | None = None
    min_qp: int | None = None
    mv_over_picture_boundaries: str | None = None
    mv_temporal_predictor: str | None = None
    par_denominator: int | None = None
    par_numerator: int | None = None
    profile: str | None = None
    qvbr_quality_level: int | None = None
    rate_control_mode: str | None = None
    scan_type: str | None = None
    scene_change_detect: str | None = None
    slices: int | None = None
    subgop_length: str | None = None
    tier: str | None = None
    tile_height: int | None = None
    tile_padding: str | None = None
    tile_width: int | None = None
    timecode_burnin_settings: TimecodeBurninSettings | None = None
    timecode_insertion: str | None = None
    treeblock_size: str | None = None


@dataclass
class Hdr10Settings(PropertyType):
    max_cll: int | None = None
    max_fall: int | None = None


@dataclass
class Hlg2020Settings(PropertyType):
    pass


@dataclass
class HlsAkamaiSettings(PropertyType):
    connection_retry_interval: int | None = None
    filecache_duration: int | None = None
    http_transfer_mode: str | None = None
    num_retries: int | None = None
    restart_delay: int | None = None
    salt: str | None = None
    token: str | None = None


@dataclass
class HlsBasicPutSettings(PropertyType):
    connection_retry_interval: int | None = None
    filecache_duration: int | None = None
    num_retries: int | None = None
    restart_delay: int | None = None


@dataclass
class HlsCdnSettings(PropertyType):
    hls_akamai_settings: HlsAkamaiSettings | None = None
    hls_basic_put_settings: HlsBasicPutSettings | None = None
    hls_media_store_settings: HlsMediaStoreSettings | None = None
    hls_s3_settings: HlsS3Settings | None = None
    hls_webdav_settings: HlsWebdavSettings | None = None


@dataclass
class HlsGroupSettings(PropertyType):
    ad_markers: list[String] = field(default_factory=list)
    base_url_content: str | None = None
    base_url_content1: str | None = None
    base_url_manifest: str | None = None
    base_url_manifest1: str | None = None
    caption_language_mappings: list[CaptionLanguageMapping] = field(
        default_factory=list
    )
    caption_language_setting: str | None = None
    client_cache: str | None = None
    codec_specification: str | None = None
    constant_iv: str | None = None
    destination: OutputLocationRef | None = None
    directory_structure: str | None = None
    discontinuity_tags: str | None = None
    encryption_type: str | None = None
    hls_cdn_settings: HlsCdnSettings | None = None
    hls_id3_segment_tagging: str | None = None
    i_frame_only_playlists: str | None = None
    incomplete_segment_behavior: str | None = None
    index_n_segments: int | None = None
    input_loss_action: str | None = None
    iv_in_manifest: str | None = None
    iv_source: str | None = None
    keep_segments: int | None = None
    key_format: str | None = None
    key_format_versions: str | None = None
    key_provider_settings: KeyProviderSettings | None = None
    manifest_compression: str | None = None
    manifest_duration_format: str | None = None
    min_segment_length: int | None = None
    mode: str | None = None
    output_selection: str | None = None
    program_date_time: str | None = None
    program_date_time_clock: str | None = None
    program_date_time_period: int | None = None
    redundant_manifest: str | None = None
    segment_length: int | None = None
    segmentation_mode: str | None = None
    segments_per_subdirectory: int | None = None
    stream_inf_resolution: str | None = None
    timed_metadata_id3_frame: str | None = None
    timed_metadata_id3_period: int | None = None
    timestamp_delta_milliseconds: int | None = None
    ts_file_mode: str | None = None


@dataclass
class HlsInputSettings(PropertyType):
    bandwidth: int | None = None
    buffer_segments: int | None = None
    retries: int | None = None
    retry_interval: int | None = None
    scte35_source: str | None = None


@dataclass
class HlsMediaStoreSettings(PropertyType):
    connection_retry_interval: int | None = None
    filecache_duration: int | None = None
    media_store_storage_class: str | None = None
    num_retries: int | None = None
    restart_delay: int | None = None


@dataclass
class HlsOutputSettings(PropertyType):
    h265_packaging_type: str | None = None
    hls_settings: HlsSettings | None = None
    name_modifier: str | None = None
    segment_modifier: str | None = None


@dataclass
class HlsS3Settings(PropertyType):
    canned_acl: str | None = None


@dataclass
class HlsSettings(PropertyType):
    audio_only_hls_settings: AudioOnlyHlsSettings | None = None
    fmp4_hls_settings: Fmp4HlsSettings | None = None
    frame_capture_hls_settings: FrameCaptureHlsSettings | None = None
    standard_hls_settings: StandardHlsSettings | None = None


@dataclass
class HlsWebdavSettings(PropertyType):
    connection_retry_interval: int | None = None
    filecache_duration: int | None = None
    http_transfer_mode: str | None = None
    num_retries: int | None = None
    restart_delay: int | None = None


@dataclass
class HtmlMotionGraphicsSettings(PropertyType):
    pass


@dataclass
class InputAttachment(PropertyType):
    automatic_input_failover_settings: AutomaticInputFailoverSettings | None = None
    input_attachment_name: str | None = None
    input_id: str | None = None
    input_settings: InputSettings | None = None
    logical_interface_names: list[String] = field(default_factory=list)


@dataclass
class InputChannelLevel(PropertyType):
    gain: int | None = None
    input_channel: int | None = None


@dataclass
class InputLocation(PropertyType):
    password_param: str | None = None
    uri: str | None = None
    username: str | None = None


@dataclass
class InputLossBehavior(PropertyType):
    black_frame_msec: int | None = None
    input_loss_image_color: str | None = None
    input_loss_image_slate: InputLocation | None = None
    input_loss_image_type: str | None = None
    repeat_frame_msec: int | None = None


@dataclass
class InputLossFailoverSettings(PropertyType):
    input_loss_threshold_msec: int | None = None


@dataclass
class InputSettings(PropertyType):
    audio_selectors: list[AudioSelector] = field(default_factory=list)
    caption_selectors: list[CaptionSelector] = field(default_factory=list)
    deblock_filter: str | None = None
    denoise_filter: str | None = None
    filter_strength: int | None = None
    input_filter: str | None = None
    network_input_settings: NetworkInputSettings | None = None
    scte35_pid: int | None = None
    smpte2038_data_preference: str | None = None
    source_end_behavior: str | None = None
    video_selector: VideoSelector | None = None


@dataclass
class InputSpecification(PropertyType):
    codec: str | None = None
    maximum_bitrate: str | None = None
    resolution: str | None = None


@dataclass
class KeyProviderSettings(PropertyType):
    static_key_settings: StaticKeySettings | None = None


@dataclass
class M2tsSettings(PropertyType):
    absent_input_audio_behavior: str | None = None
    arib: str | None = None
    arib_captions_pid: str | None = None
    arib_captions_pid_control: str | None = None
    audio_buffer_model: str | None = None
    audio_frames_per_pes: int | None = None
    audio_pids: str | None = None
    audio_stream_type: str | None = None
    bitrate: int | None = None
    buffer_model: str | None = None
    cc_descriptor: str | None = None
    dvb_nit_settings: DvbNitSettings | None = None
    dvb_sdt_settings: DvbSdtSettings | None = None
    dvb_sub_pids: str | None = None
    dvb_tdt_settings: DvbTdtSettings | None = None
    dvb_teletext_pid: str | None = None
    ebif: str | None = None
    ebp_audio_interval: str | None = None
    ebp_lookahead_ms: int | None = None
    ebp_placement: str | None = None
    ecm_pid: str | None = None
    es_rate_in_pes: str | None = None
    etv_platform_pid: str | None = None
    etv_signal_pid: str | None = None
    fragment_time: float | None = None
    klv: str | None = None
    klv_data_pids: str | None = None
    nielsen_id3_behavior: str | None = None
    null_packet_bitrate: float | None = None
    pat_interval: int | None = None
    pcr_control: str | None = None
    pcr_period: int | None = None
    pcr_pid: str | None = None
    pmt_interval: int | None = None
    pmt_pid: str | None = None
    program_num: int | None = None
    rate_mode: str | None = None
    scte27_pids: str | None = None
    scte35_control: str | None = None
    scte35_pid: str | None = None
    scte35_preroll_pullup_milliseconds: float | None = None
    segmentation_markers: str | None = None
    segmentation_style: str | None = None
    segmentation_time: float | None = None
    timed_metadata_behavior: str | None = None
    timed_metadata_pid: str | None = None
    transport_stream_id: int | None = None
    video_pid: str | None = None


@dataclass
class M3u8Settings(PropertyType):
    audio_frames_per_pes: int | None = None
    audio_pids: str | None = None
    ecm_pid: str | None = None
    klv_behavior: str | None = None
    klv_data_pids: str | None = None
    nielsen_id3_behavior: str | None = None
    pat_interval: int | None = None
    pcr_control: str | None = None
    pcr_period: int | None = None
    pcr_pid: str | None = None
    pmt_interval: int | None = None
    pmt_pid: str | None = None
    program_num: int | None = None
    scte35_behavior: str | None = None
    scte35_pid: str | None = None
    timed_metadata_behavior: str | None = None
    timed_metadata_pid: str | None = None
    transport_stream_id: int | None = None
    video_pid: str | None = None


@dataclass
class MaintenanceCreateSettings(PropertyType):
    maintenance_day: str | None = None
    maintenance_start_time: str | None = None


@dataclass
class MaintenanceUpdateSettings(PropertyType):
    maintenance_day: str | None = None
    maintenance_scheduled_date: str | None = None
    maintenance_start_time: str | None = None


@dataclass
class MediaPackageGroupSettings(PropertyType):
    destination: OutputLocationRef | None = None
    mediapackage_v2_group_settings: MediaPackageV2GroupSettings | None = None


@dataclass
class MediaPackageOutputDestinationSettings(PropertyType):
    channel_group: str | None = None
    channel_id: str | None = None
    channel_name: str | None = None


@dataclass
class MediaPackageOutputSettings(PropertyType):
    media_package_v2_destination_settings: MediaPackageV2DestinationSettings | None = (
        None
    )


@dataclass
class MediaPackageV2DestinationSettings(PropertyType):
    audio_group_id: str | None = None
    audio_rendition_sets: str | None = None
    hls_auto_select: str | None = None
    hls_default: str | None = None


@dataclass
class MediaPackageV2GroupSettings(PropertyType):
    caption_language_mappings: list[CaptionLanguageMapping] = field(
        default_factory=list
    )
    id3_behavior: str | None = None
    klv_behavior: str | None = None
    nielsen_id3_behavior: str | None = None
    scte35_type: str | None = None
    segment_length: int | None = None
    segment_length_units: str | None = None
    timed_metadata_id3_frame: str | None = None
    timed_metadata_id3_period: int | None = None
    timed_metadata_passthrough: str | None = None


@dataclass
class MotionGraphicsConfiguration(PropertyType):
    motion_graphics_insertion: str | None = None
    motion_graphics_settings: MotionGraphicsSettings | None = None


@dataclass
class MotionGraphicsSettings(PropertyType):
    html_motion_graphics_settings: HtmlMotionGraphicsSettings | None = None


@dataclass
class Mp2Settings(PropertyType):
    bitrate: float | None = None
    coding_mode: str | None = None
    sample_rate: float | None = None


@dataclass
class Mpeg2FilterSettings(PropertyType):
    temporal_filter_settings: TemporalFilterSettings | None = None


@dataclass
class Mpeg2Settings(PropertyType):
    adaptive_quantization: str | None = None
    afd_signaling: str | None = None
    color_metadata: str | None = None
    color_space: str | None = None
    display_aspect_ratio: str | None = None
    filter_settings: Mpeg2FilterSettings | None = None
    fixed_afd: str | None = None
    framerate_denominator: int | None = None
    framerate_numerator: int | None = None
    gop_closed_cadence: int | None = None
    gop_num_b_frames: int | None = None
    gop_size: float | None = None
    gop_size_units: str | None = None
    scan_type: str | None = None
    subgop_length: str | None = None
    timecode_burnin_settings: TimecodeBurninSettings | None = None
    timecode_insertion: str | None = None


@dataclass
class MsSmoothGroupSettings(PropertyType):
    acquisition_point_id: str | None = None
    audio_only_timecode_control: str | None = None
    certificate_mode: str | None = None
    connection_retry_interval: int | None = None
    destination: OutputLocationRef | None = None
    event_id: str | None = None
    event_id_mode: str | None = None
    event_stop_behavior: str | None = None
    filecache_duration: int | None = None
    fragment_length: int | None = None
    input_loss_action: str | None = None
    num_retries: int | None = None
    restart_delay: int | None = None
    segmentation_mode: str | None = None
    send_delay_ms: int | None = None
    sparse_track_type: str | None = None
    stream_manifest_behavior: str | None = None
    timestamp_offset: str | None = None
    timestamp_offset_mode: str | None = None


@dataclass
class MsSmoothOutputSettings(PropertyType):
    h265_packaging_type: str | None = None
    name_modifier: str | None = None


@dataclass
class MulticastInputSettings(PropertyType):
    source_ip_address: str | None = None


@dataclass
class MultiplexContainerSettings(PropertyType):
    multiplex_m2ts_settings: MultiplexM2tsSettings | None = None


@dataclass
class MultiplexGroupSettings(PropertyType):
    pass


@dataclass
class MultiplexM2tsSettings(PropertyType):
    absent_input_audio_behavior: str | None = None
    arib: str | None = None
    audio_buffer_model: str | None = None
    audio_frames_per_pes: int | None = None
    audio_stream_type: str | None = None
    cc_descriptor: str | None = None
    ebif: str | None = None
    es_rate_in_pes: str | None = None
    klv: str | None = None
    nielsen_id3_behavior: str | None = None
    pcr_control: str | None = None
    pcr_period: int | None = None
    scte35_control: str | None = None
    scte35_preroll_pullup_milliseconds: float | None = None


@dataclass
class MultiplexOutputSettings(PropertyType):
    container_settings: MultiplexContainerSettings | None = None
    destination: OutputLocationRef | None = None


@dataclass
class MultiplexProgramChannelDestinationSettings(PropertyType):
    multiplex_id: str | None = None
    program_name: str | None = None


@dataclass
class NetworkInputSettings(PropertyType):
    hls_input_settings: HlsInputSettings | None = None
    multicast_input_settings: MulticastInputSettings | None = None
    server_validation: str | None = None


@dataclass
class NielsenCBET(PropertyType):
    cbet_check_digit_string: str | None = None
    cbet_stepaside: str | None = None
    csid: str | None = None


@dataclass
class NielsenConfiguration(PropertyType):
    distributor_id: str | None = None
    nielsen_pcm_to_id3_tagging: str | None = None


@dataclass
class NielsenNaesIiNw(PropertyType):
    check_digit_string: str | None = None
    sid: float | None = None
    timezone: str | None = None


@dataclass
class NielsenWatermarksSettings(PropertyType):
    nielsen_cbet_settings: NielsenCBET | None = None
    nielsen_distribution_type: str | None = None
    nielsen_naes_ii_nw_settings: NielsenNaesIiNw | None = None


@dataclass
class Output(PropertyType):
    audio_description_names: list[String] = field(default_factory=list)
    caption_description_names: list[String] = field(default_factory=list)
    output_name: str | None = None
    output_settings: OutputSettings | None = None
    video_description_name: str | None = None


@dataclass
class OutputDestination(PropertyType):
    id: str | None = None
    logical_interface_names: list[String] = field(default_factory=list)
    media_package_settings: list[MediaPackageOutputDestinationSettings] = field(
        default_factory=list
    )
    multiplex_settings: MultiplexProgramChannelDestinationSettings | None = None
    settings: list[OutputDestinationSettings] = field(default_factory=list)
    srt_settings: list[SrtOutputDestinationSettings] = field(default_factory=list)


@dataclass
class OutputDestinationSettings(PropertyType):
    password_param: str | None = None
    stream_name: str | None = None
    url: str | None = None
    username: str | None = None


@dataclass
class OutputGroup(PropertyType):
    name: str | None = None
    output_group_settings: OutputGroupSettings | None = None
    outputs: list[Output] = field(default_factory=list)


@dataclass
class OutputGroupSettings(PropertyType):
    archive_group_settings: ArchiveGroupSettings | None = None
    cmaf_ingest_group_settings: CmafIngestGroupSettings | None = None
    frame_capture_group_settings: FrameCaptureGroupSettings | None = None
    hls_group_settings: HlsGroupSettings | None = None
    media_package_group_settings: MediaPackageGroupSettings | None = None
    ms_smooth_group_settings: MsSmoothGroupSettings | None = None
    multiplex_group_settings: MultiplexGroupSettings | None = None
    rtmp_group_settings: RtmpGroupSettings | None = None
    srt_group_settings: SrtGroupSettings | None = None
    udp_group_settings: UdpGroupSettings | None = None


@dataclass
class OutputLocationRef(PropertyType):
    destination_ref_id: str | None = None


@dataclass
class OutputLockingSettings(PropertyType):
    epoch_locking_settings: EpochLockingSettings | None = None
    pipeline_locking_settings: PipelineLockingSettings | None = None


@dataclass
class OutputSettings(PropertyType):
    archive_output_settings: ArchiveOutputSettings | None = None
    cmaf_ingest_output_settings: CmafIngestOutputSettings | None = None
    frame_capture_output_settings: FrameCaptureOutputSettings | None = None
    hls_output_settings: HlsOutputSettings | None = None
    media_package_output_settings: MediaPackageOutputSettings | None = None
    ms_smooth_output_settings: MsSmoothOutputSettings | None = None
    multiplex_output_settings: MultiplexOutputSettings | None = None
    rtmp_output_settings: RtmpOutputSettings | None = None
    srt_output_settings: SrtOutputSettings | None = None
    udp_output_settings: UdpOutputSettings | None = None


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
    channel_mappings: list[AudioChannelMapping] = field(default_factory=list)
    channels_in: int | None = None
    channels_out: int | None = None


@dataclass
class RtmpCaptionInfoDestinationSettings(PropertyType):
    pass


@dataclass
class RtmpGroupSettings(PropertyType):
    ad_markers: list[String] = field(default_factory=list)
    authentication_scheme: str | None = None
    cache_full_behavior: str | None = None
    cache_length: int | None = None
    caption_data: str | None = None
    include_filler_nal_units: str | None = None
    input_loss_action: str | None = None
    restart_delay: int | None = None


@dataclass
class RtmpOutputSettings(PropertyType):
    certificate_mode: str | None = None
    connection_retry_interval: int | None = None
    destination: OutputLocationRef | None = None
    num_retries: int | None = None


@dataclass
class Scte20PlusEmbeddedDestinationSettings(PropertyType):
    pass


@dataclass
class Scte20SourceSettings(PropertyType):
    convert608_to708: str | None = None
    source608_channel_number: int | None = None


@dataclass
class Scte27DestinationSettings(PropertyType):
    pass


@dataclass
class Scte27SourceSettings(PropertyType):
    ocr_language: str | None = None
    pid: int | None = None


@dataclass
class Scte35SpliceInsert(PropertyType):
    ad_avail_offset: int | None = None
    no_regional_blackout_flag: str | None = None
    web_delivery_allowed_flag: str | None = None


@dataclass
class Scte35TimeSignalApos(PropertyType):
    ad_avail_offset: int | None = None
    no_regional_blackout_flag: str | None = None
    web_delivery_allowed_flag: str | None = None


@dataclass
class SmpteTtDestinationSettings(PropertyType):
    pass


@dataclass
class SrtGroupSettings(PropertyType):
    input_loss_action: str | None = None


@dataclass
class SrtOutputDestinationSettings(PropertyType):
    encryption_passphrase_secret_arn: str | None = None
    stream_id: str | None = None
    url: str | None = None


@dataclass
class SrtOutputSettings(PropertyType):
    buffer_msec: int | None = None
    container_settings: UdpContainerSettings | None = None
    destination: OutputLocationRef | None = None
    encryption_type: str | None = None
    latency: int | None = None


@dataclass
class StandardHlsSettings(PropertyType):
    audio_rendition_sets: str | None = None
    m3u8_settings: M3u8Settings | None = None


@dataclass
class StaticKeySettings(PropertyType):
    key_provider_server: InputLocation | None = None
    static_key_value: str | None = None


@dataclass
class TeletextDestinationSettings(PropertyType):
    pass


@dataclass
class TeletextSourceSettings(PropertyType):
    output_rectangle: CaptionRectangle | None = None
    page_number: str | None = None


@dataclass
class TemporalFilterSettings(PropertyType):
    post_filter_sharpening: str | None = None
    strength: str | None = None


@dataclass
class ThumbnailConfiguration(PropertyType):
    state: str | None = None


@dataclass
class TimecodeBurninSettings(PropertyType):
    font_size: str | None = None
    position: str | None = None
    prefix: str | None = None


@dataclass
class TimecodeConfig(PropertyType):
    source: str | None = None
    sync_threshold: int | None = None


@dataclass
class TtmlDestinationSettings(PropertyType):
    style_control: str | None = None


@dataclass
class UdpContainerSettings(PropertyType):
    m2ts_settings: M2tsSettings | None = None


@dataclass
class UdpGroupSettings(PropertyType):
    input_loss_action: str | None = None
    timed_metadata_id3_frame: str | None = None
    timed_metadata_id3_period: int | None = None


@dataclass
class UdpOutputSettings(PropertyType):
    buffer_msec: int | None = None
    container_settings: UdpContainerSettings | None = None
    destination: OutputLocationRef | None = None
    fec_output_settings: FecOutputSettings | None = None


@dataclass
class VideoBlackFailoverSettings(PropertyType):
    black_detect_threshold: float | None = None
    video_black_threshold_msec: int | None = None


@dataclass
class VideoCodecSettings(PropertyType):
    av1_settings: Av1Settings | None = None
    frame_capture_settings: FrameCaptureSettings | None = None
    h264_settings: H264Settings | None = None
    h265_settings: H265Settings | None = None
    mpeg2_settings: Mpeg2Settings | None = None


@dataclass
class VideoDescription(PropertyType):
    codec_settings: VideoCodecSettings | None = None
    height: int | None = None
    name: str | None = None
    respond_to_afd: str | None = None
    scaling_behavior: str | None = None
    sharpness: int | None = None
    width: int | None = None


@dataclass
class VideoSelector(PropertyType):
    color_space: str | None = None
    color_space_settings: VideoSelectorColorSpaceSettings | None = None
    color_space_usage: str | None = None
    selector_settings: VideoSelectorSettings | None = None


@dataclass
class VideoSelectorColorSpaceSettings(PropertyType):
    hdr10_settings: Hdr10Settings | None = None


@dataclass
class VideoSelectorPid(PropertyType):
    pid: int | None = None


@dataclass
class VideoSelectorProgramId(PropertyType):
    program_id: int | None = None


@dataclass
class VideoSelectorSettings(PropertyType):
    video_selector_pid: VideoSelectorPid | None = None
    video_selector_program_id: VideoSelectorProgramId | None = None


@dataclass
class VpcOutputSettings(PropertyType):
    public_address_allocation_ids: list[String] = field(default_factory=list)
    security_group_ids: list[String] = field(default_factory=list)
    subnet_ids: list[String] = field(default_factory=list)


@dataclass
class WavSettings(PropertyType):
    bit_depth: float | None = None
    coding_mode: str | None = None
    sample_rate: float | None = None


@dataclass
class WebvttDestinationSettings(PropertyType):
    style_control: str | None = None
