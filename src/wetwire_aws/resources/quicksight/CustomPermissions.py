"""PropertyTypes for AWS::QuickSight::CustomPermissions."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Capabilities(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "create_spice_dataset": "CreateSPICEDataset",
        "view_account_spice_capacity": "ViewAccountSPICECapacity",
    }

    add_or_run_anomaly_detection_for_analyses: DslValue[str] | None = None
    analysis: DslValue[str] | None = None
    create_and_update_dashboard_email_reports: DslValue[str] | None = None
    create_and_update_data_sources: DslValue[str] | None = None
    create_and_update_datasets: DslValue[str] | None = None
    create_and_update_themes: DslValue[str] | None = None
    create_and_update_threshold_alerts: DslValue[str] | None = None
    create_shared_folders: DslValue[str] | None = None
    create_spice_dataset: DslValue[str] | None = None
    dashboard: DslValue[str] | None = None
    export_to_csv: DslValue[str] | None = None
    export_to_csv_in_scheduled_reports: DslValue[str] | None = None
    export_to_excel: DslValue[str] | None = None
    export_to_excel_in_scheduled_reports: DslValue[str] | None = None
    export_to_pdf: DslValue[str] | None = None
    export_to_pdf_in_scheduled_reports: DslValue[str] | None = None
    include_content_in_scheduled_reports_email: DslValue[str] | None = None
    print_reports: DslValue[str] | None = None
    rename_shared_folders: DslValue[str] | None = None
    share_analyses: DslValue[str] | None = None
    share_dashboards: DslValue[str] | None = None
    share_data_sources: DslValue[str] | None = None
    share_datasets: DslValue[str] | None = None
    subscribe_dashboard_email_reports: DslValue[str] | None = None
    view_account_spice_capacity: DslValue[str] | None = None
