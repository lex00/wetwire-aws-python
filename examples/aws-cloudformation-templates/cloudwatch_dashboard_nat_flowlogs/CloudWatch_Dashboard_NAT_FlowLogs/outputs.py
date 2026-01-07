"""Template outputs."""

from . import *  # noqa: F403


class DashboardArnOutput(Output):
    """ARN of the created CloudWatch Dashboard"""

    value = CloudWatchDashboard
    description = 'ARN of the created CloudWatch Dashboard'
