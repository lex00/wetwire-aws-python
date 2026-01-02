"""PropertyTypes for AWS::QuickSight::CustomPermissions."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Capabilities(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "create_spice_dataset": "CreateSPICEDataset",
        "view_account_spice_capacity": "ViewAccountSPICECapacity",
    }

    add_or_run_anomaly_detection_for_analyses: str | None = None
    analysis: str | None = None
    create_and_update_dashboard_email_reports: str | None = None
    create_and_update_data_sources: str | None = None
    create_and_update_datasets: str | None = None
    create_and_update_themes: str | None = None
    create_and_update_threshold_alerts: str | None = None
    create_shared_folders: str | None = None
    create_spice_dataset: str | None = None
    dashboard: str | None = None
    export_to_csv: str | None = None
    export_to_csv_in_scheduled_reports: str | None = None
    export_to_excel: str | None = None
    export_to_excel_in_scheduled_reports: str | None = None
    export_to_pdf: str | None = None
    export_to_pdf_in_scheduled_reports: str | None = None
    include_content_in_scheduled_reports_email: str | None = None
    print_reports: str | None = None
    rename_shared_folders: str | None = None
    share_analyses: str | None = None
    share_dashboards: str | None = None
    share_data_sources: str | None = None
    share_datasets: str | None = None
    subscribe_dashboard_email_reports: str | None = None
    view_account_spice_capacity: str | None = None
