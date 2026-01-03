"""Template outputs."""

from . import *  # noqa: F403


class DashboardArnOutput:
    """ARN of the created CloudWatch Dashboard"""

    resource: Output
    value = CloudWatchDashboard
    description = 'ARN of the created CloudWatch Dashboard'
