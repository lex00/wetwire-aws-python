"""Role resource defined in a separate file."""

from . import *  # noqa: F401, F403, F405

__all__ = ["AppRole"]


class AppRole:
    """IAM role for the application."""

    resource: iam.Role  # noqa: F405
    role_name = "app-role"
    assume_role_policy_document: dict = None
